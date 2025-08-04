# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIIndexingJob"]


class APIIndexingJob(BaseModel):
    completed_datasources: Optional[int] = None
    """Number of datasources indexed completed"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    data_source_uuids: Optional[List[str]] = None

    finished_at: Optional[datetime] = None

    knowledge_base_uuid: Optional[str] = None
    """Knowledge base id"""

    phase: Optional[
        Literal[
            "BATCH_JOB_PHASE_UNKNOWN",
            "BATCH_JOB_PHASE_PENDING",
            "BATCH_JOB_PHASE_RUNNING",
            "BATCH_JOB_PHASE_SUCCEEDED",
            "BATCH_JOB_PHASE_FAILED",
            "BATCH_JOB_PHASE_ERROR",
            "BATCH_JOB_PHASE_CANCELLED",
        ]
    ] = None

    started_at: Optional[datetime] = None

    status: Optional[
        Literal[
            "INDEX_JOB_STATUS_UNKNOWN",
            "INDEX_JOB_STATUS_PARTIAL",
            "INDEX_JOB_STATUS_IN_PROGRESS",
            "INDEX_JOB_STATUS_COMPLETED",
            "INDEX_JOB_STATUS_FAILED",
            "INDEX_JOB_STATUS_NO_CHANGES",
            "INDEX_JOB_STATUS_PENDING",
        ]
    ] = None

    tokens: Optional[int] = None
    """Number of tokens"""

    total_datasources: Optional[int] = None
    """Number of datasources being indexed"""

    total_items_failed: Optional[str] = None
    """Total Items Failed"""

    total_items_indexed: Optional[str] = None
    """Total Items Indexed"""

    total_items_skipped: Optional[str] = None
    """Total Items Skipped"""

    updated_at: Optional[datetime] = None
    """Last modified"""

    uuid: Optional[str] = None
    """Unique id"""
