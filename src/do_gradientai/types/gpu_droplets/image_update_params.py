# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ImageUpdateParams"]


class ImageUpdateParams(TypedDict, total=False):
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
