# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TagAddParams"]


class TagAddParams(TypedDict, total=False):
    tags: Required[Optional[List[str]]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names must exist in order to be referenced in a request.

    Requires `tag:create` and `tag:read` scopes.
    """
