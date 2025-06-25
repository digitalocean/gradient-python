# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EvaluationTestCaseCreateResponse"]


class EvaluationTestCaseCreateResponse(BaseModel):
    test_case_uuid: Optional[str] = None
    """Test‑case UUID."""
