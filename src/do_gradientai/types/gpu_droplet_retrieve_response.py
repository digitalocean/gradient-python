# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.droplet import Droplet

__all__ = ["GPUDropletRetrieveResponse"]


class GPUDropletRetrieveResponse(BaseModel):
    droplet: Optional[Droplet] = None
