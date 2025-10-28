"""Tests for new features added to the Gradient SDK."""

import pytest
from gradient._utils import (
    validate_api_key,
    validate_client_credentials,
    validate_client_instance,
    get_available_models,
    is_model_available,
    get_model_info,
    ResponseCache,
    RateLimiter,
    BatchProcessor,
    DataExporter,
    Paginator,
)


class TestAPIKeyValidation:
    """Test API key validation functionality."""

    def test_valid_api_keys(self):
        """Test that valid API keys pass validation."""
        valid_keys = [
            "sk-1234567890abcdef",
            "do_v1_1234567890abcdef1234567890abcdef",
            "gradient_test_key_1234567890",
            "some_long_api_key_that_is_valid_1234567890",
        ]

        for key in valid_keys:
            assert validate_api_key(key), f"Key {key} should be valid"

    def test_invalid_api_keys(self):
        """Test that invalid API keys fail validation."""
        invalid_keys = [
            "",  # empty string
            "   ",  # whitespace only
            "short",  # too short
            "123456789",  # too short with numbers
            None,  # None value
            12345,  # integer
        ]

        for key in invalid_keys:
            assert not validate_api_key(key), f"Key {key} should be invalid"

    def test_validate_client_credentials_valid(self):
        """Test that valid client credentials pass validation."""
        # Should not raise any exception
        validate_client_credentials(access_token="sk-1234567890abcdef")
        validate_client_credentials(model_access_key="gradient_test_key_1234567890")
        validate_client_credentials(agent_access_key="do_v1_1234567890abcdef1234567890abcdef")

    def test_validate_client_credentials_invalid(self):
        """Test that invalid client credentials raise ValueError."""
        # No credentials provided
        with pytest.raises(ValueError, match="At least one authentication method must be provided"):
            validate_client_credentials()

        # Invalid access token
        with pytest.raises(ValueError, match="Invalid access_token format"):
            validate_client_credentials(access_token="invalid")

        # Invalid model access key
        with pytest.raises(ValueError, match="Invalid model_access_key format"):
            validate_client_credentials(model_access_key="short")

        # Invalid agent access key - empty string is falsy, so it triggers "no credentials" error
        with pytest.raises(ValueError, match="At least one authentication method must be provided"):
            validate_client_credentials(agent_access_key="")

    def test_validate_client_credentials_comprehensive(self):
        """Test comprehensive client credentials validation."""
        # Test valid agent endpoint
        validate_client_credentials(
            agent_access_key="do_v1_1234567890abcdef1234567890abcdef",
            agent_endpoint="https://my-agent.agents.do-ai.run"
        )

        # Test invalid agent endpoint - no protocol
        with pytest.raises(ValueError, match="agent_endpoint must be a valid HTTP/HTTPS URL"):
            validate_client_credentials(
                agent_access_key="do_v1_1234567890abcdef1234567890abcdef",
                agent_endpoint="my-agent.agents.do-ai.run"
            )

        # Test invalid agent endpoint - not a string
        with pytest.raises(ValueError, match="agent_endpoint must be a string"):
            validate_client_credentials(
                agent_access_key="do_v1_1234567890abcdef1234567890abcdef",
                agent_endpoint=12345
            )

    def test_validate_client_instance(self):
        """Test client instance validation."""
        from gradient import Gradient

        # Valid client
        client = Gradient(access_token="sk-1234567890abcdef")
        validate_client_instance(client)  # Should not raise

        # Invalid client - no auth
        invalid_client = Gradient(base_url="http://test.com")
        with pytest.raises(ValueError, match="Client must have at least one authentication method configured"):
            validate_client_instance(invalid_client)

        # Invalid type
        with pytest.raises(TypeError, match="client must be a Gradient or AsyncGradient instance"):
            validate_client_instance("not a client")

    def test_validate_client_credentials_multiple_valid(self):
        """Test that multiple valid credentials are accepted."""
        validate_client_credentials(
            access_token="sk-1234567890abcdef",
            model_access_key="gradient_test_key_1234567890",
            agent_access_key="do_v1_1234567890abcdef1234567890abcdef"
        )

    def test_validate_client_credentials_mixed_valid_invalid(self):
        """Test that one invalid credential among valid ones still raises error."""
        with pytest.raises(ValueError, match="Invalid access_token format"):
            validate_client_credentials(
                access_token="invalid",
                model_access_key="gradient_test_key_1234567890"
            )


