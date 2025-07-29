# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
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
from .openai.openai import (
    OpenAIResource,
    AsyncOpenAIResource,
    OpenAIResourceWithRawResponse,
    AsyncOpenAIResourceWithRawResponse,
    OpenAIResourceWithStreamingResponse,
    AsyncOpenAIResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.agents import evaluation_metric_list_regions_params
from .anthropic.anthropic import (
    AnthropicResource,
    AsyncAnthropicResource,
    AnthropicResourceWithRawResponse,
    AsyncAnthropicResourceWithRawResponse,
    AnthropicResourceWithStreamingResponse,
    AsyncAnthropicResourceWithStreamingResponse,
)
from .workspaces.workspaces import (
    WorkspacesResource,
    AsyncWorkspacesResource,
    WorkspacesResourceWithRawResponse,
    AsyncWorkspacesResourceWithRawResponse,
    WorkspacesResourceWithStreamingResponse,
    AsyncWorkspacesResourceWithStreamingResponse,
)
from ....types.agents.evaluation_metric_list_response import EvaluationMetricListResponse
from ....types.agents.evaluation_metric_list_regions_response import EvaluationMetricListRegionsResponse

__all__ = ["EvaluationMetricsResource", "AsyncEvaluationMetricsResource"]


class EvaluationMetricsResource(SyncAPIResource):
    @cached_property
    def workspaces(self) -> WorkspacesResource:
        return WorkspacesResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def anthropic(self) -> AnthropicResource:
        return AnthropicResource(self._client)

    @cached_property
    def openai(self) -> OpenAIResource:
        return OpenAIResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluationMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return EvaluationMetricsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationMetricListResponse:
        """
        To list all evaluation metrics, send a GET request to
        `/v2/gen-ai/evaluation_metrics`.
        """
        return self._get(
            "/v2/gen-ai/evaluation_metrics"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationMetricListResponse,
        )

    def list_regions(
        self,
        *,
        serves_batch: bool | NotGiven = NOT_GIVEN,
        serves_inference: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationMetricListRegionsResponse:
        """
        To list all datacenter regions, send a GET request to `/v2/gen-ai/regions`.

        Args:
          serves_batch: Include datacenters that are capable of running batch jobs.

          serves_inference: Include datacenters that serve inference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gen-ai/regions"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "serves_batch": serves_batch,
                        "serves_inference": serves_inference,
                    },
                    evaluation_metric_list_regions_params.EvaluationMetricListRegionsParams,
                ),
            ),
            cast_to=EvaluationMetricListRegionsResponse,
        )


class AsyncEvaluationMetricsResource(AsyncAPIResource):
    @cached_property
    def workspaces(self) -> AsyncWorkspacesResource:
        return AsyncWorkspacesResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def anthropic(self) -> AsyncAnthropicResource:
        return AsyncAnthropicResource(self._client)

    @cached_property
    def openai(self) -> AsyncOpenAIResource:
        return AsyncOpenAIResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluationMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AsyncEvaluationMetricsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationMetricListResponse:
        """
        To list all evaluation metrics, send a GET request to
        `/v2/gen-ai/evaluation_metrics`.
        """
        return await self._get(
            "/v2/gen-ai/evaluation_metrics"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationMetricListResponse,
        )

    async def list_regions(
        self,
        *,
        serves_batch: bool | NotGiven = NOT_GIVEN,
        serves_inference: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationMetricListRegionsResponse:
        """
        To list all datacenter regions, send a GET request to `/v2/gen-ai/regions`.

        Args:
          serves_batch: Include datacenters that are capable of running batch jobs.

          serves_inference: Include datacenters that serve inference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gen-ai/regions"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "serves_batch": serves_batch,
                        "serves_inference": serves_inference,
                    },
                    evaluation_metric_list_regions_params.EvaluationMetricListRegionsParams,
                ),
            ),
            cast_to=EvaluationMetricListRegionsResponse,
        )


