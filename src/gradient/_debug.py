"""Enhanced debugging and logging utilities for the Gradient SDK."""

import json
import time
import logging
import functools
from typing import Any, Dict, Optional, Union, Callable
from contextlib import contextmanager
import inspect
import traceback


class GradientDebugger:
    """Enhanced debugging utilities for the Gradient SDK."""
    
    def __init__(self, enabled: bool = False, log_level: int = logging.DEBUG):
        self.enabled = enabled
        self.logger = logging.getLogger('gradient.debug')
        self.logger.setLevel(log_level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def enable(self) -> None:
        """Enable debugging."""
        self.enabled = True
        self.logger.info("Gradient debugging enabled")
    
    def disable(self) -> None:
        """Disable debugging."""
        self.enabled = False
        self.logger.info("Gradient debugging disabled")
    
    def log_request(self, method: str, url: str, headers: Optional[Dict] = None,
                   params: Optional[Dict] = None, body: Optional[Any] = None) -> None:
        """Log HTTP request details."""
        if not self.enabled:
            return
        
        self.logger.debug(f"🚀 REQUEST: {method.upper()} {url}")
        
        if headers:
            # Mask sensitive headers
            safe_headers = self._mask_sensitive_data(headers, ['authorization', 'x-api-key'])
            self.logger.debug(f"   Headers: {json.dumps(safe_headers, indent=2)}")
        
        if params:
            self.logger.debug(f"   Params: {json.dumps(params, indent=2)}")
        
        if body:
            if isinstance(body, (dict, list)):
                safe_body = self._mask_sensitive_data(body, ['password', 'token', 'key'])
                self.logger.debug(f"   Body: {json.dumps(safe_body, indent=2)}")
            else:
                self.logger.debug(f"   Body: {str(body)[:500]}...")
    
    def log_response(self, status_code: int, headers: Optional[Dict] = None,
                    body: Optional[Any] = None, duration: Optional[float] = None) -> None:
        """Log HTTP response details."""
        if not self.enabled:
            return
        
        status_emoji = "✅" if status_code < 400 else "❌"
        duration_str = f" ({duration:.3f}s)" if duration else ""
        
        self.logger.debug(f"{status_emoji} RESPONSE: {status_code}{duration_str}")
        
        if headers:
            self.logger.debug(f"   Headers: {json.dumps(dict(headers), indent=2)}")
        
        if body:
            if isinstance(body, (dict, list)):
                self.logger.debug(f"   Body: {json.dumps(body, indent=2)}")
            else:
                body_str = str(body)[:1000]
                self.logger.debug(f"   Body: {body_str}...")
    
    def log_error(self, error: Exception, context: Optional[Dict] = None) -> None:
        """Log error with context."""
        if not self.enabled:
            return
        
        self.logger.error(f"💥 ERROR: {type(error).__name__}: {error}")
        
        if context:
            self.logger.error(f"   Context: {json.dumps(context, indent=2)}")
        
        # Log stack trace for debugging
        self.logger.debug(f"   Stack trace:\n{traceback.format_exc()}")
    
    def _mask_sensitive_data(self, data: Union[Dict, Any], sensitive_keys: list) -> Any:
        """Mask sensitive data in dictionaries."""
        if not isinstance(data, dict):
            return data
        
        masked = {}
        for key, value in data.items():
            if any(sensitive_key.lower() in key.lower() for sensitive_key in sensitive_keys):
                masked[key] = "***MASKED***"
            elif isinstance(value, dict):
                masked[key] = self._mask_sensitive_data(value, sensitive_keys)
            else:
                masked[key] = value
        
        return masked
    
    @contextmanager
    def trace_operation(self, operation_name: str, **context):
        """Context manager to trace operations."""
        if not self.enabled:
            yield
            return
        
        start_time = time.time()
        self.logger.debug(f"🔍 START: {operation_name}")
        
        if context:
            self.logger.debug(f"   Context: {json.dumps(context, indent=2)}")
        
        try:
            yield
            duration = time.time() - start_time
            self.logger.debug(f"✅ COMPLETE: {operation_name} ({duration:.3f}s)")
        except Exception as e:
            duration = time.time() - start_time
            self.logger.debug(f"❌ FAILED: {operation_name} ({duration:.3f}s) - {e}")
            raise


def debug_method(func: Callable) -> Callable:
    """Decorator to add debugging to methods."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        debugger = getattr(self, '_debugger', None)
        if not debugger or not debugger.enabled:
            return func(self, *args, **kwargs)
        
        # Get method signature for logging
        sig = inspect.signature(func)
        bound_args = sig.bind(self, *args, **kwargs)
        bound_args.apply_defaults()
        
        # Remove 'self' from args for logging
        call_args = dict(bound_args.arguments)
        call_args.pop('self', None)
        
        method_name = f"{self.__class__.__name__}.{func.__name__}"
        
        with debugger.trace_operation(method_name, args=call_args):
            return func(self, *args, **kwargs)
    
    return wrapper


def debug_async_method(func: Callable) -> Callable:
    """Decorator to add debugging to async methods."""
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        debugger = getattr(self, '_debugger', None)
        if not debugger or not debugger.enabled:
            return await func(self, *args, **kwargs)
        
        # Get method signature for logging
        sig = inspect.signature(func)
        bound_args = sig.bind(self, *args, **kwargs)
        bound_args.apply_defaults()
        
        # Remove 'self' from args for logging
        call_args = dict(bound_args.arguments)
        call_args.pop('self', None)
        
        method_name = f"{self.__class__.__name__}.{func.__name__}"
        
        with debugger.trace_operation(method_name, args=call_args):
            return await func(self, *args, **kwargs)
    
    return wrapper


class RequestLogger:
    """Specialized logger for HTTP requests and responses."""
    
    def __init__(self, name: str = 'gradient.requests'):
        self.logger = logging.getLogger(name)
        self._setup_logger()
    
    def _setup_logger(self) -> None:
        """Setup logger with appropriate formatting."""
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def log_curl_command(self, method: str, url: str, headers: Optional[Dict] = None,
                        body: Optional[Any] = None) -> None:
        """Log equivalent curl command for debugging."""
        curl_parts = ['curl', '-X', method.upper()]
        
        if headers:
            for key, value in headers.items():
                if 'authorization' not in key.lower():
                    curl_parts.extend(['-H', f'"{key}: {value}"'])
                else:
                    curl_parts.extend(['-H', f'"{key}: ***MASKED***"'])
        
        if body and method.upper() in ['POST', 'PUT', 'PATCH']:
            if isinstance(body, (dict, list)):
                body_str = json.dumps(body)
            else:
                body_str = str(body)
            curl_parts.extend(['-d', f"'{body_str}'"])
        
        curl_parts.append(f'"{url}"')
        curl_command = ' '.join(curl_parts)
        
        self.logger.debug(f"Equivalent curl command:\n{curl_command}")


# Global debugger instance
_debugger = GradientDebugger()


def get_debugger() -> GradientDebugger:
    """Get the global debugger instance."""
    return _debugger


def enable_debug_logging(level: int = logging.DEBUG) -> None:
    """Enable debug logging for the entire SDK."""
    _debugger.logger.setLevel(level)
    _debugger.enable()
    
    # Also enable httpx logging for request/response details
    logging.getLogger("httpx").setLevel(level)


def disable_debug_logging() -> None:
    """Disable debug logging for the SDK."""
    _debugger.disable()
