# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["VolumeCreateParams", "VolumesExt4", "VolumesXfs"]


class VolumesExt4(TypedDict, total=False):
    name: Required[str]
    """A human-readable name for the block storage volume.

    Must be lowercase and be composed only of numbers, letters and "-", up to a
    limit of 64 characters. The name must begin with a letter.
    """

    region: Required[
        Literal[
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
    ]
    """
    The slug identifier for the region where the resource will initially be
    available.
    """

    size_gigabytes: Required[int]
    """The size of the block storage volume in GiB (1024^3).

    This field does not apply when creating a volume from a snapshot.
    """

    description: str
    """An optional free-form text field to describe a block storage volume."""

    filesystem_label: str
    """The label applied to the filesystem.

    Labels for ext4 type filesystems may contain 16 characters while labels for xfs
    type filesystems are limited to 12 characters. May only be used in conjunction
    with filesystem_type.
    """

    filesystem_type: str
    """The name of the filesystem type to be used on the volume.

    When provided, the volume will automatically be formatted to the specified
    filesystem type. Currently, the available options are `ext4` and `xfs`.
    Pre-formatted volumes are automatically mounted when attached to Ubuntu, Debian,
    Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018.
    Attaching pre-formatted volumes to other Droplets is not recommended.
    """

    snapshot_id: str
    """The unique identifier for the volume snapshot from which to create the volume."""

    tags: Optional[SequenceNotStr[str]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names may be for either existing or new tags.

    Requires `tag:create` scope.
    """


class VolumesXfs(TypedDict, total=False):
    name: Required[str]
    """A human-readable name for the block storage volume.

    Must be lowercase and be composed only of numbers, letters and "-", up to a
    limit of 64 characters. The name must begin with a letter.
    """

    region: Required[
        Literal[
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
    ]
    """
    The slug identifier for the region where the resource will initially be
    available.
    """

    size_gigabytes: Required[int]
    """The size of the block storage volume in GiB (1024^3).

    This field does not apply when creating a volume from a snapshot.
    """

    description: str
    """An optional free-form text field to describe a block storage volume."""

    filesystem_label: str
    """The label applied to the filesystem.

    Labels for ext4 type filesystems may contain 16 characters while labels for xfs
    type filesystems are limited to 12 characters. May only be used in conjunction
    with filesystem_type.
    """

    filesystem_type: str
    """The name of the filesystem type to be used on the volume.

    When provided, the volume will automatically be formatted to the specified
    filesystem type. Currently, the available options are `ext4` and `xfs`.
    Pre-formatted volumes are automatically mounted when attached to Ubuntu, Debian,
    Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018.
    Attaching pre-formatted volumes to other Droplets is not recommended.
    """

    snapshot_id: str
    """The unique identifier for the volume snapshot from which to create the volume."""

    tags: Optional[SequenceNotStr[str]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names may be for either existing or new tags.

    Requires `tag:create` scope.
    """


VolumeCreateParams: TypeAlias = Union[VolumesExt4, VolumesXfs]
