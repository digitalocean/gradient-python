# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["EvaluationRunCreateParams"]


class EvaluationRunCreateParams(TypedDict, total=False):
    agent_uuids: SequenceNotStr[str]
    """Agent UUIDs to run the test case against."""

    run_name: str
    """The name of the run."""

    test_case_uuid: str
    """Test-case UUID to run"""
