# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...api_openai_api_key_info import APIOpenAIAPIKeyInfo

__all__ = ["OpenAIRetrieveResponse"]


class OpenAIRetrieveResponse(BaseModel):
    api_key_info: Optional[APIOpenAIAPIKeyInfo] = None
    """OpenAI API Key Info"""
