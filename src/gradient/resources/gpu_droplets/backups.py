# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.gpu_droplets import backup_list_params, backup_list_policies_params
from ...types.gpu_droplets.backup_list_response import BackupListResponse
from ...types.gpu_droplets.backup_list_policies_response import BackupListPoliciesResponse
from ...types.gpu_droplets.backup_retrieve_policy_response import BackupRetrievePolicyResponse
from ...types.gpu_droplets.backup_list_supported_policies_response import BackupListSupportedPoliciesResponse

__all__ = ["BackupsResource", "AsyncBackupsResource"]


class BackupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BackupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return BackupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BackupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return BackupsResourceWithStreamingResponse(self)

    def list(
        self,
        droplet_id: int,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackupListResponse:
        """
        To retrieve any backups associated with a Droplet, send a GET request to
        `/v2/droplets/$DROPLET_ID/backups`.

        You will get back a JSON object that has a `backups` key. This will be set to an
        array of backup objects, each of which contain the standard Droplet backup
        attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/backups"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/backups",
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
                    backup_list_params.BackupListParams,
                ),
            ),
            cast_to=BackupListResponse,
        )

    def list_policies(
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
    ) -> BackupListPoliciesResponse:
        """
        To list information about the backup policies for all Droplets in the account,
        send a GET request to `/v2/droplets/backups/policies`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/droplets/backups/policies"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/backups/policies",
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
                    backup_list_policies_params.BackupListPoliciesParams,
                ),
            ),
            cast_to=BackupListPoliciesResponse,
        )

    def list_supported_policies(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackupListSupportedPoliciesResponse:
        """
        To retrieve a list of all supported Droplet backup policies, send a GET request
        to `/v2/droplets/backups/supported_policies`.
        """
        return self._get(
            "/v2/droplets/backups/supported_policies"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/backups/supported_policies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BackupListSupportedPoliciesResponse,
        )

    def retrieve_policy(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackupRetrievePolicyResponse:
        """
        To show information about an individual Droplet's backup policy, send a GET
        request to `/v2/droplets/$DROPLET_ID/backups/policy`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/backups/policy"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/backups/policy",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BackupRetrievePolicyResponse,
        )


class AsyncBackupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBackupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBackupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBackupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncBackupsResourceWithStreamingResponse(self)

    async def list(
        self,
        droplet_id: int,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackupListResponse:
        """
        To retrieve any backups associated with a Droplet, send a GET request to
        `/v2/droplets/$DROPLET_ID/backups`.

        You will get back a JSON object that has a `backups` key. This will be set to an
        array of backup objects, each of which contain the standard Droplet backup
        attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/backups"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/backups",
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
                    backup_list_params.BackupListParams,
                ),
            ),
            cast_to=BackupListResponse,
        )

    async def list_policies(
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
    ) -> BackupListPoliciesResponse:
        """
        To list information about the backup policies for all Droplets in the account,
        send a GET request to `/v2/droplets/backups/policies`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/droplets/backups/policies"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/backups/policies",
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
                    backup_list_policies_params.BackupListPoliciesParams,
                ),
            ),
            cast_to=BackupListPoliciesResponse,
        )

    async def list_supported_policies(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackupListSupportedPoliciesResponse:
        """
        To retrieve a list of all supported Droplet backup policies, send a GET request
        to `/v2/droplets/backups/supported_policies`.
        """
        return await self._get(
            "/v2/droplets/backups/supported_policies"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/backups/supported_policies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BackupListSupportedPoliciesResponse,
        )

    async def retrieve_policy(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackupRetrievePolicyResponse:
        """
        To show information about an individual Droplet's backup policy, send a GET
        request to `/v2/droplets/$DROPLET_ID/backups/policy`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/backups/policy"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/backups/policy",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BackupRetrievePolicyResponse,
        )


class BackupsResourceWithRawResponse:
    def __init__(self, backups: BackupsResource) -> None:
        self._backups = backups

        self.list = to_raw_response_wrapper(
            backups.list,
        )
        self.list_policies = to_raw_response_wrapper(
            backups.list_policies,
        )
        self.list_supported_policies = to_raw_response_wrapper(
            backups.list_supported_policies,
        )
        self.retrieve_policy = to_raw_response_wrapper(
            backups.retrieve_policy,
        )


class AsyncBackupsResourceWithRawResponse:
    def __init__(self, backups: AsyncBackupsResource) -> None:
        self._backups = backups

        self.list = async_to_raw_response_wrapper(
            backups.list,
        )
        self.list_policies = async_to_raw_response_wrapper(
            backups.list_policies,
        )
        self.list_supported_policies = async_to_raw_response_wrapper(
            backups.list_supported_policies,
        )
        self.retrieve_policy = async_to_raw_response_wrapper(
            backups.retrieve_policy,
        )


class BackupsResourceWithStreamingResponse:
    def __init__(self, backups: BackupsResource) -> None:
        self._backups = backups

        self.list = to_streamed_response_wrapper(
            backups.list,
        )
        self.list_policies = to_streamed_response_wrapper(
            backups.list_policies,
        )
        self.list_supported_policies = to_streamed_response_wrapper(
            backups.list_supported_policies,
        )
        self.retrieve_policy = to_streamed_response_wrapper(
            backups.retrieve_policy,
        )


class AsyncBackupsResourceWithStreamingResponse:
    def __init__(self, backups: AsyncBackupsResource) -> None:
        self._backups = backups

        self.list = async_to_streamed_response_wrapper(
            backups.list,
        )
        self.list_policies = async_to_streamed_response_wrapper(
            backups.list_policies,
        )
        self.list_supported_policies = async_to_streamed_response_wrapper(
            backups.list_supported_policies,
        )
        self.retrieve_policy = async_to_streamed_response_wrapper(
            backups.retrieve_policy,
        )