class TestModelManagement:
    """Test model management functionality."""

    def test_get_available_models(self):
        """Test getting available models."""
        models = get_available_models()
        assert isinstance(models, list)
        assert len(models) > 0
        assert "llama3.3-70b-instruct" in models

    def test_get_available_models_caching(self):
        """Test that get_available_models uses caching."""
        # First call
        models1 = get_available_models()
        # Second call should return the same cached result
        models2 = get_available_models()
        assert models1 is models2  # Same object reference due to caching

    def test_is_model_available(self):
        """Test checking if a model is available."""
        assert is_model_available("llama3.3-70b-instruct")
        assert not is_model_available("nonexistent-model")

    def test_get_model_info(self):
        """Test getting model information."""
        info = get_model_info("llama3.3-70b-instruct")
        assert info is not None
        assert info["name"] == "llama3.3-70b-instruct"
        assert info["available"] is True
        assert info["family"] == "Llama"
        assert "parameters" in info

    def test_get_model_info_nonexistent(self):
        """Test getting info for nonexistent model."""
        info = get_model_info("nonexistent-model")
        assert info is None


class TestCustomHeaders:
    """Test custom headers functionality."""

    def test_custom_headers_in_sync_client(self):
        """Test that custom headers are properly set in sync client."""
        from gradient import Gradient

        client = Gradient(
            base_url="http://test.com",
            access_token="test_token",
            custom_headers={"X-Custom": "custom-value", "X-Another": "another-value"}
        )

        # Check that custom headers are in the client's _custom_headers
        assert "X-Custom" in client._custom_headers
        assert client._custom_headers["X-Custom"] == "custom-value"


class TestBatchProcessor:
    """Test batch processing functionality."""

    def test_batch_processor_basic(self):
        """Test basic batch processing."""
        processor = BatchProcessor(max_batch_size=3, max_wait_time=0.1)

        # Add requests to batch
        processor.add_request("batch1", {"id": 1})
        processor.add_request("batch1", {"id": 2})

        # Should not be ready yet
        assert processor.get_batch("batch1") is None

        # Add one more to reach max size
        processor.add_request("batch1", {"id": 3})

        # Should be ready now
        batch = processor.get_batch("batch1")
        assert batch is not None
        assert len(batch) == 3
        assert batch[0]["id"] == 1
        assert batch[1]["id"] == 2
        assert batch[2]["id"] == 3

    def test_batch_processor_timeout(self):
        """Test batch processing with timeout."""
        import time

        processor = BatchProcessor(max_batch_size=10, max_wait_time=0.1)

        processor.add_request("batch1", {"id": 1})

        # Wait for timeout
        time.sleep(0.15)

        # Should be ready due to timeout
        batch = processor.get_batch("batch1")
        assert batch is not None
        assert len(batch) == 1

    def test_batch_processor_multiple_batches(self):
        """Test multiple batch keys."""
        processor = BatchProcessor(max_batch_size=2)

        processor.add_request("batch1", {"id": 1})
        processor.add_request("batch2", {"id": 2})
        processor.add_request("batch1", {"id": 3})

        # batch1 should be ready
        batch1 = processor.get_batch("batch1")
        assert batch1 is not None
        assert len(batch1) == 2

        # batch2 should not be ready yet
        assert processor.get_batch("batch2") is None

    def test_batch_processor_force_process(self):
        """Test forcing processing of all batches."""
        processor = BatchProcessor(max_batch_size=10)

        processor.add_request("batch1", {"id": 1})
        processor.add_request("batch2", {"id": 2})

        # Force process all
        all_batches = processor.force_process_all()
        assert len(all_batches) == 2
        assert "batch1" in all_batches
        assert "batch2" in all_batches
        assert len(all_batches["batch1"]) == 1
        assert len(all_batches["batch2"]) == 1


