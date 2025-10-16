"""Tests for new features added to the Gradient SDK."""

import pytest
import json
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from gradient import Gradient
from gradient._utils import (
    validate_api_key,
    validate_client_credentials,
    ResponseCache,
    RateLimiter,
    AdaptiveRateLimiter,
    BatchProcessor,
    PaginationHelper,
    export_to_json,
    export_to_csv,
    export_api_response,
    clear_response_cache,
    get_global_rate_limiter,
    get_adaptive_rate_limiter,
    get_request_metrics,
    reset_request_metrics,
)


class TestAPIKeyValidation:
    """Test API key validation functionality."""

    def test_valid_api_key(self):
        """Test that valid API keys pass validation."""
        assert validate_api_key("sk-1234567890abcdef") is True
        assert validate_api_key("do_v1_1234567890abcdef1234567890abcdef") is True

    def test_invalid_api_key_none(self):
        """Test that None API key raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty or None"):
            validate_api_key(None)

    def test_invalid_api_key_empty(self):
        """Test that empty API key raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty or whitespace only"):
            validate_api_key("")

    def test_invalid_api_key_whitespace(self):
        """Test that whitespace-only API key raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty or whitespace only"):
            validate_api_key("   ")

    def test_invalid_api_key_too_short(self):
        """Test that too-short API key raises ValueError."""
        with pytest.raises(ValueError, match="appears to be too short"):
            validate_api_key("abc")

    def test_invalid_api_key_wrong_type(self):
        """Test that non-string API key raises ValueError."""
        with pytest.raises(ValueError, match="must be a string"):
            validate_api_key(12345)

    def test_validate_client_credentials_valid(self):
        """Test that valid credentials pass validation."""
        # Should not raise any exception
        validate_client_credentials(
            access_token="do_v1_1234567890abcdef",
            model_access_key="sk-1234567890abcdef",
            agent_access_key="agent-1234567890abcdef"
        )

    def test_validate_client_credentials_minimal(self):
        """Test that at least one credential is required."""
        # Should not raise any exception
        validate_client_credentials(access_token="do_v1_1234567890abcdef")

    def test_validate_client_credentials_none(self):
        """Test that no credentials raises ValueError."""
        with pytest.raises(ValueError, match="At least one authentication method must be provided"):
            validate_client_credentials()


class TestResponseCache:
    """Test response caching functionality."""

    def test_cache_initialization(self):
        """Test cache initialization."""
        cache = ResponseCache(default_ttl=60)
        assert cache._default_ttl == 60
        assert len(cache._cache) == 0

    def test_cache_operations(self):
        """Test basic cache operations."""
        cache = ResponseCache(default_ttl=60)

        # Test cache miss
        assert cache.get("nonexistent") is None

        # Test cache set and get
        cache.set("test_key", "test_data", ttl=30)
        assert cache.get("test_key") == "test_data"

        # Test cache expiration
        cache.set("expired_key", "expired_data", ttl=0)
        assert cache.get("expired_key") is None

    def test_cache_cleanup(self):
        """Test cache cleanup functionality."""
        cache = ResponseCache(default_ttl=60)

        # Add some entries
        cache.set("key1", "data1", ttl=30)
        cache.set("key2", "data2", ttl=0)  # Expired immediately

        # Cleanup should remove expired entries
        cache.cleanup_expired()

        assert cache.get("key1") == "data1"
        assert cache.get("key2") is None

    def test_clear_cache(self):
        """Test cache clearing."""
        cache = ResponseCache()
        cache.set("key1", "data1")
        cache.set("key2", "data2")

        clear_response_cache()

        # Note: This tests the global cache, not the instance
        # In a real scenario, we'd need to mock the global instance


class TestRateLimiter:
    """Test rate limiting functionality."""

    def test_rate_limiter_initialization(self):
        """Test rate limiter initialization."""
        limiter = RateLimiter(rate=10, capacity=100)
        assert limiter.rate == 10
        assert limiter.capacity == 100
        assert limiter.tokens == 100

    def test_rate_limiter_acquire(self):
        """Test token acquisition."""
        limiter = RateLimiter(rate=10, capacity=10)

        # Should be able to acquire all tokens initially
        for _ in range(10):
            assert limiter.acquire() is True

        # Should not be able to acquire more
        assert limiter.acquire() is False

    def test_rate_limiter_replenish(self):
        """Test token replenishment over time."""
        limiter = RateLimiter(rate=10, capacity=10)

        # Use all tokens
        for _ in range(10):
            assert limiter.acquire() is True

        # Wait for some tokens to replenish (simulate time passing)
        limiter._add_tokens()  # This would normally happen over time
        assert limiter.tokens > 0

    def test_adaptive_rate_limiter(self):
        """Test adaptive rate limiter."""
        limiter = AdaptiveRateLimiter(base_rate=10, capacity=10)

        # Test successful requests
        limiter.on_success()
        assert limiter.get_current_rate() == 10  # Should stay at base rate

        # Test error handling
        limiter.on_error(status_code=429)
        assert limiter.get_current_rate() < 10  # Should reduce rate


class TestBatchProcessor:
    """Test batch processing functionality."""

    def test_batch_processor_initialization(self):
        """Test batch processor initialization."""
        processor = BatchProcessor(max_concurrent=5, max_batch_size=10)
        assert processor.max_concurrent == 5
        assert processor.max_batch_size == 10

    def test_batch_processing(self):
        """Test batch processing of items."""
        def double(x):
            return x * 2

        processor = BatchProcessor(max_concurrent=2, max_batch_size=3)
        items = [1, 2, 3, 4, 5]
        results = processor.process_batch(items, double)

        assert len(results) == 5
        assert set(results) == {2, 4, 6, 8, 10}

    @pytest.mark.asyncio
    async def test_async_batch_processing(self):
        """Test async batch processing."""
        async def async_double(x):
            return x * 2

        processor = BatchProcessor(max_concurrent=2, max_batch_size=3)
        items = [1, 2, 3, 4, 5]
        results = await processor.process_batch_async(items, async_double)

        assert len(results) == 5
        assert set(results) == {2, 4, 6, 8, 10}


class TestPaginationHelper:
    """Test pagination helper functionality."""

    def test_pagination_helper_initialization(self):
        """Test pagination helper initialization."""
        helper = PaginationHelper(auto_fetch_all=True, max_pages=5)
        assert helper.auto_fetch_all is True
        assert helper.max_pages == 5

    def test_pagination_iteration(self):
        """Test pagination iteration."""
        call_count = 0

        def mock_list_func(page=1, **kwargs):
            nonlocal call_count
            call_count += 1

            if page == 1:
                # Mock response with next page
                response = MagicMock()
                response.links = MagicMock()
                response.links.next = "next_page_url"
                return response
            elif page == 2:
                # Mock response without next page
                response = MagicMock()
                response.links = None
                return response
            else:
                raise ValueError("Unexpected page")

        helper = PaginationHelper()
        pages = list(helper.iterate_pages(mock_list_func))

        assert len(pages) == 2
        assert call_count == 2


class TestExportFunctionality:
    """Test data export functionality."""

    def test_export_to_json(self):
        """Test JSON export functionality."""
        data = {"key": "value", "number": 42}

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name

        try:
            export_to_json(data, temp_path)

            # Verify file was created and contains correct data
            assert os.path.exists(temp_path)

            with open(temp_path, 'r') as f:
                loaded_data = json.load(f)

            assert loaded_data == data

        finally:
            os.unlink(temp_path)

    def test_export_to_csv(self):
        """Test CSV export functionality."""
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]

        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            temp_path = f.name

        try:
            export_to_csv(data, temp_path)

            # Verify file was created and contains correct data
            assert os.path.exists(temp_path)

            with open(temp_path, 'r') as f:
                lines = f.readlines()

            assert len(lines) == 3  # Header + 2 data rows
            assert "name,age" in lines[0]

        finally:
            os.unlink(temp_path)

    def test_export_api_response(self):
        """Test API response export functionality."""
        # Mock API response object
        response = MagicMock()
        response.model_dump.return_value = {"test": "data"}

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name

        try:
            export_api_response(response, temp_path, format='json')

            assert os.path.exists(temp_path)

            with open(temp_path, 'r') as f:
                loaded_data = json.load(f)

            assert loaded_data == {"test": "data"}

        finally:
            os.unlink(temp_path)


class TestRequestMetrics:
    """Test request metrics functionality."""

    def test_metrics_recording(self):
        """Test metrics recording."""
        metrics = get_request_metrics()

        # Record some requests
        metrics.record_request("test.endpoint", 1.5, status_code=200)
        metrics.record_request("test.endpoint", 2.0, status_code=201)
        metrics.record_error("ValueError")

        summary = metrics.get_summary()

        assert summary["requests_total"] == 2
        assert summary["requests_by_endpoint"]["test.endpoint"] == 2
        assert summary["requests_by_status"][200] == 1
        assert summary["requests_by_status"][201] == 1
        assert summary["errors_total"] == 1
        assert summary["errors_by_type"]["ValueError"] == 1

    def test_metrics_reset(self):
        """Test metrics reset functionality."""
        metrics = get_request_metrics()

        metrics.record_request("test.endpoint", 1.0)
        assert metrics.requests_total == 1

        reset_request_metrics()
        assert metrics.requests_total == 0


class TestClientEnhancements:
    """Test enhanced client functionality."""

    def test_client_with_custom_headers(self):
        """Test client initialization with custom headers."""
        client = Gradient(
            access_token="test_token",
            custom_headers={"X-Custom": "value"}
        )

        # Verify custom headers are set
        assert "X-Custom" in client._custom_headers

    def test_client_validation(self):
        """Test client credential validation."""
        # Valid client should not raise
        Gradient(access_token="do_v1_validtoken1234567890")

        # Invalid client should raise
        with pytest.raises(ValueError):
            Gradient()  # No credentials

    @patch('gradient.resources.models.models.cached_response')
    def test_cached_models_list(self, mock_cached_response):
        """Test that models list uses caching."""
        mock_response = MagicMock()
        mock_cached_response.return_value = lambda: mock_response

        client = Gradient(access_token="test_token")

        # This should use the cached response decorator
        result = client.models.list(cache_ttl=300)

        mock_cached_response.assert_called_once()


class TestGlobalUtilities:
    """Test global utility functions."""

    def test_global_rate_limiter(self):
        """Test global rate limiter access."""
        limiter = get_global_rate_limiter()
        assert isinstance(limiter, RateLimiter)

    def test_global_adaptive_limiter(self):
        """Test global adaptive rate limiter access."""
        limiter = get_adaptive_rate_limiter()
        assert isinstance(limiter, AdaptiveRateLimiter)

    def test_global_metrics(self):
        """Test global metrics access."""
        metrics = get_request_metrics()
        assert hasattr(metrics, 'record_request')