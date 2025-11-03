# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NfDeleteParams"]


class NfDeleteParams(TypedDict, total=False):
    region: Required[str]
    """The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides."""
