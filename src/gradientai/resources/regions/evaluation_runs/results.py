# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.regions.evaluation_runs.result_retrieve_response import ResultRetrieveResponse
from ....types.regions.evaluation_runs.result_retrieve_prompt_response import ResultRetrievePromptResponse

__all__ = ["ResultsResource", "AsyncResultsResource"]


class ResultsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return ResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return ResultsResourceWithStreamingResponse(self)

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
    ) -> ResultRetrieveResponse:
        """
        To retrieve results of an evaluation run, send a GET request to
        `/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results`.

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
            f"/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultRetrieveResponse,
        )

    def retrieve_prompt(
        self,
        prompt_id: int,
        *,
        evaluation_run_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResultRetrievePromptResponse:
        """
        To retrieve results of an evaluation run, send a GET request to
        `/v2/genai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}`.

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
            f"/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultRetrievePromptResponse,
        )


class AsyncResultsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AsyncResultsResourceWithStreamingResponse(self)

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
    ) -> ResultRetrieveResponse:
        """
        To retrieve results of an evaluation run, send a GET request to
        `/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results`.

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
            f"/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultRetrieveResponse,
        )

    async def retrieve_prompt(
        self,
        prompt_id: int,
        *,
        evaluation_run_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResultRetrievePromptResponse:
        """
        To retrieve results of an evaluation run, send a GET request to
        `/v2/genai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}`.

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
            f"/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultRetrievePromptResponse,
        )


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve = to_raw_response_wrapper(
            results.retrieve,
        )
        self.retrieve_prompt = to_raw_response_wrapper(
            results.retrieve_prompt,
        )


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve = async_to_raw_response_wrapper(
            results.retrieve,
        )
        self.retrieve_prompt = async_to_raw_response_wrapper(
            results.retrieve_prompt,
        )


class ResultsResourceWithStreamingResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve = to_streamed_response_wrapper(
            results.retrieve,
        )
        self.retrieve_prompt = to_streamed_response_wrapper(
            results.retrieve_prompt,
        )


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve = async_to_streamed_response_wrapper(
            results.retrieve,
        )
        self.retrieve_prompt = async_to_streamed_response_wrapper(
            results.retrieve_prompt,
        )