class EvaluationMetricsResourceWithRawResponse:
    def __init__(self, evaluation_metrics: EvaluationMetricsResource) -> None:
        self._evaluation_metrics = evaluation_metrics

        self.list = to_raw_response_wrapper(
            evaluation_metrics.list,
        )
        self.list_regions = to_raw_response_wrapper(
            evaluation_metrics.list_regions,
        )

    @cached_property
    def workspaces(self) -> WorkspacesResourceWithRawResponse:
        return WorkspacesResourceWithRawResponse(self._evaluation_metrics.workspaces)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._evaluation_metrics.models)

    @cached_property
    def anthropic(self) -> AnthropicResourceWithRawResponse:
        return AnthropicResourceWithRawResponse(self._evaluation_metrics.anthropic)

    @cached_property
    def openai(self) -> OpenAIResourceWithRawResponse:
        return OpenAIResourceWithRawResponse(self._evaluation_metrics.openai)


class AsyncEvaluationMetricsResourceWithRawResponse:
    def __init__(self, evaluation_metrics: AsyncEvaluationMetricsResource) -> None:
        self._evaluation_metrics = evaluation_metrics

        self.list = async_to_raw_response_wrapper(
            evaluation_metrics.list,
        )
        self.list_regions = async_to_raw_response_wrapper(
            evaluation_metrics.list_regions,
        )

    @cached_property
    def workspaces(self) -> AsyncWorkspacesResourceWithRawResponse:
        return AsyncWorkspacesResourceWithRawResponse(self._evaluation_metrics.workspaces)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._evaluation_metrics.models)

    @cached_property
    def anthropic(self) -> AsyncAnthropicResourceWithRawResponse:
        return AsyncAnthropicResourceWithRawResponse(self._evaluation_metrics.anthropic)

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithRawResponse:
        return AsyncOpenAIResourceWithRawResponse(self._evaluation_metrics.openai)


class EvaluationMetricsResourceWithStreamingResponse:
    def __init__(self, evaluation_metrics: EvaluationMetricsResource) -> None:
        self._evaluation_metrics = evaluation_metrics

        self.list = to_streamed_response_wrapper(
            evaluation_metrics.list,
        )
        self.list_regions = to_streamed_response_wrapper(
            evaluation_metrics.list_regions,
        )

    @cached_property
    def workspaces(self) -> WorkspacesResourceWithStreamingResponse:
        return WorkspacesResourceWithStreamingResponse(self._evaluation_metrics.workspaces)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._evaluation_metrics.models)

    @cached_property
    def anthropic(self) -> AnthropicResourceWithStreamingResponse:
        return AnthropicResourceWithStreamingResponse(self._evaluation_metrics.anthropic)

    @cached_property
    def openai(self) -> OpenAIResourceWithStreamingResponse:
        return OpenAIResourceWithStreamingResponse(self._evaluation_metrics.openai)


class AsyncEvaluationMetricsResourceWithStreamingResponse:
    def __init__(self, evaluation_metrics: AsyncEvaluationMetricsResource) -> None:
        self._evaluation_metrics = evaluation_metrics

        self.list = async_to_streamed_response_wrapper(
            evaluation_metrics.list,
        )
        self.list_regions = async_to_streamed_response_wrapper(
            evaluation_metrics.list_regions,
        )

    @cached_property
    def workspaces(self) -> AsyncWorkspacesResourceWithStreamingResponse:
        return AsyncWorkspacesResourceWithStreamingResponse(self._evaluation_metrics.workspaces)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._evaluation_metrics.models)

    @cached_property
    def anthropic(self) -> AsyncAnthropicResourceWithStreamingResponse:
        return AsyncAnthropicResourceWithStreamingResponse(self._evaluation_metrics.anthropic)

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithStreamingResponse:
        return AsyncOpenAIResourceWithStreamingResponse(self._evaluation_metrics.openai)
