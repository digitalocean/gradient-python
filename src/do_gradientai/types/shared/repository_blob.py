# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RepositoryBlob"]


class RepositoryBlob(BaseModel):
    compressed_size_bytes: Optional[int] = None
    """The compressed size of the blob in bytes."""

    digest: Optional[str] = None
    """The digest of the blob"""
