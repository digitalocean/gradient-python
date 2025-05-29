# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrganizationGetCostsParams"]


class OrganizationGetCostsParams(TypedDict, total=False):
    start_time: Required[int]
    """Start time (Unix seconds) of the query time range, inclusive."""

    bucket_width: Literal["1d"]
    """Width of each time bucket in response.

    Currently only `1d` is supported, default to `1d`.
    """

    end_time: int
    """End time (Unix seconds) of the query time range, exclusive."""

    group_by: List[Literal["project_id", "line_item"]]
    """Group the costs by the specified fields.

    Support fields include `project_id`, `line_item` and any combination of them.
    """

    limit: int
    """A limit on the number of buckets to be returned.

    Limit can range between 1 and 180, and the default is 7.
    """

    page: str
    """A cursor for use in pagination.

    Corresponding to the `next_page` field from the previous response.
    """

    project_ids: List[str]
    """Return only costs for these projects."""
