# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIEvaluationMetricResult"]


class APIEvaluationMetricResult(BaseModel):
    error_description: Optional[str] = None
    """Error description if the metric could not be calculated."""

    metric_name: Optional[str] = None
    """Metric name"""

    metric_value_type: Optional[
        Literal[
            "METRIC_VALUE_TYPE_UNSPECIFIED",
            "METRIC_VALUE_TYPE_NUMBER",
            "METRIC_VALUE_TYPE_STRING",
            "METRIC_VALUE_TYPE_PERCENTAGE",
        ]
    ] = None

    number_value: Optional[float] = None
    """The value of the metric as a number."""

    reasoning: Optional[str] = None
    """Reasoning of the metric result."""

    string_value: Optional[str] = None
    """The value of the metric as a string."""
