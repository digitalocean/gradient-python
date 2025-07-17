# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .api_evaluation_metric_result import APIEvaluationMetricResult

__all__ = ["APIEvaluationRun"]


class APIEvaluationRun(BaseModel):
    agent_deleted: Optional[bool] = None

    agent_name: Optional[str] = None

    agent_uuid: Optional[str] = None
    """Agent UUID."""

    agent_version_hash: Optional[str] = None

    agent_workspace_uuid: Optional[str] = None

    created_by_user_email: Optional[str] = None

    created_by_user_id: Optional[str] = None

    error_description: Optional[str] = None

    evaluation_run_uuid: Optional[str] = None
    """Evaluation run UUID."""

    finished_at: Optional[datetime] = None
    """Run end time."""

    pass_status: Optional[bool] = None
    """The pass status of the evaluation run based on the star metric."""

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

    test_case_uuid: Optional[str] = None
    """Test-case UUID."""

    test_case_version: Optional[int] = None
    """Test-case-version."""
