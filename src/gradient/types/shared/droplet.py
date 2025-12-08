# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .size import Size
from .image import Image
from .kernel import Kernel
from .region import Region
from .gpu_info import GPUInfo
from ..._models import BaseModel
from .disk_info import DiskInfo
from .network_v4 import NetworkV4
from .network_v6 import NetworkV6
from .droplet_next_backup_window import DropletNextBackupWindow

__all__ = ["Droplet", "Networks"]


class Networks(BaseModel):
    """The details of the network that are configured for the Droplet instance.

    This is an object that contains keys for IPv4 and IPv6.  The value of each of these is an array that contains objects describing an individual IP resource allocated to the Droplet.  These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.
    """

    v4: Optional[List[NetworkV4]] = None

    v6: Optional[List[NetworkV6]] = None


class Droplet(BaseModel):
    id: int
    """A unique identifier for each Droplet instance.

    This is automatically generated upon Droplet creation.
    """

    backup_ids: List[int]
    """
    An array of backup IDs of any backups that have been taken of the Droplet
    instance. Droplet backups are enabled at the time of the instance creation.
    Requires `image:read` scope.
    """

    created_at: datetime
    """
    A time value given in ISO8601 combined date and time format that represents when
    the Droplet was created.
    """

    disk: int
    """The size of the Droplet's disk in gigabytes."""

    features: List[str]
    """An array of features enabled on this Droplet."""

    image: Image
    """The Droplet's image. Requires `image:read` scope."""

    locked: bool
    """
    A boolean value indicating whether the Droplet has been locked, preventing
    actions by users.
    """

    memory: int
    """Memory of the Droplet in megabytes."""

    name: str
    """The human-readable name set for the Droplet instance."""

    networks: Networks
    """The details of the network that are configured for the Droplet instance.

    This is an object that contains keys for IPv4 and IPv6. The value of each of
    these is an array that contains objects describing an individual IP resource
    allocated to the Droplet. These will define attributes like the IP address,
    netmask, and gateway of the specific network depending on the type of network it
    is.
    """

    next_backup_window: Optional[DropletNextBackupWindow] = None
    """
    The details of the Droplet's backups feature, if backups are configured for the
    Droplet. This object contains keys for the start and end times of the window
    during which the backup will start.
    """

    region: Region

    size: Size

    size_slug: str
    """The unique slug identifier for the size of this Droplet."""

    snapshot_ids: List[int]
    """
    An array of snapshot IDs of any snapshots created from the Droplet instance.
    Requires `image:read` scope.
    """

    status: Literal["new", "active", "off", "archive"]
    """A status string indicating the state of the Droplet instance.

    This may be "new", "active", "off", or "archive".
    """

    tags: List[str]
    """An array of Tags the Droplet has been tagged with. Requires `tag:read` scope."""

    vcpus: int
    """The number of virtual CPUs."""

    volume_ids: List[str]
    """
    A flat array including the unique identifier for each Block Storage volume
    attached to the Droplet. Requires `block_storage:read` scope.
    """

    disk_info: Optional[List[DiskInfo]] = None
    """
    An array of objects containing information about the disks available to the
    Droplet.
    """

    gpu_info: Optional[GPUInfo] = None
    """
    An object containing information about the GPU capabilities of Droplets created
    with this size.
    """

    kernel: Optional[Kernel] = None
    """
    **Note**: All Droplets created after March 2017 use internal kernels by default.
    These Droplets will have this attribute set to `null`.

    The current
    [kernel](https://docs.digitalocean.com/products/droplets/how-to/kernel/) for
    Droplets with externally managed kernels. This will initially be set to the
    kernel of the base image when the Droplet is created.
    """

    vpc_uuid: Optional[str] = None
    """
    A string specifying the UUID of the VPC to which the Droplet is assigned.
    Requires `vpc:read` scope.
    """
