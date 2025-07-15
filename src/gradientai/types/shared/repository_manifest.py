# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .repository_blob import RepositoryBlob

__all__ = ["RepositoryManifest"]


class RepositoryManifest(BaseModel):
    blobs: Optional[List[RepositoryBlob]] = None
    """All blobs associated with this manifest"""

    compressed_size_bytes: Optional[int] = None
    """The compressed size of the manifest in bytes."""

    digest: Optional[str] = None
    """The manifest digest"""

    registry_name: Optional[str] = None
    """The name of the container registry."""

    repository: Optional[str] = None
    """The name of the repository."""

    size_bytes: Optional[int] = None
    """
    The uncompressed size of the manifest in bytes (this size is calculated
    asynchronously so it may not be immediately available).
    """

    tags: Optional[List[str]] = None
    """All tags associated with this manifest"""

    updated_at: Optional[datetime] = None
    """The time the manifest was last updated."""
