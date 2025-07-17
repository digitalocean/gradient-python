# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .domains import Domains
from ..._models import BaseModel
from .lb_firewall import LbFirewall
from .glb_settings import GlbSettings
from .health_check import HealthCheck
from ..shared.region import Region
from .forwarding_rule import ForwardingRule
from .sticky_sessions import StickySessions

__all__ = ["LoadBalancer"]


class LoadBalancer(BaseModel):
    forwarding_rules: List[ForwardingRule]
    """An array of objects specifying the forwarding rules for a load balancer."""

    id: Optional[str] = None
    """A unique ID that can be used to identify and reference a load balancer."""

    algorithm: Optional[Literal["round_robin", "least_connections"]] = None
    """This field has been deprecated.

    You can no longer specify an algorithm for load balancers.
    """

    created_at: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format that represents when
    the load balancer was created.
    """

    disable_lets_encrypt_dns_records: Optional[bool] = None
    """
    A boolean value indicating whether to disable automatic DNS record creation for
    Let's Encrypt certificates that are added to the load balancer.
    """

    domains: Optional[List[Domains]] = None
    """
    An array of objects specifying the domain configurations for a Global load
    balancer.
    """

    droplet_ids: Optional[List[int]] = None
    """An array containing the IDs of the Droplets assigned to the load balancer."""

    enable_backend_keepalive: Optional[bool] = None
    """
    A boolean value indicating whether HTTP keepalive connections are maintained to
    target Droplets.
    """

    enable_proxy_protocol: Optional[bool] = None
    """A boolean value indicating whether PROXY Protocol is in use."""

    firewall: Optional[LbFirewall] = None
    """
    An object specifying allow and deny rules to control traffic to the load
    balancer.
    """

    glb_settings: Optional[GlbSettings] = None
    """An object specifying forwarding configurations for a Global load balancer."""

    health_check: Optional[HealthCheck] = None
    """An object specifying health check settings for the load balancer."""

    http_idle_timeout_seconds: Optional[int] = None
    """
    An integer value which configures the idle timeout for HTTP requests to the
    target droplets.
    """

    ip: Optional[str] = None
    """An attribute containing the public-facing IP address of the load balancer."""

    ipv6: Optional[str] = None
    """An attribute containing the public-facing IPv6 address of the load balancer."""

    name: Optional[str] = None
    """A human-readable name for a load balancer instance."""

    network: Optional[Literal["EXTERNAL", "INTERNAL"]] = None
    """A string indicating whether the load balancer should be external or internal.

    Internal load balancers have no public IPs and are only accessible to resources
    on the same VPC network. This property cannot be updated after creating the load
    balancer.
    """

    network_stack: Optional[Literal["IPV4", "DUALSTACK"]] = None
    """
    A string indicating whether the load balancer will support IPv4 or both IPv4 and
    IPv6 networking. This property cannot be updated after creating the load
    balancer.
    """

    project_id: Optional[str] = None
    """The ID of the project that the load balancer is associated with.

    If no ID is provided at creation, the load balancer associates with the user's
    default project. If an invalid project ID is provided, the load balancer will
    not be created.
    """

    redirect_http_to_https: Optional[bool] = None
    """
    A boolean value indicating whether HTTP requests to the load balancer on port 80
    will be redirected to HTTPS on port 443.
    """

    region: Optional[Region] = None
    """The region where the load balancer instance is located.

    When setting a region, the value should be the slug identifier for the region.
    When you query a load balancer, an entire region object will be returned.
    """

    size: Optional[Literal["lb-small", "lb-medium", "lb-large"]] = None
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

    size_unit: Optional[int] = None
    """How many nodes the load balancer contains.

    Each additional node increases the load balancer's ability to manage more
    connections. Load balancers can be scaled up or down, and you can change the
    number of nodes after creation up to once per hour. This field is currently not
    available in the AMS2, NYC2, or SFO1 regions. Use the `size` field to scale load
    balancers that reside in these regions.
    """

    status: Optional[Literal["new", "active", "errored"]] = None
    """A status string indicating the current state of the load balancer.

    This can be `new`, `active`, or `errored`.
    """

    sticky_sessions: Optional[StickySessions] = None
    """An object specifying sticky sessions settings for the load balancer."""

    tag: Optional[str] = None
    """
    The name of a Droplet tag corresponding to Droplets assigned to the load
    balancer.
    """

    target_load_balancer_ids: Optional[List[str]] = None
    """
    An array containing the UUIDs of the Regional load balancers to be used as
    target backends for a Global load balancer.
    """

    tls_cipher_policy: Optional[Literal["DEFAULT", "STRONG"]] = None
    """
    A string indicating the policy for the TLS cipher suites used by the load
    balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
    `DEFAULT`.
    """

    type: Optional[Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"]] = None
    """
    A string indicating whether the load balancer should be a standard regional HTTP
    load balancer, a regional network load balancer that routes traffic at the
    TCP/UDP transport layer, or a global load balancer.
    """

    vpc_uuid: Optional[str] = None
    """A string specifying the UUID of the VPC to which the load balancer is assigned."""
