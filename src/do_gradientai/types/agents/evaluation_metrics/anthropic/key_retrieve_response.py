# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from ....api_anthropic_api_key_info import APIAnthropicAPIKeyInfo

__all__ = ["KeyRetrieveResponse"]


class KeyRetrieveResponse(BaseModel):
    api_key_info: Optional[APIAnthropicAPIKeyInfo] = None
    """Anthropic API Key Info"""
