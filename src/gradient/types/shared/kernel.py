# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Kernel"]


class Kernel(BaseModel):
    """
    **Note**: All Droplets created after March 2017 use internal kernels by default.
    These Droplets will have this attribute set to `null`.

    The current [kernel](https://docs.digitalocean.com/products/droplets/how-to/kernel/)
    for Droplets with externally managed kernels. This will initially be set to
    the kernel of the base image when the Droplet is created.
    """

    id: Optional[int] = None
    """A unique number used to identify and reference a specific kernel."""

    name: Optional[str] = None
    """The display name of the kernel.

    This is shown in the web UI and is generally a descriptive title for the kernel
    in question.
    """

    version: Optional[str] = None
    """
    A standard kernel version string representing the version, patch, and release
    information.
    """
