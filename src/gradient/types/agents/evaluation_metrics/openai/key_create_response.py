# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from ....api_openai_api_key_info import APIOpenAIAPIKeyInfo

__all__ = ["KeyCreateResponse"]


class KeyCreateResponse(BaseModel):
    """CreateOpenAIAPIKeyOutput is used to return the newly created OpenAI API key."""

    api_key_info: Optional[APIOpenAIAPIKeyInfo] = None
    """OpenAI API Key Info"""
