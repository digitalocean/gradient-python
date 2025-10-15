#!/usr/bin/env python3
"""
Examples demonstrating the enhanced features of the Gradient Python SDK.

This example shows how to use:
- Performance monitoring and caching
- Advanced retry mechanisms with circuit breaker
- Request signing and security features
- Enhanced debugging and logging
- Rate limiting
"""

import os
import asyncio
import logging
from gradient import (
    EnhancedGradient, 
    EnhancedAsyncGradient,
    RetryConfig,
    CircuitBreakerConfig,
    enable_debug_logging,
    disable_debug_logging
)


def example_basic_enhanced_client():
    """Basic usage of enhanced client with default features."""
    print("=== Basic Enhanced Client ===")
    
    client = EnhancedGradient(
        access_token=os.environ.get("DIGITALOCEAN_ACCESS_TOKEN"),
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        # Enhanced features enabled by default
        enable_caching=True,
        enable_performance_tracking=True,
        enable_debug=False,  # Set to True for detailed logging
    )
    
    try:
        # This request will be cached for subsequent calls
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": "What is machine learning?"}],
            model="llama3.3-70b-instruct",
        )
        print(f"Response: {response.choices[0].message.content[:100]}...")
        
        # Get performance metrics
        metrics = client.get_performance_metrics()
        print(f"Performance metrics: {metrics}")
        
        # Get cache stats
        cache_stats = client.get_cache_stats()
        print(f"Cache stats: {cache_stats}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_advanced_retry_configuration():
    """Example with advanced retry and circuit breaker configuration."""
    print("\n=== Advanced Retry Configuration ===")
    
    # Configure retry behavior
    retry_config = RetryConfig(
        max_attempts=5,
        base_delay=2.0,
        max_delay=30.0,
        exponential_base=2.0,
        jitter=True,
        retryable_status_codes=[408, 429, 500, 502, 503, 504],
    )
    
    # Configure circuit breaker
    circuit_breaker_config = CircuitBreakerConfig(
        failure_threshold=3,
        recovery_timeout=30.0,
        success_threshold=2,
    )
    
    client = EnhancedGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        retry_config=retry_config,
        circuit_breaker_config=circuit_breaker_config,
        enable_debug=True,  # Enable to see retry attempts
    )
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": "Explain quantum computing"}],
            model="llama3.3-70b-instruct",
        )
        print(f"Response received: {len(response.choices[0].message.content)} characters")
        
    except Exception as e:
        print(f"Request failed after retries: {e}")


def example_security_features():
    """Example with security features enabled."""
    print("\n=== Security Features ===")
    
    client = EnhancedGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        enable_request_signing=True,
        signing_secret="your-secret-key-here",  # In production, use environment variable
        enable_rate_limiting=True,
        rate_limit_requests=50,  # 50 requests per minute
        rate_limit_window=60,
    )
    
    try:
        # Requests will be signed and rate limited
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": "What is cybersecurity?"}],
            model="llama3.3-70b-instruct",
        )
        print(f"Secure response: {response.choices[0].message.content[:100]}...")
        
    except Exception as e:
        print(f"Security error: {e}")


def example_performance_monitoring():
    """Example with performance monitoring."""
    print("\n=== Performance Monitoring ===")
    
    client = EnhancedGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        enable_performance_tracking=True,
        enable_caching=True,
        cache_ttl=600,  # 10 minutes
    )
    
    # Use performance monitoring context
    with client.performance_monitoring():
        try:
            # Make multiple requests to see caching in action
            for i in range(3):
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": "What is AI?"}],
                    model="llama3.3-70b-instruct",
                )
                print(f"Request {i+1}: {len(response.choices[0].message.content)} chars")
            
            # Get detailed metrics
            metrics = client.get_performance_metrics()
            for endpoint, stats in metrics.items():
                print(f"Endpoint: {endpoint}")
                print(f"  Requests: {stats['requests']}")
                print(f"  Cache hit rate: {stats['cache_hit_rate']:.2%}")
                print(f"  Average duration: {stats['avg_duration_ms']}ms")
                
        except Exception as e:
            print(f"Performance monitoring error: {e}")


async def example_async_enhanced_client():
    """Example with async enhanced client."""
    print("\n=== Async Enhanced Client ===")
    
    client = EnhancedAsyncGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        enable_caching=True,
        enable_performance_tracking=True,
        enable_debug=False,
    )
    
    try:
        # Make concurrent requests
        tasks = []
        for i in range(3):
            task = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Tell me about topic {i+1}"}],
                model="llama3.3-70b-instruct",
            )
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        
        for i, response in enumerate(responses):
            print(f"Async response {i+1}: {len(response.choices[0].message.content)} chars")
        
        # Get performance metrics
        metrics = client.get_performance_metrics()
        print(f"Async performance metrics: {metrics}")
        
    except Exception as e:
        print(f"Async error: {e}")
    
    finally:
        await client.close()


def example_debug_logging():
    """Example with debug logging enabled."""
    print("\n=== Debug Logging ===")
    
    # Enable global debug logging
    enable_debug_logging(logging.DEBUG)
    
    client = EnhancedGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        enable_debug=True,
    )
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": "Hello, world!"}],
            model="llama3.3-70b-instruct",
        )
        print(f"Debug response: {response.choices[0].message.content[:50]}...")
        
    except Exception as e:
        print(f"Debug error: {e}")
    
    finally:
        # Disable debug logging
        disable_debug_logging()


def example_cache_management():
    """Example showing cache management."""
    print("\n=== Cache Management ===")
    
    client = EnhancedGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        enable_caching=True,
        cache_ttl=300,  # 5 minutes
    )
    
    try:
        # Make a request that will be cached
        response1 = client.chat.completions.create(
            messages=[{"role": "user", "content": "What is caching?"}],
            model="llama3.3-70b-instruct",
        )
        print("First request completed")
        
        # Check cache stats
        stats = client.get_cache_stats()
        print(f"Cache stats after first request: {stats}")
        
        # Make the same request (should be cached)
        response2 = client.chat.completions.create(
            messages=[{"role": "user", "content": "What is caching?"}],
            model="llama3.3-70b-instruct",
        )
        print("Second request completed (should be from cache)")
        
        # Clear cache
        client.clear_cache()
        print("Cache cleared")
        
        # Check cache stats again
        stats = client.get_cache_stats()
        print(f"Cache stats after clearing: {stats}")
        
    except Exception as e:
        print(f"Cache management error: {e}")


def main():
    """Run all examples."""
    print("Gradient Enhanced Features Examples")
    print("=" * 50)
    
    # Check for required environment variables
    if not os.environ.get("GRADIENT_MODEL_ACCESS_KEY"):
        print("Please set GRADIENT_MODEL_ACCESS_KEY environment variable")
        return
    
    # Run sync examples
    example_basic_enhanced_client()
    example_advanced_retry_configuration()
    example_security_features()
    example_performance_monitoring()
    example_debug_logging()
    example_cache_management()
    
    # Run async example
    asyncio.run(example_async_enhanced_client())
    
    print("\n" + "=" * 50)
    print("All examples completed!")


if __name__ == "__main__":
    main()
