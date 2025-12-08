# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["APISpacesDataSourceParam"]


class APISpacesDataSourceParam(TypedDict, total=False):
    """Spaces Bucket Data Source"""

    bucket_name: str
    """Spaces bucket name"""

    item_path: str

    region: str
    """Region of bucket"""
