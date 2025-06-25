# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIIndexingJob"]


class APIIndexingJob(BaseModel):
    completed_datasources: Optional[int] = None

    created_at: Optional[datetime] = None

    data_source_uuids: Optional[List[str]] = None

    finished_at: Optional[datetime] = None

    knowledge_base_uuid: Optional[str] = None

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

    tokens: Optional[int] = None

    total_datasources: Optional[int] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None