class TestDataExporter:
    """Test data export functionality."""

    def test_json_export(self):
        """Test JSON export."""
        import tempfile
        import json

        data = {"key": "value", "number": 42, "nested": {"inner": "data"}}

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name

        try:
            DataExporter.to_json(data, temp_path)

            # Read back and verify
            with open(temp_path, 'r') as f:
                loaded_data = json.load(f)

            assert loaded_data == data
        finally:
            import os
            os.unlink(temp_path)

    def test_csv_export(self):
        """Test CSV export."""
        import tempfile
        import csv

        data = [
            {"name": "Alice", "age": 30, "city": "NYC"},
            {"name": "Bob", "age": 25, "city": "LA"},
        ]

        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            temp_path = f.name

        try:
            DataExporter.to_csv(data, temp_path)

            # Read back and verify
            with open(temp_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)

            assert len(rows) == 2
            assert rows[0]["name"] == "Alice"
            assert rows[0]["age"] == "30"
            assert rows[1]["name"] == "Bob"
        finally:
            import os
            os.unlink(temp_path)

    def test_flatten_response(self):
        """Test response flattening."""
        nested_data = {
            "user": {
                "name": "Alice",
                "profile": {
                    "age": 30,
                    "hobbies": ["reading", "coding"]
                }
            },
            "active": True
        }

        flattened = DataExporter.flatten_response(nested_data)

        assert flattened["user.name"] == "Alice"
        assert flattened["user.profile.age"] == 30
        assert flattened["user.profile.hobbies[0]"] == "reading"
        assert flattened["user.profile.hobbies[1]"] == "coding"
        assert flattened["active"] is True


class TestPaginator:
    """Test pagination functionality."""

    def test_paginator_basic(self):
        """Test basic pagination."""
        # Mock client method that returns pages
        class MockResponse:
            def __init__(self, data, has_more=True):
                self.data = data
                self.has_more = has_more

        call_count = 0
        def mock_client_method(**kwargs):
            nonlocal call_count
            call_count += 1
            page = kwargs.get("page", 1)

            if page == 1:
                return MockResponse([{"id": 1}, {"id": 2}], True)
            elif page == 2:
                return MockResponse([{"id": 3}, {"id": 4}], False)
            else:
                return MockResponse([], False)

        paginator = Paginator(mock_client_method, page_size=2)

        # Collect all items
        items = list(paginator.iterate_all())

        assert len(items) == 4
        assert items[0]["id"] == 1
        assert items[1]["id"] == 2
        assert items[2]["id"] == 3
        assert items[3]["id"] == 4
        assert call_count == 2  # Should have made 2 API calls

    def test_paginator_no_pagination(self):
        """Test when API doesn't support pagination."""
        def mock_client_method(**kwargs):
            return [{"id": 1}, {"id": 2}, {"id": 3}]

        paginator = Paginator(mock_client_method)

        items = list(paginator.iterate_all())
        assert len(items) == 3


