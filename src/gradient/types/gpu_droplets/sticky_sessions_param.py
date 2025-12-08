# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["StickySessionsParam"]


class StickySessionsParam(TypedDict, total=False):
    """An object specifying sticky sessions settings for the load balancer."""

    cookie_name: str
    """The name of the cookie sent to the client.

    This attribute is only returned when using `cookies` for the sticky sessions
    type.
    """

    cookie_ttl_seconds: int
    """The number of seconds until the cookie set by the load balancer expires.

    This attribute is only returned when using `cookies` for the sticky sessions
    type.
    """

    type: Literal["cookies", "none"]
    """
    An attribute indicating how and if requests from a client will be persistently
    served by the same backend Droplet. The possible values are `cookies` or `none`.
    """
