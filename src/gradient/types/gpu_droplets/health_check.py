# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HealthCheck"]


class HealthCheck(BaseModel):
    """An object specifying health check settings for the load balancer."""

    check_interval_seconds: Optional[int] = None
    """The number of seconds between between two consecutive health checks."""

    healthy_threshold: Optional[int] = None
    """
    The number of times a health check must pass for a backend Droplet to be marked
    "healthy" and be re-added to the pool.
    """

    path: Optional[str] = None
    """
    The path on the backend Droplets to which the load balancer instance will send a
    request.
    """

    port: Optional[int] = None
    """
    An integer representing the port on the backend Droplets on which the health
    check will attempt a connection.
    """

    protocol: Optional[Literal["http", "https", "tcp"]] = None
    """The protocol used for health checks sent to the backend Droplets.

    The possible values are `http`, `https`, or `tcp`.
    """

    response_timeout_seconds: Optional[int] = None
    """
    The number of seconds the load balancer instance will wait for a response until
    marking a health check as failed.
    """

    unhealthy_threshold: Optional[int] = None
    """
    The number of times a health check must fail for a backend Droplet to be marked
    "unhealthy" and be removed from the pool.
    """
