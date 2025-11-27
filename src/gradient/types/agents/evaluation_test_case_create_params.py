# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr
from .api_star_metric_param import APIStarMetricParam

__all__ = ["EvaluationTestCaseCreateParams"]


class EvaluationTestCaseCreateParams(TypedDict, total=False):
    dataset_uuid: str
    """Dataset against which the test‑case is executed."""

    description: str
    """Description of the test case."""

    metrics: SequenceNotStr[str]
    """Full metric list to use for evaluation test case."""

    name: str
    """Name of the test case."""

    star_metric: APIStarMetricParam

    workspace_uuid: str
    """The workspace uuid."""
