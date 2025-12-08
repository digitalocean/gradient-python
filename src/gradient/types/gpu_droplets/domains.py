# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Domains"]


class Domains(BaseModel):
    """An object specifying domain configurations for a Global load balancer."""

    certificate_id: Optional[str] = None
    """The ID of the TLS certificate used for SSL termination."""

    is_managed: Optional[bool] = None
    """A boolean value indicating if the domain is already managed by DigitalOcean.

    If true, all A and AAAA records required to enable Global load balancers will be
    automatically added.
    """

    name: Optional[str] = None
    """FQDN to associate with a Global load balancer."""
