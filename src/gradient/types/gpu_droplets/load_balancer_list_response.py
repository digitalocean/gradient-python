# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .load_balancer import LoadBalancer
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["LoadBalancerListResponse"]


class LoadBalancerListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    links: Optional[PageLinks] = None

    load_balancers: Optional[List[LoadBalancer]] = None
