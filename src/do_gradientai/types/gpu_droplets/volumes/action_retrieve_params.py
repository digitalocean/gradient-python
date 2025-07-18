# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionRetrieveParams"]


class ActionRetrieveParams(TypedDict, total=False):
    volume_id: Required[str]

    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""
