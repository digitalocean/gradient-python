# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["BackupListResponse", "Backup"]


class Backup(BaseModel):
    id: int
    """The unique identifier for the snapshot or backup."""

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

    size_gigabytes: float
    """The billable size of the snapshot in gigabytes."""

    type: Literal["snapshot", "backup"]
    """Describes the kind of image.

    It may be one of `snapshot` or `backup`. This specifies whether an image is a
    user-generated Droplet snapshot or automatically created Droplet backup.
    """


class BackupListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    backups: Optional[List[Backup]] = None

    links: Optional[PageLinks] = None
