# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
    evaluation_dataset_create_params,
    evaluation_dataset_create_file_upload_presigned_urls_params,
)
from ...types.agents.evaluation_dataset_create_response import EvaluationDatasetCreateResponse
from ...types.knowledge_bases.api_file_upload_data_source_param import APIFileUploadDataSourceParam
from ...types.agents.evaluation_dataset_create_file_upload_presigned_urls_response import (
    EvaluationDatasetCreateFileUploadPresignedURLsResponse,
)

__all__ = ["EvaluationDatasetsResource", "AsyncEvaluationDatasetsResource"]


class EvaluationDatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return EvaluationDatasetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_upload_dataset: APIFileUploadDataSourceParam | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationDatasetCreateResponse:
        """
        To create an evaluation dataset, send a POST request to
        `/v2/gen-ai/evaluation_datasets`.

        Args:
          file_upload_dataset: File to upload as data source for knowledge base.

          name: The name of the agent evaluation dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/evaluation_datasets"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_datasets",
            body=maybe_transform(
                {
                    "file_upload_dataset": file_upload_dataset,
                    "name": name,
                },
                evaluation_dataset_create_params.EvaluationDatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetCreateResponse,
        )

    def create_file_upload_presigned_urls(
        self,
        *,
        files: Iterable[evaluation_dataset_create_file_upload_presigned_urls_params.File] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationDatasetCreateFileUploadPresignedURLsResponse:
        """
        To create presigned URLs for evaluation dataset file upload, send a POST request
        to `/v2/gen-ai/evaluation_datasets/file_upload_presigned_urls`.

        Args:
          files: A list of files to generate presigned URLs for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/evaluation_datasets/file_upload_presigned_urls"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_datasets/file_upload_presigned_urls",
            body=maybe_transform(
                {"files": files},
                evaluation_dataset_create_file_upload_presigned_urls_params.EvaluationDatasetCreateFileUploadPresignedURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetCreateFileUploadPresignedURLsResponse,
        )


class AsyncEvaluationDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncEvaluationDatasetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_upload_dataset: APIFileUploadDataSourceParam | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationDatasetCreateResponse:
        """
        To create an evaluation dataset, send a POST request to
        `/v2/gen-ai/evaluation_datasets`.

        Args:
          file_upload_dataset: File to upload as data source for knowledge base.

          name: The name of the agent evaluation dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/evaluation_datasets"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_datasets",
            body=await async_maybe_transform(
                {
                    "file_upload_dataset": file_upload_dataset,
                    "name": name,
                },
                evaluation_dataset_create_params.EvaluationDatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetCreateResponse,
        )

    async def create_file_upload_presigned_urls(
        self,
        *,
        files: Iterable[evaluation_dataset_create_file_upload_presigned_urls_params.File] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluationDatasetCreateFileUploadPresignedURLsResponse:
        """
        To create presigned URLs for evaluation dataset file upload, send a POST request
        to `/v2/gen-ai/evaluation_datasets/file_upload_presigned_urls`.

        Args:
          files: A list of files to generate presigned URLs for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/evaluation_datasets/file_upload_presigned_urls"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/evaluation_datasets/file_upload_presigned_urls",
            body=await async_maybe_transform(
                {"files": files},
                evaluation_dataset_create_file_upload_presigned_urls_params.EvaluationDatasetCreateFileUploadPresignedURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetCreateFileUploadPresignedURLsResponse,
        )


class EvaluationDatasetsResourceWithRawResponse:
    def __init__(self, evaluation_datasets: EvaluationDatasetsResource) -> None:
        self._evaluation_datasets = evaluation_datasets

        self.create = to_raw_response_wrapper(
            evaluation_datasets.create,
        )
        self.create_file_upload_presigned_urls = to_raw_response_wrapper(
            evaluation_datasets.create_file_upload_presigned_urls,
        )


class AsyncEvaluationDatasetsResourceWithRawResponse:
    def __init__(self, evaluation_datasets: AsyncEvaluationDatasetsResource) -> None:
        self._evaluation_datasets = evaluation_datasets

        self.create = async_to_raw_response_wrapper(
            evaluation_datasets.create,
        )
        self.create_file_upload_presigned_urls = async_to_raw_response_wrapper(
            evaluation_datasets.create_file_upload_presigned_urls,
        )


class EvaluationDatasetsResourceWithStreamingResponse:
    def __init__(self, evaluation_datasets: EvaluationDatasetsResource) -> None:
        self._evaluation_datasets = evaluation_datasets

        self.create = to_streamed_response_wrapper(
            evaluation_datasets.create,
        )
        self.create_file_upload_presigned_urls = to_streamed_response_wrapper(
            evaluation_datasets.create_file_upload_presigned_urls,
        )


class AsyncEvaluationDatasetsResourceWithStreamingResponse:
    def __init__(self, evaluation_datasets: AsyncEvaluationDatasetsResource) -> None:
        self._evaluation_datasets = evaluation_datasets

        self.create = async_to_streamed_response_wrapper(
            evaluation_datasets.create,
        )
        self.create_file_upload_presigned_urls = async_to_streamed_response_wrapper(
            evaluation_datasets.create_file_upload_presigned_urls,
        )
