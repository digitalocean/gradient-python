"""Tests for rate limiting functionality."""

import time
import pytest
from gradient._utils import RateLimiter


class TestRateLimiter:
    """Test rate limiting functionality."""

    def test_rate_limiter_basic(self):
        """Test basic rate limiter operations."""
        limiter = RateLimiter(requests_per_minute=10)

        # Should allow initial requests
        assert limiter.acquire() is True
        assert limiter.acquire() is True

        # Should deny when tokens exhausted
        limiter.tokens = 0  # Force exhaustion
        assert limiter.acquire() is False

    def test_rate_limiter_wait_time(self):
        """Test wait time calculation."""
        limiter = RateLimiter(requests_per_minute=60)  # 1 request per second

        # Exhaust tokens
        limiter.tokens = 0

        # Should calculate correct wait time
        wait_time = limiter.wait_time()
        assert wait_time > 0
        assert wait_time <= 1.0  # Should not exceed 1 second

    def test_rate_limiter_refill(self):
        """Test token refill over time."""
        limiter = RateLimiter(requests_per_minute=60)  # 1 token per second

        # Exhaust tokens
        limiter.tokens = 0
        start_time = limiter._now()

        # Wait for refill
        time.sleep(0.1)

        # Should have refilled some tokens
        limiter._refill()
        assert limiter.tokens > 0

    def test_rate_limiter_custom_rate(self):
        """Test custom rate limits."""
        limiter = RateLimiter(requests_per_minute=120)  # 2 requests per second

        # Should have double the tokens of default
        assert limiter.requests_per_minute == 120
        assert limiter.refill_rate == 2.0