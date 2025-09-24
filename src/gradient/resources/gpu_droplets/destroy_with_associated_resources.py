# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.gpu_droplets import destroy_with_associated_resource_delete_selective_params
from ...types.gpu_droplets.destroy_with_associated_resource_list_response import (
    DestroyWithAssociatedResourceListResponse,
)
from ...types.gpu_droplets.destroy_with_associated_resource_check_status_response import (
    DestroyWithAssociatedResourceCheckStatusResponse,
)

__all__ = ["DestroyWithAssociatedResourcesResource", "AsyncDestroyWithAssociatedResourcesResource"]


class DestroyWithAssociatedResourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DestroyWithAssociatedResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return DestroyWithAssociatedResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestroyWithAssociatedResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return DestroyWithAssociatedResourcesResourceWithStreamingResponse(self)

    def list(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestroyWithAssociatedResourceListResponse:
        """
        To list the associated billable resources that can be destroyed along with a
        Droplet, send a GET request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources` endpoint.

        This endpoint will only return resources that you are authorized to see. For
        example, to see associated Reserved IPs, include the `reserved_ip:read` scope.

        The response will be a JSON object containing `snapshots`, `volumes`, and
        `volume_snapshots` keys. Each will be set to an array of objects containing
        information about the associated resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestroyWithAssociatedResourceListResponse,
        )

    def check_status(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestroyWithAssociatedResourceCheckStatusResponse:
        """
        To check on the status of a request to destroy a Droplet with its associated
        resources, send a GET request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/status` endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources/status"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestroyWithAssociatedResourceCheckStatusResponse,
        )

    def delete_dangerous(
        self,
        droplet_id: int,
        *,
        x_dangerous: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy a Droplet along with all of its associated resources, send a DELETE
        request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/dangerous` endpoint.
        The headers of this request must include an `X-Dangerous` key set to `true`. To
        preview which resources will be destroyed, first query the Droplet's associated
        resources. This operation _can not_ be reverse and should be used with caution.

        A successful response will include a 202 response code and no content. Use the
        status endpoint to check on the success or failure of the destruction of the
        individual resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"X-Dangerous": ("true" if x_dangerous else "false")})
        return self._delete(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources/dangerous"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources/dangerous",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_selective(
        self,
        droplet_id: int,
        *,
        floating_ips: SequenceNotStr[str] | Omit = omit,
        reserved_ips: SequenceNotStr[str] | Omit = omit,
        snapshots: SequenceNotStr[str] | Omit = omit,
        volume_snapshots: SequenceNotStr[str] | Omit = omit,
        volumes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy a Droplet along with a sub-set of its associated resources, send a
        DELETE request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/selective` endpoint.
        The JSON body of the request should include `reserved_ips`, `snapshots`,
        `volumes`, or `volume_snapshots` keys each set to an array of IDs for the
        associated resources to be destroyed. The IDs can be found by querying the
        Droplet's associated resources. Any associated resource not included in the
        request will remain and continue to accrue changes on your account.

        A successful response will include a 202 response code and no content. Use the
        status endpoint to check on the success or failure of the destruction of the
        individual resources.

        Args:
          floating_ips: An array of unique identifiers for the floating IPs to be scheduled for
              deletion.

          reserved_ips: An array of unique identifiers for the reserved IPs to be scheduled for
              deletion.

          snapshots: An array of unique identifiers for the snapshots to be scheduled for deletion.

          volume_snapshots: An array of unique identifiers for the volume snapshots to be scheduled for
              deletion.

          volumes: An array of unique identifiers for the volumes to be scheduled for deletion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources/selective"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources/selective",
            body=maybe_transform(
                {
                    "floating_ips": floating_ips,
                    "reserved_ips": reserved_ips,
                    "snapshots": snapshots,
                    "volume_snapshots": volume_snapshots,
                    "volumes": volumes,
                },
                destroy_with_associated_resource_delete_selective_params.DestroyWithAssociatedResourceDeleteSelectiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retry(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        If the status of a request to destroy a Droplet with its associated resources
        reported any errors, it can be retried by sending a POST request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/retry` endpoint.

        Only one destroy can be active at a time per Droplet. If a retry is issued while
        another destroy is in progress for the Droplet a 409 status code will be
        returned. A successful response will include a 202 response code and no content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources/retry"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDestroyWithAssociatedResourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDestroyWithAssociatedResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDestroyWithAssociatedResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestroyWithAssociatedResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncDestroyWithAssociatedResourcesResourceWithStreamingResponse(self)

    async def list(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestroyWithAssociatedResourceListResponse:
        """
        To list the associated billable resources that can be destroyed along with a
        Droplet, send a GET request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources` endpoint.

        This endpoint will only return resources that you are authorized to see. For
        example, to see associated Reserved IPs, include the `reserved_ip:read` scope.

        The response will be a JSON object containing `snapshots`, `volumes`, and
        `volume_snapshots` keys. Each will be set to an array of objects containing
        information about the associated resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestroyWithAssociatedResourceListResponse,
        )

    async def check_status(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestroyWithAssociatedResourceCheckStatusResponse:
        """
        To check on the status of a request to destroy a Droplet with its associated
        resources, send a GET request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/status` endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources/status"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestroyWithAssociatedResourceCheckStatusResponse,
        )

    async def delete_dangerous(
        self,
        droplet_id: int,
        *,
        x_dangerous: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy a Droplet along with all of its associated resources, send a DELETE
        request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/dangerous` endpoint.
        The headers of this request must include an `X-Dangerous` key set to `true`. To
        preview which resources will be destroyed, first query the Droplet's associated
        resources. This operation _can not_ be reverse and should be used with caution.

        A successful response will include a 202 response code and no content. Use the
        status endpoint to check on the success or failure of the destruction of the
        individual resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"X-Dangerous": ("true" if x_dangerous else "false")})
        return await self._delete(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources/dangerous"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources/dangerous",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_selective(
        self,
        droplet_id: int,
        *,
        floating_ips: SequenceNotStr[str] | Omit = omit,
        reserved_ips: SequenceNotStr[str] | Omit = omit,
        snapshots: SequenceNotStr[str] | Omit = omit,
        volume_snapshots: SequenceNotStr[str] | Omit = omit,
        volumes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy a Droplet along with a sub-set of its associated resources, send a
        DELETE request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/selective` endpoint.
        The JSON body of the request should include `reserved_ips`, `snapshots`,
        `volumes`, or `volume_snapshots` keys each set to an array of IDs for the
        associated resources to be destroyed. The IDs can be found by querying the
        Droplet's associated resources. Any associated resource not included in the
        request will remain and continue to accrue changes on your account.

        A successful response will include a 202 response code and no content. Use the
        status endpoint to check on the success or failure of the destruction of the
        individual resources.

        Args:
          floating_ips: An array of unique identifiers for the floating IPs to be scheduled for
              deletion.

          reserved_ips: An array of unique identifiers for the reserved IPs to be scheduled for
              deletion.

          snapshots: An array of unique identifiers for the snapshots to be scheduled for deletion.

          volume_snapshots: An array of unique identifiers for the volume snapshots to be scheduled for
              deletion.

          volumes: An array of unique identifiers for the volumes to be scheduled for deletion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources/selective"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources/selective",
            body=await async_maybe_transform(
                {
                    "floating_ips": floating_ips,
                    "reserved_ips": reserved_ips,
                    "snapshots": snapshots,
                    "volume_snapshots": volume_snapshots,
                    "volumes": volumes,
                },
                destroy_with_associated_resource_delete_selective_params.DestroyWithAssociatedResourceDeleteSelectiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retry(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        If the status of a request to destroy a Droplet with its associated resources
        reported any errors, it can be retried by sending a POST request to the
        `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/retry` endpoint.

        Only one destroy can be active at a time per Droplet. If a retry is issued while
        another destroy is in progress for the Droplet a 409 status code will be
        returned. A successful response will include a 202 response code and no content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v2/droplets/{droplet_id}/destroy_with_associated_resources/retry"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/destroy_with_associated_resources/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DestroyWithAssociatedResourcesResourceWithRawResponse:
    def __init__(self, destroy_with_associated_resources: DestroyWithAssociatedResourcesResource) -> None:
        self._destroy_with_associated_resources = destroy_with_associated_resources

        self.list = to_raw_response_wrapper(
            destroy_with_associated_resources.list,
        )
        self.check_status = to_raw_response_wrapper(
            destroy_with_associated_resources.check_status,
        )
        self.delete_dangerous = to_raw_response_wrapper(
            destroy_with_associated_resources.delete_dangerous,
        )
        self.delete_selective = to_raw_response_wrapper(
            destroy_with_associated_resources.delete_selective,
        )
        self.retry = to_raw_response_wrapper(
            destroy_with_associated_resources.retry,
        )


class AsyncDestroyWithAssociatedResourcesResourceWithRawResponse:
    def __init__(self, destroy_with_associated_resources: AsyncDestroyWithAssociatedResourcesResource) -> None:
        self._destroy_with_associated_resources = destroy_with_associated_resources

        self.list = async_to_raw_response_wrapper(
            destroy_with_associated_resources.list,
        )
        self.check_status = async_to_raw_response_wrapper(
            destroy_with_associated_resources.check_status,
        )
        self.delete_dangerous = async_to_raw_response_wrapper(
            destroy_with_associated_resources.delete_dangerous,
        )
        self.delete_selective = async_to_raw_response_wrapper(
            destroy_with_associated_resources.delete_selective,
        )
        self.retry = async_to_raw_response_wrapper(
            destroy_with_associated_resources.retry,
        )


class DestroyWithAssociatedResourcesResourceWithStreamingResponse:
    def __init__(self, destroy_with_associated_resources: DestroyWithAssociatedResourcesResource) -> None:
        self._destroy_with_associated_resources = destroy_with_associated_resources

        self.list = to_streamed_response_wrapper(
            destroy_with_associated_resources.list,
        )
        self.check_status = to_streamed_response_wrapper(
            destroy_with_associated_resources.check_status,
        )
        self.delete_dangerous = to_streamed_response_wrapper(
            destroy_with_associated_resources.delete_dangerous,
        )
        self.delete_selective = to_streamed_response_wrapper(
            destroy_with_associated_resources.delete_selective,
        )
        self.retry = to_streamed_response_wrapper(
            destroy_with_associated_resources.retry,
        )


class AsyncDestroyWithAssociatedResourcesResourceWithStreamingResponse:
    def __init__(self, destroy_with_associated_resources: AsyncDestroyWithAssociatedResourcesResource) -> None:
        self._destroy_with_associated_resources = destroy_with_associated_resources

        self.list = async_to_streamed_response_wrapper(
            destroy_with_associated_resources.list,
        )
        self.check_status = async_to_streamed_response_wrapper(
            destroy_with_associated_resources.check_status,
        )
        self.delete_dangerous = async_to_streamed_response_wrapper(
            destroy_with_associated_resources.delete_dangerous,
        )
        self.delete_selective = async_to_streamed_response_wrapper(
            destroy_with_associated_resources.delete_selective,
        )
        self.retry = async_to_streamed_response_wrapper(
            destroy_with_associated_resources.retry,
        )
