# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AutoscalePoolDynamicConfig"]


class AutoscalePoolDynamicConfig(BaseModel):
    max_instances: int
    """The maximum number of Droplets in an autoscale pool."""

    min_instances: int
    """The minimum number of Droplets in an autoscale pool."""

    cooldown_minutes: Optional[int] = None
    """The number of minutes to wait between scaling events in an autoscale pool.

    Defaults to 10 minutes.
    """

    target_cpu_utilization: Optional[float] = None
    """Target CPU utilization as a decimal."""

    target_memory_utilization: Optional[float] = None
    """Target memory utilization as a decimal."""
