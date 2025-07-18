# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.firewall_rule_target import FirewallRuleTarget

__all__ = ["Firewall", "InboundRule", "OutboundRule", "PendingChange"]


class InboundRule(BaseModel):
    ports: str
    """
    The ports on which traffic will be allowed specified as a string containing a
    single port, a range (e.g. "8000-9000"), or "0" when all ports are open for a
    protocol. For ICMP rules this parameter will always return "0".
    """

    protocol: Literal["tcp", "udp", "icmp"]
    """The type of traffic to be allowed. This may be one of `tcp`, `udp`, or `icmp`."""

    sources: FirewallRuleTarget
    """An object specifying locations from which inbound traffic will be accepted."""


class OutboundRule(BaseModel):
    destinations: FirewallRuleTarget
    """An object specifying locations to which outbound traffic that will be allowed."""

    ports: str
    """
    The ports on which traffic will be allowed specified as a string containing a
    single port, a range (e.g. "8000-9000"), or "0" when all ports are open for a
    protocol. For ICMP rules this parameter will always return "0".
    """

    protocol: Literal["tcp", "udp", "icmp"]
    """The type of traffic to be allowed. This may be one of `tcp`, `udp`, or `icmp`."""


class PendingChange(BaseModel):
    droplet_id: Optional[int] = None

    removing: Optional[bool] = None

    status: Optional[str] = None


class Firewall(BaseModel):
    id: Optional[str] = None
    """A unique ID that can be used to identify and reference a firewall."""

    created_at: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format that represents when
    the firewall was created.
    """

    droplet_ids: Optional[List[int]] = None
    """An array containing the IDs of the Droplets assigned to the firewall.

    Requires `droplet:read` scope.
    """

    inbound_rules: Optional[List[InboundRule]] = None

    name: Optional[str] = None
    """A human-readable name for a firewall.

    The name must begin with an alphanumeric character. Subsequent characters must
    either be alphanumeric characters, a period (.), or a dash (-).
    """

    outbound_rules: Optional[List[OutboundRule]] = None

    pending_changes: Optional[List[PendingChange]] = None
    """
    An array of objects each containing the fields "droplet_id", "removing", and
    "status". It is provided to detail exactly which Droplets are having their
    security policies updated. When empty, all changes have been successfully
    applied.
    """

    status: Optional[Literal["waiting", "succeeded", "failed"]] = None
    """A status string indicating the current state of the firewall.

    This can be "waiting", "succeeded", or "failed".
    """

    tags: Optional[List[str]] = None
    """A flat array of tag names as strings to be applied to the resource.

    Tag names must exist in order to be referenced in a request.

    Requires `tag:create` and `tag:read` scopes.
    """
