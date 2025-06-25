# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from .routes import (
    RoutesResource,
    AsyncRoutesResource,
    RoutesResourceWithRawResponse,
    AsyncRoutesResourceWithRawResponse,
    RoutesResourceWithStreamingResponse,
    AsyncRoutesResourceWithStreamingResponse,
)
from ...types import (
    APIRetrievalMethod,
    APIDeploymentVisibility,
    agent_list_params,
    agent_create_params,
    agent_update_params,
    agent_update_status_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .functions import (
    FunctionsResource,
    AsyncFunctionsResource,
    FunctionsResourceWithRawResponse,
    AsyncFunctionsResourceWithRawResponse,
    FunctionsResourceWithStreamingResponse,
    AsyncFunctionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .evaluation_runs import (
    EvaluationRunsResource,
    AsyncEvaluationRunsResource,
    EvaluationRunsResourceWithRawResponse,
    AsyncEvaluationRunsResourceWithRawResponse,
    EvaluationRunsResourceWithStreamingResponse,
    AsyncEvaluationRunsResourceWithStreamingResponse,
)
from .knowledge_bases import (
    KnowledgeBasesResource,
    AsyncKnowledgeBasesResource,
    KnowledgeBasesResourceWithRawResponse,
    AsyncKnowledgeBasesResourceWithRawResponse,
    KnowledgeBasesResourceWithStreamingResponse,
    AsyncKnowledgeBasesResourceWithStreamingResponse,
)
from .evaluation_metrics import (
    EvaluationMetricsResource,
    AsyncEvaluationMetricsResource,
    EvaluationMetricsResourceWithRawResponse,
    AsyncEvaluationMetricsResourceWithRawResponse,
    EvaluationMetricsResourceWithStreamingResponse,
    AsyncEvaluationMetricsResourceWithStreamingResponse,
)
from .evaluation_datasets import (
    EvaluationDatasetsResource,
    AsyncEvaluationDatasetsResource,
    EvaluationDatasetsResourceWithRawResponse,
    AsyncEvaluationDatasetsResourceWithRawResponse,
    EvaluationDatasetsResourceWithStreamingResponse,
    AsyncEvaluationDatasetsResourceWithStreamingResponse,
)
from .evaluation_test_cases import (
    EvaluationTestCasesResource,
    AsyncEvaluationTestCasesResource,
    EvaluationTestCasesResourceWithRawResponse,
    AsyncEvaluationTestCasesResourceWithRawResponse,
    EvaluationTestCasesResourceWithStreamingResponse,
    AsyncEvaluationTestCasesResourceWithStreamingResponse,
)
from ...types.agent_list_response import AgentListResponse
from ...types.api_retrieval_method import APIRetrievalMethod
from ...types.agent_create_response import AgentCreateResponse
from ...types.agent_delete_response import AgentDeleteResponse
from ...types.agent_update_response import AgentUpdateResponse
from ...types.agent_retrieve_response import AgentRetrieveResponse
from ...types.api_deployment_visibility import APIDeploymentVisibility
from ...types.agent_update_status_response import AgentUpdateStatusResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def evaluation_metrics(self) -> EvaluationMetricsResource:
        return EvaluationMetricsResource(self._client)

    @cached_property
    def evaluation_runs(self) -> EvaluationRunsResource:
        return EvaluationRunsResource(self._client)

    @cached_property
    def evaluation_test_cases(self) -> EvaluationTestCasesResource:
        return EvaluationTestCasesResource(self._client)

    @cached_property
    def evaluation_datasets(self) -> EvaluationDatasetsResource:
        return EvaluationDatasetsResource(self._client)

    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResource:
        return KnowledgeBasesResource(self._client)

    @cached_property
    def routes(self) -> RoutesResource:
        return RoutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        anthropic_key_uuid: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        instruction: str | NotGiven = NOT_GIVEN,
        knowledge_base_uuid: List[str] | NotGiven = NOT_GIVEN,
        model_uuid: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        openai_key_uuid: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentCreateResponse:
        """To create a new agent, send a POST request to `/v2/gen-ai/agents`.

        The response
        body contains a JSON object with the newly created agent object.

        Args:
          instruction: Agent instruction. Instructions help your agent to perform its job effectively.
              See
              [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
              for best practices.

          model_uuid: Identifier for the foundation model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/agents"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/agents",
            body=maybe_transform(
                {
                    "anthropic_key_uuid": anthropic_key_uuid,
                    "description": description,
                    "instruction": instruction,
                    "knowledge_base_uuid": knowledge_base_uuid,
                    "model_uuid": model_uuid,
                    "name": name,
                    "openai_key_uuid": openai_key_uuid,
                    "project_id": project_id,
                    "region": region,
                    "tags": tags,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    def retrieve(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRetrieveResponse:
        """To retrieve details of an agent, GET request to `/v2/gen-ai/agents/{uuid}`.

        The
        response body is a JSON object containing the agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/v2/gen-ai/agents/{uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    def update(
        self,
        path_uuid: str,
        *,
        anthropic_key_uuid: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        instruction: str | NotGiven = NOT_GIVEN,
        k: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_uuid: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        openai_key_uuid: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        provide_citations: bool | NotGiven = NOT_GIVEN,
        retrieval_method: APIRetrievalMethod | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        body_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentUpdateResponse:
        """To update an agent, send a PUT request to `/v2/gen-ai/agents/{uuid}`.

        The
        response body is a JSON object containing the agent.

        Args:
          instruction: Agent instruction. Instructions help your agent to perform its job effectively.
              See
              [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
              for best practices.

          max_tokens: Specifies the maximum number of tokens the model can process in a single input
              or output, set as a number between 1 and 512. This determines the length of each
              response.

          model_uuid: Identifier for the foundation model.

          temperature: Controls the model’s creativity, specified as a number between 0 and 1. Lower
              values produce more predictable and conservative responses, while higher values
              encourage creativity and variation.

          top_p: Defines the cumulative probability threshold for word selection, specified as a
              number between 0 and 1. Higher values allow for more diverse outputs, while
              lower values ensure focused and coherent responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_uuid:
            raise ValueError(f"Expected a non-empty value for `path_uuid` but received {path_uuid!r}")
        return self._put(
            f"/v2/gen-ai/agents/{path_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_uuid}",
            body=maybe_transform(
                {
                    "anthropic_key_uuid": anthropic_key_uuid,
                    "description": description,
                    "instruction": instruction,
                    "k": k,
                    "max_tokens": max_tokens,
                    "model_uuid": model_uuid,
                    "name": name,
                    "openai_key_uuid": openai_key_uuid,
                    "project_id": project_id,
                    "provide_citations": provide_citations,
                    "retrieval_method": retrieval_method,
                    "tags": tags,
                    "temperature": temperature,
                    "top_p": top_p,
                    "body_uuid": body_uuid,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
        )

    def list(
        self,
        *,
        only_deployed: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """
        To list all agents, send a GET request to `/v2/gen-ai/agents`.

        Args:
          only_deployed: only list agents that are deployed.

          page: page number.

          per_page: items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gen-ai/agents"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/agents",
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

    def delete(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentDeleteResponse:
        """
        To delete an agent, send a DELETE request to `/v2/gen-ai/agents/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/v2/gen-ai/agents/{uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    def update_status(
        self,
        path_uuid: str,
        *,
        body_uuid: str | NotGiven = NOT_GIVEN,
        visibility: APIDeploymentVisibility | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentUpdateStatusResponse:
        """Check whether an agent is public or private.

        To update the agent status, send a
        PUT request to `/v2/gen-ai/agents/{uuid}/deployment_visibility`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_uuid:
            raise ValueError(f"Expected a non-empty value for `path_uuid` but received {path_uuid!r}")
        return self._put(
            f"/v2/gen-ai/agents/{path_uuid}/deployment_visibility"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_uuid}/deployment_visibility",
            body=maybe_transform(
                {
                    "body_uuid": body_uuid,
                    "visibility": visibility,
                },
                agent_update_status_params.AgentUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateStatusResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def evaluation_metrics(self) -> AsyncEvaluationMetricsResource:
        return AsyncEvaluationMetricsResource(self._client)

    @cached_property
    def evaluation_runs(self) -> AsyncEvaluationRunsResource:
        return AsyncEvaluationRunsResource(self._client)

    @cached_property
    def evaluation_test_cases(self) -> AsyncEvaluationTestCasesResource:
        return AsyncEvaluationTestCasesResource(self._client)

    @cached_property
    def evaluation_datasets(self) -> AsyncEvaluationDatasetsResource:
        return AsyncEvaluationDatasetsResource(self._client)

    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResource:
        return AsyncKnowledgeBasesResource(self._client)

    @cached_property
    def routes(self) -> AsyncRoutesResource:
        return AsyncRoutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        anthropic_key_uuid: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        instruction: str | NotGiven = NOT_GIVEN,
        knowledge_base_uuid: List[str] | NotGiven = NOT_GIVEN,
        model_uuid: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        openai_key_uuid: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentCreateResponse:
        """To create a new agent, send a POST request to `/v2/gen-ai/agents`.

        The response
        body contains a JSON object with the newly created agent object.

        Args:
          instruction: Agent instruction. Instructions help your agent to perform its job effectively.
              See
              [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
              for best practices.

          model_uuid: Identifier for the foundation model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/agents"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/agents",
            body=await async_maybe_transform(
                {
                    "anthropic_key_uuid": anthropic_key_uuid,
                    "description": description,
                    "instruction": instruction,
                    "knowledge_base_uuid": knowledge_base_uuid,
                    "model_uuid": model_uuid,
                    "name": name,
                    "openai_key_uuid": openai_key_uuid,
                    "project_id": project_id,
                    "region": region,
                    "tags": tags,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    async def retrieve(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRetrieveResponse:
        """To retrieve details of an agent, GET request to `/v2/gen-ai/agents/{uuid}`.

        The
        response body is a JSON object containing the agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/v2/gen-ai/agents/{uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    async def update(
        self,
        path_uuid: str,
        *,
        anthropic_key_uuid: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        instruction: str | NotGiven = NOT_GIVEN,
        k: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_uuid: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        openai_key_uuid: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        provide_citations: bool | NotGiven = NOT_GIVEN,
        retrieval_method: APIRetrievalMethod | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        body_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentUpdateResponse:
        """To update an agent, send a PUT request to `/v2/gen-ai/agents/{uuid}`.

        The
        response body is a JSON object containing the agent.

        Args:
          instruction: Agent instruction. Instructions help your agent to perform its job effectively.
              See
              [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
              for best practices.

          max_tokens: Specifies the maximum number of tokens the model can process in a single input
              or output, set as a number between 1 and 512. This determines the length of each
              response.

          model_uuid: Identifier for the foundation model.

          temperature: Controls the model’s creativity, specified as a number between 0 and 1. Lower
              values produce more predictable and conservative responses, while higher values
              encourage creativity and variation.

          top_p: Defines the cumulative probability threshold for word selection, specified as a
              number between 0 and 1. Higher values allow for more diverse outputs, while
              lower values ensure focused and coherent responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_uuid:
            raise ValueError(f"Expected a non-empty value for `path_uuid` but received {path_uuid!r}")
        return await self._put(
            f"/v2/gen-ai/agents/{path_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_uuid}",
            body=await async_maybe_transform(
                {
                    "anthropic_key_uuid": anthropic_key_uuid,
                    "description": description,
                    "instruction": instruction,
                    "k": k,
                    "max_tokens": max_tokens,
                    "model_uuid": model_uuid,
                    "name": name,
                    "openai_key_uuid": openai_key_uuid,
                    "project_id": project_id,
                    "provide_citations": provide_citations,
                    "retrieval_method": retrieval_method,
                    "tags": tags,
                    "temperature": temperature,
                    "top_p": top_p,
                    "body_uuid": body_uuid,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
        )

    async def list(
        self,
        *,
        only_deployed: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """
        To list all agents, send a GET request to `/v2/gen-ai/agents`.

        Args:
          only_deployed: only list agents that are deployed.

          page: page number.

          per_page: items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gen-ai/agents"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/agents",
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

    async def delete(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentDeleteResponse:
        """
        To delete an agent, send a DELETE request to `/v2/gen-ai/agents/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/agents/{uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    async def update_status(
        self,
        path_uuid: str,
        *,
        body_uuid: str | NotGiven = NOT_GIVEN,
        visibility: APIDeploymentVisibility | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentUpdateStatusResponse:
        """Check whether an agent is public or private.

        To update the agent status, send a
        PUT request to `/v2/gen-ai/agents/{uuid}/deployment_visibility`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_uuid:
            raise ValueError(f"Expected a non-empty value for `path_uuid` but received {path_uuid!r}")
        return await self._put(
            f"/v2/gen-ai/agents/{path_uuid}/deployment_visibility"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_uuid}/deployment_visibility",
            body=await async_maybe_transform(
                {
                    "body_uuid": body_uuid,
                    "visibility": visibility,
                },
                agent_update_status_params.AgentUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateStatusResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.update_status = to_raw_response_wrapper(
            agents.update_status,
        )

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._agents.api_keys)

    @cached_property
    def evaluation_metrics(self) -> EvaluationMetricsResourceWithRawResponse:
        return EvaluationMetricsResourceWithRawResponse(self._agents.evaluation_metrics)

    @cached_property
    def evaluation_runs(self) -> EvaluationRunsResourceWithRawResponse:
        return EvaluationRunsResourceWithRawResponse(self._agents.evaluation_runs)

    @cached_property
    def evaluation_test_cases(self) -> EvaluationTestCasesResourceWithRawResponse:
        return EvaluationTestCasesResourceWithRawResponse(self._agents.evaluation_test_cases)

    @cached_property
    def evaluation_datasets(self) -> EvaluationDatasetsResourceWithRawResponse:
        return EvaluationDatasetsResourceWithRawResponse(self._agents.evaluation_datasets)

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._agents.functions)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._agents.versions)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResourceWithRawResponse:
        return KnowledgeBasesResourceWithRawResponse(self._agents.knowledge_bases)

    @cached_property
    def routes(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self._agents.routes)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.update_status = async_to_raw_response_wrapper(
            agents.update_status,
        )

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._agents.api_keys)

    @cached_property
    def evaluation_metrics(self) -> AsyncEvaluationMetricsResourceWithRawResponse:
        return AsyncEvaluationMetricsResourceWithRawResponse(self._agents.evaluation_metrics)

    @cached_property
    def evaluation_runs(self) -> AsyncEvaluationRunsResourceWithRawResponse:
        return AsyncEvaluationRunsResourceWithRawResponse(self._agents.evaluation_runs)

    @cached_property
    def evaluation_test_cases(self) -> AsyncEvaluationTestCasesResourceWithRawResponse:
        return AsyncEvaluationTestCasesResourceWithRawResponse(self._agents.evaluation_test_cases)

    @cached_property
    def evaluation_datasets(self) -> AsyncEvaluationDatasetsResourceWithRawResponse:
        return AsyncEvaluationDatasetsResourceWithRawResponse(self._agents.evaluation_datasets)

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._agents.functions)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._agents.versions)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResourceWithRawResponse:
        return AsyncKnowledgeBasesResourceWithRawResponse(self._agents.knowledge_bases)

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self._agents.routes)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.update_status = to_streamed_response_wrapper(
            agents.update_status,
        )

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._agents.api_keys)

    @cached_property
    def evaluation_metrics(self) -> EvaluationMetricsResourceWithStreamingResponse:
        return EvaluationMetricsResourceWithStreamingResponse(self._agents.evaluation_metrics)

    @cached_property
    def evaluation_runs(self) -> EvaluationRunsResourceWithStreamingResponse:
        return EvaluationRunsResourceWithStreamingResponse(self._agents.evaluation_runs)

    @cached_property
    def evaluation_test_cases(self) -> EvaluationTestCasesResourceWithStreamingResponse:
        return EvaluationTestCasesResourceWithStreamingResponse(self._agents.evaluation_test_cases)

    @cached_property
    def evaluation_datasets(self) -> EvaluationDatasetsResourceWithStreamingResponse:
        return EvaluationDatasetsResourceWithStreamingResponse(self._agents.evaluation_datasets)

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._agents.functions)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._agents.versions)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResourceWithStreamingResponse:
        return KnowledgeBasesResourceWithStreamingResponse(self._agents.knowledge_bases)

    @cached_property
    def routes(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self._agents.routes)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.update_status = async_to_streamed_response_wrapper(
            agents.update_status,
        )

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._agents.api_keys)

    @cached_property
    def evaluation_metrics(self) -> AsyncEvaluationMetricsResourceWithStreamingResponse:
        return AsyncEvaluationMetricsResourceWithStreamingResponse(self._agents.evaluation_metrics)

    @cached_property
    def evaluation_runs(self) -> AsyncEvaluationRunsResourceWithStreamingResponse:
        return AsyncEvaluationRunsResourceWithStreamingResponse(self._agents.evaluation_runs)

    @cached_property
    def evaluation_test_cases(self) -> AsyncEvaluationTestCasesResourceWithStreamingResponse:
        return AsyncEvaluationTestCasesResourceWithStreamingResponse(self._agents.evaluation_test_cases)

    @cached_property
    def evaluation_datasets(self) -> AsyncEvaluationDatasetsResourceWithStreamingResponse:
        return AsyncEvaluationDatasetsResourceWithStreamingResponse(self._agents.evaluation_datasets)

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._agents.functions)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._agents.versions)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self._agents.knowledge_bases)

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self._agents.routes)
