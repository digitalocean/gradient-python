"""Tests for response caching functionality."""

import time
import pytest
from gradient._utils import ResponseCache


class TestResponseCache:
    """Test response caching functionality."""

    def test_cache_basic_operations(self):
        """Test basic cache operations."""
        cache = ResponseCache(max_size=3, default_ttl=1)

        # Test set and get
        cache.set("GET", "/api/test", {"data": "value"})
        result = cache.get("GET", "/api/test")
        assert result == {"data": "value"}

        # Test cache miss
        result = cache.get("GET", "/api/missing")
        assert result is None

    def test_cache_with_params(self):
        """Test caching with query parameters."""
        cache = ResponseCache()

        # Set with params
        cache.set("GET", "/api/search", {"results": []}, params={"q": "test"})

        # Get with same params should hit
        result = cache.get("GET", "/api/search", params={"q": "test"})
        assert result == {"results": []}

        # Get with different params should miss
        result = cache.get("GET", "/api/search", params={"q": "other"})
        assert result is None

    def test_cache_ttl(self):
        """Test cache TTL functionality."""
        cache = ResponseCache(default_ttl=0.1)  # Very short TTL

        cache.set("GET", "/api/test", {"data": "value"})

        # Should hit immediately
        result = cache.get("GET", "/api/test")
        assert result == {"data": "value"}

        # Wait for expiry
        time.sleep(0.2)

        # Should miss after expiry
        result = cache.get("GET", "/api/test")
        assert result is None

    def test_cache_max_size(self):
        """Test cache size limits with LRU eviction."""
        cache = ResponseCache(max_size=2)

        # Fill cache
        cache.set("GET", "/api/1", "data1")
        cache.set("GET", "/api/2", "data2")
        assert cache.size() == 2

        # Add third item (should evict first)
        cache.set("GET", "/api/3", "data3")
        assert cache.size() == 2

        # First item should be gone
        assert cache.get("GET", "/api/1") is None
        assert cache.get("GET", "/api/2") == "data2"
        assert cache.get("GET", "/api/3") == "data3"

    def test_cache_clear(self):
        """Test cache clearing."""
        cache = ResponseCache()

        cache.set("GET", "/api/test", {"data": "value"})
        assert cache.size() == 1

        cache.clear()
        assert cache.size() == 0
        assert cache.get("GET", "/api/test") is None