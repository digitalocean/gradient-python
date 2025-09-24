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
from ...types.agents import (
    evaluation_test_case_create_params,
    evaluation_test_case_update_params,
    evaluation_test_case_retrieve_params,
    evaluation_test_case_list_evaluation_runs_params,
)
from ...types.agents.api_star_metric_param import APIStarMetricParam
from ...types.agents.evaluation_test_case_list_response import EvaluationTestCaseListResponse
from ...types.agents.evaluation_test_case_create_response import EvaluationTestCaseCreateResponse
from ...types.agents.evaluation_test_case_update_response import EvaluationTestCaseUpdateResponse
from ...types.agents.evaluation_test_case_retrieve_response import EvaluationTestCaseRetrieveResponse
from ...types.agents.evaluation_test_case_list_evaluation_runs_response import (
    EvaluationTestCaseListEvaluationRunsResponse,
)

__all__ = ["EvaluationTestCasesResource", "AsyncEvaluationTestCasesResource"]


class EvaluationTestCasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationTestCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationTestCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationTestCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return EvaluationTestCasesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataset_uuid: str | Omit = omit,
        description: str | Omit = omit,
        metrics: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        star_metric: APIStarMetricParam | Omit = omit,
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationTestCaseCreateResponse:
        """
        To create an evaluation test-case send a POST request to
        `/v2/gen-ai/evaluation_test_cases`.

        Args:
          dataset_uuid: Dataset against which the test‑case is executed.

          description: Description of the test case.

          metrics: Full metric list to use for evaluation test case.

          name: Name of the test case.

          workspace_uuid: The workspace uuid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/evaluation_test_cases"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases",
            body=maybe_transform(
                {
                    "dataset_uuid": dataset_uuid,
                    "description": description,
                    "metrics": metrics,
                    "name": name,
                    "star_metric": star_metric,
                    "workspace_uuid": workspace_uuid,
                },
                evaluation_test_case_create_params.EvaluationTestCaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationTestCaseCreateResponse,
        )

    def retrieve(
        self,
        test_case_uuid: str,
        *,
        evaluation_test_case_version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationTestCaseRetrieveResponse:
        """
        To retrive information about an existing evaluation test case, send a GET
        request to `/v2/gen-ai/evaluation_test_case/{test_case_uuid}`.

        Args:
          evaluation_test_case_version: Version of the test case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_uuid:
            raise ValueError(f"Expected a non-empty value for `test_case_uuid` but received {test_case_uuid!r}")
        return self._get(
            f"/v2/gen-ai/evaluation_test_cases/{test_case_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases/{test_case_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"evaluation_test_case_version": evaluation_test_case_version},
                    evaluation_test_case_retrieve_params.EvaluationTestCaseRetrieveParams,
                ),
            ),
            cast_to=EvaluationTestCaseRetrieveResponse,
        )

    def update(
        self,
        path_test_case_uuid: str,
        *,
        dataset_uuid: str | Omit = omit,
        description: str | Omit = omit,
        metrics: evaluation_test_case_update_params.Metrics | Omit = omit,
        name: str | Omit = omit,
        star_metric: APIStarMetricParam | Omit = omit,
        body_test_case_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationTestCaseUpdateResponse:
        """
        To update an evaluation test-case send a PUT request to
        `/v2/gen-ai/evaluation_test_cases/{test_case_uuid}`.

        Args:
          dataset_uuid: Dataset against which the test‑case is executed.

          description: Description of the test case.

          name: Name of the test case.

          body_test_case_uuid: Test-case UUID to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_test_case_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_test_case_uuid` but received {path_test_case_uuid!r}"
            )
        return self._put(
            f"/v2/gen-ai/evaluation_test_cases/{path_test_case_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases/{path_test_case_uuid}",
            body=maybe_transform(
                {
                    "dataset_uuid": dataset_uuid,
                    "description": description,
                    "metrics": metrics,
                    "name": name,
                    "star_metric": star_metric,
                    "body_test_case_uuid": body_test_case_uuid,
                },
                evaluation_test_case_update_params.EvaluationTestCaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationTestCaseUpdateResponse,
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
    ) -> EvaluationTestCaseListResponse:
        """
        To list all evaluation test cases, send a GET request to
        `/v2/gen-ai/evaluation_test_cases`.
        """
        return self._get(
            "/v2/gen-ai/evaluation_test_cases"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationTestCaseListResponse,
        )

    def list_evaluation_runs(
        self,
        evaluation_test_case_uuid: str,
        *,
        evaluation_test_case_version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationTestCaseListEvaluationRunsResponse:
        """
        To list all evaluation runs by test case, send a GET request to
        `/v2/gen-ai/evaluation_test_cases/{evaluation_test_case_uuid}/evaluation_runs`.

        Args:
          evaluation_test_case_version: Version of the test case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_test_case_uuid:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_test_case_uuid` but received {evaluation_test_case_uuid!r}"
            )
        return self._get(
            f"/v2/gen-ai/evaluation_test_cases/{evaluation_test_case_uuid}/evaluation_runs"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases/{evaluation_test_case_uuid}/evaluation_runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"evaluation_test_case_version": evaluation_test_case_version},
                    evaluation_test_case_list_evaluation_runs_params.EvaluationTestCaseListEvaluationRunsParams,
                ),
            ),
            cast_to=EvaluationTestCaseListEvaluationRunsResponse,
        )


class AsyncEvaluationTestCasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationTestCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationTestCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationTestCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncEvaluationTestCasesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataset_uuid: str | Omit = omit,
        description: str | Omit = omit,
        metrics: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        star_metric: APIStarMetricParam | Omit = omit,
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationTestCaseCreateResponse:
        """
        To create an evaluation test-case send a POST request to
        `/v2/gen-ai/evaluation_test_cases`.

        Args:
          dataset_uuid: Dataset against which the test‑case is executed.

          description: Description of the test case.

          metrics: Full metric list to use for evaluation test case.

          name: Name of the test case.

          workspace_uuid: The workspace uuid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/evaluation_test_cases"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases",
            body=await async_maybe_transform(
                {
                    "dataset_uuid": dataset_uuid,
                    "description": description,
                    "metrics": metrics,
                    "name": name,
                    "star_metric": star_metric,
                    "workspace_uuid": workspace_uuid,
                },
                evaluation_test_case_create_params.EvaluationTestCaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationTestCaseCreateResponse,
        )

    async def retrieve(
        self,
        test_case_uuid: str,
        *,
        evaluation_test_case_version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationTestCaseRetrieveResponse:
        """
        To retrive information about an existing evaluation test case, send a GET
        request to `/v2/gen-ai/evaluation_test_case/{test_case_uuid}`.

        Args:
          evaluation_test_case_version: Version of the test case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_uuid:
            raise ValueError(f"Expected a non-empty value for `test_case_uuid` but received {test_case_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/evaluation_test_cases/{test_case_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases/{test_case_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"evaluation_test_case_version": evaluation_test_case_version},
                    evaluation_test_case_retrieve_params.EvaluationTestCaseRetrieveParams,
                ),
            ),
            cast_to=EvaluationTestCaseRetrieveResponse,
        )

    async def update(
        self,
        path_test_case_uuid: str,
        *,
        dataset_uuid: str | Omit = omit,
        description: str | Omit = omit,
        metrics: evaluation_test_case_update_params.Metrics | Omit = omit,
        name: str | Omit = omit,
        star_metric: APIStarMetricParam | Omit = omit,
        body_test_case_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationTestCaseUpdateResponse:
        """
        To update an evaluation test-case send a PUT request to
        `/v2/gen-ai/evaluation_test_cases/{test_case_uuid}`.

        Args:
          dataset_uuid: Dataset against which the test‑case is executed.

          description: Description of the test case.

          name: Name of the test case.

          body_test_case_uuid: Test-case UUID to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_test_case_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_test_case_uuid` but received {path_test_case_uuid!r}"
            )
        return await self._put(
            f"/v2/gen-ai/evaluation_test_cases/{path_test_case_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases/{path_test_case_uuid}",
            body=await async_maybe_transform(
                {
                    "dataset_uuid": dataset_uuid,
                    "description": description,
                    "metrics": metrics,
                    "name": name,
                    "star_metric": star_metric,
                    "body_test_case_uuid": body_test_case_uuid,
                },
                evaluation_test_case_update_params.EvaluationTestCaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationTestCaseUpdateResponse,
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
    ) -> EvaluationTestCaseListResponse:
        """
        To list all evaluation test cases, send a GET request to
        `/v2/gen-ai/evaluation_test_cases`.
        """
        return await self._get(
            "/v2/gen-ai/evaluation_test_cases"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationTestCaseListResponse,
        )

    async def list_evaluation_runs(
        self,
        evaluation_test_case_uuid: str,
        *,
        evaluation_test_case_version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationTestCaseListEvaluationRunsResponse:
        """
        To list all evaluation runs by test case, send a GET request to
        `/v2/gen-ai/evaluation_test_cases/{evaluation_test_case_uuid}/evaluation_runs`.

        Args:
          evaluation_test_case_version: Version of the test case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_test_case_uuid:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_test_case_uuid` but received {evaluation_test_case_uuid!r}"
            )
        return await self._get(
            f"/v2/gen-ai/evaluation_test_cases/{evaluation_test_case_uuid}/evaluation_runs"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/evaluation_test_cases/{evaluation_test_case_uuid}/evaluation_runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"evaluation_test_case_version": evaluation_test_case_version},
                    evaluation_test_case_list_evaluation_runs_params.EvaluationTestCaseListEvaluationRunsParams,
                ),
            ),
            cast_to=EvaluationTestCaseListEvaluationRunsResponse,
        )


class EvaluationTestCasesResourceWithRawResponse:
    def __init__(self, evaluation_test_cases: EvaluationTestCasesResource) -> None:
        self._evaluation_test_cases = evaluation_test_cases

        self.create = to_raw_response_wrapper(
            evaluation_test_cases.create,
        )
        self.retrieve = to_raw_response_wrapper(
            evaluation_test_cases.retrieve,
        )
        self.update = to_raw_response_wrapper(
            evaluation_test_cases.update,
        )
        self.list = to_raw_response_wrapper(
            evaluation_test_cases.list,
        )
        self.list_evaluation_runs = to_raw_response_wrapper(
            evaluation_test_cases.list_evaluation_runs,
        )


class AsyncEvaluationTestCasesResourceWithRawResponse:
    def __init__(self, evaluation_test_cases: AsyncEvaluationTestCasesResource) -> None:
        self._evaluation_test_cases = evaluation_test_cases

        self.create = async_to_raw_response_wrapper(
            evaluation_test_cases.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            evaluation_test_cases.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            evaluation_test_cases.update,
        )
        self.list = async_to_raw_response_wrapper(
            evaluation_test_cases.list,
        )
        self.list_evaluation_runs = async_to_raw_response_wrapper(
            evaluation_test_cases.list_evaluation_runs,
        )


class EvaluationTestCasesResourceWithStreamingResponse:
    def __init__(self, evaluation_test_cases: EvaluationTestCasesResource) -> None:
        self._evaluation_test_cases = evaluation_test_cases

        self.create = to_streamed_response_wrapper(
            evaluation_test_cases.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            evaluation_test_cases.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            evaluation_test_cases.update,
        )
        self.list = to_streamed_response_wrapper(
            evaluation_test_cases.list,
        )
        self.list_evaluation_runs = to_streamed_response_wrapper(
            evaluation_test_cases.list_evaluation_runs,
        )


class AsyncEvaluationTestCasesResourceWithStreamingResponse:
    def __init__(self, evaluation_test_cases: AsyncEvaluationTestCasesResource) -> None:
        self._evaluation_test_cases = evaluation_test_cases

        self.create = async_to_streamed_response_wrapper(
            evaluation_test_cases.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            evaluation_test_cases.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            evaluation_test_cases.update,
        )
        self.list = async_to_streamed_response_wrapper(
            evaluation_test_cases.list,
        )
        self.list_evaluation_runs = async_to_streamed_response_wrapper(
            evaluation_test_cases.list_evaluation_runs,
        )
