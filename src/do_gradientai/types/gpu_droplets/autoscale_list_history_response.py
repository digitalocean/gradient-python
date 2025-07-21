# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.page_links import PageLinks
from ..shared.meta_properties import MetaProperties

__all__ = ["AutoscaleListHistoryResponse", "History"]


class History(BaseModel):
    created_at: datetime
    """
    The creation time of the history event in ISO8601 combined date and time format.
    """

    current_instance_count: int
    """The current number of Droplets in the autoscale pool."""

    desired_instance_count: int
    """The target number of Droplets for the autoscale pool after the scaling event."""

    history_event_id: str
    """The unique identifier of the history event."""

    reason: Literal["CONFIGURATION_CHANGE", "SCALE_UP", "SCALE_DOWN"]
    """The reason for the scaling event."""

    status: Literal["in_progress", "success", "error"]
    """The status of the scaling event."""

    updated_at: datetime
    """
    The last updated time of the history event in ISO8601 combined date and time
    format.
    """


class AutoscaleListHistoryResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    history: Optional[List[History]] = None

    links: Optional[PageLinks] = None
