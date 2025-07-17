# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SnapshotCreateParams"]


class SnapshotCreateParams(TypedDict, total=False):
    name: Required[str]
    """A human-readable name for the volume snapshot."""

    tags: Optional[List[str]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names may be for either existing or new tags.

    Requires `tag:create` scope.
    """
