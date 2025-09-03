# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["DestroyWithAssociatedResourceDeleteSelectiveParams"]


class DestroyWithAssociatedResourceDeleteSelectiveParams(TypedDict, total=False):
    floating_ips: SequenceNotStr[str]
    """
    An array of unique identifiers for the floating IPs to be scheduled for
    deletion.
    """

    reserved_ips: SequenceNotStr[str]
    """
    An array of unique identifiers for the reserved IPs to be scheduled for
    deletion.
    """

    snapshots: SequenceNotStr[str]
    """An array of unique identifiers for the snapshots to be scheduled for deletion."""

    volume_snapshots: SequenceNotStr[str]
    """
    An array of unique identifiers for the volume snapshots to be scheduled for
    deletion.
    """

    volumes: SequenceNotStr[str]
    """An array of unique identifiers for the volumes to be scheduled for deletion."""
