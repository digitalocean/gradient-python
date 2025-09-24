# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from .droplets import (
    DropletsResource,
    AsyncDropletsResource,
    DropletsResourceWithRawResponse,
    AsyncDropletsResourceWithRawResponse,
    DropletsResourceWithStreamingResponse,
    AsyncDropletsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .forwarding_rules import (
    ForwardingRulesResource,
    AsyncForwardingRulesResource,
    ForwardingRulesResourceWithRawResponse,
    AsyncForwardingRulesResourceWithRawResponse,
    ForwardingRulesResourceWithStreamingResponse,
    AsyncForwardingRulesResourceWithStreamingResponse,
)
from ....types.gpu_droplets import (
    load_balancer_list_params,
    load_balancer_create_params,
    load_balancer_update_params,
)
from ....types.gpu_droplets.domains_param import DomainsParam
from ....types.gpu_droplets.lb_firewall_param import LbFirewallParam
from ....types.gpu_droplets.glb_settings_param import GlbSettingsParam
from ....types.gpu_droplets.health_check_param import HealthCheckParam
from ....types.gpu_droplets.forwarding_rule_param import ForwardingRuleParam
from ....types.gpu_droplets.sticky_sessions_param import StickySessionsParam
from ....types.gpu_droplets.load_balancer_list_response import LoadBalancerListResponse
from ....types.gpu_droplets.load_balancer_create_response import LoadBalancerCreateResponse
from ....types.gpu_droplets.load_balancer_update_response import LoadBalancerUpdateResponse
from ....types.gpu_droplets.load_balancer_retrieve_response import LoadBalancerRetrieveResponse

__all__ = ["LoadBalancersResource", "AsyncLoadBalancersResource"]


