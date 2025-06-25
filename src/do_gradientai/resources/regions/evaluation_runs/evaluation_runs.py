# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .results import (
    ResultsResource,
    AsyncResultsResource,
    ResultsResourceWithRawResponse,
    AsyncResultsResourceWithRawResponse,
    ResultsResourceWithStreamingResponse,
    AsyncResultsResourceWithStreamingResponse,
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
from ...._base_client import make_request_options
from ....types.regions import evaluation_run_create_params
from ....types.regions.evaluation_run_create_response import EvaluationRunCreateResponse
from ....types.regions.evaluation_run_retrieve_response import EvaluationRunRetrieveResponse

__all__ = ["EvaluationRunsResource", "AsyncEvaluationRunsResource"]


class EvaluationRunsResource(SyncAPIResource):
    @cached_property
    def results(self) -> ResultsResource:
        return ResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return EvaluationRunsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_uuid: str | NotGiven = NOT_GIVEN,
        run_name: str | NotGiven = NOT_GIVEN,
        test_case_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationRunCreateResponse:
        """
        To run an evaluation test case, send a POST request to
        `/v2/gen-ai/evaluation_runs`.

        Args:
          agent_uuid: Agent UUID to run the test case against.

          run_name: The name of the run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/evaluation_runs"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_runs",
            body=maybe_transform(
                {
                    "agent_uuid": agent_uuid,
                    "run_name": run_name,
                    "test_case_uuid": test_case_uuid,
                },
                evaluation_run_create_params.EvaluationRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationRunCreateResponse,
        )

    def retrieve(
        self,
        evaluation_run_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationRunRetrieveResponse:
        """
        To retrive information about an existing evaluation run, send a GET request to
        `/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_run_uuid:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_run_uuid` but received {evaluation_run_uuid!r}"
            )
        return self._get(
            f"/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationRunRetrieveResponse,
        )


class AsyncEvaluationRunsResource(AsyncAPIResource):
    @cached_property
    def results(self) -> AsyncResultsResource:
        return AsyncResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AsyncEvaluationRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_uuid: str | NotGiven = NOT_GIVEN,
        run_name: str | NotGiven = NOT_GIVEN,
        test_case_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationRunCreateResponse:
        """
        To run an evaluation test case, send a POST request to
        `/v2/gen-ai/evaluation_runs`.

        Args:
          agent_uuid: Agent UUID to run the test case against.

          run_name: The name of the run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/evaluation_runs"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_runs",
            body=await async_maybe_transform(
                {
                    "agent_uuid": agent_uuid,
                    "run_name": run_name,
                    "test_case_uuid": test_case_uuid,
                },
                evaluation_run_create_params.EvaluationRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationRunCreateResponse,
        )

    async def retrieve(
        self,
        evaluation_run_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationRunRetrieveResponse:
        """
        To retrive information about an existing evaluation run, send a GET request to
        `/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_run_uuid:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_run_uuid` but received {evaluation_run_uuid!r}"
            )
        return await self._get(
            f"/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationRunRetrieveResponse,
        )


class EvaluationRunsResourceWithRawResponse:
    def __init__(self, evaluation_runs: EvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = to_raw_response_wrapper(
            evaluation_runs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            evaluation_runs.retrieve,
        )

    @cached_property
    def results(self) -> ResultsResourceWithRawResponse:
        return ResultsResourceWithRawResponse(self._evaluation_runs.results)


class AsyncEvaluationRunsResourceWithRawResponse:
    def __init__(self, evaluation_runs: AsyncEvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = async_to_raw_response_wrapper(
            evaluation_runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            evaluation_runs.retrieve,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithRawResponse:
        return AsyncResultsResourceWithRawResponse(self._evaluation_runs.results)


class EvaluationRunsResourceWithStreamingResponse:
    def __init__(self, evaluation_runs: EvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = to_streamed_response_wrapper(
            evaluation_runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            evaluation_runs.retrieve,
        )

    @cached_property
    def results(self) -> ResultsResourceWithStreamingResponse:
        return ResultsResourceWithStreamingResponse(self._evaluation_runs.results)


class AsyncEvaluationRunsResourceWithStreamingResponse:
    def __init__(self, evaluation_runs: AsyncEvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = async_to_streamed_response_wrapper(
            evaluation_runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            evaluation_runs.retrieve,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithStreamingResponse:
        return AsyncResultsResourceWithStreamingResponse(self._evaluation_runs.results)
