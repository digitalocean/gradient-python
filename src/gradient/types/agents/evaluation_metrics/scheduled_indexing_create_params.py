# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["ScheduledIndexingCreateParams"]


class ScheduledIndexingCreateParams(TypedDict, total=False):
    days: Iterable[int]
    """Days for execution (day is represented same as in a cron expression, e.g.

    Monday begins with 1 )
    """

    knowledge_base_uuid: str
    """Knowledge base uuid for which the schedule is created"""

    time: str
    """Time of execution (HH:MM) UTC"""
