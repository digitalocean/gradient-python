# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.fine_tuning.checkpoints import permission_create_params, permission_retrieve_params
from ....types.fine_tuning.checkpoints.permission_delete_response import PermissionDeleteResponse
from ....types.fine_tuning.checkpoints.list_fine_tuning_checkpoint_permission import ListFineTuningCheckpointPermission

__all__ = ["PermissionsResource", "AsyncPermissionsResource"]


class PermissionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return PermissionsResourceWithStreamingResponse(self)

    def create(
        self,
        permission_id: str,
        *,
        project_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFineTuningCheckpointPermission:
        """
        **NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

        This enables organization owners to share fine-tuned models with other projects
        in their organization.

        Args:
          project_ids: The project identifiers to grant access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return self._post(
            f"/fine_tuning/checkpoints/{permission_id}/permissions",
            body=maybe_transform({"project_ids": project_ids}, permission_create_params.PermissionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListFineTuningCheckpointPermission,
        )

    def retrieve(
        self,
        permission_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["ascending", "descending"] | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFineTuningCheckpointPermission:
        """
        **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

        Organization owners can use this endpoint to view all permissions for a
        fine-tuned model checkpoint.

        Args:
          after: Identifier for the last permission ID from the previous pagination request.

          limit: Number of permissions to retrieve.

          order: The order in which to retrieve permissions.

          project_id: The ID of the project to get permissions for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return self._get(
            f"/fine_tuning/checkpoints/{permission_id}/permissions",
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
                        "project_id": project_id,
                    },
                    permission_retrieve_params.PermissionRetrieveParams,
                ),
            ),
            cast_to=ListFineTuningCheckpointPermission,
        )

    def delete(
        self,
        permission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PermissionDeleteResponse:
        """
        **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

        Organization owners can use this endpoint to delete a permission for a
        fine-tuned model checkpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return self._delete(
            f"/fine_tuning/checkpoints/{permission_id}/permissions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionDeleteResponse,
        )


class AsyncPermissionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return AsyncPermissionsResourceWithStreamingResponse(self)

    async def create(
        self,
        permission_id: str,
        *,
        project_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFineTuningCheckpointPermission:
        """
        **NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

        This enables organization owners to share fine-tuned models with other projects
        in their organization.

        Args:
          project_ids: The project identifiers to grant access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return await self._post(
            f"/fine_tuning/checkpoints/{permission_id}/permissions",
            body=await async_maybe_transform(
                {"project_ids": project_ids}, permission_create_params.PermissionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListFineTuningCheckpointPermission,
        )

    async def retrieve(
        self,
        permission_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["ascending", "descending"] | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFineTuningCheckpointPermission:
        """
        **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

        Organization owners can use this endpoint to view all permissions for a
        fine-tuned model checkpoint.

        Args:
          after: Identifier for the last permission ID from the previous pagination request.

          limit: Number of permissions to retrieve.

          order: The order in which to retrieve permissions.

          project_id: The ID of the project to get permissions for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return await self._get(
            f"/fine_tuning/checkpoints/{permission_id}/permissions",
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
                        "project_id": project_id,
                    },
                    permission_retrieve_params.PermissionRetrieveParams,
                ),
            ),
            cast_to=ListFineTuningCheckpointPermission,
        )

    async def delete(
        self,
        permission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PermissionDeleteResponse:
        """
        **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

        Organization owners can use this endpoint to delete a permission for a
        fine-tuned model checkpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return await self._delete(
            f"/fine_tuning/checkpoints/{permission_id}/permissions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionDeleteResponse,
        )


class PermissionsResourceWithRawResponse:
    def __init__(self, permissions: PermissionsResource) -> None:
        self._permissions = permissions

        self.create = to_raw_response_wrapper(
            permissions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            permissions.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            permissions.delete,
        )


class AsyncPermissionsResourceWithRawResponse:
    def __init__(self, permissions: AsyncPermissionsResource) -> None:
        self._permissions = permissions

        self.create = async_to_raw_response_wrapper(
            permissions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            permissions.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            permissions.delete,
        )


class PermissionsResourceWithStreamingResponse:
    def __init__(self, permissions: PermissionsResource) -> None:
        self._permissions = permissions

        self.create = to_streamed_response_wrapper(
            permissions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            permissions.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            permissions.delete,
        )


class AsyncPermissionsResourceWithStreamingResponse:
    def __init__(self, permissions: AsyncPermissionsResource) -> None:
        self._permissions = permissions

        self.create = async_to_streamed_response_wrapper(
            permissions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            permissions.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            permissions.delete,
        )
