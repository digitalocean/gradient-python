# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["KeyUpdateParams"]


class KeyUpdateParams(TypedDict, total=False):
    name: str
    """
    A human-readable display name for this key, used to easily identify the SSH keys
    when they are displayed.
    """
