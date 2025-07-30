# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .volume_action import VolumeAction
from ...shared.page_links import PageLinks
from ...shared.meta_properties import MetaProperties

__all__ = ["ActionListResponse"]


class ActionListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    actions: Optional[List[VolumeAction]] = None

    links: Optional[PageLinks] = None
