# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .api_star_metric import APIStarMetric
from .api_evaluation_metric import APIEvaluationMetric

__all__ = ["APIEvaluationTestCase", "Dataset"]


class Dataset(BaseModel):
    created_at: Optional[datetime] = None
    """Time created at."""

    dataset_name: Optional[str] = None
    """Name of the dataset."""

    dataset_uuid: Optional[str] = None
    """UUID of the dataset."""

    file_size: Optional[str] = None
    """The size of the dataset uploaded file in bytes."""

    has_ground_truth: Optional[bool] = None
    """Does the dataset have a ground truth column?"""

    row_count: Optional[int] = None
    """Number of rows in the dataset."""


class APIEvaluationTestCase(BaseModel):
    archived_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    created_by_user_email: Optional[str] = None

    created_by_user_id: Optional[str] = None

    dataset: Optional[Dataset] = None

    dataset_name: Optional[str] = None

    dataset_uuid: Optional[str] = None

    description: Optional[str] = None

    latest_version_number_of_runs: Optional[int] = None

    metrics: Optional[List[APIEvaluationMetric]] = None

    name: Optional[str] = None

    star_metric: Optional[APIStarMetric] = None

    test_case_uuid: Optional[str] = None

    total_runs: Optional[int] = None

    updated_at: Optional[datetime] = None

    updated_by_user_email: Optional[str] = None

    updated_by_user_id: Optional[str] = None

    version: Optional[int] = None
