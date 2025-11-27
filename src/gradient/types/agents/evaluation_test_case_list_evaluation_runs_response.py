# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .api_evaluation_run import APIEvaluationRun

__all__ = ["EvaluationTestCaseListEvaluationRunsResponse"]


class EvaluationTestCaseListEvaluationRunsResponse(BaseModel):
    evaluation_runs: Optional[List[APIEvaluationRun]] = None
    """List of evaluation runs."""
