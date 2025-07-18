# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VpcPeering"]


class VpcPeering(BaseModel):
    id: Optional[str] = None
    """A unique ID that can be used to identify and reference the VPC peering."""

    created_at: Optional[datetime] = None
    """A time value given in ISO8601 combined date and time format."""

    name: Optional[str] = None
    """The name of the VPC peering.

    Must be unique within the team and may only contain alphanumeric characters and
    dashes.
    """

    status: Optional[Literal["PROVISIONING", "ACTIVE", "DELETING"]] = None
    """The current status of the VPC peering."""

    vpc_ids: Optional[List[str]] = None
    """An array of the two peered VPCs IDs."""
