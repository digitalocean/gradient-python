# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NetworkV4"]


class NetworkV4(BaseModel):
    gateway: Optional[str] = None
    """The gateway of the specified IPv4 network interface.

    For private interfaces, a gateway is not provided. This is denoted by returning
    `nil` as its value.
    """

    ip_address: Optional[str] = None
    """The IP address of the IPv4 network interface."""

    netmask: Optional[str] = None
    """The netmask of the IPv4 network interface."""

    type: Optional[Literal["public", "private"]] = None
    """The type of the IPv4 network interface."""
