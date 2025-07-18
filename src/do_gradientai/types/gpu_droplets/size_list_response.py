# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.size import Size
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["SizeListResponse"]


class SizeListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    sizes: List[Size]

    links: Optional[PageLinks] = None
