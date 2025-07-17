# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DiskInfo", "Size"]


class Size(BaseModel):
    amount: Optional[int] = None
    """The amount of space allocated to the disk."""

    unit: Optional[str] = None
    """The unit of measure for the disk size."""


class DiskInfo(BaseModel):
    size: Optional[Size] = None

    type: Optional[Literal["local", "scratch"]] = None
    """The type of disk.

    All Droplets contain a `local` disk. Additionally, GPU Droplets can also have a
    `scratch` disk for non-persistent data.
    """
