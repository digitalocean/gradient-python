# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.agents.evaluation_metrics.workspaces import agent_list_params, agent_move_params
from .....types.agents.evaluation_metrics.workspaces.agent_list_response import AgentListResponse
from .....types.agents.evaluation_metrics.workspaces.agent_move_response import AgentMoveResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def list(
        self,
        workspace_uuid: str,
        *,
        only_deployed: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        To list all agents by a Workspace, send a GET request to
        `/v2/gen-ai/workspaces/{workspace_uuid}/agents`.

        Args:
          only_deployed: Only list agents that are deployed.

          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_uuid:
            raise ValueError(f"Expected a non-empty value for `workspace_uuid` but received {workspace_uuid!r}")
        return self._get(
            f"/v2/gen-ai/workspaces/{workspace_uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{workspace_uuid}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "only_deployed": only_deployed,
                        "page": page,
                        "per_page": per_page,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def move(
        self,
        path_workspace_uuid: str,
        *,
        agent_uuids: SequenceNotStr[str] | Omit = omit,
        body_workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentMoveResponse:
        """
        To move all listed agents a given workspace, send a PUT request to
        `/v2/gen-ai/workspaces/{workspace_uuid}/agents`.

        Args:
          agent_uuids: Agent uuids

          body_workspace_uuid: Workspace uuid to move agents to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_workspace_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_workspace_uuid` but received {path_workspace_uuid!r}"
            )
        return self._put(
            f"/v2/gen-ai/workspaces/{path_workspace_uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{path_workspace_uuid}/agents",
            body=maybe_transform(
                {
                    "agent_uuids": agent_uuids,
                    "body_workspace_uuid": body_workspace_uuid,
                },
                agent_move_params.AgentMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentMoveResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def list(
        self,
        workspace_uuid: str,
        *,
        only_deployed: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        To list all agents by a Workspace, send a GET request to
        `/v2/gen-ai/workspaces/{workspace_uuid}/agents`.

        Args:
          only_deployed: Only list agents that are deployed.

          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_uuid:
            raise ValueError(f"Expected a non-empty value for `workspace_uuid` but received {workspace_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/workspaces/{workspace_uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{workspace_uuid}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "only_deployed": only_deployed,
                        "page": page,
                        "per_page": per_page,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def move(
        self,
        path_workspace_uuid: str,
        *,
        agent_uuids: SequenceNotStr[str] | Omit = omit,
        body_workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentMoveResponse:
        """
        To move all listed agents a given workspace, send a PUT request to
        `/v2/gen-ai/workspaces/{workspace_uuid}/agents`.

        Args:
          agent_uuids: Agent uuids

          body_workspace_uuid: Workspace uuid to move agents to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_workspace_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_workspace_uuid` but received {path_workspace_uuid!r}"
            )
        return await self._put(
            f"/v2/gen-ai/workspaces/{path_workspace_uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{path_workspace_uuid}/agents",
            body=await async_maybe_transform(
                {
                    "agent_uuids": agent_uuids,
                    "body_workspace_uuid": body_workspace_uuid,
                },
                agent_move_params.AgentMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentMoveResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.move = to_raw_response_wrapper(
            agents.move,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.move = async_to_raw_response_wrapper(
            agents.move,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.move = to_streamed_response_wrapper(
            agents.move,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.move = async_to_streamed_response_wrapper(
            agents.move,
        )
