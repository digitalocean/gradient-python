#!/usr/bin/env python3
"""
Simple integration test to verify enhanced features work correctly.
This doesn't make actual API calls but tests the client initialization and basic functionality.
"""

import sys
import os

# Add the src directory to the path so we can import gradient
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_enhanced_client_import():
    """Test that we can import the enhanced client."""
    try:
        from gradient import EnhancedGradient, EnhancedAsyncGradient
        print("✅ Successfully imported enhanced clients")
        return True
    except ImportError as e:
        print(f"❌ Failed to import enhanced clients: {e}")
        return False

def test_enhanced_client_initialization():
    """Test that we can initialize the enhanced client."""
    try:
        from gradient import EnhancedGradient
        
        client = EnhancedGradient(
            model_access_key="test-key-1234567890abcdef1234567890abcdef",
            enable_caching=True,
            enable_performance_tracking=True,
            enable_debug=False,
        )
        
        print("✅ Successfully initialized enhanced client")
        
        # Test utility methods
        stats = client.get_cache_stats()
        print(f"✅ Cache stats: {stats}")
        
        metrics = client.get_performance_metrics()
        print(f"✅ Performance metrics: {metrics}")
        
        return True
    except Exception as e:
        print(f"❌ Failed to initialize enhanced client: {e}")
        return False

def test_enhanced_features_import():
    """Test that we can import all enhanced feature modules."""
    try:
        from gradient import (
            RetryConfig,
            CircuitBreakerConfig,
            RequestSigner,
            TokenValidator,
            get_request_cache,
            get_performance_tracker,
            get_connection_pool,
            get_debugger,
            get_rate_limiter,
            enable_debug_logging,
            disable_debug_logging,
            create_retry_handler,
        )
        print("✅ Successfully imported all enhanced features")
        return True
    except ImportError as e:
        print(f"❌ Failed to import enhanced features: {e}")
        return False

def test_performance_features():
    """Test performance features work correctly."""
    try:
        from gradient import get_request_cache, get_performance_tracker
        
        # Test cache
        cache = get_request_cache()
        cache.set('GET', '/test', {'data': 'test'})
        result = cache.get('GET', '/test')
        assert result == {'data': 'test'}
        print("✅ Request cache working correctly")
        
        # Test performance tracker
        tracker = get_performance_tracker()
        tracker.record_request('GET', '/test', 0.5, 200)
        metrics = tracker.get_metrics('GET /test')
        assert metrics['count'] == 1
        print("✅ Performance tracker working correctly")
        
        return True
    except Exception as e:
        print(f"❌ Performance features test failed: {e}")
        return False

def test_security_features():
    """Test security features work correctly."""
    try:
        from gradient import RequestSigner, TokenValidator, get_rate_limiter
        
        # Test request signer
        signer = RequestSigner('test-secret')
        headers = signer.sign_request('GET', '/test', {}, None)
        assert 'X-Gradient-Signature' in headers
        print("✅ Request signer working correctly")
        
        # Test token validator
        is_valid = TokenValidator.validate_token_format('sk-1234567890abcdef1234567890abcdef')
        assert is_valid
        print("✅ Token validator working correctly")
        
        # Test rate limiter
        limiter = get_rate_limiter()
        assert limiter.is_allowed('test-user')
        print("✅ Rate limiter working correctly")
        
        return True
    except Exception as e:
        print(f"❌ Security features test failed: {e}")
        return False

def test_retry_features():
    """Test retry and circuit breaker features."""
    try:
        from gradient import RetryConfig, CircuitBreakerConfig, create_retry_handler
        
        # Test retry config
        retry_config = RetryConfig(max_attempts=3, base_delay=1.0)
        assert retry_config.max_attempts == 3
        print("✅ Retry config working correctly")
        
        # Test circuit breaker config
        cb_config = CircuitBreakerConfig(failure_threshold=5)
        assert cb_config.failure_threshold == 5
        print("✅ Circuit breaker config working correctly")
        
        # Test retry handler creation
        handler = create_retry_handler(retry_config, cb_config)
        assert handler is not None
        print("✅ Retry handler creation working correctly")
        
        return True
    except Exception as e:
        print(f"❌ Retry features test failed: {e}")
        return False

def main():
    """Run all integration tests."""
    print("🧪 Running Enhanced Features Integration Tests")
    print("=" * 50)
    
    tests = [
        test_enhanced_client_import,
        test_enhanced_features_import,
        test_enhanced_client_initialization,
        test_performance_features,
        test_security_features,
        test_retry_features,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        print(f"\n🔍 Running {test.__name__}...")
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with exception: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All integration tests passed!")
        return 0
    else:
        print("💥 Some integration tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
