# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    only_deployed: bool
    """Only list agents that are deployed."""

    page: int
    """Page number."""

    per_page: int
    """Items per page."""
