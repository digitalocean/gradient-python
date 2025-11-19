# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NfListResponse", "Share"]


class Share(BaseModel):
    id: str
    """The unique identifier of the NFS share."""

    created_at: datetime
    """Timestamp for when the NFS share was created."""

    name: str
    """The human-readable name of the share."""

    region: str
    """The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides."""

    size_gib: int
    """The desired/provisioned size of the share in GiB (Gibibytes). Must be >= 50."""

    status: Literal["CREATING", "ACTIVE", "FAILED", "DELETED"]
    """The current status of the share."""

    host: Optional[str] = None
    """The host IP of the NFS server that will be accessible from the associated VPC"""

    mount_path: Optional[str] = None
    """
    Path at which the share will be available, to be mounted at a target of the
    user's choice within the client
    """

    vpc_ids: Optional[List[str]] = None
    """List of VPC IDs that should be able to access the share."""


class NfListResponse(BaseModel):
    shares: Optional[List[Share]] = None
