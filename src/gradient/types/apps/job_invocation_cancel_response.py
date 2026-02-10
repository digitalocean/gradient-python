# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "JobInvocationCancelResponse",
    "Trigger",
    "TriggerManual",
    "TriggerManualUser",
    "TriggerScheduled",
    "TriggerScheduledSchedule",
]


class TriggerManualUser(BaseModel):
    """The user who triggered the job"""

    email: Optional[str] = None

    full_name: Optional[str] = None

    uuid: Optional[str] = None


class TriggerManual(BaseModel):
    """Details about the manual trigger, if applicable"""

    user: Optional[TriggerManualUser] = None
    """The user who triggered the job"""


class TriggerScheduledSchedule(BaseModel):
    cron: Optional[str] = None
    """The cron expression defining the schedule"""

    time_zone: Optional[str] = None
    """The time zone for the schedule"""


class TriggerScheduled(BaseModel):
    """The schedule for the job"""

    schedule: Optional[TriggerScheduledSchedule] = None


class Trigger(BaseModel):
    manual: Optional[TriggerManual] = None
    """Details about the manual trigger, if applicable"""

    scheduled: Optional[TriggerScheduled] = None
    """The schedule for the job"""

    type: Optional[Literal["MANUAL", "SCHEDULE", "UNKNOWN"]] = None
    """The type of trigger that initiated the job invocation."""


class JobInvocationCancelResponse(BaseModel):
    id: Optional[str] = None

    completed_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    deployment_id: Optional[str] = None

    job_name: Optional[str] = None

    phase: Optional[Literal["UNKNOWN", "PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELED", "SKIPPED"]] = None
    """The phase of the job invocation"""

    started_at: Optional[datetime] = None

    trigger: Optional[Trigger] = None
