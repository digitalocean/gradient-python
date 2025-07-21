# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.image import Image
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["ImageListResponse"]


class ImageListResponse(BaseModel):
    images: List[Image]

    meta: MetaProperties
    """Information about the response itself."""

    links: Optional[PageLinks] = None
