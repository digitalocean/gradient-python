"""Tests for enhanced features of the Gradient SDK."""

import pytest
import time
import asyncio
from unittest.mock import Mock, patch, MagicMock

from gradient._performance import RequestCache, ConnectionPool, PerformanceTracker
from gradient._retry import RetryHandler, RetryConfig, CircuitBreaker, CircuitBreakerConfig, CircuitState
from gradient._debug import GradientDebugger, RequestLogger
from gradient._security import RequestSigner, TokenValidator, RateLimiter, SecureHeaders, InputValidator
from gradient._enhanced_client import EnhancedGradient, EnhancedAsyncGradient


class TestRequestCache:
    """Test request caching functionality."""
    
    def test_cache_basic_operations(self):
        cache = RequestCache(default_ttl=60, max_size=10)
        
        # Test cache miss
        result = cache.get('GET', '/test')
        assert result is None
        
        # Test cache set and hit
        cache.set('GET', '/test', {'data': 'test'})
        result = cache.get('GET', '/test')
        assert result == {'data': 'test'}
        
        # Test cache size
        assert cache.size() == 1
    
    def test_cache_expiration(self):
        cache = RequestCache(default_ttl=1, max_size=10)
        
        cache.set('GET', '/test', {'data': 'test'})
        assert cache.get('GET', '/test') == {'data': 'test'}
        
        # Wait for expiration
        time.sleep(1.1)
        assert cache.get('GET', '/test') is None
    
    def test_cache_max_size(self):
        cache = RequestCache(default_ttl=60, max_size=2)
        
        cache.set('GET', '/test1', {'data': 'test1'})
        cache.set('GET', '/test2', {'data': 'test2'})
        cache.set('GET', '/test3', {'data': 'test3'})
        
        # Should only have 2 items due to max_size
        assert cache.size() == 2
    
    def test_cache_key_generation(self):
        cache = RequestCache()
        
        # Same request should generate same key
        cache.set('GET', '/test', {'data': 'test'}, params={'q': 'search'})
        result = cache.get('GET', '/test', params={'q': 'search'})
        assert result == {'data': 'test'}
        
        # Different params should generate different key
        result = cache.get('GET', '/test', params={'q': 'different'})
        assert result is None


class TestPerformanceTracker:
    """Test performance tracking functionality."""
    
    def test_record_request(self):
        tracker = PerformanceTracker()
        
        tracker.record_request('GET', '/test', 0.5, 200)
        metrics = tracker.get_metrics('GET /test')
        
        assert metrics['count'] == 1
        assert metrics['total_duration'] == 0.5
        assert metrics['min_duration'] == 0.5
        assert metrics['max_duration'] == 0.5
        assert metrics['cache_hits'] == 0
        assert metrics['errors'] == 0
    
    def test_record_cached_request(self):
        tracker = PerformanceTracker()
        
        tracker.record_request('GET', '/test', 0.1, 200, cached=True)
        metrics = tracker.get_metrics('GET /test')
        
        assert metrics['count'] == 1
        assert metrics['cache_hits'] == 1
        assert metrics['total_duration'] == 0.0  # Cached requests don't add to duration
    
    def test_record_error(self):
        tracker = PerformanceTracker()
        
        tracker.record_request('GET', '/test', 0.5, 500)
        metrics = tracker.get_metrics('GET /test')
        
        assert metrics['errors'] == 1
    
    def test_get_summary_metrics(self):
        tracker = PerformanceTracker()
        
        tracker.record_request('GET', '/test1', 0.5, 200)
        tracker.record_request('GET', '/test2', 0.3, 200)
        
        summary = tracker.get_metrics()
        assert 'GET /test1' in summary
        assert 'GET /test2' in summary
        assert summary['GET /test1']['avg_duration_ms'] == 500.0


class TestRetryHandler:
    """Test retry functionality."""
    
    def test_successful_request_no_retry(self):
        config = RetryConfig(max_attempts=3)
        handler = RetryHandler(config)
        
        mock_func = Mock(return_value='success')
        result = handler.retry(mock_func)
        
        assert result == 'success'
        assert mock_func.call_count == 1
    
    def test_retry_on_retryable_exception(self):
        config = RetryConfig(max_attempts=3, base_delay=0.01)
        handler = RetryHandler(config)
        
        mock_func = Mock(side_effect=[ConnectionError(), ConnectionError(), 'success'])
        result = handler.retry(mock_func)
        
        assert result == 'success'
        assert mock_func.call_count == 3
    
    def test_max_attempts_exceeded(self):
        config = RetryConfig(max_attempts=2, base_delay=0.01)
        handler = RetryHandler(config)
        
        mock_func = Mock(side_effect=ConnectionError())
        
        with pytest.raises(ConnectionError):
            handler.retry(mock_func)
        
        assert mock_func.call_count == 2
    
    def test_non_retryable_exception(self):
        config = RetryConfig(max_attempts=3)
        handler = RetryHandler(config)
        
        mock_func = Mock(side_effect=ValueError())
        
        with pytest.raises(ValueError):
            handler.retry(mock_func)
        
        assert mock_func.call_count == 1
    
    @pytest.mark.asyncio
    async def test_async_retry(self):
        config = RetryConfig(max_attempts=3, base_delay=0.01)
        handler = RetryHandler(config)
        
        async def mock_async_func():
            if mock_async_func.call_count == 0:
                mock_async_func.call_count += 1
                raise ConnectionError()
            return 'success'
        
        mock_async_func.call_count = 0
        
        result = await handler.aretry(mock_async_func)
        assert result == 'success'


