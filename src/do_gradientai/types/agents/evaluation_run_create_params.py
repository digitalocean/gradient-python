# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["EvaluationRunCreateParams"]


class EvaluationRunCreateParams(TypedDict, total=False):
    agent_uuids: List[str]
    """Agent UUIDs to run the test case against."""

    run_name: str
    """The name of the run."""

    test_case_uuid: str
