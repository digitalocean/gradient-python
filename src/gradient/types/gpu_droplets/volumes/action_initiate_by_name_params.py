# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ActionInitiateByNameParams", "VolumeActionPostAttach", "VolumeActionPostDetach"]


class VolumeActionPostAttach(TypedDict, total=False):
    droplet_id: Required[int]
    """
    The unique identifier for the Droplet the volume will be attached or detached
    from.
    """

    type: Required[Literal["attach", "detach", "resize"]]
    """The volume action to initiate."""

    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""

    region: Literal[
        "ams1",
        "ams2",
        "ams3",
        "blr1",
        "fra1",
        "lon1",
        "nyc1",
        "nyc2",
        "nyc3",
        "sfo1",
        "sfo2",
        "sfo3",
        "sgp1",
        "tor1",
        "syd1",
    ]
    """
    The slug identifier for the region where the resource will initially be
    available.
    """

    tags: Optional[SequenceNotStr[str]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names may be for either existing or new tags.

    Requires `tag:create` scope.
    """


class VolumeActionPostDetach(TypedDict, total=False):
    droplet_id: Required[int]
    """
    The unique identifier for the Droplet the volume will be attached or detached
    from.
    """

    type: Required[Literal["attach", "detach", "resize"]]
    """The volume action to initiate."""

    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""

    region: Literal[
        "ams1",
        "ams2",
        "ams3",
        "blr1",
        "fra1",
        "lon1",
        "nyc1",
        "nyc2",
        "nyc3",
        "sfo1",
        "sfo2",
        "sfo3",
        "sgp1",
        "tor1",
        "syd1",
    ]
    """
    The slug identifier for the region where the resource will initially be
    available.
    """


ActionInitiateByNameParams: TypeAlias = Union[VolumeActionPostAttach, VolumeActionPostDetach]
