# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Snapshots"]


class Snapshots(BaseModel):
    id: str
    """The unique identifier for the snapshot."""

    created_at: datetime
    """
    A time value given in ISO8601 combined date and time format that represents when
    the snapshot was created.
    """

    min_disk_size: int
    """The minimum size in GB required for a volume or Droplet to use this snapshot."""

    name: str
    """A human-readable name for the snapshot."""

    regions: List[str]
    """An array of the regions that the snapshot is available in.

    The regions are represented by their identifying slug values.
    """

    resource_id: str
    """The unique identifier for the resource that the snapshot originated from."""

    resource_type: Literal["droplet", "volume"]
    """The type of resource that the snapshot originated from."""

    size_gigabytes: float
    """The billable size of the snapshot in gigabytes."""

    tags: Optional[List[str]] = None
    """An array of Tags the snapshot has been tagged with.

    Requires `tag:read` scope.
    """
