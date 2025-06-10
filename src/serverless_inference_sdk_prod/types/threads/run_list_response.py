# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .run_object import RunObject

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    data: List[RunObject]

    first_id: str

    has_more: bool

    last_id: str

    object: str
