# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DomainsParam"]


class DomainsParam(TypedDict, total=False):
    """An object specifying domain configurations for a Global load balancer."""

    certificate_id: str
    """The ID of the TLS certificate used for SSL termination."""

    is_managed: bool
    """A boolean value indicating if the domain is already managed by DigitalOcean.

    If true, all A and AAAA records required to enable Global load balancers will be
    automatically added.
    """

    name: str
    """FQDN to associate with a Global load balancer."""
