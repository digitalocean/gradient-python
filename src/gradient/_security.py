"""Security utilities for the Gradient SDK."""

import hmac
import hashlib
import time
import secrets
import base64
from typing import Dict, Optional, Union, Any
from urllib.parse import urlencode, quote
import json


class RequestSigner:
    """Utility for signing API requests with HMAC."""
    
    def __init__(self, secret_key: str, algorithm: str = 'sha256'):
        self.secret_key = secret_key.encode() if isinstance(secret_key, str) else secret_key
        self.algorithm = algorithm
        self.hash_func = getattr(hashlib, algorithm)
    
    def sign_request(self, method: str, url: str, headers: Optional[Dict] = None,
                    body: Optional[Union[str, bytes, Dict]] = None, 
                    timestamp: Optional[int] = None) -> Dict[str, str]:
        """Sign a request and return signature headers."""
        timestamp = timestamp or int(time.time())
        nonce = secrets.token_hex(16)
        
        # Create canonical request string
        canonical_request = self._create_canonical_request(
            method, url, headers or {}, body, timestamp, nonce
        )
        
        # Create signature
        signature = hmac.new(
            self.secret_key,
            canonical_request.encode('utf-8'),
            self.hash_func
        ).hexdigest()
        
        return {
            'X-Gradient-Timestamp': str(timestamp),
            'X-Gradient-Nonce': nonce,
            'X-Gradient-Signature': signature,
            'X-Gradient-Algorithm': self.algorithm.upper()
        }
    
    def _create_canonical_request(self, method: str, url: str, headers: Dict,
                                 body: Optional[Union[str, bytes, Dict]], 
                                 timestamp: int, nonce: str) -> str:
        """Create canonical request string for signing."""
        # Normalize method
        method = method.upper()
        
        # Normalize URL (remove query params for now, they should be in headers)
        if '?' in url:
            url = url.split('?')[0]
        
        # Normalize headers (exclude signature headers when verifying)
        canonical_headers = {}
        excluded_headers = {'x-gradient-signature', 'x-gradient-timestamp', 'x-gradient-nonce', 'x-gradient-algorithm'}
        for key, value in headers.items():
            key_lower = key.lower()
            if key_lower in excluded_headers:
                continue
            if key_lower.startswith('x-gradient-') or key_lower == 'content-type':
                canonical_headers[key_lower] = str(value).strip()
        
        # Sort headers
        header_string = '\n'.join(f"{k}:{v}" for k, v in sorted(canonical_headers.items()))
        
        # Handle body
        if body is None:
            body_hash = hashlib.sha256(b'').hexdigest()
        elif isinstance(body, dict):
            body_str = json.dumps(body, sort_keys=True, separators=(',', ':'))
            body_hash = hashlib.sha256(body_str.encode('utf-8')).hexdigest()
        elif isinstance(body, str):
            body_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()
        else:  # bytes
            body_hash = hashlib.sha256(body).hexdigest()
        
        # Create canonical request - include all components that were used in signing
        canonical_request = f"{method}\n{url}\n{header_string}\n{timestamp}\n{nonce}\n{body_hash}"
        return canonical_request
    
    def verify_signature(self, method: str, url: str, headers: Dict,
                        body: Optional[Union[str, bytes, Dict]] = None,
                        max_age: int = 300) -> bool:
        """Verify a request signature."""
        try:
            timestamp = int(headers.get('X-Gradient-Timestamp', 0))
            nonce = headers.get('X-Gradient-Nonce', '')
            signature = headers.get('X-Gradient-Signature', '')
            algorithm = headers.get('X-Gradient-Algorithm', 'SHA256').lower()
            
            # Check timestamp (prevent replay attacks)
            current_time = int(time.time())
            if abs(current_time - timestamp) > max_age:
                return False
            
            # Verify algorithm matches
            if algorithm != self.algorithm:
                return False
            
            # Create expected signature
            canonical_request = self._create_canonical_request(
                method, url, headers, body, timestamp, nonce
            )
            
            expected_signature = hmac.new(
                self.secret_key,
                canonical_request.encode('utf-8'),
                self.hash_func
            ).hexdigest()
            
            # Use constant-time comparison
            return hmac.compare_digest(signature, expected_signature)
            
        except (ValueError, TypeError):
            return False


