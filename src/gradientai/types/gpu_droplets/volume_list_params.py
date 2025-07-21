# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["VolumeListParams"]


class VolumeListParams(TypedDict, total=False):
    name: str
    """The block storage volume's name."""

    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""

    region: Literal[
        "ams1",
        "ams2",
        "ams3",
        "blr1",
        "fra1",
        "lon1",
        "nyc1",
        "nyc2",
        "nyc3",
        "sfo1",
        "sfo2",
        "sfo3",
        "sgp1",
        "tor1",
        "syd1",
    ]
    """The slug identifier for the region where the resource is available."""