class TestResponseCache:
    """Test response caching functionality."""

    def test_cache_basic_operations(self):
        """Test basic cache operations."""
        cache = ResponseCache(max_size=10, default_ttl=60)

        # Test cache miss
        assert cache.get("GET", "/test") is None

        # Test cache set and get
        cache.set("GET", "/test", {"data": "value"})
        result = cache.get("GET", "/test")
        assert result == {"data": "value"}

        # Test cache size
        assert cache.size() == 1

        # Test cache clear
        cache.clear()
        assert cache.size() == 0
        assert cache.get("GET", "/test") is None

    def test_cache_with_params(self):
        """Test caching with query parameters."""
        cache = ResponseCache()

        # Different params should be cached separately
        cache.set("GET", "/search", {"results": [1, 2, 3]}, params={"q": "test"})
        cache.set("GET", "/search", {"results": [4, 5, 6]}, params={"q": "other"})

        result1 = cache.get("GET", "/search", params={"q": "test"})
        result2 = cache.get("GET", "/search", params={"q": "other"})

        assert result1 == {"results": [1, 2, 3]}
        assert result2 == {"results": [4, 5, 6]}
        assert cache.size() == 2

    def test_cache_ttl(self):
        """Test cache TTL functionality."""
        import time

        cache = ResponseCache(default_ttl=1)  # 1 second TTL

        cache.set("GET", "/test", {"data": "value"})
        assert cache.get("GET", "/test") == {"data": "value"}

        # Wait for expiration
        time.sleep(1.1)
        assert cache.get("GET", "/test") is None

    def test_cache_max_size(self):
        """Test cache size limits."""
        cache = ResponseCache(max_size=2)

        cache.set("GET", "/test1", {"data": "value1"})
        cache.set("GET", "/test2", {"data": "value2"})
        cache.set("GET", "/test3", {"data": "value3"})  # Should evict test1

        assert cache.size() == 2
        assert cache.get("GET", "/test1") is None  # Evicted
        assert cache.get("GET", "/test2") == {"data": "value2"}
        assert cache.get("GET", "/test3") == {"data": "value3"}


class TestRateLimiter:
    """Test rate limiting functionality."""

    def test_rate_limiter_basic(self):
        """Test basic rate limiting."""
        limiter = RateLimiter(requests_per_minute=10)

        # Should allow initial requests
        assert limiter.acquire() is True
        assert limiter.acquire() is True

        # Consume all tokens
        for _ in range(8):
            assert limiter.acquire() is True

        # Should be rate limited now
        assert limiter.acquire() is False

    def test_rate_limiter_wait_time(self):
        """Test wait time calculation."""
        limiter = RateLimiter(requests_per_minute=60)  # 1 request per second

        # Consume all tokens
        for _ in range(60):
            limiter.acquire()

        # Should need to wait
        wait_time = limiter.wait_time()
        assert wait_time > 0
        assert wait_time <= 1.0  # Should not wait more than 1 second

    def test_rate_limiter_refill(self):
        """Test token refill over time."""
        import time

        limiter = RateLimiter(requests_per_minute=120)  # 2 requests per second

        # Consume all tokens
        for _ in range(120):
            limiter.acquire()

        assert limiter.acquire() is False

        # Wait for some refill
        time.sleep(0.6)  # Should refill 1.2 tokens

        # Should be able to acquire at least 1 token
        assert limiter.acquire() is True

    def test_custom_headers_override_defaults(self):
        """Test that custom headers override default headers."""
        from gradient import Gradient

        client = Gradient(
            base_url="http://test.com",
            access_token="test_token",
            default_headers={"X-Default": "default-value"},
            custom_headers={"X-Default": "custom-override", "X-Custom": "custom-value"}
        )

        # Custom headers should override default headers in _custom_headers
        assert "X-Default" in client._custom_headers
        assert client._custom_headers["X-Default"] == "custom-override"
        assert "X-Custom" in client._custom_headers
        assert client._custom_headers["X-Custom"] == "custom-value"

    def test_custom_headers_in_async_client(self):
        """Test that custom headers are properly set in async client."""
        from gradient import AsyncGradient

        client = AsyncGradient(
            base_url="http://test.com",
            access_token="test_token",
            custom_headers={"X-Custom": "custom-value"}
        )

        # Check that custom headers are in the client's _custom_headers
        assert "X-Custom" in client._custom_headers
        assert client._custom_headers["X-Custom"] == "custom-value"