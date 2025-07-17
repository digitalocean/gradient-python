# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["AgentListParams", "FieldMask"]


class AgentListParams(TypedDict, total=False):
    field_mask: FieldMask

    only_deployed: bool
    """Only list agents that are deployed."""

    page: int
    """page number."""

    per_page: int
    """items per page."""


class FieldMask(TypedDict, total=False):
    paths: List[str]
    """The set of field mask paths."""
