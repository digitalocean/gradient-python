# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_agent_api_key_info import APIAgentAPIKeyInfo

__all__ = ["APIKeyCreateResponse"]


class APIKeyCreateResponse(BaseModel):
    api_key_info: Optional[APIAgentAPIKeyInfo] = None
    """Agent API Key Info"""
