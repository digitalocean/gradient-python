# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.agents import child_agent_add_params, child_agent_update_params
from ...types.agents.child_agent_add_response import ChildAgentAddResponse
from ...types.agents.child_agent_view_response import ChildAgentViewResponse
from ...types.agents.child_agent_delete_response import ChildAgentDeleteResponse
from ...types.agents.child_agent_update_response import ChildAgentUpdateResponse

__all__ = ["ChildAgentsResource", "AsyncChildAgentsResource"]


class ChildAgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChildAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return ChildAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChildAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return ChildAgentsResourceWithStreamingResponse(self)

    def update(
        self,
        path_child_agent_uuid: str,
        *,
        path_parent_agent_uuid: str,
        body_child_agent_uuid: str | NotGiven = NOT_GIVEN,
        if_case: str | NotGiven = NOT_GIVEN,
        body_parent_agent_uuid: str | NotGiven = NOT_GIVEN,
        route_name: str | NotGiven = NOT_GIVEN,
        uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildAgentUpdateResponse:
        """
        To update an agent route for an agent, send a PUT request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          body_parent_agent_uuid: A unique identifier for the parent agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_parent_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_parent_agent_uuid` but received {path_parent_agent_uuid!r}"
            )
        if not path_child_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_child_agent_uuid` but received {path_child_agent_uuid!r}"
            )
        return self._put(
            f"/v2/genai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}",
            body=maybe_transform(
                {
                    "body_child_agent_uuid": body_child_agent_uuid,
                    "if_case": if_case,
                    "body_parent_agent_uuid": body_parent_agent_uuid,
                    "route_name": route_name,
                    "uuid": uuid,
                },
                child_agent_update_params.ChildAgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildAgentUpdateResponse,
        )

    def delete(
        self,
        child_agent_uuid: str,
        *,
        parent_agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildAgentDeleteResponse:
        """
        To delete an agent route from a parent agent, send a DELETE request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not parent_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `parent_agent_uuid` but received {parent_agent_uuid!r}")
        if not child_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `child_agent_uuid` but received {child_agent_uuid!r}")
        return self._delete(
            f"/v2/genai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildAgentDeleteResponse,
        )

    def add(
        self,
        path_child_agent_uuid: str,
        *,
        path_parent_agent_uuid: str,
        body_child_agent_uuid: str | NotGiven = NOT_GIVEN,
        if_case: str | NotGiven = NOT_GIVEN,
        body_parent_agent_uuid: str | NotGiven = NOT_GIVEN,
        route_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildAgentAddResponse:
        """
        To add an agent route to an agent, send a POST request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          body_parent_agent_uuid: A unique identifier for the parent agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_parent_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_parent_agent_uuid` but received {path_parent_agent_uuid!r}"
            )
        if not path_child_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_child_agent_uuid` but received {path_child_agent_uuid!r}"
            )
        return self._post(
            f"/v2/genai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}",
            body=maybe_transform(
                {
                    "body_child_agent_uuid": body_child_agent_uuid,
                    "if_case": if_case,
                    "body_parent_agent_uuid": body_parent_agent_uuid,
                    "route_name": route_name,
                },
                child_agent_add_params.ChildAgentAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildAgentAddResponse,
        )

    def view(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildAgentViewResponse:
        """
        To view agent routes for an agent, send a GET requtest to
        `/v2/gen-ai/agents/{uuid}/child_agents`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/v2/genai/agents/{uuid}/child_agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildAgentViewResponse,
        )


class AsyncChildAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChildAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChildAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChildAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncChildAgentsResourceWithStreamingResponse(self)

    async def update(
        self,
        path_child_agent_uuid: str,
        *,
        path_parent_agent_uuid: str,
        body_child_agent_uuid: str | NotGiven = NOT_GIVEN,
        if_case: str | NotGiven = NOT_GIVEN,
        body_parent_agent_uuid: str | NotGiven = NOT_GIVEN,
        route_name: str | NotGiven = NOT_GIVEN,
        uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildAgentUpdateResponse:
        """
        To update an agent route for an agent, send a PUT request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          body_parent_agent_uuid: A unique identifier for the parent agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_parent_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_parent_agent_uuid` but received {path_parent_agent_uuid!r}"
            )
        if not path_child_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_child_agent_uuid` but received {path_child_agent_uuid!r}"
            )
        return await self._put(
            f"/v2/genai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}",
            body=await async_maybe_transform(
                {
                    "body_child_agent_uuid": body_child_agent_uuid,
                    "if_case": if_case,
                    "body_parent_agent_uuid": body_parent_agent_uuid,
                    "route_name": route_name,
                    "uuid": uuid,
                },
                child_agent_update_params.ChildAgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildAgentUpdateResponse,
        )

    async def delete(
        self,
        child_agent_uuid: str,
        *,
        parent_agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildAgentDeleteResponse:
        """
        To delete an agent route from a parent agent, send a DELETE request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not parent_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `parent_agent_uuid` but received {parent_agent_uuid!r}")
        if not child_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `child_agent_uuid` but received {child_agent_uuid!r}")
        return await self._delete(
            f"/v2/genai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildAgentDeleteResponse,
        )

    async def add(
        self,
        path_child_agent_uuid: str,
        *,
        path_parent_agent_uuid: str,
        body_child_agent_uuid: str | NotGiven = NOT_GIVEN,
        if_case: str | NotGiven = NOT_GIVEN,
        body_parent_agent_uuid: str | NotGiven = NOT_GIVEN,
        route_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildAgentAddResponse:
        """
        To add an agent route to an agent, send a POST request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          body_parent_agent_uuid: A unique identifier for the parent agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_parent_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_parent_agent_uuid` but received {path_parent_agent_uuid!r}"
            )
        if not path_child_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_child_agent_uuid` but received {path_child_agent_uuid!r}"
            )
        return await self._post(
            f"/v2/genai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}",
            body=await async_maybe_transform(
                {
                    "body_child_agent_uuid": body_child_agent_uuid,
                    "if_case": if_case,
                    "body_parent_agent_uuid": body_parent_agent_uuid,
                    "route_name": route_name,
                },
                child_agent_add_params.ChildAgentAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildAgentAddResponse,
        )

    async def view(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildAgentViewResponse:
        """
        To view agent routes for an agent, send a GET requtest to
        `/v2/gen-ai/agents/{uuid}/child_agents`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/v2/genai/agents/{uuid}/child_agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildAgentViewResponse,
        )


class ChildAgentsResourceWithRawResponse:
    def __init__(self, child_agents: ChildAgentsResource) -> None:
        self._child_agents = child_agents

        self.update = to_raw_response_wrapper(
            child_agents.update,
        )
        self.delete = to_raw_response_wrapper(
            child_agents.delete,
        )
        self.add = to_raw_response_wrapper(
            child_agents.add,
        )
        self.view = to_raw_response_wrapper(
            child_agents.view,
        )


class AsyncChildAgentsResourceWithRawResponse:
    def __init__(self, child_agents: AsyncChildAgentsResource) -> None:
        self._child_agents = child_agents

        self.update = async_to_raw_response_wrapper(
            child_agents.update,
        )
        self.delete = async_to_raw_response_wrapper(
            child_agents.delete,
        )
        self.add = async_to_raw_response_wrapper(
            child_agents.add,
        )
        self.view = async_to_raw_response_wrapper(
            child_agents.view,
        )


class ChildAgentsResourceWithStreamingResponse:
    def __init__(self, child_agents: ChildAgentsResource) -> None:
        self._child_agents = child_agents

        self.update = to_streamed_response_wrapper(
            child_agents.update,
        )
        self.delete = to_streamed_response_wrapper(
            child_agents.delete,
        )
        self.add = to_streamed_response_wrapper(
            child_agents.add,
        )
        self.view = to_streamed_response_wrapper(
            child_agents.view,
        )


class AsyncChildAgentsResourceWithStreamingResponse:
    def __init__(self, child_agents: AsyncChildAgentsResource) -> None:
        self._child_agents = child_agents

        self.update = async_to_streamed_response_wrapper(
            child_agents.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            child_agents.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            child_agents.add,
        )
        self.view = async_to_streamed_response_wrapper(
            child_agents.view,
        )