class LoadBalancersResource(SyncAPIResource):
    @cached_property
    def droplets(self) -> DropletsResource:
        return DropletsResource(self._client)

    @cached_property
    def forwarding_rules(self) -> ForwardingRulesResource:
        return ForwardingRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> LoadBalancersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return LoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return LoadBalancersResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        droplet_ids: Iterable[int] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerCreateResponse:
        """
        To create a new load balancer instance, send a POST request to
        `/v2/load_balancers`.

        You can specify the Droplets that will sit behind the load balancer using one of
        two methods:

        - Set `droplet_ids` to a list of specific Droplet IDs.
        - Set `tag` to the name of a tag. All Droplets with this tag applied will be
          assigned to the load balancer. Additional Droplets will be automatically
          assigned as they are tagged.

        These methods are mutually exclusive.

        Args:
          forwarding_rules: An array of objects specifying the forwarding rules for a load balancer.

          algorithm: This field has been deprecated. You can no longer specify an algorithm for load
              balancers.

          disable_lets_encrypt_dns_records: A boolean value indicating whether to disable automatic DNS record creation for
              Let's Encrypt certificates that are added to the load balancer.

          domains: An array of objects specifying the domain configurations for a Global load
              balancer.

          droplet_ids: An array containing the IDs of the Droplets assigned to the load balancer.

          enable_backend_keepalive: A boolean value indicating whether HTTP keepalive connections are maintained to
              target Droplets.

          enable_proxy_protocol: A boolean value indicating whether PROXY Protocol is in use.

          firewall: An object specifying allow and deny rules to control traffic to the load
              balancer.

          glb_settings: An object specifying forwarding configurations for a Global load balancer.

          health_check: An object specifying health check settings for the load balancer.

          http_idle_timeout_seconds: An integer value which configures the idle timeout for HTTP requests to the
              target droplets.

          name: A human-readable name for a load balancer instance.

          network: A string indicating whether the load balancer should be external or internal.
              Internal load balancers have no public IPs and are only accessible to resources
              on the same VPC network. This property cannot be updated after creating the load
              balancer.

          network_stack: A string indicating whether the load balancer will support IPv4 or both IPv4 and
              IPv6 networking. This property cannot be updated after creating the load
              balancer.

          project_id: The ID of the project that the load balancer is associated with. If no ID is
              provided at creation, the load balancer associates with the user's default
              project. If an invalid project ID is provided, the load balancer will not be
              created.

          redirect_http_to_https: A boolean value indicating whether HTTP requests to the load balancer on port 80
              will be redirected to HTTPS on port 443.

          region: The slug identifier for the region where the resource will initially be
              available.

          size: This field has been replaced by the `size_unit` field for all regions except in
              AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
              balancer having a set number of nodes.

              - `lb-small` = 1 node
              - `lb-medium` = 3 nodes
              - `lb-large` = 6 nodes

              You can resize load balancers after creation up to once per hour. You cannot
              resize a load balancer within the first hour of its creation.

          size_unit: How many nodes the load balancer contains. Each additional node increases the
              load balancer's ability to manage more connections. Load balancers can be scaled
              up or down, and you can change the number of nodes after creation up to once per
              hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions.
              Use the `size` field to scale load balancers that reside in these regions.

          sticky_sessions: An object specifying sticky sessions settings for the load balancer.

          target_load_balancer_ids: An array containing the UUIDs of the Regional load balancers to be used as
              target backends for a Global load balancer.

          tls_cipher_policy: A string indicating the policy for the TLS cipher suites used by the load
              balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
              `DEFAULT`.

          type: A string indicating whether the load balancer should be a standard regional HTTP
              load balancer, a regional network load balancer that routes traffic at the
              TCP/UDP transport layer, or a global load balancer.

          vpc_uuid: A string specifying the UUID of the VPC to which the load balancer is assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        tag: str | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerCreateResponse:
        """
        To create a new load balancer instance, send a POST request to
        `/v2/load_balancers`.

        You can specify the Droplets that will sit behind the load balancer using one of
        two methods:

        - Set `droplet_ids` to a list of specific Droplet IDs.
        - Set `tag` to the name of a tag. All Droplets with this tag applied will be
          assigned to the load balancer. Additional Droplets will be automatically
          assigned as they are tagged.

        These methods are mutually exclusive.

        Args:
          forwarding_rules: An array of objects specifying the forwarding rules for a load balancer.

          algorithm: This field has been deprecated. You can no longer specify an algorithm for load
              balancers.

          disable_lets_encrypt_dns_records: A boolean value indicating whether to disable automatic DNS record creation for
              Let's Encrypt certificates that are added to the load balancer.

          domains: An array of objects specifying the domain configurations for a Global load
              balancer.

          enable_backend_keepalive: A boolean value indicating whether HTTP keepalive connections are maintained to
              target Droplets.

          enable_proxy_protocol: A boolean value indicating whether PROXY Protocol is in use.

          firewall: An object specifying allow and deny rules to control traffic to the load
              balancer.

          glb_settings: An object specifying forwarding configurations for a Global load balancer.

          health_check: An object specifying health check settings for the load balancer.

          http_idle_timeout_seconds: An integer value which configures the idle timeout for HTTP requests to the
              target droplets.

          name: A human-readable name for a load balancer instance.

          network: A string indicating whether the load balancer should be external or internal.
              Internal load balancers have no public IPs and are only accessible to resources
              on the same VPC network. This property cannot be updated after creating the load
              balancer.

          network_stack: A string indicating whether the load balancer will support IPv4 or both IPv4 and
              IPv6 networking. This property cannot be updated after creating the load
              balancer.

          project_id: The ID of the project that the load balancer is associated with. If no ID is
              provided at creation, the load balancer associates with the user's default
              project. If an invalid project ID is provided, the load balancer will not be
              created.

          redirect_http_to_https: A boolean value indicating whether HTTP requests to the load balancer on port 80
              will be redirected to HTTPS on port 443.

          region: The slug identifier for the region where the resource will initially be
              available.

          size: This field has been replaced by the `size_unit` field for all regions except in
              AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
              balancer having a set number of nodes.

              - `lb-small` = 1 node
              - `lb-medium` = 3 nodes
              - `lb-large` = 6 nodes

              You can resize load balancers after creation up to once per hour. You cannot
              resize a load balancer within the first hour of its creation.

          size_unit: How many nodes the load balancer contains. Each additional node increases the
              load balancer's ability to manage more connections. Load balancers can be scaled
              up or down, and you can change the number of nodes after creation up to once per
              hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions.
              Use the `size` field to scale load balancers that reside in these regions.

          sticky_sessions: An object specifying sticky sessions settings for the load balancer.

          tag: The name of a Droplet tag corresponding to Droplets assigned to the load
              balancer.

          target_load_balancer_ids: An array containing the UUIDs of the Regional load balancers to be used as
              target backends for a Global load balancer.

          tls_cipher_policy: A string indicating the policy for the TLS cipher suites used by the load
              balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
              `DEFAULT`.

          type: A string indicating whether the load balancer should be a standard regional HTTP
              load balancer, a regional network load balancer that routes traffic at the
              TCP/UDP transport layer, or a global load balancer.

          vpc_uuid: A string specifying the UUID of the VPC to which the load balancer is assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["forwarding_rules"])
    def create(
        self,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        droplet_ids: Iterable[int] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerCreateResponse:
        return self._post(
            "/v2/load_balancers"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/load_balancers",
            body=maybe_transform(
                {
                    "forwarding_rules": forwarding_rules,
                    "algorithm": algorithm,
                    "disable_lets_encrypt_dns_records": disable_lets_encrypt_dns_records,
                    "domains": domains,
                    "droplet_ids": droplet_ids,
                    "enable_backend_keepalive": enable_backend_keepalive,
                    "enable_proxy_protocol": enable_proxy_protocol,
                    "firewall": firewall,
                    "glb_settings": glb_settings,
                    "health_check": health_check,
                    "http_idle_timeout_seconds": http_idle_timeout_seconds,
                    "name": name,
                    "network": network,
                    "network_stack": network_stack,
                    "project_id": project_id,
                    "redirect_http_to_https": redirect_http_to_https,
                    "region": region,
                    "size": size,
                    "size_unit": size_unit,
                    "sticky_sessions": sticky_sessions,
                    "target_load_balancer_ids": target_load_balancer_ids,
                    "tls_cipher_policy": tls_cipher_policy,
                    "type": type,
                    "vpc_uuid": vpc_uuid,
                    "tag": tag,
                },
                load_balancer_create_params.LoadBalancerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerCreateResponse,
        )

    def retrieve(
        self,
        lb_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerRetrieveResponse:
        """
        To show information about a load balancer instance, send a GET request to
        `/v2/load_balancers/$LOAD_BALANCER_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        return self._get(
            f"/v2/load_balancers/{lb_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerRetrieveResponse,
        )

    @overload
    def update(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        droplet_ids: Iterable[int] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerUpdateResponse:
        """
        To update a load balancer's settings, send a PUT request to
        `/v2/load_balancers/$LOAD_BALANCER_ID`. The request should contain a full
        representation of the load balancer including existing attributes. It may
        contain _one of_ the `droplets_ids` or `tag` attributes as they are mutually
        exclusive. **Note that any attribute that is not provided will be reset to its
        default value.**

        Args:
          forwarding_rules: An array of objects specifying the forwarding rules for a load balancer.

          algorithm: This field has been deprecated. You can no longer specify an algorithm for load
              balancers.

          disable_lets_encrypt_dns_records: A boolean value indicating whether to disable automatic DNS record creation for
              Let's Encrypt certificates that are added to the load balancer.

          domains: An array of objects specifying the domain configurations for a Global load
              balancer.

          droplet_ids: An array containing the IDs of the Droplets assigned to the load balancer.

          enable_backend_keepalive: A boolean value indicating whether HTTP keepalive connections are maintained to
              target Droplets.

          enable_proxy_protocol: A boolean value indicating whether PROXY Protocol is in use.

          firewall: An object specifying allow and deny rules to control traffic to the load
              balancer.

          glb_settings: An object specifying forwarding configurations for a Global load balancer.

          health_check: An object specifying health check settings for the load balancer.

          http_idle_timeout_seconds: An integer value which configures the idle timeout for HTTP requests to the
              target droplets.

          name: A human-readable name for a load balancer instance.

          network: A string indicating whether the load balancer should be external or internal.
              Internal load balancers have no public IPs and are only accessible to resources
              on the same VPC network. This property cannot be updated after creating the load
              balancer.

          network_stack: A string indicating whether the load balancer will support IPv4 or both IPv4 and
              IPv6 networking. This property cannot be updated after creating the load
              balancer.

          project_id: The ID of the project that the load balancer is associated with. If no ID is
              provided at creation, the load balancer associates with the user's default
              project. If an invalid project ID is provided, the load balancer will not be
              created.

          redirect_http_to_https: A boolean value indicating whether HTTP requests to the load balancer on port 80
              will be redirected to HTTPS on port 443.

          region: The slug identifier for the region where the resource will initially be
              available.

          size: This field has been replaced by the `size_unit` field for all regions except in
              AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
              balancer having a set number of nodes.

              - `lb-small` = 1 node
              - `lb-medium` = 3 nodes
              - `lb-large` = 6 nodes

              You can resize load balancers after creation up to once per hour. You cannot
              resize a load balancer within the first hour of its creation.

          size_unit: How many nodes the load balancer contains. Each additional node increases the
              load balancer's ability to manage more connections. Load balancers can be scaled
              up or down, and you can change the number of nodes after creation up to once per
              hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions.
              Use the `size` field to scale load balancers that reside in these regions.

          sticky_sessions: An object specifying sticky sessions settings for the load balancer.

          target_load_balancer_ids: An array containing the UUIDs of the Regional load balancers to be used as
              target backends for a Global load balancer.

          tls_cipher_policy: A string indicating the policy for the TLS cipher suites used by the load
              balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
              `DEFAULT`.

          type: A string indicating whether the load balancer should be a standard regional HTTP
              load balancer, a regional network load balancer that routes traffic at the
              TCP/UDP transport layer, or a global load balancer.

          vpc_uuid: A string specifying the UUID of the VPC to which the load balancer is assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        tag: str | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerUpdateResponse:
        """
        To update a load balancer's settings, send a PUT request to
        `/v2/load_balancers/$LOAD_BALANCER_ID`. The request should contain a full
        representation of the load balancer including existing attributes. It may
        contain _one of_ the `droplets_ids` or `tag` attributes as they are mutually
        exclusive. **Note that any attribute that is not provided will be reset to its
        default value.**

        Args:
          forwarding_rules: An array of objects specifying the forwarding rules for a load balancer.

          algorithm: This field has been deprecated. You can no longer specify an algorithm for load
              balancers.

          disable_lets_encrypt_dns_records: A boolean value indicating whether to disable automatic DNS record creation for
              Let's Encrypt certificates that are added to the load balancer.

          domains: An array of objects specifying the domain configurations for a Global load
              balancer.

          enable_backend_keepalive: A boolean value indicating whether HTTP keepalive connections are maintained to
              target Droplets.

          enable_proxy_protocol: A boolean value indicating whether PROXY Protocol is in use.

          firewall: An object specifying allow and deny rules to control traffic to the load
              balancer.

          glb_settings: An object specifying forwarding configurations for a Global load balancer.

          health_check: An object specifying health check settings for the load balancer.

          http_idle_timeout_seconds: An integer value which configures the idle timeout for HTTP requests to the
              target droplets.

          name: A human-readable name for a load balancer instance.

          network: A string indicating whether the load balancer should be external or internal.
              Internal load balancers have no public IPs and are only accessible to resources
              on the same VPC network. This property cannot be updated after creating the load
              balancer.

          network_stack: A string indicating whether the load balancer will support IPv4 or both IPv4 and
              IPv6 networking. This property cannot be updated after creating the load
              balancer.

          project_id: The ID of the project that the load balancer is associated with. If no ID is
              provided at creation, the load balancer associates with the user's default
              project. If an invalid project ID is provided, the load balancer will not be
              created.

          redirect_http_to_https: A boolean value indicating whether HTTP requests to the load balancer on port 80
              will be redirected to HTTPS on port 443.

          region: The slug identifier for the region where the resource will initially be
              available.

          size: This field has been replaced by the `size_unit` field for all regions except in
              AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
              balancer having a set number of nodes.

              - `lb-small` = 1 node
              - `lb-medium` = 3 nodes
              - `lb-large` = 6 nodes

              You can resize load balancers after creation up to once per hour. You cannot
              resize a load balancer within the first hour of its creation.

          size_unit: How many nodes the load balancer contains. Each additional node increases the
              load balancer's ability to manage more connections. Load balancers can be scaled
              up or down, and you can change the number of nodes after creation up to once per
              hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions.
              Use the `size` field to scale load balancers that reside in these regions.

          sticky_sessions: An object specifying sticky sessions settings for the load balancer.

          tag: The name of a Droplet tag corresponding to Droplets assigned to the load
              balancer.

          target_load_balancer_ids: An array containing the UUIDs of the Regional load balancers to be used as
              target backends for a Global load balancer.

          tls_cipher_policy: A string indicating the policy for the TLS cipher suites used by the load
              balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
              `DEFAULT`.

          type: A string indicating whether the load balancer should be a standard regional HTTP
              load balancer, a regional network load balancer that routes traffic at the
              TCP/UDP transport layer, or a global load balancer.

          vpc_uuid: A string specifying the UUID of the VPC to which the load balancer is assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["forwarding_rules"])
    def update(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        droplet_ids: Iterable[int] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerUpdateResponse:
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        return self._put(
            f"/v2/load_balancers/{lb_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}",
            body=maybe_transform(
                {
                    "forwarding_rules": forwarding_rules,
                    "algorithm": algorithm,
                    "disable_lets_encrypt_dns_records": disable_lets_encrypt_dns_records,
                    "domains": domains,
                    "droplet_ids": droplet_ids,
                    "enable_backend_keepalive": enable_backend_keepalive,
                    "enable_proxy_protocol": enable_proxy_protocol,
                    "firewall": firewall,
                    "glb_settings": glb_settings,
                    "health_check": health_check,
                    "http_idle_timeout_seconds": http_idle_timeout_seconds,
                    "name": name,
                    "network": network,
                    "network_stack": network_stack,
                    "project_id": project_id,
                    "redirect_http_to_https": redirect_http_to_https,
                    "region": region,
                    "size": size,
                    "size_unit": size_unit,
                    "sticky_sessions": sticky_sessions,
                    "target_load_balancer_ids": target_load_balancer_ids,
                    "tls_cipher_policy": tls_cipher_policy,
                    "type": type,
                    "vpc_uuid": vpc_uuid,
                    "tag": tag,
                },
                load_balancer_update_params.LoadBalancerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerListResponse:
        """
        To list all of the load balancer instances on your account, send a GET request
        to `/v2/load_balancers`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/load_balancers"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/load_balancers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    load_balancer_list_params.LoadBalancerListParams,
                ),
            ),
            cast_to=LoadBalancerListResponse,
        )

    def delete(
        self,
        lb_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a load balancer instance, disassociating any Droplets assigned to it
        and removing it from your account, send a DELETE request to
        `/v2/load_balancers/$LOAD_BALANCER_ID`.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/load_balancers/{lb_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_cache(
        self,
        lb_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a Global load balancer CDN cache, send a DELETE request to
        `/v2/load_balancers/$LOAD_BALANCER_ID/cache`.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/load_balancers/{lb_id}/cache"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}/cache",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLoadBalancersResource(AsyncAPIResource):
    @cached_property
    def droplets(self) -> AsyncDropletsResource:
        return AsyncDropletsResource(self._client)

    @cached_property
    def forwarding_rules(self) -> AsyncForwardingRulesResource:
        return AsyncForwardingRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoadBalancersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncLoadBalancersResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        droplet_ids: Iterable[int] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerCreateResponse:
        """
        To create a new load balancer instance, send a POST request to
        `/v2/load_balancers`.

        You can specify the Droplets that will sit behind the load balancer using one of
        two methods:

        - Set `droplet_ids` to a list of specific Droplet IDs.
        - Set `tag` to the name of a tag. All Droplets with this tag applied will be
          assigned to the load balancer. Additional Droplets will be automatically
          assigned as they are tagged.

        These methods are mutually exclusive.

        Args:
          forwarding_rules: An array of objects specifying the forwarding rules for a load balancer.

          algorithm: This field has been deprecated. You can no longer specify an algorithm for load
              balancers.

          disable_lets_encrypt_dns_records: A boolean value indicating whether to disable automatic DNS record creation for
              Let's Encrypt certificates that are added to the load balancer.

          domains: An array of objects specifying the domain configurations for a Global load
              balancer.

          droplet_ids: An array containing the IDs of the Droplets assigned to the load balancer.

          enable_backend_keepalive: A boolean value indicating whether HTTP keepalive connections are maintained to
              target Droplets.

          enable_proxy_protocol: A boolean value indicating whether PROXY Protocol is in use.

          firewall: An object specifying allow and deny rules to control traffic to the load
              balancer.

          glb_settings: An object specifying forwarding configurations for a Global load balancer.

          health_check: An object specifying health check settings for the load balancer.

          http_idle_timeout_seconds: An integer value which configures the idle timeout for HTTP requests to the
              target droplets.

          name: A human-readable name for a load balancer instance.

          network: A string indicating whether the load balancer should be external or internal.
              Internal load balancers have no public IPs and are only accessible to resources
              on the same VPC network. This property cannot be updated after creating the load
              balancer.

          network_stack: A string indicating whether the load balancer will support IPv4 or both IPv4 and
              IPv6 networking. This property cannot be updated after creating the load
              balancer.

          project_id: The ID of the project that the load balancer is associated with. If no ID is
              provided at creation, the load balancer associates with the user's default
              project. If an invalid project ID is provided, the load balancer will not be
              created.

          redirect_http_to_https: A boolean value indicating whether HTTP requests to the load balancer on port 80
              will be redirected to HTTPS on port 443.

          region: The slug identifier for the region where the resource will initially be
              available.

          size: This field has been replaced by the `size_unit` field for all regions except in
              AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
              balancer having a set number of nodes.

              - `lb-small` = 1 node
              - `lb-medium` = 3 nodes
              - `lb-large` = 6 nodes

              You can resize load balancers after creation up to once per hour. You cannot
              resize a load balancer within the first hour of its creation.

          size_unit: How many nodes the load balancer contains. Each additional node increases the
              load balancer's ability to manage more connections. Load balancers can be scaled
              up or down, and you can change the number of nodes after creation up to once per
              hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions.
              Use the `size` field to scale load balancers that reside in these regions.

          sticky_sessions: An object specifying sticky sessions settings for the load balancer.

          target_load_balancer_ids: An array containing the UUIDs of the Regional load balancers to be used as
              target backends for a Global load balancer.

          tls_cipher_policy: A string indicating the policy for the TLS cipher suites used by the load
              balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
              `DEFAULT`.

          type: A string indicating whether the load balancer should be a standard regional HTTP
              load balancer, a regional network load balancer that routes traffic at the
              TCP/UDP transport layer, or a global load balancer.

          vpc_uuid: A string specifying the UUID of the VPC to which the load balancer is assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        tag: str | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerCreateResponse:
        """
        To create a new load balancer instance, send a POST request to
        `/v2/load_balancers`.

        You can specify the Droplets that will sit behind the load balancer using one of
        two methods:

        - Set `droplet_ids` to a list of specific Droplet IDs.
        - Set `tag` to the name of a tag. All Droplets with this tag applied will be
          assigned to the load balancer. Additional Droplets will be automatically
          assigned as they are tagged.

        These methods are mutually exclusive.

        Args:
          forwarding_rules: An array of objects specifying the forwarding rules for a load balancer.

          algorithm: This field has been deprecated. You can no longer specify an algorithm for load
              balancers.

          disable_lets_encrypt_dns_records: A boolean value indicating whether to disable automatic DNS record creation for
              Let's Encrypt certificates that are added to the load balancer.

          domains: An array of objects specifying the domain configurations for a Global load
              balancer.

          enable_backend_keepalive: A boolean value indicating whether HTTP keepalive connections are maintained to
              target Droplets.

          enable_proxy_protocol: A boolean value indicating whether PROXY Protocol is in use.

          firewall: An object specifying allow and deny rules to control traffic to the load
              balancer.

          glb_settings: An object specifying forwarding configurations for a Global load balancer.

          health_check: An object specifying health check settings for the load balancer.

          http_idle_timeout_seconds: An integer value which configures the idle timeout for HTTP requests to the
              target droplets.

          name: A human-readable name for a load balancer instance.

          network: A string indicating whether the load balancer should be external or internal.
              Internal load balancers have no public IPs and are only accessible to resources
              on the same VPC network. This property cannot be updated after creating the load
              balancer.

          network_stack: A string indicating whether the load balancer will support IPv4 or both IPv4 and
              IPv6 networking. This property cannot be updated after creating the load
              balancer.

          project_id: The ID of the project that the load balancer is associated with. If no ID is
              provided at creation, the load balancer associates with the user's default
              project. If an invalid project ID is provided, the load balancer will not be
              created.

          redirect_http_to_https: A boolean value indicating whether HTTP requests to the load balancer on port 80
              will be redirected to HTTPS on port 443.

          region: The slug identifier for the region where the resource will initially be
              available.

          size: This field has been replaced by the `size_unit` field for all regions except in
              AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
              balancer having a set number of nodes.

              - `lb-small` = 1 node
              - `lb-medium` = 3 nodes
              - `lb-large` = 6 nodes

              You can resize load balancers after creation up to once per hour. You cannot
              resize a load balancer within the first hour of its creation.

          size_unit: How many nodes the load balancer contains. Each additional node increases the
              load balancer's ability to manage more connections. Load balancers can be scaled
              up or down, and you can change the number of nodes after creation up to once per
              hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions.
              Use the `size` field to scale load balancers that reside in these regions.

          sticky_sessions: An object specifying sticky sessions settings for the load balancer.

          tag: The name of a Droplet tag corresponding to Droplets assigned to the load
              balancer.

          target_load_balancer_ids: An array containing the UUIDs of the Regional load balancers to be used as
              target backends for a Global load balancer.

          tls_cipher_policy: A string indicating the policy for the TLS cipher suites used by the load
              balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
              `DEFAULT`.

          type: A string indicating whether the load balancer should be a standard regional HTTP
              load balancer, a regional network load balancer that routes traffic at the
              TCP/UDP transport layer, or a global load balancer.

          vpc_uuid: A string specifying the UUID of the VPC to which the load balancer is assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["forwarding_rules"])
    async def create(
        self,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        droplet_ids: Iterable[int] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerCreateResponse:
        return await self._post(
            "/v2/load_balancers"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/load_balancers",
            body=await async_maybe_transform(
                {
                    "forwarding_rules": forwarding_rules,
                    "algorithm": algorithm,
                    "disable_lets_encrypt_dns_records": disable_lets_encrypt_dns_records,
                    "domains": domains,
                    "droplet_ids": droplet_ids,
                    "enable_backend_keepalive": enable_backend_keepalive,
                    "enable_proxy_protocol": enable_proxy_protocol,
                    "firewall": firewall,
                    "glb_settings": glb_settings,
                    "health_check": health_check,
                    "http_idle_timeout_seconds": http_idle_timeout_seconds,
                    "name": name,
                    "network": network,
                    "network_stack": network_stack,
                    "project_id": project_id,
                    "redirect_http_to_https": redirect_http_to_https,
                    "region": region,
                    "size": size,
                    "size_unit": size_unit,
                    "sticky_sessions": sticky_sessions,
                    "target_load_balancer_ids": target_load_balancer_ids,
                    "tls_cipher_policy": tls_cipher_policy,
                    "type": type,
                    "vpc_uuid": vpc_uuid,
                    "tag": tag,
                },
                load_balancer_create_params.LoadBalancerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerCreateResponse,
        )

    async def retrieve(
        self,
        lb_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerRetrieveResponse:
        """
        To show information about a load balancer instance, send a GET request to
        `/v2/load_balancers/$LOAD_BALANCER_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        return await self._get(
            f"/v2/load_balancers/{lb_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerRetrieveResponse,
        )

    @overload
    async def update(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        droplet_ids: Iterable[int] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerUpdateResponse:
        """
        To update a load balancer's settings, send a PUT request to
        `/v2/load_balancers/$LOAD_BALANCER_ID`. The request should contain a full
        representation of the load balancer including existing attributes. It may
        contain _one of_ the `droplets_ids` or `tag` attributes as they are mutually
        exclusive. **Note that any attribute that is not provided will be reset to its
        default value.**

        Args:
          forwarding_rules: An array of objects specifying the forwarding rules for a load balancer.

          algorithm: This field has been deprecated. You can no longer specify an algorithm for load
              balancers.

          disable_lets_encrypt_dns_records: A boolean value indicating whether to disable automatic DNS record creation for
              Let's Encrypt certificates that are added to the load balancer.

          domains: An array of objects specifying the domain configurations for a Global load
              balancer.

          droplet_ids: An array containing the IDs of the Droplets assigned to the load balancer.

          enable_backend_keepalive: A boolean value indicating whether HTTP keepalive connections are maintained to
              target Droplets.

          enable_proxy_protocol: A boolean value indicating whether PROXY Protocol is in use.

          firewall: An object specifying allow and deny rules to control traffic to the load
              balancer.

          glb_settings: An object specifying forwarding configurations for a Global load balancer.

          health_check: An object specifying health check settings for the load balancer.

          http_idle_timeout_seconds: An integer value which configures the idle timeout for HTTP requests to the
              target droplets.

          name: A human-readable name for a load balancer instance.

          network: A string indicating whether the load balancer should be external or internal.
              Internal load balancers have no public IPs and are only accessible to resources
              on the same VPC network. This property cannot be updated after creating the load
              balancer.

          network_stack: A string indicating whether the load balancer will support IPv4 or both IPv4 and
              IPv6 networking. This property cannot be updated after creating the load
              balancer.

          project_id: The ID of the project that the load balancer is associated with. If no ID is
              provided at creation, the load balancer associates with the user's default
              project. If an invalid project ID is provided, the load balancer will not be
              created.

          redirect_http_to_https: A boolean value indicating whether HTTP requests to the load balancer on port 80
              will be redirected to HTTPS on port 443.

          region: The slug identifier for the region where the resource will initially be
              available.

          size: This field has been replaced by the `size_unit` field for all regions except in
              AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
              balancer having a set number of nodes.

              - `lb-small` = 1 node
              - `lb-medium` = 3 nodes
              - `lb-large` = 6 nodes

              You can resize load balancers after creation up to once per hour. You cannot
              resize a load balancer within the first hour of its creation.

          size_unit: How many nodes the load balancer contains. Each additional node increases the
              load balancer's ability to manage more connections. Load balancers can be scaled
              up or down, and you can change the number of nodes after creation up to once per
              hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions.
              Use the `size` field to scale load balancers that reside in these regions.

          sticky_sessions: An object specifying sticky sessions settings for the load balancer.

          target_load_balancer_ids: An array containing the UUIDs of the Regional load balancers to be used as
              target backends for a Global load balancer.

          tls_cipher_policy: A string indicating the policy for the TLS cipher suites used by the load
              balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
              `DEFAULT`.

          type: A string indicating whether the load balancer should be a standard regional HTTP
              load balancer, a regional network load balancer that routes traffic at the
              TCP/UDP transport layer, or a global load balancer.

          vpc_uuid: A string specifying the UUID of the VPC to which the load balancer is assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        tag: str | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerUpdateResponse:
        """
        To update a load balancer's settings, send a PUT request to
        `/v2/load_balancers/$LOAD_BALANCER_ID`. The request should contain a full
        representation of the load balancer including existing attributes. It may
        contain _one of_ the `droplets_ids` or `tag` attributes as they are mutually
        exclusive. **Note that any attribute that is not provided will be reset to its
        default value.**

        Args:
          forwarding_rules: An array of objects specifying the forwarding rules for a load balancer.

          algorithm: This field has been deprecated. You can no longer specify an algorithm for load
              balancers.

          disable_lets_encrypt_dns_records: A boolean value indicating whether to disable automatic DNS record creation for
              Let's Encrypt certificates that are added to the load balancer.

          domains: An array of objects specifying the domain configurations for a Global load
              balancer.

          enable_backend_keepalive: A boolean value indicating whether HTTP keepalive connections are maintained to
              target Droplets.

          enable_proxy_protocol: A boolean value indicating whether PROXY Protocol is in use.

          firewall: An object specifying allow and deny rules to control traffic to the load
              balancer.

          glb_settings: An object specifying forwarding configurations for a Global load balancer.

          health_check: An object specifying health check settings for the load balancer.

          http_idle_timeout_seconds: An integer value which configures the idle timeout for HTTP requests to the
              target droplets.

          name: A human-readable name for a load balancer instance.

          network: A string indicating whether the load balancer should be external or internal.
              Internal load balancers have no public IPs and are only accessible to resources
              on the same VPC network. This property cannot be updated after creating the load
              balancer.

          network_stack: A string indicating whether the load balancer will support IPv4 or both IPv4 and
              IPv6 networking. This property cannot be updated after creating the load
              balancer.

          project_id: The ID of the project that the load balancer is associated with. If no ID is
              provided at creation, the load balancer associates with the user's default
              project. If an invalid project ID is provided, the load balancer will not be
              created.

          redirect_http_to_https: A boolean value indicating whether HTTP requests to the load balancer on port 80
              will be redirected to HTTPS on port 443.

          region: The slug identifier for the region where the resource will initially be
              available.

          size: This field has been replaced by the `size_unit` field for all regions except in
              AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load
              balancer having a set number of nodes.

              - `lb-small` = 1 node
              - `lb-medium` = 3 nodes
              - `lb-large` = 6 nodes

              You can resize load balancers after creation up to once per hour. You cannot
              resize a load balancer within the first hour of its creation.

          size_unit: How many nodes the load balancer contains. Each additional node increases the
              load balancer's ability to manage more connections. Load balancers can be scaled
              up or down, and you can change the number of nodes after creation up to once per
              hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions.
              Use the `size` field to scale load balancers that reside in these regions.

          sticky_sessions: An object specifying sticky sessions settings for the load balancer.

          tag: The name of a Droplet tag corresponding to Droplets assigned to the load
              balancer.

          target_load_balancer_ids: An array containing the UUIDs of the Regional load balancers to be used as
              target backends for a Global load balancer.

          tls_cipher_policy: A string indicating the policy for the TLS cipher suites used by the load
              balancer. The possible values are `DEFAULT` or `STRONG`. The default value is
              `DEFAULT`.

          type: A string indicating whether the load balancer should be a standard regional HTTP
              load balancer, a regional network load balancer that routes traffic at the
              TCP/UDP transport layer, or a global load balancer.

          vpc_uuid: A string specifying the UUID of the VPC to which the load balancer is assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["forwarding_rules"])
    async def update(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        algorithm: Literal["round_robin", "least_connections"] | Omit = omit,
        disable_lets_encrypt_dns_records: bool | Omit = omit,
        domains: Iterable[DomainsParam] | Omit = omit,
        droplet_ids: Iterable[int] | Omit = omit,
        enable_backend_keepalive: bool | Omit = omit,
        enable_proxy_protocol: bool | Omit = omit,
        firewall: LbFirewallParam | Omit = omit,
        glb_settings: GlbSettingsParam | Omit = omit,
        health_check: HealthCheckParam | Omit = omit,
        http_idle_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        network: Literal["EXTERNAL", "INTERNAL"] | Omit = omit,
        network_stack: Literal["IPV4", "DUALSTACK"] | Omit = omit,
        project_id: str | Omit = omit,
        redirect_http_to_https: bool | Omit = omit,
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
        | Omit = omit,
        size: Literal["lb-small", "lb-medium", "lb-large"] | Omit = omit,
        size_unit: int | Omit = omit,
        sticky_sessions: StickySessionsParam | Omit = omit,
        target_load_balancer_ids: SequenceNotStr[str] | Omit = omit,
        tls_cipher_policy: Literal["DEFAULT", "STRONG"] | Omit = omit,
        type: Literal["REGIONAL", "REGIONAL_NETWORK", "GLOBAL"] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerUpdateResponse:
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        return await self._put(
            f"/v2/load_balancers/{lb_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}",
            body=await async_maybe_transform(
                {
                    "forwarding_rules": forwarding_rules,
                    "algorithm": algorithm,
                    "disable_lets_encrypt_dns_records": disable_lets_encrypt_dns_records,
                    "domains": domains,
                    "droplet_ids": droplet_ids,
                    "enable_backend_keepalive": enable_backend_keepalive,
                    "enable_proxy_protocol": enable_proxy_protocol,
                    "firewall": firewall,
                    "glb_settings": glb_settings,
                    "health_check": health_check,
                    "http_idle_timeout_seconds": http_idle_timeout_seconds,
                    "name": name,
                    "network": network,
                    "network_stack": network_stack,
                    "project_id": project_id,
                    "redirect_http_to_https": redirect_http_to_https,
                    "region": region,
                    "size": size,
                    "size_unit": size_unit,
                    "sticky_sessions": sticky_sessions,
                    "target_load_balancer_ids": target_load_balancer_ids,
                    "tls_cipher_policy": tls_cipher_policy,
                    "type": type,
                    "vpc_uuid": vpc_uuid,
                    "tag": tag,
                },
                load_balancer_update_params.LoadBalancerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerListResponse:
        """
        To list all of the load balancer instances on your account, send a GET request
        to `/v2/load_balancers`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/load_balancers"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/load_balancers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    load_balancer_list_params.LoadBalancerListParams,
                ),
            ),
            cast_to=LoadBalancerListResponse,
        )

    async def delete(
        self,
        lb_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a load balancer instance, disassociating any Droplets assigned to it
        and removing it from your account, send a DELETE request to
        `/v2/load_balancers/$LOAD_BALANCER_ID`.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/load_balancers/{lb_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_cache(
        self,
        lb_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a Global load balancer CDN cache, send a DELETE request to
        `/v2/load_balancers/$LOAD_BALANCER_ID/cache`.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/load_balancers/{lb_id}/cache"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}/cache",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LoadBalancersResourceWithRawResponse:
    def __init__(self, load_balancers: LoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = to_raw_response_wrapper(
            load_balancers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            load_balancers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            load_balancers.update,
        )
        self.list = to_raw_response_wrapper(
            load_balancers.list,
        )
        self.delete = to_raw_response_wrapper(
            load_balancers.delete,
        )
        self.delete_cache = to_raw_response_wrapper(
            load_balancers.delete_cache,
        )

    @cached_property
    def droplets(self) -> DropletsResourceWithRawResponse:
        return DropletsResourceWithRawResponse(self._load_balancers.droplets)

    @cached_property
    def forwarding_rules(self) -> ForwardingRulesResourceWithRawResponse:
        return ForwardingRulesResourceWithRawResponse(self._load_balancers.forwarding_rules)


class AsyncLoadBalancersResourceWithRawResponse:
    def __init__(self, load_balancers: AsyncLoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = async_to_raw_response_wrapper(
            load_balancers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            load_balancers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            load_balancers.update,
        )
        self.list = async_to_raw_response_wrapper(
            load_balancers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            load_balancers.delete,
        )
        self.delete_cache = async_to_raw_response_wrapper(
            load_balancers.delete_cache,
        )

    @cached_property
    def droplets(self) -> AsyncDropletsResourceWithRawResponse:
        return AsyncDropletsResourceWithRawResponse(self._load_balancers.droplets)

    @cached_property
    def forwarding_rules(self) -> AsyncForwardingRulesResourceWithRawResponse:
        return AsyncForwardingRulesResourceWithRawResponse(self._load_balancers.forwarding_rules)


class LoadBalancersResourceWithStreamingResponse:
    def __init__(self, load_balancers: LoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = to_streamed_response_wrapper(
            load_balancers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            load_balancers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            load_balancers.update,
        )
        self.list = to_streamed_response_wrapper(
            load_balancers.list,
        )
        self.delete = to_streamed_response_wrapper(
            load_balancers.delete,
        )
        self.delete_cache = to_streamed_response_wrapper(
            load_balancers.delete_cache,
        )

    @cached_property
    def droplets(self) -> DropletsResourceWithStreamingResponse:
        return DropletsResourceWithStreamingResponse(self._load_balancers.droplets)

    @cached_property
    def forwarding_rules(self) -> ForwardingRulesResourceWithStreamingResponse:
        return ForwardingRulesResourceWithStreamingResponse(self._load_balancers.forwarding_rules)


class AsyncLoadBalancersResourceWithStreamingResponse:
    def __init__(self, load_balancers: AsyncLoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = async_to_streamed_response_wrapper(
            load_balancers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            load_balancers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            load_balancers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            load_balancers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            load_balancers.delete,
        )
        self.delete_cache = async_to_streamed_response_wrapper(
            load_balancers.delete_cache,
        )

    @cached_property
    def droplets(self) -> AsyncDropletsResourceWithStreamingResponse:
        return AsyncDropletsResourceWithStreamingResponse(self._load_balancers.droplets)

    @cached_property
    def forwarding_rules(self) -> AsyncForwardingRulesResourceWithStreamingResponse:
        return AsyncForwardingRulesResourceWithStreamingResponse(self._load_balancers.forwarding_rules)
