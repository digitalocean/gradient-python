# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .api_evaluation_test_case import APIEvaluationTestCase

__all__ = ["EvaluationTestCaseListResponse"]


class EvaluationTestCaseListResponse(BaseModel):
    evaluation_test_cases: Optional[List[APIEvaluationTestCase]] = None
    """
    Alternative way of authentication for internal usage only - should not be
    exposed to public api
    """
