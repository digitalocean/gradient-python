# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["APIStarMetricParam"]


class APIStarMetricParam(TypedDict, total=False):
    metric_uuid: str

    name: str

    success_threshold: float
    """
    The success threshold for the star metric. This is a value that the metric must
    reach to be considered successful.
    """

    success_threshold_pct: int
    """
    The success threshold for the star metric. This is a percentage value between 0
    and 100.
    """
