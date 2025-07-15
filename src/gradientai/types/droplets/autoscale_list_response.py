# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .autoscale_pool import AutoscalePool
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["AutoscaleListResponse"]


class AutoscaleListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    autoscale_pools: Optional[List[AutoscalePool]] = None

    links: Optional[PageLinks] = None
