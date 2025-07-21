# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .api_evaluation_metric_result import APIEvaluationMetricResult

__all__ = ["APIEvaluationRun"]


class APIEvaluationRun(BaseModel):
    agent_deleted: Optional[bool] = None
    """Whether agent is deleted"""

    agent_name: Optional[str] = None
    """Agent name"""

    agent_uuid: Optional[str] = None
    """Agent UUID."""

    agent_version_hash: Optional[str] = None
    """Version hash"""

    agent_workspace_uuid: Optional[str] = None
    """Agent workspace uuid"""

    created_by_user_email: Optional[str] = None

    created_by_user_id: Optional[str] = None

    error_description: Optional[str] = None
    """The error description"""

    evaluation_run_uuid: Optional[str] = None
    """Evaluation run UUID."""

    evaluation_test_case_workspace_uuid: Optional[str] = None
    """Evaluation test case workspace uuid"""

    finished_at: Optional[datetime] = None
    """Run end time."""

    pass_status: Optional[bool] = None
    """The pass status of the evaluation run based on the star metric."""

    queued_at: Optional[datetime] = None
    """Run queued time."""

    run_level_metric_results: Optional[List[APIEvaluationMetricResult]] = None

    run_name: Optional[str] = None
    """Run name."""

    star_metric_result: Optional[APIEvaluationMetricResult] = None

    started_at: Optional[datetime] = None
    """Run start time."""

    status: Optional[
        Literal[
            "EVALUATION_RUN_STATUS_UNSPECIFIED",
            "EVALUATION_RUN_QUEUED",
            "EVALUATION_RUN_RUNNING_DATASET",
            "EVALUATION_RUN_EVALUATING_RESULTS",
            "EVALUATION_RUN_CANCELLING",
            "EVALUATION_RUN_CANCELLED",
            "EVALUATION_RUN_SUCCESSFUL",
            "EVALUATION_RUN_PARTIALLY_SUCCESSFUL",
            "EVALUATION_RUN_FAILED",
        ]
    ] = None
    """Evaluation Run Statuses"""

    test_case_description: Optional[str] = None
    """Test case description."""

    test_case_name: Optional[str] = None
    """Test case name."""

    test_case_uuid: Optional[str] = None
    """Test-case UUID."""

    test_case_version: Optional[int] = None
    """Test-case-version."""
