# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ...types import nf_list_params, nf_create_params, nf_delete_params, nf_retrieve_params, nf_initiate_action_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .snapshots import (
    SnapshotsResource,
    AsyncSnapshotsResource,
    SnapshotsResourceWithRawResponse,
    AsyncSnapshotsResourceWithRawResponse,
    SnapshotsResourceWithStreamingResponse,
    AsyncSnapshotsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.nf_list_response import NfListResponse
from ...types.nf_create_response import NfCreateResponse
from ...types.nf_retrieve_response import NfRetrieveResponse
from ...types.nf_initiate_action_response import NfInitiateActionResponse

__all__ = ["NfsResource", "AsyncNfsResource"]


class NfsResource(SyncAPIResource):
    @cached_property
    def snapshots(self) -> SnapshotsResource:
        return SnapshotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return NfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return NfsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        region: str,
        size_gib: int,
        vpc_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfCreateResponse:
        """
        To create a new NFS share, send a POST request to `/v2/nfs`.

        Args:
          name: The human-readable name of the share.

          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          size_gib: The desired/provisioned size of the share in GiB (Gibibytes). Must be >= 50.

          vpc_ids: List of VPC IDs that should be able to access the share.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/nfs" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/nfs",
            body=maybe_transform(
                {
                    "name": name,
                    "region": region,
                    "size_gib": size_gib,
                    "vpc_ids": vpc_ids,
                },
                nf_create_params.NfCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NfCreateResponse,
        )

    def retrieve(
        self,
        nfs_id: str,
        *,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfRetrieveResponse:
        """
        To get an NFS share, send a GET request to `/v2/nfs/{nfs_id}?region=${region}`.

        A successful request will return the NFS share.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nfs_id:
            raise ValueError(f"Expected a non-empty value for `nfs_id` but received {nfs_id!r}")
        return self._get(
            f"/v2/nfs/{nfs_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/{nfs_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, nf_retrieve_params.NfRetrieveParams),
            ),
            cast_to=NfRetrieveResponse,
        )

    def list(
        self,
        *,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfListResponse:
        """
        To list NFS shares, send a GET request to `/v2/nfs?region=${region}`.

        A successful request will return all NFS shares belonging to the authenticated
        user.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/nfs" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/nfs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, nf_list_params.NfListParams),
            ),
            cast_to=NfListResponse,
        )

    def delete(
        self,
        nfs_id: str,
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
        To delete an NFS share, send a DELETE request to
        `/v2/nfs/{nfs_id}?region=${region}`.

        A successful request will return a `204 No Content` status code.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nfs_id:
            raise ValueError(f"Expected a non-empty value for `nfs_id` but received {nfs_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/nfs/{nfs_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/{nfs_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, nf_delete_params.NfDeleteParams),
            ),
            cast_to=NoneType,
        )

    @overload
    def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionResizeParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        """
        To execute an action (such as resize) on a specified NFS share, send a POST
        request to `/v2/nfs/{nfs_id}/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                  | Details                                                                          |
        | ----------------------- | -------------------------------------------------------------------------------- |
        | <nobr>`resize`</nobr>   | Resizes an NFS share. Set the size_gib attribute to a desired value in GiB       |
        | <nobr>`snapshot`</nobr> | Takes a snapshot of an NFS share                                                 |
        | <nobr>`attach`</nobr>   | Attaches an NFS share to a VPC. Set the vpc_id attribute to the desired VPC ID   |
        | <nobr>`detach`</nobr>   | Detaches an NFS share from a VPC. Set the vpc_id attribute to the desired VPC ID |

        Args:
          region: The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides.

          type: The type of action to initiate for the NFS share (such as resize or snapshot).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionSnapshotParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        """
        To execute an action (such as resize) on a specified NFS share, send a POST
        request to `/v2/nfs/{nfs_id}/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                  | Details                                                                          |
        | ----------------------- | -------------------------------------------------------------------------------- |
        | <nobr>`resize`</nobr>   | Resizes an NFS share. Set the size_gib attribute to a desired value in GiB       |
        | <nobr>`snapshot`</nobr> | Takes a snapshot of an NFS share                                                 |
        | <nobr>`attach`</nobr>   | Attaches an NFS share to a VPC. Set the vpc_id attribute to the desired VPC ID   |
        | <nobr>`detach`</nobr>   | Detaches an NFS share from a VPC. Set the vpc_id attribute to the desired VPC ID |

        Args:
          region: The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides.

          type: The type of action to initiate for the NFS share (such as resize or snapshot).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionAttachParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        """
        To execute an action (such as resize) on a specified NFS share, send a POST
        request to `/v2/nfs/{nfs_id}/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                  | Details                                                                          |
        | ----------------------- | -------------------------------------------------------------------------------- |
        | <nobr>`resize`</nobr>   | Resizes an NFS share. Set the size_gib attribute to a desired value in GiB       |
        | <nobr>`snapshot`</nobr> | Takes a snapshot of an NFS share                                                 |
        | <nobr>`attach`</nobr>   | Attaches an NFS share to a VPC. Set the vpc_id attribute to the desired VPC ID   |
        | <nobr>`detach`</nobr>   | Detaches an NFS share from a VPC. Set the vpc_id attribute to the desired VPC ID |

        Args:
          region: The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides.

          type: The type of action to initiate for the NFS share (such as resize or snapshot).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionDetachParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        """
        To execute an action (such as resize) on a specified NFS share, send a POST
        request to `/v2/nfs/{nfs_id}/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                  | Details                                                                          |
        | ----------------------- | -------------------------------------------------------------------------------- |
        | <nobr>`resize`</nobr>   | Resizes an NFS share. Set the size_gib attribute to a desired value in GiB       |
        | <nobr>`snapshot`</nobr> | Takes a snapshot of an NFS share                                                 |
        | <nobr>`attach`</nobr>   | Attaches an NFS share to a VPC. Set the vpc_id attribute to the desired VPC ID   |
        | <nobr>`detach`</nobr>   | Detaches an NFS share from a VPC. Set the vpc_id attribute to the desired VPC ID |

        Args:
          region: The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides.

          type: The type of action to initiate for the NFS share (such as resize or snapshot).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["region", "type"])
    def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionResizeParams
        | nf_initiate_action_params.NfsActionSnapshotParams
        | nf_initiate_action_params.NfsActionAttachParams
        | nf_initiate_action_params.NfsActionDetachParams
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        if not nfs_id:
            raise ValueError(f"Expected a non-empty value for `nfs_id` but received {nfs_id!r}")
        return self._post(
            f"/v2/nfs/{nfs_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/{nfs_id}/actions",
            body=maybe_transform(
                {
                    "region": region,
                    "type": type,
                    "params": params,
                },
                nf_initiate_action_params.NfInitiateActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NfInitiateActionResponse,
        )


class AsyncNfsResource(AsyncAPIResource):
    @cached_property
    def snapshots(self) -> AsyncSnapshotsResource:
        return AsyncSnapshotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncNfsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        region: str,
        size_gib: int,
        vpc_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfCreateResponse:
        """
        To create a new NFS share, send a POST request to `/v2/nfs`.

        Args:
          name: The human-readable name of the share.

          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          size_gib: The desired/provisioned size of the share in GiB (Gibibytes). Must be >= 50.

          vpc_ids: List of VPC IDs that should be able to access the share.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/nfs" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/nfs",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "region": region,
                    "size_gib": size_gib,
                    "vpc_ids": vpc_ids,
                },
                nf_create_params.NfCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NfCreateResponse,
        )

    async def retrieve(
        self,
        nfs_id: str,
        *,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfRetrieveResponse:
        """
        To get an NFS share, send a GET request to `/v2/nfs/{nfs_id}?region=${region}`.

        A successful request will return the NFS share.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nfs_id:
            raise ValueError(f"Expected a non-empty value for `nfs_id` but received {nfs_id!r}")
        return await self._get(
            f"/v2/nfs/{nfs_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/{nfs_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, nf_retrieve_params.NfRetrieveParams),
            ),
            cast_to=NfRetrieveResponse,
        )

    async def list(
        self,
        *,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfListResponse:
        """
        To list NFS shares, send a GET request to `/v2/nfs?region=${region}`.

        A successful request will return all NFS shares belonging to the authenticated
        user.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/nfs" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/nfs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, nf_list_params.NfListParams),
            ),
            cast_to=NfListResponse,
        )

    async def delete(
        self,
        nfs_id: str,
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
        To delete an NFS share, send a DELETE request to
        `/v2/nfs/{nfs_id}?region=${region}`.

        A successful request will return a `204 No Content` status code.

        Args:
          region: The DigitalOcean region slug (e.g., nyc2, atl1) where the NFS share resides.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not nfs_id:
            raise ValueError(f"Expected a non-empty value for `nfs_id` but received {nfs_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/nfs/{nfs_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/{nfs_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, nf_delete_params.NfDeleteParams),
            ),
            cast_to=NoneType,
        )

    @overload
    async def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionResizeParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        """
        To execute an action (such as resize) on a specified NFS share, send a POST
        request to `/v2/nfs/{nfs_id}/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                  | Details                                                                          |
        | ----------------------- | -------------------------------------------------------------------------------- |
        | <nobr>`resize`</nobr>   | Resizes an NFS share. Set the size_gib attribute to a desired value in GiB       |
        | <nobr>`snapshot`</nobr> | Takes a snapshot of an NFS share                                                 |
        | <nobr>`attach`</nobr>   | Attaches an NFS share to a VPC. Set the vpc_id attribute to the desired VPC ID   |
        | <nobr>`detach`</nobr>   | Detaches an NFS share from a VPC. Set the vpc_id attribute to the desired VPC ID |

        Args:
          region: The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides.

          type: The type of action to initiate for the NFS share (such as resize or snapshot).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionSnapshotParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        """
        To execute an action (such as resize) on a specified NFS share, send a POST
        request to `/v2/nfs/{nfs_id}/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                  | Details                                                                          |
        | ----------------------- | -------------------------------------------------------------------------------- |
        | <nobr>`resize`</nobr>   | Resizes an NFS share. Set the size_gib attribute to a desired value in GiB       |
        | <nobr>`snapshot`</nobr> | Takes a snapshot of an NFS share                                                 |
        | <nobr>`attach`</nobr>   | Attaches an NFS share to a VPC. Set the vpc_id attribute to the desired VPC ID   |
        | <nobr>`detach`</nobr>   | Detaches an NFS share from a VPC. Set the vpc_id attribute to the desired VPC ID |

        Args:
          region: The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides.

          type: The type of action to initiate for the NFS share (such as resize or snapshot).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionAttachParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        """
        To execute an action (such as resize) on a specified NFS share, send a POST
        request to `/v2/nfs/{nfs_id}/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                  | Details                                                                          |
        | ----------------------- | -------------------------------------------------------------------------------- |
        | <nobr>`resize`</nobr>   | Resizes an NFS share. Set the size_gib attribute to a desired value in GiB       |
        | <nobr>`snapshot`</nobr> | Takes a snapshot of an NFS share                                                 |
        | <nobr>`attach`</nobr>   | Attaches an NFS share to a VPC. Set the vpc_id attribute to the desired VPC ID   |
        | <nobr>`detach`</nobr>   | Detaches an NFS share from a VPC. Set the vpc_id attribute to the desired VPC ID |

        Args:
          region: The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides.

          type: The type of action to initiate for the NFS share (such as resize or snapshot).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionDetachParams | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        """
        To execute an action (such as resize) on a specified NFS share, send a POST
        request to `/v2/nfs/{nfs_id}/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                  | Details                                                                          |
        | ----------------------- | -------------------------------------------------------------------------------- |
        | <nobr>`resize`</nobr>   | Resizes an NFS share. Set the size_gib attribute to a desired value in GiB       |
        | <nobr>`snapshot`</nobr> | Takes a snapshot of an NFS share                                                 |
        | <nobr>`attach`</nobr>   | Attaches an NFS share to a VPC. Set the vpc_id attribute to the desired VPC ID   |
        | <nobr>`detach`</nobr>   | Detaches an NFS share from a VPC. Set the vpc_id attribute to the desired VPC ID |

        Args:
          region: The DigitalOcean region slug (e.g. atl1, nyc2) where the NFS snapshot resides.

          type: The type of action to initiate for the NFS share (such as resize or snapshot).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["region", "type"])
    async def initiate_action(
        self,
        nfs_id: str,
        *,
        region: str,
        type: Literal["resize", "snapshot"],
        params: nf_initiate_action_params.NfsActionResizeParams
        | nf_initiate_action_params.NfsActionSnapshotParams
        | nf_initiate_action_params.NfsActionAttachParams
        | nf_initiate_action_params.NfsActionDetachParams
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NfInitiateActionResponse:
        if not nfs_id:
            raise ValueError(f"Expected a non-empty value for `nfs_id` but received {nfs_id!r}")
        return await self._post(
            f"/v2/nfs/{nfs_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/nfs/{nfs_id}/actions",
            body=await async_maybe_transform(
                {
                    "region": region,
                    "type": type,
                    "params": params,
                },
                nf_initiate_action_params.NfInitiateActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NfInitiateActionResponse,
        )


class NfsResourceWithRawResponse:
    def __init__(self, nfs: NfsResource) -> None:
        self._nfs = nfs

        self.create = to_raw_response_wrapper(
            nfs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            nfs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            nfs.list,
        )
        self.delete = to_raw_response_wrapper(
            nfs.delete,
        )
        self.initiate_action = to_raw_response_wrapper(
            nfs.initiate_action,
        )

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithRawResponse:
        return SnapshotsResourceWithRawResponse(self._nfs.snapshots)


class AsyncNfsResourceWithRawResponse:
    def __init__(self, nfs: AsyncNfsResource) -> None:
        self._nfs = nfs

        self.create = async_to_raw_response_wrapper(
            nfs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            nfs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            nfs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            nfs.delete,
        )
        self.initiate_action = async_to_raw_response_wrapper(
            nfs.initiate_action,
        )

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithRawResponse:
        return AsyncSnapshotsResourceWithRawResponse(self._nfs.snapshots)


class NfsResourceWithStreamingResponse:
    def __init__(self, nfs: NfsResource) -> None:
        self._nfs = nfs

        self.create = to_streamed_response_wrapper(
            nfs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            nfs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            nfs.list,
        )
        self.delete = to_streamed_response_wrapper(
            nfs.delete,
        )
        self.initiate_action = to_streamed_response_wrapper(
            nfs.initiate_action,
        )

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithStreamingResponse:
        return SnapshotsResourceWithStreamingResponse(self._nfs.snapshots)


class AsyncNfsResourceWithStreamingResponse:
    def __init__(self, nfs: AsyncNfsResource) -> None:
        self._nfs = nfs

        self.create = async_to_streamed_response_wrapper(
            nfs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            nfs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            nfs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            nfs.delete,
        )
        self.initiate_action = async_to_streamed_response_wrapper(
            nfs.initiate_action,
        )

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        return AsyncSnapshotsResourceWithStreamingResponse(self._nfs.snapshots)
