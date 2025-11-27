# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Kernel"]


class Kernel(BaseModel):
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
