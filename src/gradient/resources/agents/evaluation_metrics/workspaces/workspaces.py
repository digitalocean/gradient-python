# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)
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
from .....types.agents.evaluation_metrics import workspace_create_params, workspace_update_params
from .....types.agents.evaluation_metrics.workspace_list_response import WorkspaceListResponse
from .....types.agents.evaluation_metrics.workspace_create_response import WorkspaceCreateResponse
from .....types.agents.evaluation_metrics.workspace_delete_response import WorkspaceDeleteResponse
from .....types.agents.evaluation_metrics.workspace_update_response import WorkspaceUpdateResponse
from .....types.agents.evaluation_metrics.workspace_retrieve_response import WorkspaceRetrieveResponse
from .....types.agents.evaluation_metrics.workspace_list_evaluation_test_cases_response import (
    WorkspaceListEvaluationTestCasesResponse,
)

__all__ = ["WorkspacesResource", "AsyncWorkspacesResource"]


class WorkspacesResource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return WorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return WorkspacesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_uuids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceCreateResponse:
        """To create a new workspace, send a POST request to `/v2/gen-ai/workspaces`.

        The
        response body contains a JSON object with the newly created workspace object.

        Args:
          agent_uuids: Ids of the agents(s) to attach to the workspace

          description: Description of the workspace

          name: Name of the workspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/workspaces"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/workspaces",
            body=maybe_transform(
                {
                    "agent_uuids": agent_uuids,
                    "description": description,
                    "name": name,
                },
                workspace_create_params.WorkspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceCreateResponse,
        )

    def retrieve(
        self,
        workspace_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceRetrieveResponse:
        """
        To retrieve details of a workspace, GET request to
        `/v2/gen-ai/workspaces/{workspace_uuid}`. The response body is a JSON object
        containing the workspace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_uuid:
            raise ValueError(f"Expected a non-empty value for `workspace_uuid` but received {workspace_uuid!r}")
        return self._get(
            f"/v2/gen-ai/workspaces/{workspace_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{workspace_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceRetrieveResponse,
        )

    def update(
        self,
        path_workspace_uuid: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        body_workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceUpdateResponse:
        """
        To update a workspace, send a PUT request to
        `/v2/gen-ai/workspaces/{workspace_uuid}`. The response body is a JSON object
        containing the workspace.

        Args:
          description: The new description of the workspace

          name: The new name of the workspace

          body_workspace_uuid: Workspace UUID.

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
            f"/v2/gen-ai/workspaces/{path_workspace_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{path_workspace_uuid}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "body_workspace_uuid": body_workspace_uuid,
                },
                workspace_update_params.WorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceListResponse:
        """To list all workspaces, send a GET request to `/v2/gen-ai/workspaces`."""
        return self._get(
            "/v2/gen-ai/workspaces"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/workspaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListResponse,
        )

    def delete(
        self,
        workspace_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceDeleteResponse:
        """
        To delete a workspace, send a DELETE request to
        `/v2/gen-ai/workspace/{workspace_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_uuid:
            raise ValueError(f"Expected a non-empty value for `workspace_uuid` but received {workspace_uuid!r}")
        return self._delete(
            f"/v2/gen-ai/workspaces/{workspace_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{workspace_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceDeleteResponse,
        )

    def list_evaluation_test_cases(
        self,
        workspace_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceListEvaluationTestCasesResponse:
        """
        To list all evaluation test cases by a workspace, send a GET request to
        `/v2/gen-ai/workspaces/{workspace_uuid}/evaluation_test_cases`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_uuid:
            raise ValueError(f"Expected a non-empty value for `workspace_uuid` but received {workspace_uuid!r}")
        return self._get(
            f"/v2/gen-ai/workspaces/{workspace_uuid}/evaluation_test_cases"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{workspace_uuid}/evaluation_test_cases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListEvaluationTestCasesResponse,
        )


class AsyncWorkspacesResource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncWorkspacesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_uuids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceCreateResponse:
        """To create a new workspace, send a POST request to `/v2/gen-ai/workspaces`.

        The
        response body contains a JSON object with the newly created workspace object.

        Args:
          agent_uuids: Ids of the agents(s) to attach to the workspace

          description: Description of the workspace

          name: Name of the workspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/workspaces"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/workspaces",
            body=await async_maybe_transform(
                {
                    "agent_uuids": agent_uuids,
                    "description": description,
                    "name": name,
                },
                workspace_create_params.WorkspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceCreateResponse,
        )

    async def retrieve(
        self,
        workspace_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceRetrieveResponse:
        """
        To retrieve details of a workspace, GET request to
        `/v2/gen-ai/workspaces/{workspace_uuid}`. The response body is a JSON object
        containing the workspace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_uuid:
            raise ValueError(f"Expected a non-empty value for `workspace_uuid` but received {workspace_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/workspaces/{workspace_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{workspace_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceRetrieveResponse,
        )

    async def update(
        self,
        path_workspace_uuid: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        body_workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceUpdateResponse:
        """
        To update a workspace, send a PUT request to
        `/v2/gen-ai/workspaces/{workspace_uuid}`. The response body is a JSON object
        containing the workspace.

        Args:
          description: The new description of the workspace

          name: The new name of the workspace

          body_workspace_uuid: Workspace UUID.

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
            f"/v2/gen-ai/workspaces/{path_workspace_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{path_workspace_uuid}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "body_workspace_uuid": body_workspace_uuid,
                },
                workspace_update_params.WorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceListResponse:
        """To list all workspaces, send a GET request to `/v2/gen-ai/workspaces`."""
        return await self._get(
            "/v2/gen-ai/workspaces"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/workspaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListResponse,
        )

    async def delete(
        self,
        workspace_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceDeleteResponse:
        """
        To delete a workspace, send a DELETE request to
        `/v2/gen-ai/workspace/{workspace_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_uuid:
            raise ValueError(f"Expected a non-empty value for `workspace_uuid` but received {workspace_uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/workspaces/{workspace_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{workspace_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceDeleteResponse,
        )

    async def list_evaluation_test_cases(
        self,
        workspace_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceListEvaluationTestCasesResponse:
        """
        To list all evaluation test cases by a workspace, send a GET request to
        `/v2/gen-ai/workspaces/{workspace_uuid}/evaluation_test_cases`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_uuid:
            raise ValueError(f"Expected a non-empty value for `workspace_uuid` but received {workspace_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/workspaces/{workspace_uuid}/evaluation_test_cases"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/workspaces/{workspace_uuid}/evaluation_test_cases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListEvaluationTestCasesResponse,
        )


class WorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.create = to_raw_response_wrapper(
            workspaces.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workspaces.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workspaces.update,
        )
        self.list = to_raw_response_wrapper(
            workspaces.list,
        )
        self.delete = to_raw_response_wrapper(
            workspaces.delete,
        )
        self.list_evaluation_test_cases = to_raw_response_wrapper(
            workspaces.list_evaluation_test_cases,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._workspaces.agents)


class AsyncWorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.create = async_to_raw_response_wrapper(
            workspaces.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workspaces.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workspaces.update,
        )
        self.list = async_to_raw_response_wrapper(
            workspaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workspaces.delete,
        )
        self.list_evaluation_test_cases = async_to_raw_response_wrapper(
            workspaces.list_evaluation_test_cases,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._workspaces.agents)


class WorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.create = to_streamed_response_wrapper(
            workspaces.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workspaces.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workspaces.update,
        )
        self.list = to_streamed_response_wrapper(
            workspaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            workspaces.delete,
        )
        self.list_evaluation_test_cases = to_streamed_response_wrapper(
            workspaces.list_evaluation_test_cases,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._workspaces.agents)


class AsyncWorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.create = async_to_streamed_response_wrapper(
            workspaces.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workspaces.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workspaces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workspaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workspaces.delete,
        )
        self.list_evaluation_test_cases = async_to_streamed_response_wrapper(
            workspaces.list_evaluation_test_cases,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._workspaces.agents)
