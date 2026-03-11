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
    "NfsActionAttach",
    "NfsActionAttachParams",
    "NfsActionDetach",
    "NfsActionDetachParams",
    "NfsActionSwitchPerformanceTier",
    "NfsActionSwitchPerformanceTierParams",
]


class NfsActionResize(TypedDict, total=False):
    type: Required[Literal["resize", "snapshot"]]
    """The type of action to initiate for the NFS share (such as resize or snapshot)."""

    params: NfsActionResizeParams

    region: str
    """The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides."""


class NfsActionResizeParams(TypedDict, total=False):
    size_gib: Required[int]
    """The new size for the NFS share."""


class NfsActionSnapshot(TypedDict, total=False):
    type: Required[Literal["resize", "snapshot"]]
    """The type of action to initiate for the NFS share (such as resize or snapshot)."""

    params: NfsActionSnapshotParams

    region: str
    """The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides."""


class NfsActionSnapshotParams(TypedDict, total=False):
    name: Required[str]
    """Snapshot name of the NFS share"""


class NfsActionAttach(TypedDict, total=False):
    type: Required[Literal["resize", "snapshot"]]
    """The type of action to initiate for the NFS share (such as resize or snapshot)."""

    params: NfsActionAttachParams

    region: str
    """The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides."""


class NfsActionAttachParams(TypedDict, total=False):
    vpc_id: Required[str]
    """The ID of the VPC to which the NFS share will be attached"""


class NfsActionDetach(TypedDict, total=False):
    type: Required[Literal["resize", "snapshot"]]
    """The type of action to initiate for the NFS share (such as resize or snapshot)."""

    params: NfsActionDetachParams

    region: str
    """The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides."""


class NfsActionDetachParams(TypedDict, total=False):
    vpc_id: Required[str]
    """The ID of the VPC from which the NFS share will be detached"""


class NfsActionSwitchPerformanceTier(TypedDict, total=False):
    type: Required[Literal["resize", "snapshot"]]
    """The type of action to initiate for the NFS share (such as resize or snapshot)."""

    params: NfsActionSwitchPerformanceTierParams

    region: str
    """The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides."""


class NfsActionSwitchPerformanceTierParams(TypedDict, total=False):
    performance_tier: Required[str]
    """
    The performance tier to which the NFS share will be switched (e.g., standard,
    high).
    """


NfInitiateActionParams: TypeAlias = Union[
    NfsActionResize, NfsActionSnapshot, NfsActionAttach, NfsActionDetach, NfsActionSwitchPerformanceTier
]
