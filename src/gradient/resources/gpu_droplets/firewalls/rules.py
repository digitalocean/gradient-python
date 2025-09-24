# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.gpu_droplets.firewalls import rule_add_params, rule_remove_params

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    def add(
        self,
        firewall_id: str,
        *,
        inbound_rules: Optional[Iterable[rule_add_params.InboundRule]] | Omit = omit,
        outbound_rules: Optional[Iterable[rule_add_params.OutboundRule]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To add additional access rules to a firewall, send a POST request to
        `/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an
        inbound_rules and/or outbound_rules attribute containing an array of rules to be
        added.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v2/firewalls/{firewall_id}/rules"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/rules",
            body=maybe_transform(
                {
                    "inbound_rules": inbound_rules,
                    "outbound_rules": outbound_rules,
                },
                rule_add_params.RuleAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        firewall_id: str,
        *,
        inbound_rules: Optional[Iterable[rule_remove_params.InboundRule]] | Omit = omit,
        outbound_rules: Optional[Iterable[rule_remove_params.OutboundRule]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To remove access rules from a firewall, send a DELETE request to
        `/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an
        `inbound_rules` and/or `outbound_rules` attribute containing an array of rules
        to be removed.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/firewalls/{firewall_id}/rules"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/rules",
            body=maybe_transform(
                {
                    "inbound_rules": inbound_rules,
                    "outbound_rules": outbound_rules,
                },
                rule_remove_params.RuleRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    async def add(
        self,
        firewall_id: str,
        *,
        inbound_rules: Optional[Iterable[rule_add_params.InboundRule]] | Omit = omit,
        outbound_rules: Optional[Iterable[rule_add_params.OutboundRule]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To add additional access rules to a firewall, send a POST request to
        `/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an
        inbound_rules and/or outbound_rules attribute containing an array of rules to be
        added.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v2/firewalls/{firewall_id}/rules"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/rules",
            body=await async_maybe_transform(
                {
                    "inbound_rules": inbound_rules,
                    "outbound_rules": outbound_rules,
                },
                rule_add_params.RuleAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        firewall_id: str,
        *,
        inbound_rules: Optional[Iterable[rule_remove_params.InboundRule]] | Omit = omit,
        outbound_rules: Optional[Iterable[rule_remove_params.OutboundRule]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To remove access rules from a firewall, send a DELETE request to
        `/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an
        `inbound_rules` and/or `outbound_rules` attribute containing an array of rules
        to be removed.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/firewalls/{firewall_id}/rules"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/rules",
            body=await async_maybe_transform(
                {
                    "inbound_rules": inbound_rules,
                    "outbound_rules": outbound_rules,
                },
                rule_remove_params.RuleRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.add = to_raw_response_wrapper(
            rules.add,
        )
        self.remove = to_raw_response_wrapper(
            rules.remove,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.add = async_to_raw_response_wrapper(
            rules.add,
        )
        self.remove = async_to_raw_response_wrapper(
            rules.remove,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.add = to_streamed_response_wrapper(
            rules.add,
        )
        self.remove = to_streamed_response_wrapper(
            rules.remove,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.add = async_to_streamed_response_wrapper(
            rules.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            rules.remove,
        )
