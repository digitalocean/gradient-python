# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents.evaluation_metric_list_response import EvaluationMetricListResponse

__all__ = ["EvaluationMetricsResource", "AsyncEvaluationMetricsResource"]


class EvaluationMetricsResource(SyncAPIResource):
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


class AsyncEvaluationMetricsResource(AsyncAPIResource):
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


class EvaluationMetricsResourceWithRawResponse:
    def __init__(self, evaluation_metrics: EvaluationMetricsResource) -> None:
        self._evaluation_metrics = evaluation_metrics

        self.list = to_raw_response_wrapper(
            evaluation_metrics.list,
        )


class AsyncEvaluationMetricsResourceWithRawResponse:
    def __init__(self, evaluation_metrics: AsyncEvaluationMetricsResource) -> None:
        self._evaluation_metrics = evaluation_metrics

        self.list = async_to_raw_response_wrapper(
            evaluation_metrics.list,
        )


class EvaluationMetricsResourceWithStreamingResponse:
    def __init__(self, evaluation_metrics: EvaluationMetricsResource) -> None:
        self._evaluation_metrics = evaluation_metrics

        self.list = to_streamed_response_wrapper(
            evaluation_metrics.list,
        )


class AsyncEvaluationMetricsResourceWithStreamingResponse:
    def __init__(self, evaluation_metrics: AsyncEvaluationMetricsResource) -> None:
        self._evaluation_metrics = evaluation_metrics

        self.list = async_to_streamed_response_wrapper(
            evaluation_metrics.list,
        )
