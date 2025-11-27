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
from ....types.gpu_droplets.firewalls import droplet_add_params, droplet_remove_params

__all__ = ["DropletsResource", "AsyncDropletsResource"]


class DropletsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DropletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return DropletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DropletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return DropletsResourceWithStreamingResponse(self)

    def add(
        self,
        firewall_id: str,
        *,
        droplet_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To assign a Droplet to a firewall, send a POST request to
        `/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should
        be a `droplet_ids` attribute containing a list of Droplet IDs.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          droplet_ids: An array containing the IDs of the Droplets to be assigned to the firewall.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v2/firewalls/{firewall_id}/droplets"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/droplets",
            body=maybe_transform({"droplet_ids": droplet_ids}, droplet_add_params.DropletAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        firewall_id: str,
        *,
        droplet_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To remove a Droplet from a firewall, send a DELETE request to
        `/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should
        be a `droplet_ids` attribute containing a list of Droplet IDs.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          droplet_ids: An array containing the IDs of the Droplets to be removed from the firewall.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/firewalls/{firewall_id}/droplets"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/droplets",
            body=maybe_transform({"droplet_ids": droplet_ids}, droplet_remove_params.DropletRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDropletsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDropletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDropletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDropletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncDropletsResourceWithStreamingResponse(self)

    async def add(
        self,
        firewall_id: str,
        *,
        droplet_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To assign a Droplet to a firewall, send a POST request to
        `/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should
        be a `droplet_ids` attribute containing a list of Droplet IDs.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          droplet_ids: An array containing the IDs of the Droplets to be assigned to the firewall.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v2/firewalls/{firewall_id}/droplets"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/droplets",
            body=await async_maybe_transform({"droplet_ids": droplet_ids}, droplet_add_params.DropletAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        firewall_id: str,
        *,
        droplet_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To remove a Droplet from a firewall, send a DELETE request to
        `/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should
        be a `droplet_ids` attribute containing a list of Droplet IDs.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          droplet_ids: An array containing the IDs of the Droplets to be removed from the firewall.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/firewalls/{firewall_id}/droplets"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/droplets",
            body=await async_maybe_transform({"droplet_ids": droplet_ids}, droplet_remove_params.DropletRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DropletsResourceWithRawResponse:
    def __init__(self, droplets: DropletsResource) -> None:
        self._droplets = droplets

        self.add = to_raw_response_wrapper(
            droplets.add,
        )
        self.remove = to_raw_response_wrapper(
            droplets.remove,
        )


class AsyncDropletsResourceWithRawResponse:
    def __init__(self, droplets: AsyncDropletsResource) -> None:
        self._droplets = droplets

        self.add = async_to_raw_response_wrapper(
            droplets.add,
        )
        self.remove = async_to_raw_response_wrapper(
            droplets.remove,
        )


class DropletsResourceWithStreamingResponse:
    def __init__(self, droplets: DropletsResource) -> None:
        self._droplets = droplets

        self.add = to_streamed_response_wrapper(
            droplets.add,
        )
        self.remove = to_streamed_response_wrapper(
            droplets.remove,
        )


class AsyncDropletsResourceWithStreamingResponse:
    def __init__(self, droplets: AsyncDropletsResource) -> None:
        self._droplets = droplets

        self.add = async_to_streamed_response_wrapper(
            droplets.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            droplets.remove,
        )
