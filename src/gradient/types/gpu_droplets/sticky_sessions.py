# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StickySessions"]


class StickySessions(BaseModel):
    """An object specifying sticky sessions settings for the load balancer."""

    cookie_name: Optional[str] = None
    """The name of the cookie sent to the client.

    This attribute is only returned when using `cookies` for the sticky sessions
    type.
    """

    cookie_ttl_seconds: Optional[int] = None
    """The number of seconds until the cookie set by the load balancer expires.

    This attribute is only returned when using `cookies` for the sticky sessions
    type.
    """

    type: Optional[Literal["cookies", "none"]] = None
    """
    An attribute indicating how and if requests from a client will be persistently
    served by the same backend Droplet. The possible values are `cookies` or `none`.
    """
