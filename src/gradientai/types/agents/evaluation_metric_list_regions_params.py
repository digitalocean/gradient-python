# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EvaluationMetricListRegionsParams"]


class EvaluationMetricListRegionsParams(TypedDict, total=False):
    serves_batch: bool
    """Include datacenters that are capable of running batch jobs."""

    serves_inference: bool
    """Include datacenters that serve inference."""
