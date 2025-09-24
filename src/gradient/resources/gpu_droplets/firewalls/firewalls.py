# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from .droplets import (
    DropletsResource,
    AsyncDropletsResource,
    DropletsResourceWithRawResponse,
    AsyncDropletsResourceWithRawResponse,
    DropletsResourceWithStreamingResponse,
    AsyncDropletsResourceWithStreamingResponse,
)
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
from ....types.gpu_droplets import firewall_list_params, firewall_create_params, firewall_update_params
from ....types.gpu_droplets.firewall_param import FirewallParam
from ....types.gpu_droplets.firewall_list_response import FirewallListResponse
from ....types.gpu_droplets.firewall_create_response import FirewallCreateResponse
from ....types.gpu_droplets.firewall_update_response import FirewallUpdateResponse
from ....types.gpu_droplets.firewall_retrieve_response import FirewallRetrieveResponse

__all__ = ["FirewallsResource", "AsyncFirewallsResource"]


class FirewallsResource(SyncAPIResource):
    @cached_property
    def droplets(self) -> DropletsResource:
        return DropletsResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return FirewallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return FirewallsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: firewall_create_params.Body | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallCreateResponse:
        """To create a new firewall, send a POST request to `/v2/firewalls`.

        The request
        must contain at least one inbound or outbound access rule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/firewalls" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/firewalls",
            body=maybe_transform(body, firewall_create_params.FirewallCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallCreateResponse,
        )

    def retrieve(
        self,
        firewall_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallRetrieveResponse:
        """
        To show information about an existing firewall, send a GET request to
        `/v2/firewalls/$FIREWALL_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        return self._get(
            f"/v2/firewalls/{firewall_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRetrieveResponse,
        )

    def update(
        self,
        firewall_id: str,
        *,
        firewall: FirewallParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallUpdateResponse:
        """
        To update the configuration of an existing firewall, send a PUT request to
        `/v2/firewalls/$FIREWALL_ID`. The request should contain a full representation
        of the firewall including existing attributes. **Note that any attributes that
        are not provided will be reset to their default values.**

        You must have read access (e.g. `droplet:read`) to all resources attached to the
        firewall to successfully update the firewall.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        return self._put(
            f"/v2/firewalls/{firewall_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}",
            body=maybe_transform(firewall, firewall_update_params.FirewallUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallUpdateResponse,
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
    ) -> FirewallListResponse:
        """
        To list all of the firewalls available on your account, send a GET request to
        `/v2/firewalls`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/firewalls" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/firewalls",
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
                    firewall_list_params.FirewallListParams,
                ),
            ),
            cast_to=FirewallListResponse,
        )

    def delete(
        self,
        firewall_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a firewall send a DELETE request to `/v2/firewalls/$FIREWALL_ID`.

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
            f"/v2/firewalls/{firewall_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFirewallsResource(AsyncAPIResource):
    @cached_property
    def droplets(self) -> AsyncDropletsResource:
        return AsyncDropletsResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFirewallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFirewallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncFirewallsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: firewall_create_params.Body | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallCreateResponse:
        """To create a new firewall, send a POST request to `/v2/firewalls`.

        The request
        must contain at least one inbound or outbound access rule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/firewalls" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/firewalls",
            body=await async_maybe_transform(body, firewall_create_params.FirewallCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallCreateResponse,
        )

    async def retrieve(
        self,
        firewall_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallRetrieveResponse:
        """
        To show information about an existing firewall, send a GET request to
        `/v2/firewalls/$FIREWALL_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        return await self._get(
            f"/v2/firewalls/{firewall_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallRetrieveResponse,
        )

    async def update(
        self,
        firewall_id: str,
        *,
        firewall: FirewallParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FirewallUpdateResponse:
        """
        To update the configuration of an existing firewall, send a PUT request to
        `/v2/firewalls/$FIREWALL_ID`. The request should contain a full representation
        of the firewall including existing attributes. **Note that any attributes that
        are not provided will be reset to their default values.**

        You must have read access (e.g. `droplet:read`) to all resources attached to the
        firewall to successfully update the firewall.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        return await self._put(
            f"/v2/firewalls/{firewall_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}",
            body=await async_maybe_transform(firewall, firewall_update_params.FirewallUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FirewallUpdateResponse,
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
    ) -> FirewallListResponse:
        """
        To list all of the firewalls available on your account, send a GET request to
        `/v2/firewalls`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/firewalls" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/firewalls",
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
                    firewall_list_params.FirewallListParams,
                ),
            ),
            cast_to=FirewallListResponse,
        )

    async def delete(
        self,
        firewall_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a firewall send a DELETE request to `/v2/firewalls/$FIREWALL_ID`.

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
            f"/v2/firewalls/{firewall_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FirewallsResourceWithRawResponse:
    def __init__(self, firewalls: FirewallsResource) -> None:
        self._firewalls = firewalls

        self.create = to_raw_response_wrapper(
            firewalls.create,
        )
        self.retrieve = to_raw_response_wrapper(
            firewalls.retrieve,
        )
        self.update = to_raw_response_wrapper(
            firewalls.update,
        )
        self.list = to_raw_response_wrapper(
            firewalls.list,
        )
        self.delete = to_raw_response_wrapper(
            firewalls.delete,
        )

    @cached_property
    def droplets(self) -> DropletsResourceWithRawResponse:
        return DropletsResourceWithRawResponse(self._firewalls.droplets)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._firewalls.tags)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._firewalls.rules)


class AsyncFirewallsResourceWithRawResponse:
    def __init__(self, firewalls: AsyncFirewallsResource) -> None:
        self._firewalls = firewalls

        self.create = async_to_raw_response_wrapper(
            firewalls.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            firewalls.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            firewalls.update,
        )
        self.list = async_to_raw_response_wrapper(
            firewalls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            firewalls.delete,
        )

    @cached_property
    def droplets(self) -> AsyncDropletsResourceWithRawResponse:
        return AsyncDropletsResourceWithRawResponse(self._firewalls.droplets)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._firewalls.tags)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._firewalls.rules)


class FirewallsResourceWithStreamingResponse:
    def __init__(self, firewalls: FirewallsResource) -> None:
        self._firewalls = firewalls

        self.create = to_streamed_response_wrapper(
            firewalls.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            firewalls.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            firewalls.update,
        )
        self.list = to_streamed_response_wrapper(
            firewalls.list,
        )
        self.delete = to_streamed_response_wrapper(
            firewalls.delete,
        )

    @cached_property
    def droplets(self) -> DropletsResourceWithStreamingResponse:
        return DropletsResourceWithStreamingResponse(self._firewalls.droplets)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._firewalls.tags)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._firewalls.rules)


class AsyncFirewallsResourceWithStreamingResponse:
    def __init__(self, firewalls: AsyncFirewallsResource) -> None:
        self._firewalls = firewalls

        self.create = async_to_streamed_response_wrapper(
            firewalls.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            firewalls.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            firewalls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            firewalls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            firewalls.delete,
        )

    @cached_property
    def droplets(self) -> AsyncDropletsResourceWithStreamingResponse:
        return AsyncDropletsResourceWithStreamingResponse(self._firewalls.droplets)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._firewalls.tags)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._firewalls.rules)
