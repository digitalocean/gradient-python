# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ForwardingRule"]


class ForwardingRule(BaseModel):
    """An object specifying a forwarding rule for a load balancer."""

    entry_port: int
    """
    An integer representing the port on which the load balancer instance will
    listen.
    """

    entry_protocol: Literal["http", "https", "http2", "http3", "tcp", "udp"]
    """The protocol used for traffic to the load balancer.

    The possible values are: `http`, `https`, `http2`, `http3`, `tcp`, or `udp`. If
    you set the `entry_protocol` to `udp`, the `target_protocol` must be set to
    `udp`. When using UDP, the load balancer requires that you set up a health check
    with a port that uses TCP, HTTP, or HTTPS to work properly.
    """

    target_port: int
    """
    An integer representing the port on the backend Droplets to which the load
    balancer will send traffic.
    """

    target_protocol: Literal["http", "https", "http2", "tcp", "udp"]
    """The protocol used for traffic from the load balancer to the backend Droplets.

    The possible values are: `http`, `https`, `http2`, `tcp`, or `udp`. If you set
    the `target_protocol` to `udp`, the `entry_protocol` must be set to `udp`. When
    using UDP, the load balancer requires that you set up a health check with a port
    that uses TCP, HTTP, or HTTPS to work properly.
    """

    certificate_id: Optional[str] = None
    """The ID of the TLS certificate used for SSL termination if enabled."""

    tls_passthrough: Optional[bool] = None
    """
    A boolean value indicating whether SSL encrypted traffic will be passed through
    to the backend Droplets.
    """
