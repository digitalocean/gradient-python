# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GlbSettings", "Cdn"]


class Cdn(BaseModel):
    """An object specifying CDN configurations for a Global load balancer."""

    is_enabled: Optional[bool] = None
    """A boolean flag to enable CDN caching."""


class GlbSettings(BaseModel):
    """An object specifying forwarding configurations for a Global load balancer."""

    cdn: Optional[Cdn] = None
    """An object specifying CDN configurations for a Global load balancer."""

    failover_threshold: Optional[int] = None
    """
    An integer value as a percentage to indicate failure threshold to decide how the
    regional priorities will take effect. A value of `50` would indicate that the
    Global load balancer will choose a lower priority region to forward traffic to
    once this failure threshold has been reached for the higher priority region.
    """

    region_priorities: Optional[Dict[str, int]] = None
    """
    A map of region string to an integer priority value indicating preference for
    which regional target a Global load balancer will forward traffic to. A lower
    value indicates a higher priority.
    """

    target_port: Optional[int] = None
    """
    An integer representing the port on the target backends which the load balancer
    will forward traffic to.
    """

    target_protocol: Optional[Literal["http", "https", "http2"]] = None
    """
    The protocol used for forwarding traffic from the load balancer to the target
    backends. The possible values are `http`, `https` and `http2`.
    """
