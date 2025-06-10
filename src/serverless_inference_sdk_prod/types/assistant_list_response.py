# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .assistant_object import AssistantObject

__all__ = ["AssistantListResponse"]


class AssistantListResponse(BaseModel):
    data: List[AssistantObject]

    first_id: str

    has_more: bool

    last_id: str

    object: str
