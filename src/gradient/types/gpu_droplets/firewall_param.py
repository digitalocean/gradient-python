# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..shared_params.firewall_rule_target import FirewallRuleTarget

__all__ = ["FirewallParam", "InboundRule", "OutboundRule"]


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


class FirewallParam(TypedDict, total=False):
    droplet_ids: Optional[Iterable[int]]
    """An array containing the IDs of the Droplets assigned to the firewall.

    Requires `droplet:read` scope.
    """

    inbound_rules: Optional[Iterable[InboundRule]]

    name: str
    """A human-readable name for a firewall.

    The name must begin with an alphanumeric character. Subsequent characters must
    either be alphanumeric characters, a period (.), or a dash (-).
    """

    outbound_rules: Optional[Iterable[OutboundRule]]

    tags: Optional[SequenceNotStr[str]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names must exist in order to be referenced in a request.

    Requires `tag:create` and `tag:read` scopes.
    """
