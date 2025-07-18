# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AutoscaleListParams"]


class AutoscaleListParams(TypedDict, total=False):
    name: str
    """The name of the autoscale pool"""

    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""