class TestCircuitBreaker:
    """Test circuit breaker functionality."""
    
    def test_circuit_closed_initially(self):
        config = CircuitBreakerConfig(failure_threshold=3)
        breaker = CircuitBreaker(config)
        
        assert breaker.state == CircuitState.CLOSED
        assert breaker.can_execute() is True
    
    def test_circuit_opens_after_failures(self):
        config = CircuitBreakerConfig(failure_threshold=2)
        breaker = CircuitBreaker(config)
        
        # Record failures
        breaker._record_failure()
        assert breaker.state == CircuitState.CLOSED
        
        breaker._record_failure()
        assert breaker.state == CircuitState.OPEN
        assert breaker.can_execute() is False
    
    def test_circuit_half_open_after_timeout(self):
        config = CircuitBreakerConfig(failure_threshold=1, recovery_timeout=0.1)
        breaker = CircuitBreaker(config)
        
        # Open circuit
        breaker._record_failure()
        assert breaker.state == CircuitState.OPEN
        
        # Wait for recovery timeout
        time.sleep(0.2)
        assert breaker.can_execute() is True
        assert breaker.state == CircuitState.HALF_OPEN
    
    def test_circuit_closes_after_success(self):
        config = CircuitBreakerConfig(failure_threshold=1, success_threshold=2)
        breaker = CircuitBreaker(config)
        
        # Open circuit
        breaker._record_failure()
        breaker.state = CircuitState.HALF_OPEN  # Simulate half-open state
        
        # Record successes
        breaker._record_success()
        assert breaker.state == CircuitState.HALF_OPEN
        
        breaker._record_success()
        assert breaker.state == CircuitState.CLOSED


class TestRequestSigner:
    """Test request signing functionality."""
    
    def test_sign_request(self):
        signer = RequestSigner('secret-key')
        
        signature_headers = signer.sign_request('GET', '/test', {}, None)
        
        assert 'X-Gradient-Timestamp' in signature_headers
        assert 'X-Gradient-Nonce' in signature_headers
        assert 'X-Gradient-Signature' in signature_headers
        assert 'X-Gradient-Algorithm' in signature_headers
    
    def test_verify_signature(self):
        signer = RequestSigner('secret-key')
        
        # Sign a request
        headers = {}
        signature_headers = signer.sign_request('GET', '/test', headers, None)
        headers.update(signature_headers)
        
        # Verify the signature
        is_valid = signer.verify_signature('GET', '/test', headers, None)
        assert is_valid is True
    
    def test_verify_invalid_signature(self):
        signer = RequestSigner('secret-key')
        
        headers = {
            'X-Gradient-Timestamp': str(int(time.time())),
            'X-Gradient-Nonce': 'test-nonce',
            'X-Gradient-Signature': 'invalid-signature',
            'X-Gradient-Algorithm': 'SHA256'
        }
        
        is_valid = signer.verify_signature('GET', '/test', headers, None)
        assert is_valid is False


class TestTokenValidator:
    """Test token validation functionality."""
    
    def test_validate_valid_token(self):
        valid_token = 'sk-1234567890abcdef1234567890abcdef'
        assert TokenValidator.validate_token_format(valid_token) is True
    
    def test_validate_invalid_token_too_short(self):
        short_token = 'sk-123'
        assert TokenValidator.validate_token_format(short_token) is False
    
    def test_validate_invalid_token_bad_chars(self):
        bad_token = 'sk-1234567890abcdef!@#$%^&*()'
        assert TokenValidator.validate_token_format(bad_token) is False
    
    def test_validate_with_prefix(self):
        token = 'sk-1234567890abcdef1234567890abcdef'
        assert TokenValidator.validate_token_format(token, 'sk-') is True
        assert TokenValidator.validate_token_format(token, 'pk-') is False
    
    def test_mask_token(self):
        token = 'sk-1234567890abcdef1234567890abcdef'
        masked = TokenValidator.mask_token(token)
        assert masked.startswith('sk-1')
        assert masked.endswith('cdef')
        assert '...' in masked


class TestRateLimiter:
    """Test rate limiting functionality."""
    
    def test_rate_limit_allows_requests(self):
        limiter = RateLimiter(max_requests=5, time_window=60)
        
        # Should allow first 5 requests
        for i in range(5):
            assert limiter.is_allowed('user1') is True
        
        # Should deny 6th request
        assert limiter.is_allowed('user1') is False
    
    def test_rate_limit_different_users(self):
        limiter = RateLimiter(max_requests=2, time_window=60)
        
        # Each user should have their own limit
        assert limiter.is_allowed('user1') is True
        assert limiter.is_allowed('user2') is True
        assert limiter.is_allowed('user1') is True
        assert limiter.is_allowed('user2') is True
        
        # Both should be at limit now
        assert limiter.is_allowed('user1') is False
        assert limiter.is_allowed('user2') is False
    
    def test_rate_limit_time_window(self):
        limiter = RateLimiter(max_requests=1, time_window=1)
        
        assert limiter.is_allowed('user1') is True
        assert limiter.is_allowed('user1') is False
        
        # Wait for time window to pass
        time.sleep(1.1)
        assert limiter.is_allowed('user1') is True


