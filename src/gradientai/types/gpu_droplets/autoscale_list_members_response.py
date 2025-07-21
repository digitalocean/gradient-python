# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["AutoscaleListMembersResponse", "Droplet", "DropletCurrentUtilization"]


class DropletCurrentUtilization(BaseModel):
    cpu: Optional[float] = None
    """The CPU utilization average of the individual Droplet."""

    memory: Optional[float] = None
    """The memory utilization average of the individual Droplet."""


class Droplet(BaseModel):
    created_at: datetime
    """The creation time of the Droplet in ISO8601 combined date and time format."""

    current_utilization: DropletCurrentUtilization

    droplet_id: int
    """The unique identifier of the Droplet."""

    health_status: str
    """The health status of the Droplet."""

    status: Literal["provisioning", "active", "deleting", "off"]
    """The power status of the Droplet."""

    updated_at: datetime
    """The last updated time of the Droplet in ISO8601 combined date and time format."""


class AutoscaleListMembersResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    droplets: Optional[List[Droplet]] = None

    links: Optional[PageLinks] = None
