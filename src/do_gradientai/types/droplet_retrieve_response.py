# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.droplet import Droplet

__all__ = ["DropletRetrieveResponse"]


class DropletRetrieveResponse(BaseModel):
    droplet: Optional[Droplet] = None
