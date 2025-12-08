# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...api_anthropic_api_key_info import APIAnthropicAPIKeyInfo

__all__ = ["AnthropicUpdateResponse"]


class AnthropicUpdateResponse(BaseModel):
    """UpdateAnthropicAPIKeyOutput is used to return the updated Anthropic API key."""

    api_key_info: Optional[APIAnthropicAPIKeyInfo] = None
    """Anthropic API Key Info"""
