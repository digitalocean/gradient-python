# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .agents.api_evaluation_test_case import APIEvaluationTestCase

__all__ = ["APIWorkspace"]


class APIWorkspace(BaseModel):
    agents: Optional[List["APIAgent"]] = None
    """Agents"""

    created_at: Optional[datetime] = None
    """Creation date"""

    created_by: Optional[str] = None
    """The id of user who created this workspace"""

    created_by_email: Optional[str] = None
    """The email of the user who created this workspace"""

    deleted_at: Optional[datetime] = None
    """Deleted date"""

    description: Optional[str] = None
    """Description of the workspace"""

    evaluation_test_cases: Optional[List[APIEvaluationTestCase]] = None
    """Evaluations"""

    name: Optional[str] = None
    """Name of the workspace"""

    updated_at: Optional[datetime] = None
    """Update date"""

    uuid: Optional[str] = None
    """Unique id"""


from .api_agent import APIAgent
