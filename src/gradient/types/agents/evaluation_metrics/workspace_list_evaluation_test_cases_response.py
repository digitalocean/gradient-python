# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..api_evaluation_test_case import APIEvaluationTestCase

__all__ = ["WorkspaceListEvaluationTestCasesResponse"]


class WorkspaceListEvaluationTestCasesResponse(BaseModel):
    evaluation_test_cases: Optional[List[APIEvaluationTestCase]] = None
