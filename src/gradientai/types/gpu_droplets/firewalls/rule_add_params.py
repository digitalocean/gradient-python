# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...shared_params.firewall_rule_target import FirewallRuleTarget

__all__ = ["RuleAddParams", "InboundRule", "OutboundRule"]


class RuleAddParams(TypedDict, total=False):
    inbound_rules: Optional[Iterable[InboundRule]]

    outbound_rules: Optional[Iterable[OutboundRule]]


class InboundRule(TypedDict, total=False):
    ports: Required[str]
    """
    The ports on which traffic will be allowed specified as a string containing a
    single port, a range (e.g. "8000-9000"), or "0" when all ports are open for a
    protocol. For ICMP rules this parameter will always return "0".
    """

    protocol: Required[Literal["tcp", "udp", "icmp"]]
    """The type of traffic to be allowed. This may be one of `tcp`, `udp`, or `icmp`."""

    sources: Required[FirewallRuleTarget]
    """An object specifying locations from which inbound traffic will be accepted."""


class OutboundRule(TypedDict, total=False):
    destinations: Required[FirewallRuleTarget]
    """An object specifying locations to which outbound traffic that will be allowed."""

    ports: Required[str]
    """
    The ports on which traffic will be allowed specified as a string containing a
    single port, a range (e.g. "8000-9000"), or "0" when all ports are open for a
    protocol. For ICMP rules this parameter will always return "0".
    """

    protocol: Required[Literal["tcp", "udp", "icmp"]]
    """The type of traffic to be allowed. This may be one of `tcp`, `udp`, or `icmp`."""
