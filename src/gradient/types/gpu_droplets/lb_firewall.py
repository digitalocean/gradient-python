# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LbFirewall"]


class LbFirewall(BaseModel):
    """
    An object specifying allow and deny rules to control traffic to the load balancer.
    """

    allow: Optional[List[str]] = None
    """
    the rules for allowing traffic to the load balancer (in the form 'ip:1.2.3.4' or
    'cidr:1.2.0.0/16')
    """

    deny: Optional[List[str]] = None
    """
    the rules for denying traffic to the load balancer (in the form 'ip:1.2.3.4' or
    'cidr:1.2.0.0/16')
    """
