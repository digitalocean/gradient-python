# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["JobInvocationCancelParams"]


class JobInvocationCancelParams(TypedDict, total=False):
    app_id: Required[str]

    job_name: str
    """The job name to list job invocations for."""
