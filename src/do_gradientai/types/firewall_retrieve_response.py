# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .firewall import Firewall

__all__ = ["FirewallRetrieveResponse"]


class FirewallRetrieveResponse(BaseModel):
    firewall: Optional[Firewall] = None
