# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import overload

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.gpu_droplets import floating_ip_list_params, floating_ip_create_params
from ....types.gpu_droplets.floating_ip_list_response import FloatingIPListResponse
from ....types.gpu_droplets.floating_ip_create_response import FloatingIPCreateResponse
from ....types.gpu_droplets.floating_ip_retrieve_response import FloatingIPRetrieveResponse

__all__ = ["FloatingIPsResource", "AsyncFloatingIPsResource"]


class FloatingIPsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FloatingIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return FloatingIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FloatingIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return FloatingIPsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        droplet_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIPCreateResponse:
        """
        On creation, a floating IP must be either assigned to a Droplet or reserved to a
        region.

        - To create a new floating IP assigned to a Droplet, send a POST request to
          `/v2/floating_ips` with the `droplet_id` attribute.

        - To create a new floating IP reserved to a region, send a POST request to
          `/v2/floating_ips` with the `region` attribute.

        Args:
          droplet_id: The ID of the Droplet that the floating IP will be assigned to.

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
        region: str,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIPCreateResponse:
        """
        On creation, a floating IP must be either assigned to a Droplet or reserved to a
        region.

        - To create a new floating IP assigned to a Droplet, send a POST request to
          `/v2/floating_ips` with the `droplet_id` attribute.

        - To create a new floating IP reserved to a region, send a POST request to
          `/v2/floating_ips` with the `region` attribute.

        Args:
          region: The slug identifier for the region the floating IP will be reserved to.

          project_id: The UUID of the project to which the floating IP will be assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["droplet_id"], ["region"])
    def create(
        self,
        *,
        droplet_id: int | Omit = omit,
        region: str | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIPCreateResponse:
        return self._post(
            "/v2/floating_ips" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/floating_ips",
            body=maybe_transform(
                {
                    "droplet_id": droplet_id,
                    "region": region,
                    "project_id": project_id,
                },
                floating_ip_create_params.FloatingIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIPCreateResponse,
        )

    def retrieve(
        self,
        floating_ip: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIPRetrieveResponse:
        """
        To show information about a floating IP, send a GET request to
        `/v2/floating_ips/$FLOATING_IP_ADDR`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        return self._get(
            f"/v2/floating_ips/{floating_ip}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIPRetrieveResponse,
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
    ) -> FloatingIPListResponse:
        """
        To list all of the floating IPs available on your account, send a GET request to
        `/v2/floating_ips`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/floating_ips" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/floating_ips",
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
                    floating_ip_list_params.FloatingIPListParams,
                ),
            ),
            cast_to=FloatingIPListResponse,
        )

    def delete(
        self,
        floating_ip: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a floating IP and remove it from your account, send a DELETE request
        to `/v2/floating_ips/$FLOATING_IP_ADDR`.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/floating_ips/{floating_ip}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFloatingIPsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFloatingIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFloatingIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFloatingIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncFloatingIPsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        droplet_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIPCreateResponse:
        """
        On creation, a floating IP must be either assigned to a Droplet or reserved to a
        region.

        - To create a new floating IP assigned to a Droplet, send a POST request to
          `/v2/floating_ips` with the `droplet_id` attribute.

        - To create a new floating IP reserved to a region, send a POST request to
          `/v2/floating_ips` with the `region` attribute.

        Args:
          droplet_id: The ID of the Droplet that the floating IP will be assigned to.

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
        region: str,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIPCreateResponse:
        """
        On creation, a floating IP must be either assigned to a Droplet or reserved to a
        region.

        - To create a new floating IP assigned to a Droplet, send a POST request to
          `/v2/floating_ips` with the `droplet_id` attribute.

        - To create a new floating IP reserved to a region, send a POST request to
          `/v2/floating_ips` with the `region` attribute.

        Args:
          region: The slug identifier for the region the floating IP will be reserved to.

          project_id: The UUID of the project to which the floating IP will be assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["droplet_id"], ["region"])
    async def create(
        self,
        *,
        droplet_id: int | Omit = omit,
        region: str | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIPCreateResponse:
        return await self._post(
            "/v2/floating_ips" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/floating_ips",
            body=await async_maybe_transform(
                {
                    "droplet_id": droplet_id,
                    "region": region,
                    "project_id": project_id,
                },
                floating_ip_create_params.FloatingIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIPCreateResponse,
        )

    async def retrieve(
        self,
        floating_ip: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIPRetrieveResponse:
        """
        To show information about a floating IP, send a GET request to
        `/v2/floating_ips/$FLOATING_IP_ADDR`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        return await self._get(
            f"/v2/floating_ips/{floating_ip}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIPRetrieveResponse,
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
    ) -> FloatingIPListResponse:
        """
        To list all of the floating IPs available on your account, send a GET request to
        `/v2/floating_ips`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/floating_ips" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/floating_ips",
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
                    floating_ip_list_params.FloatingIPListParams,
                ),
            ),
            cast_to=FloatingIPListResponse,
        )

    async def delete(
        self,
        floating_ip: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a floating IP and remove it from your account, send a DELETE request
        to `/v2/floating_ips/$FLOATING_IP_ADDR`.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/floating_ips/{floating_ip}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FloatingIPsResourceWithRawResponse:
    def __init__(self, floating_ips: FloatingIPsResource) -> None:
        self._floating_ips = floating_ips

        self.create = to_raw_response_wrapper(
            floating_ips.create,
        )
        self.retrieve = to_raw_response_wrapper(
            floating_ips.retrieve,
        )
        self.list = to_raw_response_wrapper(
            floating_ips.list,
        )
        self.delete = to_raw_response_wrapper(
            floating_ips.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._floating_ips.actions)


class AsyncFloatingIPsResourceWithRawResponse:
    def __init__(self, floating_ips: AsyncFloatingIPsResource) -> None:
        self._floating_ips = floating_ips

        self.create = async_to_raw_response_wrapper(
            floating_ips.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            floating_ips.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            floating_ips.list,
        )
        self.delete = async_to_raw_response_wrapper(
            floating_ips.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._floating_ips.actions)


class FloatingIPsResourceWithStreamingResponse:
    def __init__(self, floating_ips: FloatingIPsResource) -> None:
        self._floating_ips = floating_ips

        self.create = to_streamed_response_wrapper(
            floating_ips.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            floating_ips.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            floating_ips.list,
        )
        self.delete = to_streamed_response_wrapper(
            floating_ips.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._floating_ips.actions)


class AsyncFloatingIPsResourceWithStreamingResponse:
    def __init__(self, floating_ips: AsyncFloatingIPsResource) -> None:
        self._floating_ips = floating_ips

        self.create = async_to_streamed_response_wrapper(
            floating_ips.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            floating_ips.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            floating_ips.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            floating_ips.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._floating_ips.actions)
