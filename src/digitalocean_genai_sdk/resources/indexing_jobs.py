# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import indexing_job_list_params, indexing_job_create_params, indexing_job_update_cancel_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.indexing_job_list_response import IndexingJobListResponse
from ..types.indexing_job_create_response import IndexingJobCreateResponse
from ..types.indexing_job_retrieve_response import IndexingJobRetrieveResponse
from ..types.indexing_job_update_cancel_response import IndexingJobUpdateCancelResponse
from ..types.indexing_job_retrieve_data_sources_response import IndexingJobRetrieveDataSourcesResponse

__all__ = ["IndexingJobsResource", "AsyncIndexingJobsResource"]


class IndexingJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndexingJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return IndexingJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexingJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return IndexingJobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data_source_uuids: List[str] | NotGiven = NOT_GIVEN,
        knowledge_base_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexingJobCreateResponse:
        """
        To start an indexing job for a knowledge base, send a POST request to
        `/v2/gen-ai/indexing_jobs`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/genai/indexing_jobs",
            body=maybe_transform(
                {
                    "data_source_uuids": data_source_uuids,
                    "knowledge_base_uuid": knowledge_base_uuid,
                },
                indexing_job_create_params.IndexingJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobCreateResponse,
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
    ) -> IndexingJobRetrieveResponse:
        """
        To get status of an indexing Job for a knowledge base, send a GET request to
        `/v2/gen-ai/indexing_jobs/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/v2/genai/indexing_jobs/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexingJobListResponse:
        """
        To list all indexing jobs for a knowledge base, send a GET request to
        `/v2/gen-ai/indexing_jobs`.

        Args:
          page: page number.

          per_page: items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/genai/indexing_jobs",
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
                    indexing_job_list_params.IndexingJobListParams,
                ),
            ),
            cast_to=IndexingJobListResponse,
        )

    def retrieve_data_sources(
        self,
        indexing_job_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexingJobRetrieveDataSourcesResponse:
        """
        To list all datasources for an indexing job, send a GET request to
        `/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not indexing_job_uuid:
            raise ValueError(f"Expected a non-empty value for `indexing_job_uuid` but received {indexing_job_uuid!r}")
        return self._get(
            f"/v2/genai/indexing_jobs/{indexing_job_uuid}/data_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveDataSourcesResponse,
        )

    def update_cancel(
        self,
        path_uuid: str,
        *,
        body_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexingJobUpdateCancelResponse:
        """
        To cancel an indexing job for a knowledge base, send a PUT request to
        `/v2/gen-ai/indexing_jobs/{uuid}/cancel`.

        Args:
          body_uuid: A unique identifier for an indexing job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_uuid:
            raise ValueError(f"Expected a non-empty value for `path_uuid` but received {path_uuid!r}")
        return self._put(
            f"/v2/genai/indexing_jobs/{path_uuid}/cancel",
            body=maybe_transform(
                {"body_uuid": body_uuid}, indexing_job_update_cancel_params.IndexingJobUpdateCancelParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobUpdateCancelResponse,
        )


class AsyncIndexingJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndexingJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndexingJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexingJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncIndexingJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data_source_uuids: List[str] | NotGiven = NOT_GIVEN,
        knowledge_base_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexingJobCreateResponse:
        """
        To start an indexing job for a knowledge base, send a POST request to
        `/v2/gen-ai/indexing_jobs`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/genai/indexing_jobs",
            body=await async_maybe_transform(
                {
                    "data_source_uuids": data_source_uuids,
                    "knowledge_base_uuid": knowledge_base_uuid,
                },
                indexing_job_create_params.IndexingJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobCreateResponse,
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
    ) -> IndexingJobRetrieveResponse:
        """
        To get status of an indexing Job for a knowledge base, send a GET request to
        `/v2/gen-ai/indexing_jobs/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/v2/genai/indexing_jobs/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexingJobListResponse:
        """
        To list all indexing jobs for a knowledge base, send a GET request to
        `/v2/gen-ai/indexing_jobs`.

        Args:
          page: page number.

          per_page: items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/genai/indexing_jobs",
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
                    indexing_job_list_params.IndexingJobListParams,
                ),
            ),
            cast_to=IndexingJobListResponse,
        )

    async def retrieve_data_sources(
        self,
        indexing_job_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexingJobRetrieveDataSourcesResponse:
        """
        To list all datasources for an indexing job, send a GET request to
        `/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not indexing_job_uuid:
            raise ValueError(f"Expected a non-empty value for `indexing_job_uuid` but received {indexing_job_uuid!r}")
        return await self._get(
            f"/v2/genai/indexing_jobs/{indexing_job_uuid}/data_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveDataSourcesResponse,
        )

    async def update_cancel(
        self,
        path_uuid: str,
        *,
        body_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexingJobUpdateCancelResponse:
        """
        To cancel an indexing job for a knowledge base, send a PUT request to
        `/v2/gen-ai/indexing_jobs/{uuid}/cancel`.

        Args:
          body_uuid: A unique identifier for an indexing job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_uuid:
            raise ValueError(f"Expected a non-empty value for `path_uuid` but received {path_uuid!r}")
        return await self._put(
            f"/v2/genai/indexing_jobs/{path_uuid}/cancel",
            body=await async_maybe_transform(
                {"body_uuid": body_uuid}, indexing_job_update_cancel_params.IndexingJobUpdateCancelParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobUpdateCancelResponse,
        )


class IndexingJobsResourceWithRawResponse:
    def __init__(self, indexing_jobs: IndexingJobsResource) -> None:
        self._indexing_jobs = indexing_jobs

        self.create = to_raw_response_wrapper(
            indexing_jobs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            indexing_jobs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            indexing_jobs.list,
        )
        self.retrieve_data_sources = to_raw_response_wrapper(
            indexing_jobs.retrieve_data_sources,
        )
        self.update_cancel = to_raw_response_wrapper(
            indexing_jobs.update_cancel,
        )


class AsyncIndexingJobsResourceWithRawResponse:
    def __init__(self, indexing_jobs: AsyncIndexingJobsResource) -> None:
        self._indexing_jobs = indexing_jobs

        self.create = async_to_raw_response_wrapper(
            indexing_jobs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            indexing_jobs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            indexing_jobs.list,
        )
        self.retrieve_data_sources = async_to_raw_response_wrapper(
            indexing_jobs.retrieve_data_sources,
        )
        self.update_cancel = async_to_raw_response_wrapper(
            indexing_jobs.update_cancel,
        )


class IndexingJobsResourceWithStreamingResponse:
    def __init__(self, indexing_jobs: IndexingJobsResource) -> None:
        self._indexing_jobs = indexing_jobs

        self.create = to_streamed_response_wrapper(
            indexing_jobs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            indexing_jobs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            indexing_jobs.list,
        )
        self.retrieve_data_sources = to_streamed_response_wrapper(
            indexing_jobs.retrieve_data_sources,
        )
        self.update_cancel = to_streamed_response_wrapper(
            indexing_jobs.update_cancel,
        )


class AsyncIndexingJobsResourceWithStreamingResponse:
    def __init__(self, indexing_jobs: AsyncIndexingJobsResource) -> None:
        self._indexing_jobs = indexing_jobs

        self.create = async_to_streamed_response_wrapper(
            indexing_jobs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            indexing_jobs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            indexing_jobs.list,
        )
        self.retrieve_data_sources = async_to_streamed_response_wrapper(
            indexing_jobs.retrieve_data_sources,
        )
        self.update_cancel = async_to_streamed_response_wrapper(
            indexing_jobs.update_cancel,
        )
