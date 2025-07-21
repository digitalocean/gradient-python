# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.page_links import PageLinks
from .gpu_droplets.firewall import Firewall
from .shared.meta_properties import MetaProperties

__all__ = ["GPUDropletListFirewallsResponse"]


class GPUDropletListFirewallsResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    firewalls: Optional[List[Firewall]] = None

    links: Optional[PageLinks] = None
