# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .floating_ip import FloatingIP
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["FloatingIPListResponse"]


class FloatingIPListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    floating_ips: Optional[List[FloatingIP]] = None

    links: Optional[PageLinks] = None