class TokenValidator:
    """Utility for validating API tokens and keys."""
    
    @staticmethod
    def validate_token_format(token: str, expected_prefix: Optional[str] = None) -> bool:
        """Validate token format."""
        if not token or not isinstance(token, str):
            return False
        
        # Check minimum length
        if len(token) < 20:
            return False
        
        # Check prefix if specified
        if expected_prefix and not token.startswith(expected_prefix):
            return False
        
        # Check for valid characters (base64-like)
        import re
        if not re.match(r'^[A-Za-z0-9+/=_-]+$', token):
            return False
        
        return True
    
    @staticmethod
    def mask_token(token: str, visible_chars: int = 4) -> str:
        """Mask token for logging, showing only first/last few characters."""
        if not token or len(token) <= visible_chars * 2:
            return "***MASKED***"
        
        return f"{token[:visible_chars]}...{token[-visible_chars:]}"


class RateLimiter:
    """Simple rate limiter for API requests."""
    
    def __init__(self, max_requests: int, time_window: int = 60):
        self.max_requests = max_requests
        self.time_window = time_window
        self._requests: Dict[str, list] = {}
    
    def is_allowed(self, identifier: str) -> bool:
        """Check if request is allowed for given identifier."""
        current_time = time.time()
        
        # Initialize or get request history
        if identifier not in self._requests:
            self._requests[identifier] = []
        
        request_times = self._requests[identifier]
        
        # Remove old requests outside time window
        cutoff_time = current_time - self.time_window
        request_times[:] = [t for t in request_times if t > cutoff_time]
        
        # Check if under limit
        if len(request_times) < self.max_requests:
            request_times.append(current_time)
            return True
        
        return False
    
    def time_until_reset(self, identifier: str) -> float:
        """Get time until rate limit resets for identifier."""
        if identifier not in self._requests:
            return 0.0
        
        request_times = self._requests[identifier]
        if not request_times:
            return 0.0
        
        oldest_request = min(request_times)
        reset_time = oldest_request + self.time_window
        current_time = time.time()
        
        return max(0.0, reset_time - current_time)


class SecureHeaders:
    """Utility for managing secure HTTP headers."""
    
    @staticmethod
    def get_security_headers() -> Dict[str, str]:
        """Get recommended security headers."""
        return {
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block',
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        }
    
    @staticmethod
    def sanitize_headers(headers: Dict[str, Any]) -> Dict[str, str]:
        """Sanitize headers by removing potentially dangerous values."""
        sanitized = {}
        
        for key, value in headers.items():
            # Convert to string and strip
            key_str = str(key).strip()
            value_str = str(value).strip()
            
            # Skip empty headers
            if not key_str or not value_str:
                continue
            
            # Remove control characters
            key_clean = ''.join(c for c in key_str if ord(c) >= 32 and ord(c) != 127)
            value_clean = ''.join(c for c in value_str if ord(c) >= 32 and ord(c) != 127)
            
            sanitized[key_clean] = value_clean
        
        return sanitized


class InputValidator:
    """Utility for validating and sanitizing inputs."""
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """Validate URL format and security."""
        if not url or not isinstance(url, str):
            return False
        
        # Check for basic URL format
        if not url.startswith(('http://', 'https://')):
            return False
        
        # Check for dangerous characters
        dangerous_chars = ['<', '>', '"', "'", '&', '\n', '\r', '\t']
        if any(char in url for char in dangerous_chars):
            return False
        
        # Check length
        if len(url) > 2048:  # Common URL length limit
            return False
        
        return True
    
    @staticmethod
    def sanitize_string(value: str, max_length: int = 1000) -> str:
        """Sanitize string input."""
        if not isinstance(value, str):
            value = str(value)
        
        # Truncate if too long
        if len(value) > max_length:
            value = value[:max_length]
        
        # Remove control characters except common whitespace
        sanitized = ''.join(c for c in value 
                          if ord(c) >= 32 or c in ['\n', '\r', '\t'])
        
        return sanitized.strip()
    
    @staticmethod
    def validate_json(data: str) -> bool:
        """Validate JSON string."""
        try:
            json.loads(data)
            return True
        except (json.JSONDecodeError, TypeError):
            return False


# Default instances
_default_rate_limiter = RateLimiter(max_requests=100, time_window=60)


def get_rate_limiter() -> RateLimiter:
    """Get the default rate limiter instance."""
    return _default_rate_limiter
