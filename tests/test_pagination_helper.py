"""Tests for pagination helper functionality."""

import pytest
from gradient._utils import PaginationHelper


class TestPaginationHelper:
    """Test pagination helper functionality."""

    def test_pagination_helper_basic(self):
        """Test basic pagination functionality."""
        helper = PaginationHelper(page_size=2, max_pages=3)

        # Mock responses with different pages
        responses = [
            {"data": ["item1", "item2"]},  # Page 1
            {"data": ["item3", "item4"]},  # Page 2
            {"data": ["item5"]},          # Page 3 (partial)
        ]
        response_index = 0

        def mock_fetch(params):
            nonlocal response_index
            if response_index < len(responses):
                result = responses[response_index]
                response_index += 1
                return result
            return {"data": []}

        result = helper.paginate(mock_fetch)
        assert result == ["item1", "item2", "item3", "item4", "item5"]

    def test_pagination_helper_max_pages(self):
        """Test pagination with max pages limit."""
        helper = PaginationHelper(page_size=2, max_pages=2)

        responses = [
            {"data": ["item1", "item2"]},
            {"data": ["item3", "item4"]},
            {"data": ["item5", "item6"]},  # Should not be reached
        ]
        response_index = 0

        def mock_fetch(params):
            nonlocal response_index
            if response_index < len(responses):
                result = responses[response_index]
                response_index += 1
                return result
            return {"data": []}

        result = helper.paginate(mock_fetch)
        assert result == ["item1", "item2", "item3", "item4"]

    def test_pagination_helper_empty_response(self):
        """Test pagination with empty response."""
        helper = PaginationHelper(page_size=2)

        def mock_fetch(params):
            return {"data": []}

        result = helper.paginate(mock_fetch)
        assert result == []

    def test_pagination_helper_different_response_formats(self):
        """Test pagination with different response formats."""
        helper = PaginationHelper(page_size=2)

        # Test different response formats
        test_cases = [
            {"data": ["item1", "item2"]},
            {"items": ["item3", "item4"]},
            {"results": ["item5", "item6"]},
            ["item7", "item8"],  # Direct list
        ]

        for i, expected_format in enumerate(test_cases):
            response_index = 0

            def mock_fetch(params):
                nonlocal response_index
                if response_index == 0:
                    response_index += 1
                    return expected_format
                return {"data": []}

            result = helper.paginate(mock_fetch)
            expected_items = expected_format if isinstance(expected_format, list) else expected_format.get(
                list(expected_format.keys())[0], []
            )
            assert result == expected_items

    def test_pagination_helper_extract_items(self):
        """Test item extraction from different response formats."""
        helper = PaginationHelper()

        # Test various response formats
        test_responses = [
            type('MockResponse', (), {'data': ['item1']})(),
            type('MockResponse', (), {'items': ['item2']})(),
            type('MockResponse', (), {'results': ['item3']})(),
            ['item4'],
            {'data': ['item5']},
            {'unknown': ['should_be_empty']},
        ]

        for i, response in enumerate(test_responses):
            items = helper._extract_items(response)
            expected_items = [f'item{i+1}'] if i < 5 else []
            assert items == expected_items