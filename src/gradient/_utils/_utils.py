import logging
import time
from typing import Dict, Any, Optional, Callable, Union, List, TypeVar, Generic, Iterator, AsyncIterator
from functools import wraps
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed


class RequestMetrics:
    """Tracks metrics for API requests."""

    def __init__(self):
        self.requests_total = 0
        self.requests_by_endpoint: Dict[str, int] = defaultdict(int)
        self.requests_by_status: Dict[int, int] = defaultdict(int)
        self.request_durations: List[float] = []
        self.errors_total = 0
        self.errors_by_type: Dict[str, int] = defaultdict(int)
        self.cache_hits = 0
        self.cache_misses = 0

    def record_request(self, endpoint: str, duration: float, status_code: Optional[int] = None):
        """Record a completed request."""
        self.requests_total += 1
        self.requests_by_endpoint[endpoint] += 1
        if status_code:
            self.requests_by_status[status_code] += 1
        self.request_durations.append(duration)

    def record_error(self, error_type: str):
        """Record an error."""
        self.errors_total += 1
        self.errors_by_type[error_type] += 1

    def record_cache_hit(self):
        """Record a cache hit."""
        self.cache_hits += 1

    def record_cache_miss(self):
        """Record a cache miss."""
        self.cache_misses += 1

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of all metrics."""
        total_duration = sum(self.request_durations)
        avg_duration = total_duration / len(self.request_durations) if self.request_durations else 0

        return {
            "requests_total": self.requests_total,
            "requests_by_endpoint": dict(self.requests_by_endpoint),
            "requests_by_status": dict(self.requests_by_status),
            "total_duration": total_duration,
            "avg_request_duration": avg_duration,
            "errors_total": self.errors_total,
            "errors_by_type": dict(self.errors_by_type),
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "cache_hit_rate": self.cache_hits / (self.cache_hits + self.cache_misses) if (self.cache_hits + self.cache_misses) > 0 else 0,
        }

    def reset(self):
        """Reset all metrics."""
        self.requests_total = 0
        self.requests_by_endpoint.clear()
        self.requests_by_status.clear()
        self.request_durations.clear()
        self.errors_total = 0
        self.errors_by_type.clear()
        self.cache_hits = 0
        self.cache_misses = 0


# Global metrics instance
_request_metrics = RequestMetrics()


def get_request_metrics() -> RequestMetrics:
    """Get the global request metrics instance."""
    return _request_metrics


def reset_request_metrics():
    """Reset global request metrics."""
    _request_metrics.reset()


def metrics_logger(
    log_requests: bool = True,
    log_errors: bool = True,
    log_cache: bool = False
) -> Callable:
    """Decorator to log request metrics.

    Args:
        log_requests: Whether to log request details
        log_errors: Whether to log errors
        log_cache: Whether to log cache hits/misses
    """
    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(f"gradient.{func.__module__}.{func.__name__}")

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            endpoint = f"{func.__module__}.{func.__name__}"

            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time

                # Record metrics
                _request_metrics.record_request(endpoint, duration)

                if log_requests:
                    logger.info(f"Request to {endpoint} completed in {duration:.3f}s")

                return result

            except Exception as e:
                duration = time.time() - start_time
                error_type = type(e).__name__

                # Record error metrics
                _request_metrics.record_error(error_type)

                if log_errors:
                    logger.error(f"Request to {endpoint} failed after {duration:.3f}s: {error_type}: {e}")

                raise

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            endpoint = f"{func.__module__}.{func.__name__}"

            try:
                result = await func(*args, **kwargs)
                duration = time.time() - start_time

                # Record metrics
                _request_metrics.record_request(endpoint, duration)

                if log_requests:
                    logger.info(f"Async request to {endpoint} completed in {duration:.3f}s")

                return result

            except Exception as e:
                duration = time.time() - start_time
                error_type = type(e).__name__

                # Record error metrics
                _request_metrics.record_error(error_type)

                if log_errors:
                    logger.error(f"Async request to {endpoint} failed after {duration:.3f}s: {error_type}: {e}")

                raise

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return wrapper

    return decorator


def cache_metrics_logger(func: Callable) -> Callable:
    """Decorator to log cache metrics."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # This would be used internally by the cache system
        # For now, just call the function
        return func(*args, **kwargs)
    return wrapper


# Import asyncio here to avoid circular imports
import asyncio


class PaginationHelper: