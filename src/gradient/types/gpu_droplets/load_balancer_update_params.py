# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .domains_param import DomainsParam
from .lb_firewall_param import LbFirewallParam
from .glb_settings_param import GlbSettingsParam
from .health_check_param import HealthCheckParam
from .forwarding_rule_param import ForwardingRuleParam
from .sticky_sessions_param import StickySessionsParam

__all__ = ["LoadBalancerUpdateParams", "AssignDropletsByID", "AssignDropletsByTag"]


class AssignDropletsByID(TypedDict, total=False):
    forwarding_rules: Required[Iterable[ForwardingRuleParam]]
    """An array of objects specifying the forwarding rules for a load balancer."""

    algorithm: Literal["round_robin", "least_connections"]
    """This field has been deprecated.

    You can no longer specify an algorithm for load balancers.
    """

    disable_lets_encrypt_dns_records: bool
    """
    A boolean value indicating whether to disable automatic DNS record creation for
    Let's Encrypt certificates that are added to the load balancer.
    """

    domains: Iterable[DomainsParam]
    """
    An array of objects specifying the domain configurations for a Global load
    balancer.
    """

    droplet_ids: Iterable[int]
    """An array containing the IDs of the Droplets assigned to the load balancer."""

    enable_backend_keepalive: bool
    """
    A boolean value indicating whether HTTP keepalive connections are maintained to
    target Droplets.
    """

    enable_proxy_protocol: bool
    """A boolean value indicating whether PROXY Protocol is in use."""

    firewall: LbFirewallParam
    """
    An object specifying allow and deny rules to control traffic to the load
    balancer.
    """

    glb_settings: GlbSettingsParam
    """An object specifying forwarding configurations for a Global load balancer."""

    health_check: HealthCheckParam
    """An object specifying health check settings for the load balancer."""

    http_idle_timeout_seconds: int
    """
    An integer value which configures the idle timeout for HTTP requests to the
    target droplets.
    """

    name: str
    """A human-readable name for a load balancer instance."""

    network: Literal["EXTERNAL", "INTERNAL"]
    """A string indicating whether the load balancer should be external or internal.

    Internal load balancers have no public IPs and are only accessible to resources
    on the same VPC network. This property cannot be updated after creating the load
    balancer.
    """

    network_stack: Literal["IPV4", "DUALSTACK"]
    """
    A string indicating whether the load balancer will support IPv4 or both IPv4 and
    IPv6 networking. This property cannot be updated after creating the load
    balancer.
    """

    project_id: str
    """The ID of the project that the load balancer is associated with.

    If no ID is provided at creation, the load balancer associates with the user's
    default project. If an invalid project ID is provided, the load balancer will
    not be created.
    """

    redirect_http_to_https: bool
    """
    A boolean value indicating whether HTTP requests to the load balancer on port 80
    will be redirected to HTTPS on port 443.
    """

    region: Literal[
        "ams1",
        "ams2",
        "ams3",
        "blr1",
        "fra1",
        "lon1",
        "nyc1",
        "nyc2",
        "nyc3",
        "sfo1",
        "sfo2",
        "sfo3",
        "sgp1",
        "tor1",
        "syd1",
    ]
    """
    The slug identifier for the region where the resource will initially be
    available.
    """

    size: Literal["lb-small", "lb-medium", "lb-large"]
    """
    This field has been replaced by the `size_unit` field for all regions except in
    AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
    balancer having a set number of nodes.

    - `lb-small` = 1 node
    - `lb-medium` = 3 nodes
    - `lb-large` = 6 nodes

    You can resize load balancers after creation up to once per hour. You cannot
    resize a load balancer within the first hour of its creation.
    """

    size_unit: int
    """How many nodes the load balancer contains.

    Each additional node increases the load balancer's ability to manage more
    connections. Load balancers can be scaled up or down, and you can change the
    number of nodes after creation up to once per hour. This field is currently not
    available in the AMS2, NYC2, or SFO1 regions. Use the `size` field to scale load
    balancers that reside in these regions.
    """

    sticky_sessions: StickySessionsParam
    """An object specifying sticky sessions settings for the load balancer."""

    target_load_balancer_ids: SequenceNotStr[str]
    """
    An array containing the UUIDs of the Regional load balancers to be used as
    target backends for a Global load balancer.
    """

    tls_cipher_policy: Literal["DEFAULT", "STRONG"]
    """
    A string indicating the policy for the TLS cipher suites used by the load
    balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
    `DEFAULT`.
    """

    type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"]
    """
    A string indicating whether the load balancer should be a standard regional HTTP
    load balancer, a regional network load balancer that routes traffic at the
    TCP/UDP transport layer, or a global load balancer.
    """

    vpc_uuid: str
    """A string specifying the UUID of the VPC to which the load balancer is assigned."""


class AssignDropletsByTag(TypedDict, total=False):
    forwarding_rules: Required[Iterable[ForwardingRuleParam]]
    """An array of objects specifying the forwarding rules for a load balancer."""

    algorithm: Literal["round_robin", "least_connections"]
    """This field has been deprecated.

    You can no longer specify an algorithm for load balancers.
    """

    disable_lets_encrypt_dns_records: bool
    """
    A boolean value indicating whether to disable automatic DNS record creation for
    Let's Encrypt certificates that are added to the load balancer.
    """

    domains: Iterable[DomainsParam]
    """
    An array of objects specifying the domain configurations for a Global load
    balancer.
    """

    enable_backend_keepalive: bool
    """
    A boolean value indicating whether HTTP keepalive connections are maintained to
    target Droplets.
    """

    enable_proxy_protocol: bool
    """A boolean value indicating whether PROXY Protocol is in use."""

    firewall: LbFirewallParam
    """
    An object specifying allow and deny rules to control traffic to the load
    balancer.
    """

    glb_settings: GlbSettingsParam
    """An object specifying forwarding configurations for a Global load balancer."""

    health_check: HealthCheckParam
    """An object specifying health check settings for the load balancer."""

    http_idle_timeout_seconds: int
    """
    An integer value which configures the idle timeout for HTTP requests to the
    target droplets.
    """

    name: str
    """A human-readable name for a load balancer instance."""

    network: Literal["EXTERNAL", "INTERNAL"]
    """A string indicating whether the load balancer should be external or internal.

    Internal load balancers have no public IPs and are only accessible to resources
    on the same VPC network. This property cannot be updated after creating the load
    balancer.
    """

    network_stack: Literal["IPV4", "DUALSTACK"]
    """
    A string indicating whether the load balancer will support IPv4 or both IPv4 and
    IPv6 networking. This property cannot be updated after creating the load
    balancer.
    """

    project_id: str
    """The ID of the project that the load balancer is associated with.

    If no ID is provided at creation, the load balancer associates with the user's
    default project. If an invalid project ID is provided, the load balancer will
    not be created.
    """

    redirect_http_to_https: bool
    """
    A boolean value indicating whether HTTP requests to the load balancer on port 80
    will be redirected to HTTPS on port 443.
    """

    region: Literal[
        "ams1",
        "ams2",
        "ams3",
        "blr1",
        "fra1",
        "lon1",
        "nyc1",
        "nyc2",
        "nyc3",
        "sfo1",
        "sfo2",
        "sfo3",
        "sgp1",
        "tor1",
        "syd1",
    ]
    """
    The slug identifier for the region where the resource will initially be
    available.
    """

    size: Literal["lb-small", "lb-medium", "lb-large"]
    """
    This field has been replaced by the `size_unit` field for all regions except in
    AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
    balancer having a set number of nodes.

    - `lb-small` = 1 node
    - `lb-medium` = 3 nodes
    - `lb-large` = 6 nodes

    You can resize load balancers after creation up to once per hour. You cannot
    resize a load balancer within the first hour of its creation.
    """

    size_unit: int
    """How many nodes the load balancer contains.

    Each additional node increases the load balancer's ability to manage more
    connections. Load balancers can be scaled up or down, and you can change the
    number of nodes after creation up to once per hour. This field is currently not
    available in the AMS2, NYC2, or SFO1 regions. Use the `size` field to scale load
    balancers that reside in these regions.
    """

    sticky_sessions: StickySessionsParam
    """An object specifying sticky sessions settings for the load balancer."""

    tag: str
    """
    The name of a Droplet tag corresponding to Droplets assigned to the load
    balancer.
    """

    target_load_balancer_ids: SequenceNotStr[str]
    """
    An array containing the UUIDs of the Regional load balancers to be used as
    target backends for a Global load balancer.
    """

    tls_cipher_policy: Literal["DEFAULT", "STRONG"]
    """
    A string indicating the policy for the TLS cipher suites used by the load
    balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
    `DEFAULT`.
    """

    type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"]
    """
    A string indicating whether the load balancer should be a standard regional HTTP
    load balancer, a regional network load balancer that routes traffic at the
    TCP/UDP transport layer, or a global load balancer.
    """

    vpc_uuid: str
    """A string specifying the UUID of the VPC to which the load balancer is assigned."""


LoadBalancerUpdateParams: TypeAlias = Union[AssignDropletsByID, AssignDropletsByTag]
