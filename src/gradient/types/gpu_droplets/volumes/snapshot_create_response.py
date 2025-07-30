# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...shared.snapshots import Snapshots

__all__ = ["SnapshotCreateResponse"]


class SnapshotCreateResponse(BaseModel):
    snapshot: Optional[Snapshots] = None