class TestSecureHeaders:
    """Test secure headers functionality."""
    
    def test_get_security_headers(self):
        headers = SecureHeaders.get_security_headers()
        
        assert 'X-Content-Type-Options' in headers
        assert 'X-Frame-Options' in headers
        assert 'X-XSS-Protection' in headers
        assert headers['X-Content-Type-Options'] == 'nosniff'
    
    def test_sanitize_headers(self):
        dirty_headers = {
            'Valid-Header': 'valid-value',
            'Header-With-Control\x00Char': 'value',
            '': 'empty-key',
            'Empty-Value': '',
            'Normal-Header': 'normal\x7fvalue'
        }
        
        clean_headers = SecureHeaders.sanitize_headers(dirty_headers)
        
        assert 'Valid-Header' in clean_headers
        assert 'Header-With-ControlChar' in clean_headers  # Control char removed
        assert '' not in clean_headers  # Empty key removed
        assert 'Empty-Value' not in clean_headers  # Empty value removed


class TestInputValidator:
    """Test input validation functionality."""
    
    def test_validate_valid_url(self):
        assert InputValidator.validate_url('https://api.example.com/v1/test') is True
        assert InputValidator.validate_url('http://localhost:8080/api') is True
    
    def test_validate_invalid_url(self):
        assert InputValidator.validate_url('ftp://example.com') is False
        assert InputValidator.validate_url('https://example.com/<script>') is False
        assert InputValidator.validate_url('') is False
        assert InputValidator.validate_url(None) is False
    
    def test_sanitize_string(self):
        dirty_string = 'Hello\x00World\x1f!\nThis is a test.'
        clean_string = InputValidator.sanitize_string(dirty_string)
        
        assert '\x00' not in clean_string
        assert '\x1f' not in clean_string
        assert '\n' in clean_string  # Newlines should be preserved
    
    def test_validate_json(self):
        assert InputValidator.validate_json('{"key": "value"}') is True
        assert InputValidator.validate_json('[]') is True
        assert InputValidator.validate_json('invalid json') is False
        assert InputValidator.validate_json('') is False


class TestGradientDebugger:
    """Test debugging functionality."""
    
    def test_debugger_enable_disable(self):
        debugger = GradientDebugger()
        
        assert debugger.enabled is False
        
        debugger.enable()
        assert debugger.enabled is True
        
        debugger.disable()
        assert debugger.enabled is False
    
    def test_mask_sensitive_data(self):
        debugger = GradientDebugger()
        
        data = {
            'username': 'user',
            'password': 'secret',
            'authorization': 'Bearer token',
            'normal_field': 'value'
        }
        
        masked = debugger._mask_sensitive_data(data, ['password', 'authorization'])
        
        assert masked['username'] == 'user'
        assert masked['password'] == '***MASKED***'
        assert masked['authorization'] == '***MASKED***'
        assert masked['normal_field'] == 'value'


@pytest.mark.integration
class TestEnhancedClient:
    """Integration tests for enhanced client."""
    
    @patch('gradient._enhanced_client.super')
    def test_enhanced_client_initialization(self, mock_super):
        client = EnhancedGradient(
            access_token='test-token',
            enable_caching=True,
            enable_performance_tracking=True,
            enable_debug=False,
        )
        
        assert client._cache is not None
        assert client._performance_tracker is not None
        assert client._debugger is not None
    
    @patch('gradient._enhanced_client.super')
    def test_enhanced_client_with_security(self, mock_super):
        client = EnhancedGradient(
            access_token='test-token',
            enable_request_signing=True,
            signing_secret='test-secret',
            enable_rate_limiting=True,
        )
        
        assert client._request_signer is not None
        assert client._rate_limiter is not None
    
    def test_cache_stats(self):
        client = EnhancedGradient(
            access_token='test-token',
            enable_caching=True,
        )
        
        stats = client.get_cache_stats()
        assert 'size' in stats
        assert 'max_size' in stats
        assert 'default_ttl' in stats
    
    def test_performance_metrics(self):
        client = EnhancedGradient(
            access_token='test-token',
            enable_performance_tracking=True,
        )
        
        metrics = client.get_performance_metrics()
        assert isinstance(metrics, dict)
    
    def test_debug_enable_disable(self):
        client = EnhancedGradient(
            access_token='test-token',
            enable_debug=False,
        )
        
        assert client._debugger.enabled is False
        
        client.enable_debug()
        assert client._debugger.enabled is True
        
        client.disable_debug()
        assert client._debugger.enabled is False


if __name__ == '__main__':
    pytest.main([__file__])
