# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.region import Region

__all__ = ["VolumeCreateResponse", "Volume"]


class Volume(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the block storage volume."""

    created_at: Optional[str] = None
    """
    A time value given in ISO8601 combined date and time format that represents when
    the block storage volume was created.
    """

    description: Optional[str] = None
    """An optional free-form text field to describe a block storage volume."""

    droplet_ids: Optional[List[int]] = None
    """An array containing the IDs of the Droplets the volume is attached to.

    Note that at this time, a volume can only be attached to a single Droplet.
    """

    filesystem_label: Optional[str] = None
    """The label currently applied to the filesystem."""

    filesystem_type: Optional[str] = None
    """The type of filesystem currently in-use on the volume."""

    name: Optional[str] = None
    """A human-readable name for the block storage volume.

    Must be lowercase and be composed only of numbers, letters and "-", up to a
    limit of 64 characters. The name must begin with a letter.
    """

    region: Optional[Region] = None
    """The region that the block storage volume is located in.

    When setting a region, the value should be the slug identifier for the region.
    When you query a block storage volume, the entire region object will be
    returned.
    """

    size_gigabytes: Optional[int] = None
    """The size of the block storage volume in GiB (1024^3).

    This field does not apply when creating a volume from a snapshot.
    """

    tags: Optional[List[str]] = None
    """A flat array of tag names as strings applied to the resource.

    Requires `tag:read` scope.
    """


class VolumeCreateResponse(BaseModel):
    volume: Optional[Volume] = None
