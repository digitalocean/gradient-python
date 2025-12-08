# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SnapshotRetrieveResponse", "Snapshot"]


class Snapshot(BaseModel):
    """Represents an NFS snapshot."""

    id: str
    """The unique identifier of the snapshot."""

    created_at: datetime
    """The timestamp when the snapshot was created."""

    name: str
    """The human-readable name of the snapshot."""

    region: str
    """The DigitalOcean region slug where the snapshot is located."""

    share_id: str
    """The unique identifier of the share from which this snapshot was created."""

    size_gib: int
    """The size of the snapshot in GiB."""

    status: Literal["UNKNOWN", "CREATING", "ACTIVE", "FAILED", "DELETED"]
    """The current status of the snapshot."""


class SnapshotRetrieveResponse(BaseModel):
    snapshot: Optional[Snapshot] = None
    """Represents an NFS snapshot."""
