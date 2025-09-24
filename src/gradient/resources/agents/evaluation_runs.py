# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.agents import evaluation_run_create_params, evaluation_run_list_results_params
from ...types.agents.evaluation_run_create_response import EvaluationRunCreateResponse
from ...types.agents.evaluation_run_retrieve_response import EvaluationRunRetrieveResponse
from ...types.agents.evaluation_run_list_results_response import EvaluationRunListResultsResponse
from ...types.agents.evaluation_run_retrieve_results_response import EvaluationRunRetrieveResultsResponse

__all__ = ["EvaluationRunsResource", "AsyncEvaluationRunsResource"]


class EvaluationRunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return EvaluationRunsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_uuids: SequenceNotStr[str] | Omit = omit,
        run_name: str | Omit = omit,
        test_case_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationRunCreateResponse:
        """
        To run an evaluation test case, send a POST request to
        `/v2/gen-ai/evaluation_runs`.

        Args:
          agent_uuids: Agent UUIDs to run the test case against.

          run_name: The name of the run.

          test_case_uuid: Test-case UUID to run

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
                    "agent_uuids": agent_uuids,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def list_results(
        self,
        evaluation_run_uuid: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationRunListResultsResponse:
        """
        To retrieve results of an evaluation run, send a GET request to
        `/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results`.

        Args:
          page: Page number.

          per_page: Items per page.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    evaluation_run_list_results_params.EvaluationRunListResultsParams,
                ),
            ),
            cast_to=EvaluationRunListResultsResponse,
        )

    def retrieve_results(
        self,
        prompt_id: int,
        *,
        evaluation_run_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationRunRetrieveResultsResponse:
        """
        To retrieve results of an evaluation run, send a GET request to
        `/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}`.

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
            cast_to=EvaluationRunRetrieveResultsResponse,
        )


class AsyncEvaluationRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncEvaluationRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_uuids: SequenceNotStr[str] | Omit = omit,
        run_name: str | Omit = omit,
        test_case_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationRunCreateResponse:
        """
        To run an evaluation test case, send a POST request to
        `/v2/gen-ai/evaluation_runs`.

        Args:
          agent_uuids: Agent UUIDs to run the test case against.

          run_name: The name of the run.

          test_case_uuid: Test-case UUID to run

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
                    "agent_uuids": agent_uuids,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def list_results(
        self,
        evaluation_run_uuid: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationRunListResultsResponse:
        """
        To retrieve results of an evaluation run, send a GET request to
        `/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results`.

        Args:
          page: Page number.

          per_page: Items per page.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    evaluation_run_list_results_params.EvaluationRunListResultsParams,
                ),
            ),
            cast_to=EvaluationRunListResultsResponse,
        )

    async def retrieve_results(
        self,
        prompt_id: int,
        *,
        evaluation_run_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationRunRetrieveResultsResponse:
        """
        To retrieve results of an evaluation run, send a GET request to
        `/v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}`.

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
            cast_to=EvaluationRunRetrieveResultsResponse,
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
        self.list_results = to_raw_response_wrapper(
            evaluation_runs.list_results,
        )
        self.retrieve_results = to_raw_response_wrapper(
            evaluation_runs.retrieve_results,
        )


class AsyncEvaluationRunsResourceWithRawResponse:
    def __init__(self, evaluation_runs: AsyncEvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = async_to_raw_response_wrapper(
            evaluation_runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            evaluation_runs.retrieve,
        )
        self.list_results = async_to_raw_response_wrapper(
            evaluation_runs.list_results,
        )
        self.retrieve_results = async_to_raw_response_wrapper(
            evaluation_runs.retrieve_results,
        )


class EvaluationRunsResourceWithStreamingResponse:
    def __init__(self, evaluation_runs: EvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = to_streamed_response_wrapper(
            evaluation_runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            evaluation_runs.retrieve,
        )
        self.list_results = to_streamed_response_wrapper(
            evaluation_runs.list_results,
        )
        self.retrieve_results = to_streamed_response_wrapper(
            evaluation_runs.retrieve_results,
        )


class AsyncEvaluationRunsResourceWithStreamingResponse:
    def __init__(self, evaluation_runs: AsyncEvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = async_to_streamed_response_wrapper(
            evaluation_runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            evaluation_runs.retrieve,
        )
        self.list_results = async_to_streamed_response_wrapper(
            evaluation_runs.list_results,
        )
        self.retrieve_results = async_to_streamed_response_wrapper(
            evaluation_runs.retrieve_results,
        )
