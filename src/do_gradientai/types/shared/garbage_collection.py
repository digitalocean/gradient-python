# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GarbageCollection"]


class GarbageCollection(BaseModel):
    blobs_deleted: Optional[int] = None
    """The number of blobs deleted as a result of this garbage collection."""

    created_at: Optional[datetime] = None
    """The time the garbage collection was created."""

    freed_bytes: Optional[int] = None
    """The number of bytes freed as a result of this garbage collection."""

    registry_name: Optional[str] = None
    """The name of the container registry."""

    status: Optional[
        Literal[
            "requested",
            "waiting for write JWTs to expire",
            "scanning manifests",
            "deleting unreferenced blobs",
            "cancelling",
            "failed",
            "succeeded",
            "cancelled",
        ]
    ] = None
    """The current status of this garbage collection."""

    updated_at: Optional[datetime] = None
    """The time the garbage collection was last updated."""

    uuid: Optional[str] = None
    """A string specifying the UUID of the garbage collection."""
