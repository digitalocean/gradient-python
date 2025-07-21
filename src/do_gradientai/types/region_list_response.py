# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.region import Region
from .shared.page_links import PageLinks
from .shared.meta_properties import MetaProperties

__all__ = ["RegionListResponse"]


class RegionListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    regions: List[Region]

    links: Optional[PageLinks] = None
