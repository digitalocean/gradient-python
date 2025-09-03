# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ImageCreateParams"]


class ImageCreateParams(TypedDict, total=False):
    description: str
    """An optional free-form text field to describe an image."""

    distribution: Literal[
        "Arch Linux",
        "CentOS",
        "CoreOS",
        "Debian",
        "Fedora",
        "Fedora Atomic",
        "FreeBSD",
        "Gentoo",
        "openSUSE",
        "RancherOS",
        "Rocky Linux",
        "Ubuntu",
        "Unknown",
    ]
    """The name of a custom image's distribution.

    Currently, the valid values are `Arch Linux`, `CentOS`, `CoreOS`, `Debian`,
    `Fedora`, `Fedora Atomic`, `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`,
    `Rocky Linux`, `Ubuntu`, and `Unknown`. Any other value will be accepted but
    ignored, and `Unknown` will be used in its place.
    """

    name: str
    """The display name that has been given to an image.

    This is what is shown in the control panel and is generally a descriptive title
    for the image in question.
    """

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

    url: str
    """A URL from which the custom Linux virtual machine image may be retrieved.

    The image it points to must be in the raw, qcow2, vhdx, vdi, or vmdk format. It
    may be compressed using gzip or bzip2 and must be smaller than 100 GB after
    being decompressed.
    """
