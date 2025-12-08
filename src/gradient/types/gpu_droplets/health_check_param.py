# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["HealthCheckParam"]


class HealthCheckParam(TypedDict, total=False):
    """An object specifying health check settings for the load balancer."""

    check_interval_seconds: int
    """The number of seconds between between two consecutive health checks."""

    healthy_threshold: int
    """
    The number of times a health check must pass for a backend Droplet to be marked
    "healthy" and be re-added to the pool.
    """

    path: str
    """
    The path on the backend Droplets to which the load balancer instance will send a
    request.
    """

    port: int
    """
    An integer representing the port on the backend Droplets on which the health
    check will attempt a connection.
    """

    protocol: Literal["http", "https", "tcp"]
    """The protocol used for health checks sent to the backend Droplets.

    The possible values are `http`, `https`, or `tcp`.
    """

    response_timeout_seconds: int
    """
    The number of seconds the load balancer instance will wait for a response until
    marking a health check as failed.
    """

    unhealthy_threshold: int
    """
    The number of times a health check must fail for a backend Droplet to be marked
    "unhealthy" and be removed from the pool.
    """
