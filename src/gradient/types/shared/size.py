# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .gpu_info import GPUInfo
from ..._models import BaseModel
from .disk_info import DiskInfo

__all__ = ["Size"]


class Size(BaseModel):
    available: bool
    """
    This is a boolean value that represents whether new Droplets can be created with
    this size.
    """

    description: str
    """A string describing the class of Droplets created from this size.

    For example: Basic, General Purpose, CPU-Optimized, Memory-Optimized, or
    Storage-Optimized.
    """

    disk: int
    """The amount of disk space set aside for Droplets of this size.

    The value is represented in gigabytes.
    """

    memory: int
    """The amount of RAM allocated to Droplets created of this size.

    The value is represented in megabytes.
    """

    price_hourly: float
    """This describes the price of the Droplet size as measured hourly.

    The value is measured in US dollars.
    """

    price_monthly: float
    """
    This attribute describes the monthly cost of this Droplet size if the Droplet is
    kept for an entire month. The value is measured in US dollars.
    """

    regions: List[str]
    """
    An array containing the region slugs where this size is available for Droplet
    creates.
    """

    slug: str
    """A human-readable string that is used to uniquely identify each size."""

    transfer: float
    """
    The amount of transfer bandwidth that is available for Droplets created in this
    size. This only counts traffic on the public interface. The value is given in
    terabytes.
    """

    vcpus: int
    """The number of CPUs allocated to Droplets of this size."""

    disk_info: Optional[List[DiskInfo]] = None
    """
    An array of objects containing information about the disks available to Droplets
    created with this size.
    """

    gpu_info: Optional[GPUInfo] = None
    """
    An object containing information about the GPU capabilities of Droplets created
    with this size.
    """
