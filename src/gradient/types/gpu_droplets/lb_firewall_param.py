# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["LbFirewallParam"]


class LbFirewallParam(TypedDict, total=False):
    """
    An object specifying allow and deny rules to control traffic to the load balancer.
    """

    allow: SequenceNotStr[str]
    """
    the rules for allowing traffic to the load balancer (in the form 'ip:1.2.3.4' or
    'cidr:1.2.0.0/16')
    """

    deny: SequenceNotStr[str]
    """
    the rules for denying traffic to the load balancer (in the form 'ip:1.2.3.4' or
    'cidr:1.2.0.0/16')
    """
