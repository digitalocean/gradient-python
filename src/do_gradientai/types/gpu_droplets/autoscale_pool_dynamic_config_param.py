# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutoscalePoolDynamicConfigParam"]


class AutoscalePoolDynamicConfigParam(TypedDict, total=False):
    max_instances: Required[int]
    """The maximum number of Droplets in an autoscale pool."""

    min_instances: Required[int]
    """The minimum number of Droplets in an autoscale pool."""

    cooldown_minutes: int
    """The number of minutes to wait between scaling events in an autoscale pool.

    Defaults to 10 minutes.
    """

    target_cpu_utilization: float
    """Target CPU utilization as a decimal."""

    target_memory_utilization: float
    """Target memory utilization as a decimal."""
