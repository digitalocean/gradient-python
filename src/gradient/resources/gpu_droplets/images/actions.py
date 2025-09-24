# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.shared.action import Action
from ....types.gpu_droplets.images import action_create_params
from ....types.gpu_droplets.images.action_list_response import ActionListResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        image_id: int,
        *,
        type: Literal["convert", "transfer"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Action:
        """
        The following actions are available on an Image.

        ## Convert an Image to a Snapshot

        To convert an image, for example, a backup to a snapshot, send a POST request to
        `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `convert`.

        ## Transfer an Image

        To transfer an image to another region, send a POST request to
        `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `transfer` and set
        `region` attribute to the slug identifier of the region you wish to transfer to.

        Args:
          type: The action to be taken on the image. Can be either `convert` or `transfer`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        image_id: int,
        *,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ],
        type: Literal["convert", "transfer"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Action:
        """
        The following actions are available on an Image.

        ## Convert an Image to a Snapshot

        To convert an image, for example, a backup to a snapshot, send a POST request to
        `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `convert`.

        ## Transfer an Image

        To transfer an image to another region, send a POST request to
        `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `transfer` and set
        `region` attribute to the slug identifier of the region you wish to transfer to.

        Args:
          region: The slug identifier for the region where the resource will initially be
              available.

          type: The action to be taken on the image. Can be either `convert` or `transfer`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"], ["region", "type"])
    def create(
        self,
        image_id: int,
        *,
        type: Literal["convert", "transfer"],
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Action:
        return self._post(
            f"/v2/images/{image_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}/actions",
            body=maybe_transform(
                {
                    "type": type,
                    "region": region,
                },
                action_create_params.ActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Action,
        )

    def retrieve(
        self,
        action_id: int,
        *,
        image_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Action:
        """
        To retrieve the status of an image action, send a GET request to
        `/v2/images/$IMAGE_ID/actions/$IMAGE_ACTION_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/images/{image_id}/actions/{action_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Action,
        )

    def list(
        self,
        image_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionListResponse:
        """
        To retrieve all actions that have been executed on an image, send a GET request
        to `/v2/images/$IMAGE_ID/actions`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/images/{image_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}/actions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionListResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        image_id: int,
        *,
        type: Literal["convert", "transfer"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Action:
        """
        The following actions are available on an Image.

        ## Convert an Image to a Snapshot

        To convert an image, for example, a backup to a snapshot, send a POST request to
        `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `convert`.

        ## Transfer an Image

        To transfer an image to another region, send a POST request to
        `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `transfer` and set
        `region` attribute to the slug identifier of the region you wish to transfer to.

        Args:
          type: The action to be taken on the image. Can be either `convert` or `transfer`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        image_id: int,
        *,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ],
        type: Literal["convert", "transfer"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Action:
        """
        The following actions are available on an Image.

        ## Convert an Image to a Snapshot

        To convert an image, for example, a backup to a snapshot, send a POST request to
        `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `convert`.

        ## Transfer an Image

        To transfer an image to another region, send a POST request to
        `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `transfer` and set
        `region` attribute to the slug identifier of the region you wish to transfer to.

        Args:
          region: The slug identifier for the region where the resource will initially be
              available.

          type: The action to be taken on the image. Can be either `convert` or `transfer`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"], ["region", "type"])
    async def create(
        self,
        image_id: int,
        *,
        type: Literal["convert", "transfer"],
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Action:
        return await self._post(
            f"/v2/images/{image_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}/actions",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "region": region,
                },
                action_create_params.ActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Action,
        )

    async def retrieve(
        self,
        action_id: int,
        *,
        image_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Action:
        """
        To retrieve the status of an image action, send a GET request to
        `/v2/images/$IMAGE_ID/actions/$IMAGE_ACTION_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/images/{image_id}/actions/{action_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Action,
        )

    async def list(
        self,
        image_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionListResponse:
        """
        To retrieve all actions that have been executed on an image, send a GET request
        to `/v2/images/$IMAGE_ID/actions`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/images/{image_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}/actions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionListResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_raw_response_wrapper(
            actions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            actions.list,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_raw_response_wrapper(
            actions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            actions.list,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_streamed_response_wrapper(
            actions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            actions.list,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_streamed_response_wrapper(
            actions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
