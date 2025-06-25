# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import region_list_params
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
from ...types.region_list_response import RegionListResponse
from .evaluation_runs.evaluation_runs import (
    EvaluationRunsResource,
    AsyncEvaluationRunsResource,
    EvaluationRunsResourceWithRawResponse,
    AsyncEvaluationRunsResourceWithRawResponse,
    EvaluationRunsResourceWithStreamingResponse,
    AsyncEvaluationRunsResourceWithStreamingResponse,
)
from ...types.region_list_evaluation_metrics_response import RegionListEvaluationMetricsResponse

__all__ = ["RegionsResource", "AsyncRegionsResource"]


class RegionsResource(SyncAPIResource):
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
    def with_raw_response(self) -> RegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return RegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return RegionsResourceWithStreamingResponse(self)

    def list(
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
    ) -> RegionListResponse:
        """
        To list all datacenter regions, send a GET request to `/v2/gen-ai/regions`.

        Args:
          serves_batch: include datacenters that are capable of running batch jobs.

          serves_inference: include datacenters that serve inference.

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
                    region_list_params.RegionListParams,
                ),
            ),
            cast_to=RegionListResponse,
        )

    def list_evaluation_metrics(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionListEvaluationMetricsResponse:
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
            cast_to=RegionListEvaluationMetricsResponse,
        )


class AsyncRegionsResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncRegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AsyncRegionsResourceWithStreamingResponse(self)

    async def list(
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
    ) -> RegionListResponse:
        """
        To list all datacenter regions, send a GET request to `/v2/gen-ai/regions`.

        Args:
          serves_batch: include datacenters that are capable of running batch jobs.

          serves_inference: include datacenters that serve inference.

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
                    region_list_params.RegionListParams,
                ),
            ),
            cast_to=RegionListResponse,
        )

    async def list_evaluation_metrics(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionListEvaluationMetricsResponse:
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
            cast_to=RegionListEvaluationMetricsResponse,
        )


class RegionsResourceWithRawResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.list = to_raw_response_wrapper(
            regions.list,
        )
        self.list_evaluation_metrics = to_raw_response_wrapper(
            regions.list_evaluation_metrics,
        )

    @cached_property
    def evaluation_runs(self) -> EvaluationRunsResourceWithRawResponse:
        return EvaluationRunsResourceWithRawResponse(self._regions.evaluation_runs)

    @cached_property
    def evaluation_test_cases(self) -> EvaluationTestCasesResourceWithRawResponse:
        return EvaluationTestCasesResourceWithRawResponse(self._regions.evaluation_test_cases)

    @cached_property
    def evaluation_datasets(self) -> EvaluationDatasetsResourceWithRawResponse:
        return EvaluationDatasetsResourceWithRawResponse(self._regions.evaluation_datasets)


class AsyncRegionsResourceWithRawResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.list = async_to_raw_response_wrapper(
            regions.list,
        )
        self.list_evaluation_metrics = async_to_raw_response_wrapper(
            regions.list_evaluation_metrics,
        )

    @cached_property
    def evaluation_runs(self) -> AsyncEvaluationRunsResourceWithRawResponse:
        return AsyncEvaluationRunsResourceWithRawResponse(self._regions.evaluation_runs)

    @cached_property
    def evaluation_test_cases(self) -> AsyncEvaluationTestCasesResourceWithRawResponse:
        return AsyncEvaluationTestCasesResourceWithRawResponse(self._regions.evaluation_test_cases)

    @cached_property
    def evaluation_datasets(self) -> AsyncEvaluationDatasetsResourceWithRawResponse:
        return AsyncEvaluationDatasetsResourceWithRawResponse(self._regions.evaluation_datasets)


class RegionsResourceWithStreamingResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.list = to_streamed_response_wrapper(
            regions.list,
        )
        self.list_evaluation_metrics = to_streamed_response_wrapper(
            regions.list_evaluation_metrics,
        )

    @cached_property
    def evaluation_runs(self) -> EvaluationRunsResourceWithStreamingResponse:
        return EvaluationRunsResourceWithStreamingResponse(self._regions.evaluation_runs)

    @cached_property
    def evaluation_test_cases(self) -> EvaluationTestCasesResourceWithStreamingResponse:
        return EvaluationTestCasesResourceWithStreamingResponse(self._regions.evaluation_test_cases)

    @cached_property
    def evaluation_datasets(self) -> EvaluationDatasetsResourceWithStreamingResponse:
        return EvaluationDatasetsResourceWithStreamingResponse(self._regions.evaluation_datasets)


class AsyncRegionsResourceWithStreamingResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.list = async_to_streamed_response_wrapper(
            regions.list,
        )
        self.list_evaluation_metrics = async_to_streamed_response_wrapper(
            regions.list_evaluation_metrics,
        )

    @cached_property
    def evaluation_runs(self) -> AsyncEvaluationRunsResourceWithStreamingResponse:
        return AsyncEvaluationRunsResourceWithStreamingResponse(self._regions.evaluation_runs)

    @cached_property
    def evaluation_test_cases(self) -> AsyncEvaluationTestCasesResourceWithStreamingResponse:
        return AsyncEvaluationTestCasesResourceWithStreamingResponse(self._regions.evaluation_test_cases)

    @cached_property
    def evaluation_datasets(self) -> AsyncEvaluationDatasetsResourceWithStreamingResponse:
        return AsyncEvaluationDatasetsResourceWithStreamingResponse(self._regions.evaluation_datasets)
