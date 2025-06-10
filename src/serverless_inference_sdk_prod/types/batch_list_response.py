# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .batch import Batch
from .._models import BaseModel

__all__ = ["BatchListResponse"]


class BatchListResponse(BaseModel):
    data: List[Batch]

    has_more: bool

    object: Literal["list"]

    first_id: Optional[str] = None

    last_id: Optional[str] = None
