# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DropletBackupPolicy"]


class DropletBackupPolicy(BaseModel):
    hour: Optional[Literal[0, 4, 8, 12, 16, 20]] = None
    """The hour of the day that the backup window will start."""

    plan: Optional[Literal["daily", "weekly"]] = None
    """The backup plan used for the Droplet.

    The plan can be either `daily` or `weekly`.
    """

    retention_period_days: Optional[int] = None
    """The number of days the backup will be retained."""

    weekday: Optional[Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]] = None
    """The day of the week on which the backup will occur."""

    window_length_hours: Optional[int] = None
    """The length of the backup window starting from `hour`."""
