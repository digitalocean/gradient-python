# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .api_key import APIKey
from ...._models import BaseModel

__all__ = ["APIKeyListResponse"]


class APIKeyListResponse(BaseModel):
    data: List[APIKey]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
