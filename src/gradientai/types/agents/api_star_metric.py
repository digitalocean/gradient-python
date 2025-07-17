# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APIStarMetric"]


class APIStarMetric(BaseModel):
    metric_uuid: Optional[str] = None

    name: Optional[str] = None

    success_threshold: Optional[float] = None
    """
    The success threshold for the star metric. This is a value that the metric must
    reach to be considered successful.
    """

    success_threshold_pct: Optional[int] = None
    """
    The success threshold for the star metric. This is a percentage value between 0
    and 100.
    """
