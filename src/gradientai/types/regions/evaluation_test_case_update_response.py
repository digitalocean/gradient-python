# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EvaluationTestCaseUpdateResponse"]


class EvaluationTestCaseUpdateResponse(BaseModel):
    test_case_uuid: Optional[str] = None

    version: Optional[int] = None
    """The new verson of the test case."""
