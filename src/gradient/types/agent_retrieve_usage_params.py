# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentRetrieveUsageParams"]


class AgentRetrieveUsageParams(TypedDict, total=False):
    start: str
    """Return all usage data from this date."""

    stop: str
    """
    Return all usage data up to this date, if omitted, will return up to the current
    date.
    """
