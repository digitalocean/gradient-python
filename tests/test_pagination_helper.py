"""Tests for PaginationHelper utility class."""

from __future__ import annotations

import pytest
from unittest.mock import Mock, call

from gradient._utils import PaginationHelper


class TestPaginationHelper:
    """Test cases for PaginationHelper class."""

    def test_init(self) -> None:
        """Test PaginationHelper initialization."""
        helper = PaginationHelper(page_size=50, max_pages=10)
        assert helper.page_size == 50
        assert helper.max_pages == 10

        # Test defaults
        helper_default = PaginationHelper()
        assert helper_default.page_size == 20
        assert helper_default.max_pages is None

    def test_paginate_basic(self) -> None:
        """Test basic pagination functionality."""
        helper = PaginationHelper(page_size=2, max_pages=3)

        # Mock fetch function that returns different data for each page
        call_count = 0
        def mock_fetch(params):
            nonlocal call_count
            call_count += 1
            page = params.get('page', 1)
            per_page = params.get('per_page', 2)

            if call_count == 1:
                return {'data': ['item1', 'item2']}
            elif call_count == 2:
                return {'data': ['item3', 'item4']}
            elif call_count == 3:
                return {'data': ['item5']}  # Last page with fewer items
            else:
                return {'data': []}  # No more data

        result = helper.paginate(mock_fetch)

        assert result == ['item1', 'item2', 'item3', 'item4', 'item5']
        assert call_count == 3

    def test_paginate_with_kwargs(self) -> None:
        """Test pagination with additional kwargs."""
        helper = PaginationHelper(page_size=1)

        def mock_fetch(params):
            # Should include both pagination params and custom params
            assert 'page' in params
            assert 'per_page' in params
            assert params['custom_param'] == 'value'
            return {'data': [f'item{params["page"]}']}

        # Mock to return only one page
        call_count = 0
        def mock_fetch_single(params):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return {'data': ['item1']}
            return {'data': []}

        result = helper.paginate(mock_fetch_single, custom_param='value')
        assert result == ['item1']

    def test_paginate_max_pages_limit(self) -> None:
        """Test that max_pages limits the number of pages fetched."""
        helper = PaginationHelper(page_size=1, max_pages=2)

        call_count = 0
        def mock_fetch(params):
            nonlocal call_count
            call_count += 1
            return {'data': [f'item{call_count}']}

        result = helper.paginate(mock_fetch)
        assert result == ['item1', 'item2']
        assert call_count == 2

    def test_paginate_different_response_formats(self) -> None:
        """Test pagination with different response formats."""
        helper = PaginationHelper(page_size=1)

        # Test different response formats
        responses = [
            {'data': ['item1']},  # Standard format
            {'items': ['item2']},  # Alternative format
            {'results': ['item3']},  # Another format
            ['item4'],  # Direct list
            {'objects': ['item5']},  # Another common format
        ]

        call_count = 0
        def mock_fetch(params):
            nonlocal call_count
            call_count += 1
            if call_count <= len(responses):
                return responses[call_count - 1]
            return []

        result = helper.paginate(mock_fetch)
        assert result == ['item1', 'item2', 'item3', 'item4', 'item5']

    def test_paginate_empty_response(self) -> None:
        """Test pagination with empty response."""
        helper = PaginationHelper()

        def mock_fetch(params):
            return {'data': []}

        result = helper.paginate(mock_fetch)
        assert result == []

    def test_paginate_error_handling(self) -> None:
        """Test pagination error handling."""
        helper = PaginationHelper(page_size=1)

        call_count = 0
        def mock_fetch(params):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return {'data': ['item1']}
            elif call_count == 2:
                raise ValueError("Page not found")
            return {'data': []}

        # Should stop when error indicates end of pagination
        result = helper.paginate(mock_fetch)
        assert result == ['item1']
        assert call_count == 2

    def test_paginate_response_object_with_attributes(self) -> None:
        """Test pagination with response objects that have attributes."""
        helper = PaginationHelper(page_size=1)

        # Mock response objects
        class MockResponse:
            def __init__(self, data):
                self.data = data

        call_count = 0
        def mock_fetch(params):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return MockResponse(['item1'])
            return MockResponse([])

        result = helper.paginate(mock_fetch)
        assert result == ['item1']

    def test_paginate_partial_page_stops_pagination(self) -> None:
        """Test that getting fewer items than page_size stops pagination."""
        helper = PaginationHelper(page_size=3)

        call_count = 0
        def mock_fetch(params):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return {'data': ['item1', 'item2']}  # Fewer than page_size
            return {'data': ['item3', 'item4', 'item5']}  # This shouldn't be called

        result = helper.paginate(mock_fetch)
        assert result == ['item1', 'item2']
        assert call_count == 1

    @pytest.mark.asyncio
    async def test_paginate_async(self) -> None:
        """Test async pagination functionality."""
        helper = PaginationHelper(page_size=2, max_pages=2)

        call_count = 0
        async def mock_fetch(params):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return {'data': ['item1', 'item2']}
            elif call_count == 2:
                return {'data': ['item3']}  # Last page
            return {'data': []}

        result = await helper.paginate_async(mock_fetch)
        assert result == ['item1', 'item2', 'item3']
        assert call_count == 2

    def test_extract_items_edge_cases(self) -> None:
        """Test _extract_items method with edge cases."""
        helper = PaginationHelper()

        # Test None response
        assert helper._extract_items(None) == []

        # Test dict without expected keys
        assert helper._extract_items({'other_key': 'value'}) == []

        # Test dict with non-list values
        assert helper._extract_items({'data': 'not_a_list'}) == []

        # Test nested structures
        assert helper._extract_items({'data': {'nested': ['item']}}) == []

    def test_is_pagination_end_error(self) -> None:
        """Test _is_pagination_end_error method."""
        helper = PaginationHelper()

        # Should return True for pagination end errors
        assert helper._is_pagination_end_error(ValueError("Page not found"))
        assert helper._is_pagination_end_error(ValueError("Invalid page"))
        assert helper._is_pagination_end_error(ValueError("No more pages"))

        # Should return False for other errors
        assert not helper._is_pagination_end_error(ValueError("Network error"))
        assert not helper._is_pagination_end_error(ValueError("Timeout"))

        # Should handle different error types
        assert helper._is_pagination_end_error(Exception("page not found"))
        assert not helper._is_pagination_end_error(Exception("other error"))