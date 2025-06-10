# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel
from .project_api_key import ProjectAPIKey

__all__ = ["APIKeyListResponse"]


class APIKeyListResponse(BaseModel):
    data: List[ProjectAPIKey]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
