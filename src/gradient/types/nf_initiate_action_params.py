# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "NfInitiateActionParams",
    "NfsActionResize",
    "NfsActionResizeParams",
    "NfsActionSnapshot",
    "NfsActionSnapshotParams",
]


class NfsActionResize(TypedDict, total=False):
    region: Required[str]
    """The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides."""

    type: Required[Literal["resize", "snapshot"]]
    """The type of action to initiate for the NFS share (such as resize or snapshot)."""

    params: NfsActionResizeParams


class NfsActionResizeParams(TypedDict, total=False):
    size_gib: Required[int]
    """The new size for the NFS share."""


class NfsActionSnapshot(TypedDict, total=False):
    region: Required[str]
    """The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides."""

    type: Required[Literal["resize", "snapshot"]]
    """The type of action to initiate for the NFS share (such as resize or snapshot)."""

    params: NfsActionSnapshotParams


class NfsActionSnapshotParams(TypedDict, total=False):
    name: Required[str]
    """Snapshot name of the NFS share"""


NfInitiateActionParams: TypeAlias = Union[NfsActionResize, NfsActionSnapshot]
