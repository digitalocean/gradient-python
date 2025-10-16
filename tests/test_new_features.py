"""Tests for new features added to the Gradient SDK."""

import pytest
from gradient._utils import validate_api_key, validate_client_credentials


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
            None,  # None value
            12345,  # integer
        ]

        for key in invalid_keys:
            assert not validate_api_key(key), f"Key {key} should be invalid"

    def test_validate_client_credentials_valid(self):
        """Test that valid client credentials pass validation."""
        # Should not raise any exception
        validate_client_credentials(access_token="sk-1234567890abcdef")
        validate_client_credentials(model_access_key="gradient_test_key_1234567890")
        validate_client_credentials(agent_access_key="do_v1_1234567890abcdef1234567890abcdef")

    def test_validate_client_credentials_invalid(self):
        """Test that invalid client credentials raise ValueError."""
        # No credentials provided
        with pytest.raises(ValueError, match="At least one authentication method must be provided"):
            validate_client_credentials()

        # Invalid access token
        with pytest.raises(ValueError, match="Invalid access_token format"):
            validate_client_credentials(access_token="invalid")

        # Invalid model access key
        with pytest.raises(ValueError, match="Invalid model_access_key format"):
            validate_client_credentials(model_access_key="short")

        # Invalid agent access key - empty string is falsy, so it triggers "no credentials" error
        with pytest.raises(ValueError, match="At least one authentication method must be provided"):
            validate_client_credentials(agent_access_key="")

    def test_validate_client_credentials_multiple_valid(self):
        """Test that multiple valid credentials are accepted."""
        validate_client_credentials(
            access_token="sk-1234567890abcdef",
            model_access_key="gradient_test_key_1234567890",
            agent_access_key="do_v1_1234567890abcdef1234567890abcdef"
        )

    def test_validate_client_credentials_mixed_valid_invalid(self):
        """Test that one invalid credential among valid ones still raises error."""
        with pytest.raises(ValueError, match="Invalid access_token format"):
            validate_client_credentials(
                access_token="invalid",
                model_access_key="gradient_test_key_1234567890"
            )