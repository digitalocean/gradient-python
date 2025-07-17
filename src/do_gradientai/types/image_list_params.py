# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ImageListParams"]


class ImageListParams(TypedDict, total=False):
    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""

    private: bool
    """Used to filter only user images."""

    tag_name: str
    """Used to filter images by a specific tag."""

    type: Literal["application", "distribution"]
    """
    Filters results based on image type which can be either `application` or
    `distribution`.
    """
