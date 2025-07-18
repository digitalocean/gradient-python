# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .firewall import Firewall
from ..._models import BaseModel

__all__ = ["FirewallUpdateResponse"]


class FirewallUpdateResponse(BaseModel):
    firewall: Optional[Firewall] = None
