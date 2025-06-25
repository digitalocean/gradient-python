# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .api_evaluation_test_case import APIEvaluationTestCase

__all__ = ["EvaluationTestCaseRetrieveResponse"]


class EvaluationTestCaseRetrieveResponse(BaseModel):
    evaluation_test_case: Optional[APIEvaluationTestCase] = None
