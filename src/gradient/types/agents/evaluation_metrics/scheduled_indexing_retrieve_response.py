# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ScheduledIndexingRetrieveResponse", "IndexingInfo"]


class IndexingInfo(BaseModel):
    """Metadata for scheduled indexing entries"""

    created_at: Optional[datetime] = None
    """Created at timestamp"""

    days: Optional[List[int]] = None
    """Days for execution (day is represented same as in a cron expression, e.g.

    Monday begins with 1 )
    """

    deleted_at: Optional[datetime] = None
    """Deleted at timestamp (if soft deleted)"""

    is_active: Optional[bool] = None
    """Whether the schedule is currently active"""

    knowledge_base_uuid: Optional[str] = None
    """Knowledge base uuid associated with this schedule"""

    last_ran_at: Optional[datetime] = None
    """Last time the schedule was executed"""

    next_run_at: Optional[datetime] = None
    """Next scheduled run"""

    time: Optional[str] = None
    """Scheduled time of execution (HH:MM:SS format)"""

    updated_at: Optional[datetime] = None
    """Updated at timestamp"""

    uuid: Optional[str] = None
    """Unique identifier for the scheduled indexing entry"""


class ScheduledIndexingRetrieveResponse(BaseModel):
    indexing_info: Optional[IndexingInfo] = None
    """Metadata for scheduled indexing entries"""
