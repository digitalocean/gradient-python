"""Performance utilities for the Gradient SDK."""

import time
import hashlib
from typing import Any, Dict, Optional, Tuple, Union
from threading import Lock
import weakref


class RequestCache:
    """Simple in-memory cache for API responses with TTL support."""
    
    def __init__(self, default_ttl: int = 300, max_size: int = 1000):
        self._cache: Dict[str, Tuple[Any, float]] = {}
        self._default_ttl = default_ttl
        self._max_size = max_size
        self._lock = Lock()
    
    def _generate_key(self, method: str, url: str, params: Optional[Dict] = None, 
                     body: Optional[Union[str, bytes]] = None) -> str:
        """Generate a cache key from request parameters."""
        key_parts = [method.upper(), url]
        
        if params:
            sorted_params = sorted(params.items())
            key_parts.append(str(sorted_params))
        
        if body:
            if isinstance(body, bytes):
                body_str = body.decode('utf-8', errors='ignore')
            else:
                body_str = str(body)
            key_parts.append(body_str)
        
        key_string = '|'.join(key_parts)
        return hashlib.md5(key_string.encode()).hexdigest()
    
    def get(self, method: str, url: str, params: Optional[Dict] = None, 
            body: Optional[Union[str, bytes]] = None) -> Optional[Any]:
        """Get cached response if available and not expired."""
        key = self._generate_key(method, url, params, body)
        
        with self._lock:
            if key in self._cache:
                value, expiry = self._cache[key]
                if time.time() < expiry:
                    return value
                else:
                    del self._cache[key]
        
        return None
    
    def set(self, method: str, url: str, response: Any, ttl: Optional[int] = None,
            params: Optional[Dict] = None, body: Optional[Union[str, bytes]] = None) -> None:
        """Cache a response with TTL."""
        key = self._generate_key(method, url, params, body)
        ttl = ttl or self._default_ttl
        expiry = time.time() + ttl
        
        with self._lock:
            # Simple LRU: remove oldest if at capacity
            if len(self._cache) >= self._max_size:
                oldest_key = min(self._cache.keys(), 
                               key=lambda k: self._cache[k][1])
                del self._cache[oldest_key]
            
            self._cache[key] = (response, expiry)
    
    def clear(self) -> None:
        """Clear all cached responses."""
        with self._lock:
            self._cache.clear()
    
    def size(self) -> int:
        """Get current cache size."""
        with self._lock:
            return len(self._cache)


class ConnectionPool:
    """Manages HTTP connection pools for better performance."""
    
    def __init__(self, max_connections: int = 100, max_keepalive: int = 20):
        self.max_connections = max_connections
        self.max_keepalive = max_keepalive
        self._pools: Dict[str, Any] = {}
        self._lock = Lock()
    
    def get_pool_config(self) -> Dict[str, Any]:
        """Get connection pool configuration for httpx."""
        import httpx
        return {
            'limits': httpx.Limits(
                max_connections=self.max_connections,
                max_keepalive_connections=self.max_keepalive,
            ),
            'timeout': httpx.Timeout(
                connect=10.0,
                read=30.0,
                write=10.0,
                pool=5.0,
            )
        }


class PerformanceTracker:
    """Track performance metrics for API calls."""
    
    def __init__(self):
        self._metrics: Dict[str, Dict[str, Any]] = {}
        self._lock = Lock()
    
    def record_request(self, method: str, url: str, duration: float, 
                      status_code: int, cached: bool = False) -> None:
        """Record metrics for a request."""
        endpoint = f"{method.upper()} {url}"
        
        with self._lock:
            if endpoint not in self._metrics:
                self._metrics[endpoint] = {
                    'count': 0,
                    'total_duration': 0.0,
                    'min_duration': float('inf'),
                    'max_duration': 0.0,
                    'cache_hits': 0,
                    'errors': 0,
                }
            
            metrics = self._metrics[endpoint]
            metrics['count'] += 1
            
            if not cached:
                metrics['total_duration'] += duration
                metrics['min_duration'] = min(metrics['min_duration'], duration)
                metrics['max_duration'] = max(metrics['max_duration'], duration)
            else:
                metrics['cache_hits'] += 1
            
            if status_code >= 400:
                metrics['errors'] += 1
    
    def get_metrics(self, endpoint: Optional[str] = None) -> Dict[str, Any]:
        """Get performance metrics."""
        with self._lock:
            if endpoint:
                return self._metrics.get(endpoint, {})
            
            # Return summary of all endpoints
            summary = {}
            for ep, metrics in self._metrics.items():
                avg_duration = (metrics['total_duration'] / 
                              max(1, metrics['count'] - metrics['cache_hits']))
                
                summary[ep] = {
                    'requests': metrics['count'],
                    'cache_hit_rate': metrics['cache_hits'] / max(1, metrics['count']),
                    'error_rate': metrics['errors'] / max(1, metrics['count']),
                    'avg_duration_ms': round(avg_duration * 1000, 2),
                    'min_duration_ms': round(metrics['min_duration'] * 1000, 2),
                    'max_duration_ms': round(metrics['max_duration'] * 1000, 2),
                }
            
            return summary
    
    def reset(self) -> None:
        """Reset all metrics."""
        with self._lock:
            self._metrics.clear()


# Global instances
_request_cache = RequestCache()
_performance_tracker = PerformanceTracker()
_connection_pool = ConnectionPool()


def get_request_cache() -> RequestCache:
    """Get the global request cache instance."""
    return _request_cache


def get_performance_tracker() -> PerformanceTracker:
    """Get the global performance tracker instance."""
    return _performance_tracker


def get_connection_pool() -> ConnectionPool:
    """Get the global connection pool instance."""
    return _connection_pool
