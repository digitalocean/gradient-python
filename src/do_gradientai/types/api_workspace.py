# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .agents.api_evaluation_test_case import APIEvaluationTestCase

__all__ = ["APIWorkspace"]


class APIWorkspace(BaseModel):
    agents: Optional[List["APIAgent"]] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    created_by_email: Optional[str] = None

    deleted_at: Optional[datetime] = None

    description: Optional[str] = None

    evaluation_test_cases: Optional[List[APIEvaluationTestCase]] = None

    name: Optional[str] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


from .api_agent import APIAgent
