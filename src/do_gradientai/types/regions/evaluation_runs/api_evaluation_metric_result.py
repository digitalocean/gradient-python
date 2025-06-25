# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["APIEvaluationMetricResult"]


class APIEvaluationMetricResult(BaseModel):
    metric_name: Optional[str] = None

    number_value: Optional[float] = None
    """The value of the metric as a number."""

    string_value: Optional[str] = None
    """The value of the metric as a string."""
