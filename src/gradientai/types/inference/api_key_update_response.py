# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .api_model_api_key_info import APIModelAPIKeyInfo

__all__ = ["APIKeyUpdateResponse"]


class APIKeyUpdateResponse(BaseModel):
    api_key_info: Optional[APIModelAPIKeyInfo] = None
    """Model API Key Info"""
