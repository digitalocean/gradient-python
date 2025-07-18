# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...shared.snapshots import Snapshots

__all__ = ["SnapshotRetrieveResponse"]


class SnapshotRetrieveResponse(BaseModel):
    snapshot: Optional[Snapshots] = None
