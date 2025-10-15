"""Advanced retry mechanisms with circuit breaker pattern."""

import time
import random
import logging
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Type, Union
from dataclasses import dataclass
import asyncio


logger = logging.getLogger(__name__)


class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if service recovered


@dataclass
class RetryConfig:
    """Configuration for retry behavior."""
    max_attempts: int = 3
    base_delay: float = 1.0
    max_delay: float = 60.0
    exponential_base: float = 2.0
    jitter: bool = True
    retryable_status_codes: List[int] = None
    retryable_exceptions: List[Type[Exception]] = None
    
    def __post_init__(self):
        if self.retryable_status_codes is None:
            self.retryable_status_codes = [408, 429, 500, 502, 503, 504]
        if self.retryable_exceptions is None:
            self.retryable_exceptions = [ConnectionError, TimeoutError]


@dataclass
class CircuitBreakerConfig:
    """Configuration for circuit breaker."""
    failure_threshold: int = 5
    recovery_timeout: float = 60.0
    expected_exception: Type[Exception] = Exception
    success_threshold: int = 3  # Successes needed to close circuit


class CircuitBreaker:
    """Circuit breaker implementation for fault tolerance."""
    
    def __init__(self, config: CircuitBreakerConfig):
        self.config = config
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = 0.0
        self._lock = asyncio.Lock() if hasattr(asyncio, 'current_task') else None
    
    def _should_attempt_reset(self) -> bool:
        """Check if we should attempt to reset the circuit."""
        return (self.state == CircuitState.OPEN and 
                time.time() - self.last_failure_time >= self.config.recovery_timeout)
    
    def _record_success(self) -> None:
        """Record a successful operation."""
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.config.success_threshold:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
                self.success_count = 0
                logger.info("Circuit breaker closed - service recovered")
        elif self.state == CircuitState.CLOSED:
            self.failure_count = max(0, self.failure_count - 1)
    
    def _record_failure(self) -> None:
        """Record a failed operation."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.state == CircuitState.CLOSED:
            if self.failure_count >= self.config.failure_threshold:
                self.state = CircuitState.OPEN
                logger.warning(f"Circuit breaker opened after {self.failure_count} failures")
        elif self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN
            self.success_count = 0
            logger.warning("Circuit breaker reopened during recovery attempt")
    
    def can_execute(self) -> bool:
        """Check if operation can be executed."""
        if self.state == CircuitState.CLOSED:
            return True
        elif self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                self.success_count = 0
                logger.info("Circuit breaker half-open - testing service")
                return True
            return False
        else:  # HALF_OPEN
            return True
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with circuit breaker protection."""
        if not self.can_execute():
            raise Exception("Circuit breaker is open")
        
        try:
            result = func(*args, **kwargs)
            self._record_success()
            return result
        except self.config.expected_exception as e:
            self._record_failure()
            raise e
    
    async def acall(self, func: Callable, *args, **kwargs) -> Any:
        """Async version of call method."""
        if not self.can_execute():
            raise Exception("Circuit breaker is open")
        
        try:
            if asyncio.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
            self._record_success()
            return result
        except self.config.expected_exception as e:
            self._record_failure()
            raise e


class RetryHandler:
    """Advanced retry handler with exponential backoff and jitter."""
    
    def __init__(self, config: RetryConfig, circuit_breaker: Optional[CircuitBreaker] = None):
        self.config = config
        self.circuit_breaker = circuit_breaker
    
    def _calculate_delay(self, attempt: int) -> float:
        """Calculate delay for given attempt with exponential backoff and jitter."""
        delay = min(
            self.config.base_delay * (self.config.exponential_base ** (attempt - 1)),
            self.config.max_delay
        )
        
        if self.config.jitter:
            # Add jitter to prevent thundering herd
            delay *= (0.5 + random.random() * 0.5)
        
        return delay
    
    def _is_retryable_exception(self, exception: Exception) -> bool:
        """Check if exception is retryable."""
        return any(isinstance(exception, exc_type) 
                  for exc_type in self.config.retryable_exceptions)
    
    def _is_retryable_status(self, status_code: int) -> bool:
        """Check if HTTP status code is retryable."""
        return status_code in self.config.retryable_status_codes
    
    def retry(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with retry logic."""
        last_exception = None
        
        for attempt in range(1, self.config.max_attempts + 1):
            try:
                if self.circuit_breaker:
                    return self.circuit_breaker.call(func, *args, **kwargs)
                else:
                    return func(*args, **kwargs)
            
            except Exception as e:
                last_exception = e
                
                # Check if we should retry
                should_retry = False
                
                if hasattr(e, 'status_code'):
                    should_retry = self._is_retryable_status(e.status_code)
                else:
                    should_retry = self._is_retryable_exception(e)
                
                if not should_retry or attempt == self.config.max_attempts:
                    logger.error(f"Request failed after {attempt} attempts: {e}")
                    raise e
                
                delay = self._calculate_delay(attempt)
                logger.warning(f"Request failed (attempt {attempt}/{self.config.max_attempts}), "
                             f"retrying in {delay:.2f}s: {e}")
                time.sleep(delay)
        
        # This should never be reached, but just in case
        if last_exception:
            raise last_exception
    
    async def aretry(self, func: Callable, *args, **kwargs) -> Any:
        """Async version of retry method."""
        last_exception = None
        
        for attempt in range(1, self.config.max_attempts + 1):
            try:
                if self.circuit_breaker:
                    return await self.circuit_breaker.acall(func, *args, **kwargs)
                else:
                    if asyncio.iscoroutinefunction(func):
                        return await func(*args, **kwargs)
                    else:
                        return func(*args, **kwargs)
            
            except Exception as e:
                last_exception = e
                
                # Check if we should retry
                should_retry = False
                
                if hasattr(e, 'status_code'):
                    should_retry = self._is_retryable_status(e.status_code)
                else:
                    should_retry = self._is_retryable_exception(e)
                
                if not should_retry or attempt == self.config.max_attempts:
                    logger.error(f"Request failed after {attempt} attempts: {e}")
                    raise e
                
                delay = self._calculate_delay(attempt)
                logger.warning(f"Request failed (attempt {attempt}/{self.config.max_attempts}), "
                             f"retrying in {delay:.2f}s: {e}")
                await asyncio.sleep(delay)
        
        # This should never be reached, but just in case
        if last_exception:
            raise last_exception


# Default configurations
DEFAULT_RETRY_CONFIG = RetryConfig()
DEFAULT_CIRCUIT_BREAKER_CONFIG = CircuitBreakerConfig()


def create_retry_handler(retry_config: Optional[RetryConfig] = None,
                        circuit_breaker_config: Optional[CircuitBreakerConfig] = None) -> RetryHandler:
    """Create a retry handler with optional circuit breaker."""
    retry_config = retry_config or DEFAULT_RETRY_CONFIG
    
    circuit_breaker = None
    if circuit_breaker_config:
        circuit_breaker = CircuitBreaker(circuit_breaker_config)
    
    return RetryHandler(retry_config, circuit_breaker)
