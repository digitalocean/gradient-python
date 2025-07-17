# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .load_balancer import LoadBalancer

__all__ = ["LoadBalancerCreateResponse"]


class LoadBalancerCreateResponse(BaseModel):
    load_balancer: Optional[LoadBalancer] = None
