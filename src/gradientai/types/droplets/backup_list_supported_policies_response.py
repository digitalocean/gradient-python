# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BackupListSupportedPoliciesResponse", "SupportedPolicy"]


class SupportedPolicy(BaseModel):
    name: Optional[str] = None
    """The name of the Droplet backup plan."""

    possible_days: Optional[List[str]] = None
    """The day of the week the backup will occur."""

    possible_window_starts: Optional[List[int]] = None
    """An array of integers representing the hours of the day that a backup can start."""

    retention_period_days: Optional[int] = None
    """The number of days that a backup will be kept."""

    window_length_hours: Optional[int] = None
    """The number of hours that a backup window is open."""


class BackupListSupportedPoliciesResponse(BaseModel):
    supported_policies: Optional[List[SupportedPolicy]] = None
