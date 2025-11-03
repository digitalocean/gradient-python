# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.nfs import snapshot_list_params, snapshot_delete_params, snapshot_retrieve_params
from ..._base_client import make_request_options
from ...types.nfs.snapshot_list_response import SnapshotListResponse
from ...types.nfs.snapshot_retrieve_response import SnapshotRetrieveResponse

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
        nfs_snapshot_id: str,
        *,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotRetrieveResponse:
        """
        To get an NFS snapshot, send a GET request to
        `/v2/nfs/snapshots/{nfs_snapshot_id}?region=${region}`.

        A successful request will return the NFS snapshot.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nfs_snapshot_id:
            raise ValueError(f"Expected a non-empty value for `nfs_snapshot_id` but received {nfs_snapshot_id!r}")
        return self._get(
            f"/v2/nfs/snapshots/{nfs_snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/snapshots/{nfs_snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, snapshot_retrieve_params.SnapshotRetrieveParams),
            ),
            cast_to=SnapshotRetrieveResponse,
        )

    def list(
        self,
        *,
        region: str,
        share_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """
        To list all NFS snapshots, send a GET request to
        `/v2/nfs/snapshots?region=${region}&share_id={share_id}`.

        A successful request will return all NFS snapshots belonging to the
        authenticated user in the specified region.

        Optionally, you can filter snapshots by a specific NFS share by including the
        `share_id` query parameter.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          share_id: The unique ID of an NFS share. If provided, only snapshots of this specific
              share will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/nfs/snapshots"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/nfs/snapshots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "region": region,
                        "share_id": share_id,
                    },
                    snapshot_list_params.SnapshotListParams,
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    def delete(
        self,
        nfs_snapshot_id: str,
        *,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete an NFS snapshot, send a DELETE request to
        `/v2/nfs/snapshots/{nfs_snapshot_id}?region=${region}`.

        A successful request will return a `204 No Content` status code.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nfs_snapshot_id:
            raise ValueError(f"Expected a non-empty value for `nfs_snapshot_id` but received {nfs_snapshot_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/nfs/snapshots/{nfs_snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/snapshots/{nfs_snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, snapshot_delete_params.SnapshotDeleteParams),
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
        nfs_snapshot_id: str,
        *,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotRetrieveResponse:
        """
        To get an NFS snapshot, send a GET request to
        `/v2/nfs/snapshots/{nfs_snapshot_id}?region=${region}`.

        A successful request will return the NFS snapshot.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nfs_snapshot_id:
            raise ValueError(f"Expected a non-empty value for `nfs_snapshot_id` but received {nfs_snapshot_id!r}")
        return await self._get(
            f"/v2/nfs/snapshots/{nfs_snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/snapshots/{nfs_snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, snapshot_retrieve_params.SnapshotRetrieveParams),
            ),
            cast_to=SnapshotRetrieveResponse,
        )

    async def list(
        self,
        *,
        region: str,
        share_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """
        To list all NFS snapshots, send a GET request to
        `/v2/nfs/snapshots?region=${region}&share_id={share_id}`.

        A successful request will return all NFS snapshots belonging to the
        authenticated user in the specified region.

        Optionally, you can filter snapshots by a specific NFS share by including the
        `share_id` query parameter.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          share_id: The unique ID of an NFS share. If provided, only snapshots of this specific
              share will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/nfs/snapshots"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/nfs/snapshots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "region": region,
                        "share_id": share_id,
                    },
                    snapshot_list_params.SnapshotListParams,
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    async def delete(
        self,
        nfs_snapshot_id: str,
        *,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete an NFS snapshot, send a DELETE request to
        `/v2/nfs/snapshots/{nfs_snapshot_id}?region=${region}`.

        A successful request will return a `204 No Content` status code.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nfs_snapshot_id:
            raise ValueError(f"Expected a non-empty value for `nfs_snapshot_id` but received {nfs_snapshot_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/nfs/snapshots/{nfs_snapshot_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/snapshots/{nfs_snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, snapshot_delete_params.SnapshotDeleteParams),
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
