# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIEvaluationMetric"]


class APIEvaluationMetric(BaseModel):
    category: Optional[
        Literal[
            "METRIC_CATEGORY_UNSPECIFIED",
            "METRIC_CATEGORY_CORRECTNESS",
            "METRIC_CATEGORY_USER_OUTCOMES",
            "METRIC_CATEGORY_SAFETY_AND_SECURITY",
            "METRIC_CATEGORY_CONTEXT_QUALITY",
            "METRIC_CATEGORY_MODEL_FIT",
        ]
    ] = None

    description: Optional[str] = None

    inverted: Optional[bool] = None
    """If true, the metric is inverted, meaning that a lower value is better."""

    is_metric_goal: Optional[bool] = None

    metric_name: Optional[str] = None

    metric_rank: Optional[int] = None

    metric_type: Optional[
        Literal["METRIC_TYPE_UNSPECIFIED", "METRIC_TYPE_GENERAL_QUALITY", "METRIC_TYPE_RAG_AND_TOOL"]
    ] = None

    metric_uuid: Optional[str] = None

    metric_value_type: Optional[
        Literal[
            "METRIC_VALUE_TYPE_UNSPECIFIED",
            "METRIC_VALUE_TYPE_NUMBER",
            "METRIC_VALUE_TYPE_STRING",
            "METRIC_VALUE_TYPE_PERCENTAGE",
        ]
    ] = None

    range_max: Optional[float] = None
    """The maximum value for the metric."""

    range_min: Optional[float] = None
    """The minimum value for the metric."""
