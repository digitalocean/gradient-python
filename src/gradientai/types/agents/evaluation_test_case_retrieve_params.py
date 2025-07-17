# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EvaluationTestCaseRetrieveParams"]


class EvaluationTestCaseRetrieveParams(TypedDict, total=False):
    evaluation_test_case_version: int
    """Version of the test case."""
