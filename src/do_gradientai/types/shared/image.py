# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Image"]


class Image(BaseModel):
    id: Optional[int] = None
    """A unique number that can be used to identify and reference a specific image."""

    created_at: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format that represents when
    the image was created.
    """

    description: Optional[str] = None
    """An optional free-form text field to describe an image."""

    distribution: Optional[
        Literal[
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
    ] = None
    """The name of a custom image's distribution.

    Currently, the valid values are `Arch Linux`, `CentOS`, `CoreOS`, `Debian`,
    `Fedora`, `Fedora Atomic`, `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`,
    `Rocky Linux`, `Ubuntu`, and `Unknown`. Any other value will be accepted but
    ignored, and `Unknown` will be used in its place.
    """

    error_message: Optional[str] = None
    """
    A string containing information about errors that may occur when importing a
    custom image.
    """

    min_disk_size: Optional[int] = None
    """The minimum disk size in GB required for a Droplet to use this image."""

    name: Optional[str] = None
    """The display name that has been given to an image.

    This is what is shown in the control panel and is generally a descriptive title
    for the image in question.
    """

    public: Optional[bool] = None
    """
    This is a boolean value that indicates whether the image in question is public
    or not. An image that is public is available to all accounts. A non-public image
    is only accessible from your account.
    """

    regions: Optional[
        List[
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
    ] = None
    """This attribute is an array of the regions that the image is available in.

    The regions are represented by their identifying slug values.
    """

    size_gigabytes: Optional[float] = None
    """The size of the image in gigabytes."""

    slug: Optional[str] = None
    """
    A uniquely identifying string that is associated with each of the
    DigitalOcean-provided public images. These can be used to reference a public
    image as an alternative to the numeric id.
    """

    status: Optional[Literal["NEW", "available", "pending", "deleted", "retired"]] = None
    """A status string indicating the state of a custom image.

    This may be `NEW`, `available`, `pending`, `deleted`, or `retired`.
    """

    tags: Optional[List[str]] = None
    """A flat array of tag names as strings to be applied to the resource.

    Tag names may be for either existing or new tags.

    Requires `tag:create` scope.
    """

    type: Optional[Literal["base", "snapshot", "backup", "custom", "admin"]] = None
    """Describes the kind of image.

    It may be one of `base`, `snapshot`, `backup`, `custom`, or `admin`.
    Respectively, this specifies whether an image is a DigitalOcean base OS image,
    user-generated Droplet snapshot, automatically created Droplet backup,
    user-provided virtual machine image, or an image used for DigitalOcean managed
    resources (e.g. DOKS worker nodes).
    """
