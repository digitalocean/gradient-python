# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .floating_ip import FloatingIP
from ..shared.action_link import ActionLink

__all__ = ["FloatingIPCreateResponse", "Links"]


class Links(BaseModel):
    actions: Optional[List[ActionLink]] = None

    droplets: Optional[List[ActionLink]] = None


class FloatingIPCreateResponse(BaseModel):
    floating_ip: Optional[FloatingIP] = None

    links: Optional[Links] = None
