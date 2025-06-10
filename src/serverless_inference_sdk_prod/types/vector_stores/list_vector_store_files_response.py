# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .vector_store_file_object import VectorStoreFileObject

__all__ = ["ListVectorStoreFilesResponse"]


class ListVectorStoreFilesResponse(BaseModel):
    data: List[VectorStoreFileObject]

    first_id: str

    has_more: bool

    last_id: str

    object: str
