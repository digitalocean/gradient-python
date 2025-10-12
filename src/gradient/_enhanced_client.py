"""Enhanced client with performance, security, and debugging features."""

import time
import logging
from typing import Any, Dict, Optional, Union, Callable
from contextlib import contextmanager

from ._client import Gradient, AsyncGradient
from ._performance import get_request_cache, get_performance_tracker, get_connection_pool
from ._retry import create_retry_handler, RetryConfig, CircuitBreakerConfig
from ._debug import get_debugger, RequestLogger
from ._security import RequestSigner, TokenValidator, get_rate_limiter, SecureHeaders
from ._base_client import DefaultHttpxClient


class EnhancedGradient(Gradient):
    """Enhanced Gradient client with performance, security, and debugging features."""
    
    def __init__(
        self,
        *,
        access_token: Optional[str] = None,
        model_access_key: Optional[str] = None,
        agent_access_key: Optional[str] = None,
        agent_endpoint: Optional[str] = None,
        inference_endpoint: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: int = 2,
        # Enhanced features
        enable_caching: bool = True,
        cache_ttl: int = 300,
        enable_performance_tracking: bool = True,
        enable_debug: bool = False,
        enable_request_signing: bool = False,
        signing_secret: Optional[str] = None,
        enable_rate_limiting: bool = True,
        rate_limit_requests: int = 100,
        rate_limit_window: int = 60,
        retry_config: Optional[RetryConfig] = None,
        circuit_breaker_config: Optional[CircuitBreakerConfig] = None,
        **kwargs
    ):
        # Initialize performance features
        self._cache = get_request_cache() if enable_caching else None
        self._performance_tracker = get_performance_tracker() if enable_performance_tracking else None
        self._debugger = get_debugger()
        self._request_logger = RequestLogger()
        
        # Initialize security features
        self._request_signer = None
        if enable_request_signing and signing_secret:
            self._request_signer = RequestSigner(signing_secret)
        
        self._rate_limiter = get_rate_limiter() if enable_rate_limiting else None
        if self._rate_limiter and (rate_limit_requests != 100 or rate_limit_window != 60):
            from ._security import RateLimiter
            self._rate_limiter = RateLimiter(rate_limit_requests, rate_limit_window)
        
        # Initialize retry handler
        self._retry_handler = create_retry_handler(retry_config, circuit_breaker_config)
        
        # Configure connection pooling
        connection_pool = get_connection_pool()
        if 'http_client' not in kwargs:
            try:
                pool_config = connection_pool.get_pool_config()
                kwargs['http_client'] = DefaultHttpxClient(**pool_config)
            except Exception:
                # Fallback to default client if pool config fails
                kwargs['http_client'] = DefaultHttpxClient()
        
        # Enable debugging if requested
        if enable_debug:
            self._debugger.enable()
        
        # Validate tokens
        if access_token and not TokenValidator.validate_token_format(access_token):
            logging.warning("Access token format appears invalid")
        
        if model_access_key and not TokenValidator.validate_token_format(model_access_key):
            logging.warning("Model access key format appears invalid")
        
        super().__init__(
            access_token=access_token,
            model_access_key=model_access_key,
            agent_access_key=agent_access_key,
            agent_endpoint=agent_endpoint,
            inference_endpoint=inference_endpoint,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            **kwargs
        )
    
    def _make_request(self, method: str, url: str, **kwargs) -> Any:
        """Enhanced request method with caching, performance tracking, and security."""
        start_time = time.time()
        
        # Rate limiting check
        if self._rate_limiter:
            client_id = getattr(self, '_access_token', 'default')[:10]  # Use part of token as ID
            if not self._rate_limiter.is_allowed(client_id):
                wait_time = self._rate_limiter.time_until_reset(client_id)
                raise Exception(f"Rate limit exceeded. Try again in {wait_time:.1f} seconds")
        
        # Extract request details for caching and logging
        headers = kwargs.get('headers', {})
        params = kwargs.get('params')
        body = kwargs.get('json') or kwargs.get('data')
        
        # Add security headers
        security_headers = SecureHeaders.get_security_headers()
        headers.update(security_headers)
        kwargs['headers'] = headers
        
        # Add request signing if enabled
        if self._request_signer:
            signature_headers = self._request_signer.sign_request(method, url, headers, body)
            headers.update(signature_headers)
        
        # Check cache first
        cached_response = None
        if self._cache and method.upper() == 'GET':
            cached_response = self._cache.get(method, url, params, body)
            if cached_response:
                if self._performance_tracker:
                    self._performance_tracker.record_request(
                        method, url, time.time() - start_time, 200, cached=True
                    )
                return cached_response
        
        # Log request details
        self._debugger.log_request(method, url, headers, params, body)
        self._request_logger.log_curl_command(method, url, headers, body)
        
        try:
            # Make request with retry logic
            response = self._retry_handler.retry(super()._make_request, method, url, **kwargs)
            
            duration = time.time() - start_time
            
            # Log response
            response_headers = getattr(response, 'headers', {})
            response_body = getattr(response, 'json', lambda: None)()
            status_code = getattr(response, 'status_code', 200)
            
            self._debugger.log_response(status_code, response_headers, response_body, duration)
            
            # Cache successful GET responses
            if self._cache and method.upper() == 'GET' and status_code < 400:
                self._cache.set(method, url, response, params=params, body=body)
            
            # Track performance
            if self._performance_tracker:
                self._performance_tracker.record_request(method, url, duration, status_code)
            
            return response
            
        except Exception as e:
            duration = time.time() - start_time
            
            # Log error
            self._debugger.log_error(e, {
                'method': method,
                'url': url,
                'duration': duration
            })
            
            # Track error
            if self._performance_tracker:
                status_code = getattr(e, 'status_code', 500)
                self._performance_tracker.record_request(method, url, duration, status_code)
            
            raise
    
    @contextmanager
    def performance_monitoring(self):
        """Context manager for performance monitoring."""
        if not self._performance_tracker:
            yield
            return
        
        start_metrics = self._performance_tracker.get_metrics()
        yield
        end_metrics = self._performance_tracker.get_metrics()
        
        # Log performance summary
        logging.info("Performance Summary:")
        for endpoint, metrics in end_metrics.items():
            if endpoint not in start_metrics:
                logging.info(f"  {endpoint}: {metrics}")
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics."""
        if not self._performance_tracker:
            return {}
        return self._performance_tracker.get_metrics()
    
    def clear_cache(self) -> None:
        """Clear the request cache."""
        if self._cache:
            self._cache.clear()
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        if not self._cache:
            return {}
        return {
            'size': self._cache.size(),
            'max_size': self._cache._max_size,
            'default_ttl': self._cache._default_ttl
        }
    
    def enable_debug(self) -> None:
        """Enable debug logging."""
        self._debugger.enable()
    
    def disable_debug(self) -> None:
        """Disable debug logging."""
        self._debugger.disable()


class EnhancedAsyncGradient(AsyncGradient):
    """Enhanced async Gradient client with performance, security, and debugging features."""
    
    def __init__(
        self,
        *,
        access_token: Optional[str] = None,
        model_access_key: Optional[str] = None,
        agent_access_key: Optional[str] = None,
        agent_endpoint: Optional[str] = None,
        inference_endpoint: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: int = 2,
        # Enhanced features
        enable_caching: bool = True,
        cache_ttl: int = 300,
        enable_performance_tracking: bool = True,
        enable_debug: bool = False,
        enable_request_signing: bool = False,
        signing_secret: Optional[str] = None,
        enable_rate_limiting: bool = True,
        rate_limit_requests: int = 100,
        rate_limit_window: int = 60,
        retry_config: Optional[RetryConfig] = None,
        circuit_breaker_config: Optional[CircuitBreakerConfig] = None,
        **kwargs
    ):
        # Initialize same features as sync client
        self._cache = get_request_cache() if enable_caching else None
        self._performance_tracker = get_performance_tracker() if enable_performance_tracking else None
        self._debugger = get_debugger()
        self._request_logger = RequestLogger()
        
        self._request_signer = None
        if enable_request_signing and signing_secret:
            self._request_signer = RequestSigner(signing_secret)
        
        self._rate_limiter = get_rate_limiter() if enable_rate_limiting else None
        if self._rate_limiter and (rate_limit_requests != 100 or rate_limit_window != 60):
            from ._security import RateLimiter
            self._rate_limiter = RateLimiter(rate_limit_requests, rate_limit_window)
        
        self._retry_handler = create_retry_handler(retry_config, circuit_breaker_config)
        
        # Configure connection pooling
        connection_pool = get_connection_pool()
        if 'http_client' not in kwargs:
            try:
                pool_config = connection_pool.get_pool_config()
                kwargs['http_client'] = DefaultHttpxClient(**pool_config)
            except Exception:
                # Fallback to default client if pool config fails
                kwargs['http_client'] = DefaultHttpxClient()
        
        if enable_debug:
            self._debugger.enable()
        
        # Validate tokens
        if access_token and not TokenValidator.validate_token_format(access_token):
            logging.warning("Access token format appears invalid")
        
        super().__init__(
            access_token=access_token,
            model_access_key=model_access_key,
            agent_access_key=agent_access_key,
            agent_endpoint=agent_endpoint,
            inference_endpoint=inference_endpoint,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            **kwargs
        )
    
    async def _make_request(self, method: str, url: str, **kwargs) -> Any:
        """Enhanced async request method."""
        start_time = time.time()
        
        # Rate limiting check
        if self._rate_limiter:
            client_id = getattr(self, '_access_token', 'default')[:10]
            if not self._rate_limiter.is_allowed(client_id):
                wait_time = self._rate_limiter.time_until_reset(client_id)
                raise Exception(f"Rate limit exceeded. Try again in {wait_time:.1f} seconds")
        
        # Extract request details
        headers = kwargs.get('headers', {})
        params = kwargs.get('params')
        body = kwargs.get('json') or kwargs.get('data')
        
        # Add security headers
        security_headers = SecureHeaders.get_security_headers()
        headers.update(security_headers)
        kwargs['headers'] = headers
        
        # Add request signing if enabled
        if self._request_signer:
            signature_headers = self._request_signer.sign_request(method, url, headers, body)
            headers.update(signature_headers)
        
        # Check cache first
        cached_response = None
        if self._cache and method.upper() == 'GET':
            cached_response = self._cache.get(method, url, params, body)
            if cached_response:
                if self._performance_tracker:
                    self._performance_tracker.record_request(
                        method, url, time.time() - start_time, 200, cached=True
                    )
                return cached_response
        
        # Log request details
        self._debugger.log_request(method, url, headers, params, body)
        self._request_logger.log_curl_command(method, url, headers, body)
        
        try:
            # Make request with retry logic
            response = await self._retry_handler.aretry(super()._make_request, method, url, **kwargs)
            
            duration = time.time() - start_time
            
            # Log response
            response_headers = getattr(response, 'headers', {})
            response_body = getattr(response, 'json', lambda: None)()
            status_code = getattr(response, 'status_code', 200)
            
            self._debugger.log_response(status_code, response_headers, response_body, duration)
            
            # Cache successful GET responses
            if self._cache and method.upper() == 'GET' and status_code < 400:
                self._cache.set(method, url, response, params=params, body=body)
            
            # Track performance
            if self._performance_tracker:
                self._performance_tracker.record_request(method, url, duration, status_code)
            
            return response
            
        except Exception as e:
            duration = time.time() - start_time
            
            # Log error
            self._debugger.log_error(e, {
                'method': method,
                'url': url,
                'duration': duration
            })
            
            # Track error
            if self._performance_tracker:
                status_code = getattr(e, 'status_code', 500)
                self._performance_tracker.record_request(method, url, duration, status_code)
            
            raise
    
    # Same utility methods as sync client
    def get_performance_metrics(self) -> Dict[str, Any]:
        if not self._performance_tracker:
            return {}
        return self._performance_tracker.get_metrics()
    
    def clear_cache(self) -> None:
        if self._cache:
            self._cache.clear()
    
    def get_cache_stats(self) -> Dict[str, Any]:
        if not self._cache:
            return {}
        return {
            'size': self._cache.size(),
            'max_size': self._cache._max_size,
            'default_ttl': self._cache._default_ttl
        }
    
    def enable_debug(self) -> None:
        self._debugger.enable()
    
    def disable_debug(self) -> None:
        self._debugger.disable()
