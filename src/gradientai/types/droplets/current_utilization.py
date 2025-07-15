# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CurrentUtilization"]


class CurrentUtilization(BaseModel):
    cpu: Optional[float] = None
    """The average CPU utilization of the autoscale pool."""

    memory: Optional[float] = None
    """The average memory utilization of the autoscale pool."""
