# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["TagRemoveParams"]


class TagRemoveParams(TypedDict, total=False):
    tags: Required[Optional[SequenceNotStr[str]]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names must exist in order to be referenced in a request.

    Requires `tag:create` and `tag:read` scopes.
    """
