# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIEvaluationMetric"]


class APIEvaluationMetric(BaseModel):
    description: Optional[str] = None

    metric_name: Optional[str] = None

    metric_type: Optional[
        Literal["METRIC_TYPE_UNSPECIFIED", "METRIC_TYPE_GENERAL_QUALITY", "METRIC_TYPE_RAG_AND_TOOL"]
    ] = None

    metric_uuid: Optional[str] = None

    metric_value_type: Optional[
        Literal["METRIC_VALUE_TYPE_UNSPECIFIED", "METRIC_VALUE_TYPE_NUMBER", "METRIC_VALUE_TYPE_STRING"]
    ] = None
