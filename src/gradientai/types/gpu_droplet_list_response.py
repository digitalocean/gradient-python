# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.droplet import Droplet
from .shared.page_links import PageLinks
from .shared.meta_properties import MetaProperties

__all__ = ["GPUDropletListResponse"]


class GPUDropletListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    droplets: Optional[List[Droplet]] = None

    links: Optional[PageLinks] = None
