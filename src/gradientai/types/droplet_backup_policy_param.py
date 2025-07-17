# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DropletBackupPolicyParam"]


class DropletBackupPolicyParam(TypedDict, total=False):
    hour: Literal[0, 4, 8, 12, 16, 20]
    """The hour of the day that the backup window will start."""

    plan: Literal["daily", "weekly"]
    """The backup plan used for the Droplet.

    The plan can be either `daily` or `weekly`.
    """

    weekday: Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    """The day of the week on which the backup will occur."""
