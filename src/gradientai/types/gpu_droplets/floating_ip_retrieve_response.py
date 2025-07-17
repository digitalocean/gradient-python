# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .floating_ip import FloatingIP

__all__ = ["FloatingIPRetrieveResponse"]


class FloatingIPRetrieveResponse(BaseModel):
    floating_ip: Optional[FloatingIP] = None
