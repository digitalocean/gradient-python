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
from ....types.gpu_droplets.floating_ips import action_create_params
from ....types.gpu_droplets.floating_ips.action_list_response import ActionListResponse
from ....types.gpu_droplets.floating_ips.action_create_response import ActionCreateResponse
from ....types.gpu_droplets.floating_ips.action_retrieve_response import ActionRetrieveResponse

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
        floating_ip: str,
        *,
        type: Literal["assign", "unassign"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """
        To initiate an action on a floating IP send a POST request to
        `/v2/floating_ips/$FLOATING_IP/actions`. In the JSON body to the request, set
        the `type` attribute to on of the supported action types:

        | Action     | Details                               |
        | ---------- | ------------------------------------- |
        | `assign`   | Assigns a floating IP to a Droplet    |
        | `unassign` | Unassign a floating IP from a Droplet |

        Args:
          type: The type of action to initiate for the floating IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        floating_ip: str,
        *,
        droplet_id: int,
        type: Literal["assign", "unassign"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """
        To initiate an action on a floating IP send a POST request to
        `/v2/floating_ips/$FLOATING_IP/actions`. In the JSON body to the request, set
        the `type` attribute to on of the supported action types:

        | Action     | Details                               |
        | ---------- | ------------------------------------- |
        | `assign`   | Assigns a floating IP to a Droplet    |
        | `unassign` | Unassign a floating IP from a Droplet |

        Args:
          droplet_id: The ID of the Droplet that the floating IP will be assigned to.

          type: The type of action to initiate for the floating IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"], ["droplet_id", "type"])
    def create(
        self,
        floating_ip: str,
        *,
        type: Literal["assign", "unassign"],
        droplet_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        return self._post(
            f"/v2/floating_ips/{floating_ip}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}/actions",
            body=maybe_transform(
                {
                    "type": type,
                    "droplet_id": droplet_id,
                },
                action_create_params.ActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionCreateResponse,
        )

    def retrieve(
        self,
        action_id: int,
        *,
        floating_ip: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        """
        To retrieve the status of a floating IP action, send a GET request to
        `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        return self._get(
            f"/v2/floating_ips/{floating_ip}/actions/{action_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    def list(
        self,
        floating_ip: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionListResponse:
        """
        To retrieve all actions that have been executed on a floating IP, send a GET
        request to `/v2/floating_ips/$FLOATING_IP/actions`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        return self._get(
            f"/v2/floating_ips/{floating_ip}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}/actions",
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
        floating_ip: str,
        *,
        type: Literal["assign", "unassign"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """
        To initiate an action on a floating IP send a POST request to
        `/v2/floating_ips/$FLOATING_IP/actions`. In the JSON body to the request, set
        the `type` attribute to on of the supported action types:

        | Action     | Details                               |
        | ---------- | ------------------------------------- |
        | `assign`   | Assigns a floating IP to a Droplet    |
        | `unassign` | Unassign a floating IP from a Droplet |

        Args:
          type: The type of action to initiate for the floating IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        floating_ip: str,
        *,
        droplet_id: int,
        type: Literal["assign", "unassign"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """
        To initiate an action on a floating IP send a POST request to
        `/v2/floating_ips/$FLOATING_IP/actions`. In the JSON body to the request, set
        the `type` attribute to on of the supported action types:

        | Action     | Details                               |
        | ---------- | ------------------------------------- |
        | `assign`   | Assigns a floating IP to a Droplet    |
        | `unassign` | Unassign a floating IP from a Droplet |

        Args:
          droplet_id: The ID of the Droplet that the floating IP will be assigned to.

          type: The type of action to initiate for the floating IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"], ["droplet_id", "type"])
    async def create(
        self,
        floating_ip: str,
        *,
        type: Literal["assign", "unassign"],
        droplet_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        return await self._post(
            f"/v2/floating_ips/{floating_ip}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}/actions",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "droplet_id": droplet_id,
                },
                action_create_params.ActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionCreateResponse,
        )

    async def retrieve(
        self,
        action_id: int,
        *,
        floating_ip: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        """
        To retrieve the status of a floating IP action, send a GET request to
        `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        return await self._get(
            f"/v2/floating_ips/{floating_ip}/actions/{action_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    async def list(
        self,
        floating_ip: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionListResponse:
        """
        To retrieve all actions that have been executed on a floating IP, send a GET
        request to `/v2/floating_ips/$FLOATING_IP/actions`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not floating_ip:
            raise ValueError(f"Expected a non-empty value for `floating_ip` but received {floating_ip!r}")
        return await self._get(
            f"/v2/floating_ips/{floating_ip}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/floating_ips/{floating_ip}/actions",
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
