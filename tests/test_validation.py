"""Tests for API key validation functionality."""

import pytest
from gradient._utils import validate_api_key, validate_client_credentials, validate_client_instance


class TestAPIKeyValidation:
    """Test API key validation functionality."""

    def test_valid_api_keys(self):
        """Test that valid API keys pass validation."""
        valid_keys = [
            "sk-1234567890abcdef",
            "do_v1_1234567890abcdef1234567890abcdef",
            "gradient_test_key_1234567890",
            "some_long_api_key_that_is_valid_1234567890",
        ]

        for key in valid_keys:
            assert validate_api_key(key), f"Key {key} should be valid"

    def test_invalid_api_keys(self):
        """Test that invalid API keys fail validation."""
        invalid_keys = [
            "",  # empty string
            "   ",  # whitespace only
            "short",  # too short
            "123456789",  # too short with numbers
            12345,  # integer
        ]

        for key in invalid_keys:
            assert not validate_api_key(key), f"Key {key} should be invalid"

        # Test None separately since we made it valid for optional keys
        assert validate_api_key(None), "None should be valid for optional keys"

    def test_validate_client_credentials_valid(self):
        """Test that valid client credentials pass validation."""
        # Should not raise any exception
        validate_client_credentials(access_token="sk-1234567890abcdef")

    def test_validate_client_credentials_invalid(self):
        """Test that invalid client credentials raise appropriate errors."""
        # No authentication provided
        with pytest.raises(ValueError, match="At least one authentication method must be provided"):
            validate_client_credentials()

        # Invalid access token format
        with pytest.raises(ValueError, match="Invalid access_token format"):
            validate_client_credentials(access_token="invalid-key")

        # Invalid model access key format
        with pytest.raises(ValueError, match="Invalid model_access_key format"):
            validate_client_credentials(model_access_key="short")

        # Invalid agent access key format
        with pytest.raises(ValueError, match="Invalid agent_access_key format"):
            validate_client_credentials(agent_access_key="bad")

        # Invalid agent endpoint
        with pytest.raises(ValueError, match="agent_endpoint must be a string"):
            validate_client_credentials(access_token="sk-1234567890abcdef", agent_endpoint=123)

        # Invalid agent endpoint URL
        with pytest.raises(ValueError, match="agent_endpoint must be a valid HTTP/HTTPS URL"):
            validate_client_credentials(access_token="sk-1234567890abcdef", agent_endpoint="ftp://example.com")

    def test_validate_client_credentials_comprehensive(self):
        """Test comprehensive client credentials validation scenarios."""
        # Valid combinations
        validate_client_credentials(access_token="sk-1234567890abcdef")
        validate_client_credentials(model_access_key="gradient_key_1234567890")
        validate_client_credentials(agent_access_key="agent_key_1234567890")
        validate_client_credentials(
            access_token="sk-1234567890abcdef",
            model_access_key="gradient_key_1234567890",
            agent_access_key="agent_key_1234567890",
            agent_endpoint="https://my-agent.agents.do-ai.run"
        )

        # Invalid combinations
        with pytest.raises(ValueError):
            validate_client_credentials(access_token="short")

        with pytest.raises(ValueError):
            validate_client_credentials(agent_endpoint="https://example.com")  # No auth keys

    def test_validate_client_instance(self):
        """Test client instance validation."""
        from gradient import Gradient

        # Valid client
        client = Gradient(access_token="sk-1234567890abcdef")
        validate_client_instance(client)  # Should not raise

        # Invalid client - no authentication
        invalid_client = Gradient()
        with pytest.raises(ValueError, match="Client must have at least one authentication method configured"):
            validate_client_instance(invalid_client)

        # Invalid client - wrong type
        with pytest.raises(TypeError, match="client must be a Gradient or AsyncGradient instance"):
            validate_client_instance("not a client")

        # Invalid client - bad credentials
        bad_client = Gradient(access_token="short")
        with pytest.raises(ValueError, match="Client authentication validation failed"):
            validate_client_instance(bad_client)

    def test_validate_client_credentials_multiple_valid(self):
        """Test that multiple valid authentication methods work."""
        # All valid methods
        validate_client_credentials(
            access_token="sk-1234567890abcdef",
            model_access_key="gradient_key_1234567890",
            agent_access_key="agent_key_1234567890"
        )

        # Mixed valid/invalid should fail
        with pytest.raises(ValueError):
            validate_client_credentials(
                access_token="sk-1234567890abcdef",
                model_access_key="short"  # invalid
            )

    def test_validate_client_credentials_mixed_valid_invalid(self):
        """Test mixed valid and invalid credentials."""
        # Valid access token with invalid model key
        with pytest.raises(ValueError, match="Invalid model_access_key format"):
            validate_client_credentials(
                access_token="sk-1234567890abcdef",
                model_access_key="short"
            )

        # Valid model key with invalid agent endpoint
        with pytest.raises(ValueError, match="agent_endpoint must be a valid HTTP/HTTPS URL"):
            validate_client_credentials(
                model_access_key="gradient_key_1234567890",
                agent_endpoint="invalid-url"
            )