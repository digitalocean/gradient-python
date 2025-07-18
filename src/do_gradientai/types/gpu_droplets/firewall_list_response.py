# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .firewall import Firewall
from ..._models import BaseModel
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["FirewallListResponse"]


class FirewallListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    firewalls: Optional[List[Firewall]] = None

    links: Optional[PageLinks] = None
