# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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
from ...types.organization import invite_list_params, invite_create_params
from ...types.organization.invite import Invite
from ...types.organization.invite_list_response import InviteListResponse
from ...types.organization.invite_delete_response import InviteDeleteResponse

__all__ = ["InvitesResource", "AsyncInvitesResource"]


class InvitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#accessing-raw-response-data-eg-headers
        """
        return InvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#with_streaming_response
        """
        return InvitesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        role: Literal["reader", "owner"],
        projects: Iterable[invite_create_params.Project] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invite:
        """Create an invite for a user to the organization.

        The invite must be accepted by
        the user before they have access to the organization.

        Args:
          email: Send an email to this address

          role: `owner` or `reader`

          projects: An array of projects to which membership is granted at the same time the org
              invite is accepted. If omitted, the user will be invited to the default project
              for compatibility with legacy behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organization/invites",
            body=maybe_transform(
                {
                    "email": email,
                    "role": role,
                    "projects": projects,
                },
                invite_create_params.InviteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invite,
        )

    def retrieve(
        self,
        invite_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invite:
        """
        Retrieves an invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return self._get(
            f"/organization/invites/{invite_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invite,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteListResponse:
        """
        Returns a list of invites in the organization.

        Args:
          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/invites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    invite_list_params.InviteListParams,
                ),
            ),
            cast_to=InviteListResponse,
        )

    def delete(
        self,
        invite_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteDeleteResponse:
        """Delete an invite.

        If the invite has already been accepted, it cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return self._delete(
            f"/organization/invites/{invite_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteDeleteResponse,
        )


class AsyncInvitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#with_streaming_response
        """
        return AsyncInvitesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        role: Literal["reader", "owner"],
        projects: Iterable[invite_create_params.Project] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invite:
        """Create an invite for a user to the organization.

        The invite must be accepted by
        the user before they have access to the organization.

        Args:
          email: Send an email to this address

          role: `owner` or `reader`

          projects: An array of projects to which membership is granted at the same time the org
              invite is accepted. If omitted, the user will be invited to the default project
              for compatibility with legacy behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organization/invites",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "role": role,
                    "projects": projects,
                },
                invite_create_params.InviteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invite,
        )

    async def retrieve(
        self,
        invite_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invite:
        """
        Retrieves an invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return await self._get(
            f"/organization/invites/{invite_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invite,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteListResponse:
        """
        Returns a list of invites in the organization.

        Args:
          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/invites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    invite_list_params.InviteListParams,
                ),
            ),
            cast_to=InviteListResponse,
        )

    async def delete(
        self,
        invite_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteDeleteResponse:
        """Delete an invite.

        If the invite has already been accepted, it cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return await self._delete(
            f"/organization/invites/{invite_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteDeleteResponse,
        )


class InvitesResourceWithRawResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.create = to_raw_response_wrapper(
            invites.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invites.retrieve,
        )
        self.list = to_raw_response_wrapper(
            invites.list,
        )
        self.delete = to_raw_response_wrapper(
            invites.delete,
        )


class AsyncInvitesResourceWithRawResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.create = async_to_raw_response_wrapper(
            invites.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invites.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            invites.list,
        )
        self.delete = async_to_raw_response_wrapper(
            invites.delete,
        )


class InvitesResourceWithStreamingResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.create = to_streamed_response_wrapper(
            invites.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invites.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            invites.list,
        )
        self.delete = to_streamed_response_wrapper(
            invites.delete,
        )


class AsyncInvitesResourceWithStreamingResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.create = async_to_streamed_response_wrapper(
            invites.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invites.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            invites.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            invites.delete,
        )
