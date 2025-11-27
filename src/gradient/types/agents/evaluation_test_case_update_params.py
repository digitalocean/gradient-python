# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .api_star_metric_param import APIStarMetricParam

__all__ = ["EvaluationTestCaseUpdateParams", "Metrics"]


class EvaluationTestCaseUpdateParams(TypedDict, total=False):
    dataset_uuid: str
    """Dataset against which the test‑case is executed."""

    description: str
    """Description of the test case."""

    metrics: Metrics

    name: str
    """Name of the test case."""

    star_metric: APIStarMetricParam

    body_test_case_uuid: Annotated[str, PropertyInfo(alias="test_case_uuid")]
    """Test-case UUID to update"""


class Metrics(TypedDict, total=False):
    metric_uuids: SequenceNotStr[str]
