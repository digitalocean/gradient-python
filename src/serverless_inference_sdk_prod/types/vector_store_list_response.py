# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .vector_store_object import VectorStoreObject

__all__ = ["VectorStoreListResponse"]


class VectorStoreListResponse(BaseModel):
    data: List[VectorStoreObject]

    first_id: str

    has_more: bool

    last_id: str

    object: str
