# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AnthropicListParams"]


class AnthropicListParams(TypedDict, total=False):
    page: int
    """page number."""

    per_page: int
    """items per page."""
