# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["SnapshotCreateParams"]


class SnapshotCreateParams(TypedDict, total=False):
    name: Required[str]
    """A human-readable name for the volume snapshot."""

    tags: Optional[SequenceNotStr[str]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names may be for either existing or new tags.

    Requires `tag:create` scope.
    """
