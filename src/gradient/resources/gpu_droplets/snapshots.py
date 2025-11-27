# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.gpu_droplets import snapshot_list_params
from ...types.gpu_droplets.snapshot_list_response import SnapshotListResponse
from ...types.gpu_droplets.snapshot_retrieve_response import SnapshotRetrieveResponse

__all__ = ["SnapshotsResource", "AsyncSnapshotsResource"]


class SnapshotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SnapshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return SnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return SnapshotsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        snapshot_id: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotRetrieveResponse:
        """
        To retrieve information about a snapshot, send a GET request to
        `/v2/snapshots/$SNAPSHOT_ID`.

        The response will be a JSON object with a key called `snapshot`. The value of
        this will be an snapshot object containing the standard snapshot attributes.

        Args:
          snapshot_id: The ID of a Droplet snapshot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/snapshots/{snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/snapshots/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        resource_type: Literal["droplet", "volume"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """
        To list all of the snapshots available on your account, send a GET request to
        `/v2/snapshots`.

        The response will be a JSON object with a key called `snapshots`. This will be
        set to an array of `snapshot` objects, each of which will contain the standard
        snapshot attributes.

        ### Filtering Results by Resource Type

        It's possible to request filtered results by including certain query parameters.

        #### List Droplet Snapshots

        To retrieve only snapshots based on Droplets, include the `resource_type` query
        parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.

        #### List Volume Snapshots

        To retrieve only snapshots based on volumes, include the `resource_type` query
        parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          resource_type: Used to filter snapshots by a resource type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/snapshots" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/snapshots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "resource_type": resource_type,
                    },
                    snapshot_list_params.SnapshotListParams,
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    def delete(
        self,
        snapshot_id: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Both Droplet and volume snapshots are managed through the `/v2/snapshots/`
        endpoint. To delete a snapshot, send a DELETE request to
        `/v2/snapshots/$SNAPSHOT_ID`.

        A status of 204 will be given. This indicates that the request was processed
        successfully, but that no response body is needed.

        Args:
          snapshot_id: The ID of a Droplet snapshot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/snapshots/{snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/snapshots/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSnapshotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSnapshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncSnapshotsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        snapshot_id: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotRetrieveResponse:
        """
        To retrieve information about a snapshot, send a GET request to
        `/v2/snapshots/$SNAPSHOT_ID`.

        The response will be a JSON object with a key called `snapshot`. The value of
        this will be an snapshot object containing the standard snapshot attributes.

        Args:
          snapshot_id: The ID of a Droplet snapshot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/snapshots/{snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/snapshots/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        resource_type: Literal["droplet", "volume"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """
        To list all of the snapshots available on your account, send a GET request to
        `/v2/snapshots`.

        The response will be a JSON object with a key called `snapshots`. This will be
        set to an array of `snapshot` objects, each of which will contain the standard
        snapshot attributes.

        ### Filtering Results by Resource Type

        It's possible to request filtered results by including certain query parameters.

        #### List Droplet Snapshots

        To retrieve only snapshots based on Droplets, include the `resource_type` query
        parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.

        #### List Volume Snapshots

        To retrieve only snapshots based on volumes, include the `resource_type` query
        parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          resource_type: Used to filter snapshots by a resource type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/snapshots" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/snapshots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "resource_type": resource_type,
                    },
                    snapshot_list_params.SnapshotListParams,
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    async def delete(
        self,
        snapshot_id: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Both Droplet and volume snapshots are managed through the `/v2/snapshots/`
        endpoint. To delete a snapshot, send a DELETE request to
        `/v2/snapshots/$SNAPSHOT_ID`.

        A status of 204 will be given. This indicates that the request was processed
        successfully, but that no response body is needed.

        Args:
          snapshot_id: The ID of a Droplet snapshot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/snapshots/{snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/snapshots/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.retrieve = to_raw_response_wrapper(
            snapshots.retrieve,
        )
        self.list = to_raw_response_wrapper(
            snapshots.list,
        )
        self.delete = to_raw_response_wrapper(
            snapshots.delete,
        )


class AsyncSnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.retrieve = async_to_raw_response_wrapper(
            snapshots.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            snapshots.list,
        )
        self.delete = async_to_raw_response_wrapper(
            snapshots.delete,
        )


class SnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.retrieve = to_streamed_response_wrapper(
            snapshots.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            snapshots.list,
        )
        self.delete = to_streamed_response_wrapper(
            snapshots.delete,
        )


class AsyncSnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.retrieve = async_to_streamed_response_wrapper(
            snapshots.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            snapshots.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            snapshots.delete,
        )
