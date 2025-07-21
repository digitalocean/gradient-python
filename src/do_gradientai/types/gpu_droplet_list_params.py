# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GPUDropletListParams"]


class GPUDropletListParams(TypedDict, total=False):
    name: str
    """Used to filter list response by Droplet name returning only exact matches.

    It is case-insensitive and can not be combined with `tag_name`.
    """

    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""

    tag_name: str
    """Used to filter Droplets by a specific tag.

    Can not be combined with `name` or `type`. Requires `tag:read` scope.
    """

    type: Literal["droplets", "gpus"]
    """When `type` is set to `gpus`, only GPU Droplets will be returned.

    By default, only non-GPU Droplets are returned. Can not be combined with
    `tag_name`.
    """
