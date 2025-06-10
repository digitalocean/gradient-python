# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.organization import admin_api_key_list_params, admin_api_key_create_params
from ...types.organization.admin_api_key import AdminAPIKey
from ...types.organization.admin_api_key_list_response import AdminAPIKeyListResponse
from ...types.organization.admin_api_key_delete_response import AdminAPIKeyDeleteResponse

__all__ = ["AdminAPIKeysResource", "AsyncAdminAPIKeysResource"]


class AdminAPIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdminAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#accessing-raw-response-data-eg-headers
        """
        return AdminAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#with_streaming_response
        """
        return AdminAPIKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminAPIKey:
        """
        Create a new admin-level API key for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organization/admin_api_keys",
            body=maybe_transform({"name": name}, admin_api_key_create_params.AdminAPIKeyCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminAPIKey,
        )

    def retrieve(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminAPIKey:
        """
        Get details for a specific organization API key by its ID.

        Args:
          key_id: The ID of the API key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._get(
            f"/organization/admin_api_keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminAPIKey,
        )

    def list(
        self,
        *,
        after: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminAPIKeyListResponse:
        """
        Retrieve a paginated list of organization admin API keys.

        Args:
          after: Return keys with IDs that come after this ID in the pagination order.

          limit: Maximum number of keys to return.

          order: Order results by creation time, ascending or descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/admin_api_keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "order": order,
                    },
                    admin_api_key_list_params.AdminAPIKeyListParams,
                ),
            ),
            cast_to=AdminAPIKeyListResponse,
        )

    def delete(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminAPIKeyDeleteResponse:
        """
        Delete the specified admin API key.

        Args:
          key_id: The ID of the API key to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._delete(
            f"/organization/admin_api_keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminAPIKeyDeleteResponse,
        )


class AsyncAdminAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdminAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#with_streaming_response
        """
        return AsyncAdminAPIKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminAPIKey:
        """
        Create a new admin-level API key for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organization/admin_api_keys",
            body=await async_maybe_transform({"name": name}, admin_api_key_create_params.AdminAPIKeyCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminAPIKey,
        )

    async def retrieve(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminAPIKey:
        """
        Get details for a specific organization API key by its ID.

        Args:
          key_id: The ID of the API key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._get(
            f"/organization/admin_api_keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminAPIKey,
        )

    async def list(
        self,
        *,
        after: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminAPIKeyListResponse:
        """
        Retrieve a paginated list of organization admin API keys.

        Args:
          after: Return keys with IDs that come after this ID in the pagination order.

          limit: Maximum number of keys to return.

          order: Order results by creation time, ascending or descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/admin_api_keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "order": order,
                    },
                    admin_api_key_list_params.AdminAPIKeyListParams,
                ),
            ),
            cast_to=AdminAPIKeyListResponse,
        )

    async def delete(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminAPIKeyDeleteResponse:
        """
        Delete the specified admin API key.

        Args:
          key_id: The ID of the API key to be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._delete(
            f"/organization/admin_api_keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminAPIKeyDeleteResponse,
        )


class AdminAPIKeysResourceWithRawResponse:
    def __init__(self, admin_api_keys: AdminAPIKeysResource) -> None:
        self._admin_api_keys = admin_api_keys

        self.create = to_raw_response_wrapper(
            admin_api_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            admin_api_keys.retrieve,
        )
        self.list = to_raw_response_wrapper(
            admin_api_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            admin_api_keys.delete,
        )


class AsyncAdminAPIKeysResourceWithRawResponse:
    def __init__(self, admin_api_keys: AsyncAdminAPIKeysResource) -> None:
        self._admin_api_keys = admin_api_keys

        self.create = async_to_raw_response_wrapper(
            admin_api_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            admin_api_keys.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            admin_api_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            admin_api_keys.delete,
        )


class AdminAPIKeysResourceWithStreamingResponse:
    def __init__(self, admin_api_keys: AdminAPIKeysResource) -> None:
        self._admin_api_keys = admin_api_keys

        self.create = to_streamed_response_wrapper(
            admin_api_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            admin_api_keys.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            admin_api_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            admin_api_keys.delete,
        )


class AsyncAdminAPIKeysResourceWithStreamingResponse:
    def __init__(self, admin_api_keys: AsyncAdminAPIKeysResource) -> None:
        self._admin_api_keys = admin_api_keys

        self.create = async_to_streamed_response_wrapper(
            admin_api_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            admin_api_keys.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            admin_api_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            admin_api_keys.delete,
        )
