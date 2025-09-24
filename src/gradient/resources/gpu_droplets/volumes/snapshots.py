# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.gpu_droplets.volumes import snapshot_list_params, snapshot_create_params
from ....types.gpu_droplets.volumes.snapshot_list_response import SnapshotListResponse
from ....types.gpu_droplets.volumes.snapshot_create_response import SnapshotCreateResponse
from ....types.gpu_droplets.volumes.snapshot_retrieve_response import SnapshotRetrieveResponse

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

    def create(
        self,
        volume_id: str,
        *,
        name: str,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotCreateResponse:
        """
        To create a snapshot from a volume, sent a POST request to
        `/v2/volumes/$VOLUME_ID/snapshots`.

        Args:
          name: A human-readable name for the volume snapshot.

          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              may be for either existing or new tags.

              Requires `tag:create` scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._post(
            f"/v2/volumes/{volume_id}/snapshots"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/snapshots",
            body=maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                snapshot_create_params.SnapshotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotCreateResponse,
        )

    def retrieve(
        self,
        snapshot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotRetrieveResponse:
        """
        To retrieve the details of a snapshot that has been created from a volume, send
        a GET request to `/v2/volumes/snapshots/$VOLUME_SNAPSHOT_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._get(
            f"/v2/volumes/snapshots/{snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/snapshots/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotRetrieveResponse,
        )

    def list(
        self,
        volume_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """
        To retrieve the snapshots that have been created from a volume, send a GET
        request to `/v2/volumes/$VOLUME_ID/snapshots`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._get(
            f"/v2/volumes/{volume_id}/snapshots"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/snapshots",
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
                    snapshot_list_params.SnapshotListParams,
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    def delete(
        self,
        snapshot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a volume snapshot, send a DELETE request to
        `/v2/volumes/snapshots/$VOLUME_SNAPSHOT_ID`.

        A status of 204 will be given. This indicates that the request was processed
        successfully, but that no response body is needed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/volumes/snapshots/{snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/snapshots/{snapshot_id}",
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

    async def create(
        self,
        volume_id: str,
        *,
        name: str,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotCreateResponse:
        """
        To create a snapshot from a volume, sent a POST request to
        `/v2/volumes/$VOLUME_ID/snapshots`.

        Args:
          name: A human-readable name for the volume snapshot.

          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              may be for either existing or new tags.

              Requires `tag:create` scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._post(
            f"/v2/volumes/{volume_id}/snapshots"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/snapshots",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                snapshot_create_params.SnapshotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotCreateResponse,
        )

    async def retrieve(
        self,
        snapshot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotRetrieveResponse:
        """
        To retrieve the details of a snapshot that has been created from a volume, send
        a GET request to `/v2/volumes/snapshots/$VOLUME_SNAPSHOT_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._get(
            f"/v2/volumes/snapshots/{snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/snapshots/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotRetrieveResponse,
        )

    async def list(
        self,
        volume_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """
        To retrieve the snapshots that have been created from a volume, send a GET
        request to `/v2/volumes/$VOLUME_ID/snapshots`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._get(
            f"/v2/volumes/{volume_id}/snapshots"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/snapshots",
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
                    snapshot_list_params.SnapshotListParams,
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    async def delete(
        self,
        snapshot_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a volume snapshot, send a DELETE request to
        `/v2/volumes/snapshots/$VOLUME_SNAPSHOT_ID`.

        A status of 204 will be given. This indicates that the request was processed
        successfully, but that no response body is needed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/volumes/snapshots/{snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/snapshots/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.create = to_raw_response_wrapper(
            snapshots.create,
        )
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

        self.create = async_to_raw_response_wrapper(
            snapshots.create,
        )
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

        self.create = to_streamed_response_wrapper(
            snapshots.create,
        )
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

        self.create = async_to_streamed_response_wrapper(
            snapshots.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            snapshots.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            snapshots.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            snapshots.delete,
        )
