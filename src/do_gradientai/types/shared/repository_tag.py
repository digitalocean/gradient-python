# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["RepositoryTag"]


class RepositoryTag(BaseModel):
    compressed_size_bytes: Optional[int] = None
    """The compressed size of the tag in bytes."""

    manifest_digest: Optional[str] = None
    """The digest of the manifest associated with the tag."""

    registry_name: Optional[str] = None
    """The name of the container registry."""

    repository: Optional[str] = None
    """The name of the repository."""

    size_bytes: Optional[int] = None
    """
    The uncompressed size of the tag in bytes (this size is calculated
    asynchronously so it may not be immediately available).
    """

    tag: Optional[str] = None
    """The name of the tag."""

    updated_at: Optional[datetime] = None
    """The time the tag was last updated."""
