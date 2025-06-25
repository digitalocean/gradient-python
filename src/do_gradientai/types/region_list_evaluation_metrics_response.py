# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_evaluation_metric import APIEvaluationMetric

__all__ = ["RegionListEvaluationMetricsResponse"]


class RegionListEvaluationMetricsResponse(BaseModel):
    metrics: Optional[List[APIEvaluationMetric]] = None
