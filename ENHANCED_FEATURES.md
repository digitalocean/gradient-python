# Enhanced Features Documentation

The Gradient Python SDK now includes advanced features for performance optimization, security, debugging, and reliability. This document provides comprehensive information about these enhancements.

## Table of Contents

- [Enhanced Client](#enhanced-client)
- [Performance Features](#performance-features)
- [Security Features](#security-features)
- [Debugging and Logging](#debugging-and-logging)
- [Reliability Features](#reliability-features)
- [Configuration Options](#configuration-options)
- [Examples](#examples)
- [Best Practices](#best-practices)

## Enhanced Client

The `EnhancedGradient` and `EnhancedAsyncGradient` clients provide all the functionality of the standard clients plus additional features for production use.

### Basic Usage

```python
from gradient import EnhancedGradient

client = EnhancedGradient(
    model_access_key="your-inference-key",
    enable_caching=True,
    enable_performance_tracking=True,
    enable_debug=False,
)

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Hello!"}],
    model="llama3.3-70b-instruct",
)
```

### Async Usage

```python
from gradient import EnhancedAsyncGradient
import asyncio

async def main():
    client = EnhancedAsyncGradient(
        model_access_key="your-inference-key",
        enable_caching=True,
    )
    
    response = await client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello!"}],
        model="llama3.3-70b-instruct",
    )
    
    await client.close()

asyncio.run(main())
```

## Performance Features

### Request Caching

Automatically cache GET requests to reduce API calls and improve response times.

```python
client = EnhancedGradient(
    model_access_key="your-key",
    enable_caching=True,
    cache_ttl=600,  # Cache for 10 minutes
)

# First request hits the API
response1 = client.chat.completions.create(...)

# Second identical request uses cache
response2 = client.chat.completions.create(...)

# Check cache statistics
stats = client.get_cache_stats()
print(f"Cache size: {stats['size']}")
```

### Connection Pooling

Optimized HTTP connection management for better performance.

```python
client = EnhancedGradient(
    model_access_key="your-key",
    # Connection pooling is enabled by default
    # Configures max_connections=100, max_keepalive=20
)
```

### Performance Tracking

Monitor API call performance and identify bottlenecks.

```python
client = EnhancedGradient(
    model_access_key="your-key",
    enable_performance_tracking=True,
)

# Make some requests
response = client.chat.completions.create(...)

# Get performance metrics
metrics = client.get_performance_metrics()
for endpoint, stats in metrics.items():
    print(f"Endpoint: {endpoint}")
    print(f"  Average duration: {stats['avg_duration_ms']}ms")
    print(f"  Cache hit rate: {stats['cache_hit_rate']:.2%}")
    print(f"  Error rate: {stats['error_rate']:.2%}")
```

### Performance Monitoring Context

Use context manager for detailed performance monitoring:

```python
with client.performance_monitoring():
    # Make multiple requests
    for i in range(10):
        response = client.chat.completions.create(...)
    
    # Performance summary is automatically logged
```

## Security Features

### Request Signing

Sign requests with HMAC for additional security.

```python
client = EnhancedGradient(
    model_access_key="your-key",
    enable_request_signing=True,
    signing_secret="your-secret-key",  # Store securely!
)

# All requests will be automatically signed
response = client.chat.completions.create(...)
```

### Rate Limiting

Prevent API abuse with client-side rate limiting.

```python
client = EnhancedGradient(
    model_access_key="your-key",
    enable_rate_limiting=True,
    rate_limit_requests=50,  # 50 requests
    rate_limit_window=60,    # per minute
)

# Requests exceeding the limit will raise an exception
```

### Token Validation

Validate API tokens before making requests.

```python
from gradient import TokenValidator

# Validate token format
is_valid = TokenValidator.validate_token_format("your-token")

# Mask token for logging
masked = TokenValidator.mask_token("your-token")
print(f"Using token: {masked}")  # "your...oken"
```

### Secure Headers

Automatically add security headers to requests.

```python
from gradient import SecureHeaders

# Get recommended security headers
headers = SecureHeaders.get_security_headers()

# Sanitize headers
clean_headers = SecureHeaders.sanitize_headers(user_headers)
```

## Debugging and Logging

### Enhanced Debugging

Enable detailed request/response logging and tracing.

```python
from gradient import enable_debug_logging

# Enable global debug logging
enable_debug_logging()

client = EnhancedGradient(
    model_access_key="your-key",
    enable_debug=True,
)

# All requests will be logged with detailed information
response = client.chat.completions.create(...)
```

### Request Tracing

Trace operations with context information.

```python
client = EnhancedGradient(
    model_access_key="your-key",
    enable_debug=True,
)

# Enable debugging for this client
client.enable_debug()

# Requests will show detailed timing and context
response = client.chat.completions.create(...)

# Disable debugging
client.disable_debug()
```

### cURL Command Generation

Generate equivalent cURL commands for debugging.

```python
# When debug logging is enabled, equivalent cURL commands
# are automatically logged for each request
```

## Reliability Features

### Advanced Retry Logic

Configure sophisticated retry behavior with exponential backoff.

```python
from gradient import RetryConfig

retry_config = RetryConfig(
    max_attempts=5,
    base_delay=1.0,
    max_delay=60.0,
    exponential_base=2.0,
    jitter=True,
    retryable_status_codes=[408, 429, 500, 502, 503, 504],
    retryable_exceptions=[ConnectionError, TimeoutError],
)

client = EnhancedGradient(
    model_access_key="your-key",
    retry_config=retry_config,
)
```

### Circuit Breaker Pattern

Prevent cascading failures with circuit breaker protection.

```python
from gradient import CircuitBreakerConfig

circuit_config = CircuitBreakerConfig(
    failure_threshold=5,      # Open after 5 failures
    recovery_timeout=60.0,    # Try recovery after 60 seconds
    success_threshold=3,      # Close after 3 successes
)

client = EnhancedGradient(
    model_access_key="your-key",
    circuit_breaker_config=circuit_config,
)
```

### Combined Retry and Circuit Breaker

Use both retry logic and circuit breaker for maximum reliability.

```python
client = EnhancedGradient(
    model_access_key="your-key",
    retry_config=retry_config,
    circuit_breaker_config=circuit_config,
)

# Requests will be retried with exponential backoff
# Circuit breaker will prevent requests if service is down
```

## Configuration Options

### Complete Configuration Example

```python
from gradient import EnhancedGradient, RetryConfig, CircuitBreakerConfig

client = EnhancedGradient(
    # Standard options
    model_access_key="your-inference-key",
    access_token="your-access-token",
    agent_key="your-agent-key",
    agent_endpoint="https://your-agent.agents.do-ai.run",
    base_url="https://api.gradient.ai",
    timeout=30.0,
    max_retries=2,
    
    # Performance options
    enable_caching=True,
    cache_ttl=300,
    enable_performance_tracking=True,
    
    # Security options
    enable_request_signing=True,
    signing_secret="your-signing-secret",
    enable_rate_limiting=True,
    rate_limit_requests=100,
    rate_limit_window=60,
    
    # Debugging options
    enable_debug=False,
    
    # Reliability options
    retry_config=RetryConfig(
        max_attempts=3,
        base_delay=1.0,
        max_delay=30.0,
        exponential_base=2.0,
        jitter=True,
    ),
    circuit_breaker_config=CircuitBreakerConfig(
        failure_threshold=5,
        recovery_timeout=60.0,
        success_threshold=3,
    ),
)
```

## Examples

### Production Configuration

```python
import os
from gradient import EnhancedGradient, RetryConfig, CircuitBreakerConfig

# Production-ready configuration
client = EnhancedGradient(
    model_access_key=os.environ["GRADIENT_MODEL_ACCESS_KEY"],
    
    # Enable all performance features
    enable_caching=True,
    cache_ttl=600,  # 10 minutes
    enable_performance_tracking=True,
    
    # Enable security features
    enable_request_signing=True,
    signing_secret=os.environ["GRADIENT_SIGNING_SECRET"],
    enable_rate_limiting=True,
    rate_limit_requests=1000,  # 1000 requests per hour
    rate_limit_window=3600,
    
    # Robust retry configuration
    retry_config=RetryConfig(
        max_attempts=5,
        base_delay=2.0,
        max_delay=120.0,
        exponential_base=2.0,
        jitter=True,
    ),
    
    # Circuit breaker for fault tolerance
    circuit_breaker_config=CircuitBreakerConfig(
        failure_threshold=10,
        recovery_timeout=300.0,  # 5 minutes
        success_threshold=5,
    ),
)
```

### Development Configuration

```python
# Development configuration with debugging
client = EnhancedGradient(
    model_access_key=os.environ["GRADIENT_MODEL_ACCESS_KEY"],
    
    # Enable debugging
    enable_debug=True,
    
    # Minimal caching for development
    enable_caching=True,
    cache_ttl=60,  # 1 minute
    
    # Track performance
    enable_performance_tracking=True,
    
    # Lenient rate limiting
    enable_rate_limiting=True,
    rate_limit_requests=100,
    rate_limit_window=60,
)

# Enable global debug logging
from gradient import enable_debug_logging
enable_debug_logging()
```

### High-Performance Configuration

```python
# Configuration optimized for high throughput
client = EnhancedGradient(
    model_access_key=os.environ["GRADIENT_MODEL_ACCESS_KEY"],
    
    # Aggressive caching
    enable_caching=True,
    cache_ttl=1800,  # 30 minutes
    
    # Performance tracking
    enable_performance_tracking=True,
    
    # High rate limits
    enable_rate_limiting=True,
    rate_limit_requests=10000,
    rate_limit_window=3600,
    
    # Fast retry configuration
    retry_config=RetryConfig(
        max_attempts=3,
        base_delay=0.5,
        max_delay=10.0,
        exponential_base=1.5,
        jitter=True,
    ),
)
```

## Best Practices

### 1. Environment-Specific Configuration

Use different configurations for different environments:

```python
import os

def create_client():
    env = os.environ.get("ENVIRONMENT", "development")
    
    if env == "production":
        return EnhancedGradient(
            model_access_key=os.environ["GRADIENT_MODEL_ACCESS_KEY"],
            enable_caching=True,
            cache_ttl=600,
            enable_performance_tracking=True,
            enable_request_signing=True,
            signing_secret=os.environ["GRADIENT_SIGNING_SECRET"],
            enable_debug=False,
        )
    else:
        return EnhancedGradient(
            model_access_key=os.environ["GRADIENT_MODEL_ACCESS_KEY"],
            enable_debug=True,
            enable_caching=True,
            cache_ttl=60,
        )
```

### 2. Monitoring and Alerting

Regularly check performance metrics:

```python
def check_performance(client):
    metrics = client.get_performance_metrics()
    
    for endpoint, stats in metrics.items():
        # Alert if error rate is high
        if stats['error_rate'] > 0.05:  # 5%
            print(f"High error rate for {endpoint}: {stats['error_rate']:.2%}")
        
        # Alert if average response time is high
        if stats['avg_duration_ms'] > 5000:  # 5 seconds
            print(f"Slow response for {endpoint}: {stats['avg_duration_ms']}ms")
```

### 3. Graceful Degradation

Handle circuit breaker states gracefully:

```python
try:
    response = client.chat.completions.create(...)
except Exception as e:
    if "Circuit breaker is open" in str(e):
        # Fallback to cached response or default behavior
        return handle_service_unavailable()
    else:
        raise
```

### 4. Security Best Practices

- Store signing secrets securely (environment variables, key management systems)
- Use appropriate rate limits based on your API quotas
- Regularly rotate signing secrets
- Monitor for unusual request patterns

### 5. Performance Optimization

- Use caching for read-heavy workloads
- Monitor cache hit rates and adjust TTL accordingly
- Use connection pooling for high-throughput applications
- Implement proper retry strategies based on your use case

### 6. Debugging and Troubleshooting

- Enable debug logging in development environments
- Use performance tracking to identify bottlenecks
- Monitor circuit breaker states
- Review retry patterns and adjust configuration as needed

## Migration Guide

### From Standard Client

```python
# Before
from gradient import Gradient
client = Gradient(model_access_key="your-key")

# After
from gradient import EnhancedGradient
client = EnhancedGradient(
    model_access_key="your-key",
    enable_caching=True,
    enable_performance_tracking=True,
)
```

### Gradual Feature Adoption

You can enable features incrementally:

```python
# Start with basic enhanced client
client = EnhancedGradient(model_access_key="your-key")

# Add caching
client = EnhancedGradient(
    model_access_key="your-key",
    enable_caching=True,
)

# Add performance tracking
client = EnhancedGradient(
    model_access_key="your-key",
    enable_caching=True,
    enable_performance_tracking=True,
)

# Add security features
client = EnhancedGradient(
    model_access_key="your-key",
    enable_caching=True,
    enable_performance_tracking=True,
    enable_request_signing=True,
    signing_secret="your-secret",
)
```

## Troubleshooting

### Common Issues

1. **High Memory Usage**: Reduce cache size or TTL
2. **Rate Limit Errors**: Adjust rate limiting configuration
3. **Circuit Breaker Always Open**: Check failure threshold and recovery timeout
4. **Slow Performance**: Enable performance tracking to identify bottlenecks

### Debug Information

Enable debug logging to get detailed information:

```python
from gradient import enable_debug_logging
import logging

enable_debug_logging(logging.DEBUG)
```

This will show:
- Request/response details
- Cache hits/misses
- Retry attempts
- Circuit breaker state changes
- Performance metrics

## Support

For issues related to enhanced features:

1. Check the debug logs
2. Review performance metrics
3. Verify configuration options
4. Check environment variables
5. Open an issue on GitHub with detailed information

## Contributing

To contribute to the enhanced features:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Update documentation
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.
