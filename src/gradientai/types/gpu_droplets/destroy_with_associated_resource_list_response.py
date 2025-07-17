# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .associated_resource import AssociatedResource

__all__ = ["DestroyWithAssociatedResourceListResponse"]


class DestroyWithAssociatedResourceListResponse(BaseModel):
    floating_ips: Optional[List[AssociatedResource]] = None
    """
    Floating IPs that are associated with this Droplet. Requires `reserved_ip:read`
    scope.
    """

    reserved_ips: Optional[List[AssociatedResource]] = None
    """
    Reserved IPs that are associated with this Droplet. Requires `reserved_ip:read`
    scope.
    """

    snapshots: Optional[List[AssociatedResource]] = None
    """Snapshots that are associated with this Droplet. Requires `image:read` scope."""

    volume_snapshots: Optional[List[AssociatedResource]] = None
    """
    Volume Snapshots that are associated with this Droplet. Requires
    `block_storage_snapshot:read` scope.
    """

    volumes: Optional[List[AssociatedResource]] = None
    """
    Volumes that are associated with this Droplet. Requires `block_storage:read`
    scope.
    """
