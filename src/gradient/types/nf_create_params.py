# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["NfCreateParams"]


class NfCreateParams(TypedDict, total=False):
    name: Required[str]
    """The human-readable name of the share."""

    region: Required[str]
    """The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides."""

    size_gib: Required[int]
    """The desired/provisioned size of the share in GiB (Gibibytes). Must be >= 50."""

    vpc_ids: Required[SequenceNotStr[str]]
    """List of VPC IDs that should be able to access the share."""
