# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.droplet import Droplet

__all__ = ["GPUDropletListNeighborsResponse"]


class GPUDropletListNeighborsResponse(BaseModel):
    droplets: Optional[List[Droplet]] = None
