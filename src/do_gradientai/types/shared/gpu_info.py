# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GPUInfo", "Vram"]


class Vram(BaseModel):
    amount: Optional[int] = None
    """The amount of VRAM allocated to the GPU."""

    unit: Optional[str] = None
    """The unit of measure for the VRAM."""


class GPUInfo(BaseModel):
    count: Optional[int] = None
    """The number of GPUs allocated to the Droplet."""

    model: Optional[str] = None
    """The model of the GPU."""

    vram: Optional[Vram] = None
