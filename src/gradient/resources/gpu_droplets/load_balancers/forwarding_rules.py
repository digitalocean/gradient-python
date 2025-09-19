# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from ....types.gpu_droplets.load_balancers import forwarding_rule_add_params, forwarding_rule_remove_params
from ....types.gpu_droplets.forwarding_rule_param import ForwardingRuleParam

__all__ = ["ForwardingRulesResource", "AsyncForwardingRulesResource"]


class ForwardingRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForwardingRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ForwardingRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForwardingRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ForwardingRulesResourceWithStreamingResponse(self)

    def add(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To add an additional forwarding rule to a load balancer instance, send a POST
        request to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body
        of the request, there should be a `forwarding_rules` attribute containing an
        array of rules to be added.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v2/load_balancers/{lb_id}/forwarding_rules"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}/forwarding_rules",
            body=maybe_transform(
                {"forwarding_rules": forwarding_rules}, forwarding_rule_add_params.ForwardingRuleAddParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To remove forwarding rules from a load balancer instance, send a DELETE request
        to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body of the
        request, there should be a `forwarding_rules` attribute containing an array of
        rules to be removed.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

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
            f"/v2/load_balancers/{lb_id}/forwarding_rules"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}/forwarding_rules",
            body=maybe_transform(
                {"forwarding_rules": forwarding_rules}, forwarding_rule_remove_params.ForwardingRuleRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncForwardingRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForwardingRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncForwardingRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForwardingRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncForwardingRulesResourceWithStreamingResponse(self)

    async def add(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To add an additional forwarding rule to a load balancer instance, send a POST
        request to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body
        of the request, there should be a `forwarding_rules` attribute containing an
        array of rules to be added.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lb_id:
            raise ValueError(f"Expected a non-empty value for `lb_id` but received {lb_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v2/load_balancers/{lb_id}/forwarding_rules"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}/forwarding_rules",
            body=await async_maybe_transform(
                {"forwarding_rules": forwarding_rules}, forwarding_rule_add_params.ForwardingRuleAddParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        lb_id: str,
        *,
        forwarding_rules: Iterable[ForwardingRuleParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To remove forwarding rules from a load balancer instance, send a DELETE request
        to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body of the
        request, there should be a `forwarding_rules` attribute containing an array of
        rules to be removed.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

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
            f"/v2/load_balancers/{lb_id}/forwarding_rules"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/load_balancers/{lb_id}/forwarding_rules",
            body=await async_maybe_transform(
                {"forwarding_rules": forwarding_rules}, forwarding_rule_remove_params.ForwardingRuleRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ForwardingRulesResourceWithRawResponse:
    def __init__(self, forwarding_rules: ForwardingRulesResource) -> None:
        self._forwarding_rules = forwarding_rules

        self.add = to_raw_response_wrapper(
            forwarding_rules.add,
        )
        self.remove = to_raw_response_wrapper(
            forwarding_rules.remove,
        )


class AsyncForwardingRulesResourceWithRawResponse:
    def __init__(self, forwarding_rules: AsyncForwardingRulesResource) -> None:
        self._forwarding_rules = forwarding_rules

        self.add = async_to_raw_response_wrapper(
            forwarding_rules.add,
        )
        self.remove = async_to_raw_response_wrapper(
            forwarding_rules.remove,
        )


class ForwardingRulesResourceWithStreamingResponse:
    def __init__(self, forwarding_rules: ForwardingRulesResource) -> None:
        self._forwarding_rules = forwarding_rules

        self.add = to_streamed_response_wrapper(
            forwarding_rules.add,
        )
        self.remove = to_streamed_response_wrapper(
            forwarding_rules.remove,
        )


class AsyncForwardingRulesResourceWithStreamingResponse:
    def __init__(self, forwarding_rules: AsyncForwardingRulesResource) -> None:
        self._forwarding_rules = forwarding_rules

        self.add = async_to_streamed_response_wrapper(
            forwarding_rules.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            forwarding_rules.remove,
        )
