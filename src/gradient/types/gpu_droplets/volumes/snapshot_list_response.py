# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.snapshots import Snapshots
from ...shared.page_links import PageLinks
from ...shared.meta_properties import MetaProperties

__all__ = ["SnapshotListResponse"]


class SnapshotListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    links: Optional[PageLinks] = None

    snapshots: Optional[List[Snapshots]] = None
