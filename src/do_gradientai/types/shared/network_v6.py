# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NetworkV6"]


class NetworkV6(BaseModel):
    gateway: Optional[str] = None
    """The gateway of the specified IPv6 network interface."""

    ip_address: Optional[str] = None
    """The IP address of the IPv6 network interface."""

    netmask: Optional[int] = None
    """The netmask of the IPv6 network interface."""

    type: Optional[Literal["public"]] = None
    """The type of the IPv6 network interface.

    **Note**: IPv6 private networking is not currently supported.
    """
