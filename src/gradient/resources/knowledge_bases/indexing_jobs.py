# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
import asyncio

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
from ..._exceptions import IndexingJobError, IndexingJobTimeoutError
from ..._base_client import make_request_options
from ...types.knowledge_bases import (
    indexing_job_list_params,
    indexing_job_create_params,
    indexing_job_update_cancel_params,
)
from ...types.knowledge_bases.indexing_job_list_response import IndexingJobListResponse
from ...types.knowledge_bases.indexing_job_create_response import IndexingJobCreateResponse
from ...types.knowledge_bases.indexing_job_retrieve_response import IndexingJobRetrieveResponse
from ...types.knowledge_bases.indexing_job_update_cancel_response import IndexingJobUpdateCancelResponse
from ...types.knowledge_bases.indexing_job_retrieve_signed_url_response import IndexingJobRetrieveSignedURLResponse
from ...types.knowledge_bases.indexing_job_retrieve_data_sources_response import IndexingJobRetrieveDataSourcesResponse

__all__ = ["IndexingJobsResource", "AsyncIndexingJobsResource"]


class IndexingJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndexingJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return IndexingJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexingJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return IndexingJobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data_source_uuids: SequenceNotStr[str] | Omit = omit,
        knowledge_base_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingJobCreateResponse:
        """
        To start an indexing job for a knowledge base, send a POST request to
        `/v2/gen-ai/indexing_jobs`.

        Args:
          data_source_uuids: List of data source ids to index, if none are provided, all data sources will be
              indexed

          knowledge_base_uuid: Knowledge base id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/indexing_jobs"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/indexing_jobs",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v2/gen-ai/indexing_jobs/{uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/indexing_jobs/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingJobListResponse:
        """
        To list all indexing jobs for a knowledge base, send a GET request to
        `/v2/gen-ai/indexing_jobs`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gen-ai/indexing_jobs"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/indexing_jobs",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveDataSourcesResponse,
        )

    def retrieve_signed_url(
        self,
        indexing_job_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingJobRetrieveSignedURLResponse:
        """
        To get a signed URL for indexing job details, send a GET request to
        `/v2/gen-ai/indexing_jobs/{uuid}/details_signed_url`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not indexing_job_uuid:
            raise ValueError(f"Expected a non-empty value for `indexing_job_uuid` but received {indexing_job_uuid!r}")
        return self._get(
            f"/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/details_signed_url"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/details_signed_url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveSignedURLResponse,
        )

    def update_cancel(
        self,
        path_uuid: str,
        *,
        body_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v2/gen-ai/indexing_jobs/{path_uuid}/cancel"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/indexing_jobs/{path_uuid}/cancel",
            body=maybe_transform(
                {"body_uuid": body_uuid}, indexing_job_update_cancel_params.IndexingJobUpdateCancelParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobUpdateCancelResponse,
        )

    def wait_for_completion(
        self,
        uuid: str,
        *,
        poll_interval: float = 5,
        timeout: float | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingJobRetrieveResponse:
        """
        Wait for an indexing job to complete by polling its status.

        This method polls the indexing job status at regular intervals until it reaches
        a terminal state (succeeded, failed, error, or cancelled). It raises an exception
        if the job fails or times out.

        Args:
          uuid: The UUID of the indexing job to wait for.

          poll_interval: Time in seconds between status checks (default: 5 seconds).

          timeout: Maximum time in seconds to wait for completion. If None, waits indefinitely.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          request_timeout: Override the client-level default timeout for this request, in seconds

        Returns:
          The final IndexingJobRetrieveResponse when the job completes successfully.

        Raises:
          IndexingJobTimeoutError: If the job doesn't complete within the specified timeout.
          IndexingJobError: If the job fails, errors, or is cancelled.
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")

        start_time = time.time()

        while True:
            response = self.retrieve(
                uuid,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=request_timeout,
            )

            # Check if job is in a terminal state
            if response.job and response.job.phase:
                phase = response.job.phase

                # Success state
                if phase == "BATCH_JOB_PHASE_SUCCEEDED":
                    return response

                # Failure states
                if phase == "BATCH_JOB_PHASE_FAILED":
                    raise IndexingJobError(
                        f"Indexing job {uuid} failed. ",
                        uuid=uuid,
                        phase=phase,
                    )

                if phase == "BATCH_JOB_PHASE_ERROR":
                    raise IndexingJobError(
                        f"Indexing job {uuid} encountered an error",
                        uuid=uuid,
                        phase=phase,
                    )

                if phase == "BATCH_JOB_PHASE_CANCELLED":
                    raise IndexingJobError(
                        f"Indexing job {uuid} was cancelled",
                        uuid=uuid,
                        phase=phase,
                    )

                # Still in progress (UNKNOWN, PENDING, or RUNNING)
                # Check timeout
                if timeout is not None:
                    elapsed = time.time() - start_time
                    if elapsed >= timeout:
                        raise IndexingJobTimeoutError(
                            f"Indexing job {uuid} did not complete within {timeout} seconds. Current phase: {phase}",
                            uuid=uuid,
                            phase=phase,
                            timeout=timeout,
                        )

            # Wait before next poll
            time.sleep(poll_interval)


class AsyncIndexingJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndexingJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndexingJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexingJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncIndexingJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data_source_uuids: SequenceNotStr[str] | Omit = omit,
        knowledge_base_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingJobCreateResponse:
        """
        To start an indexing job for a knowledge base, send a POST request to
        `/v2/gen-ai/indexing_jobs`.

        Args:
          data_source_uuids: List of data source ids to index, if none are provided, all data sources will be
              indexed

          knowledge_base_uuid: Knowledge base id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/indexing_jobs"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/indexing_jobs",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v2/gen-ai/indexing_jobs/{uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/indexing_jobs/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingJobListResponse:
        """
        To list all indexing jobs for a knowledge base, send a GET request to
        `/v2/gen-ai/indexing_jobs`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gen-ai/indexing_jobs"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/indexing_jobs",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveDataSourcesResponse,
        )

    async def retrieve_signed_url(
        self,
        indexing_job_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingJobRetrieveSignedURLResponse:
        """
        To get a signed URL for indexing job details, send a GET request to
        `/v2/gen-ai/indexing_jobs/{uuid}/details_signed_url`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not indexing_job_uuid:
            raise ValueError(f"Expected a non-empty value for `indexing_job_uuid` but received {indexing_job_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/details_signed_url"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/indexing_jobs/{indexing_job_uuid}/details_signed_url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobRetrieveSignedURLResponse,
        )

    async def update_cancel(
        self,
        path_uuid: str,
        *,
        body_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/v2/gen-ai/indexing_jobs/{path_uuid}/cancel"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/indexing_jobs/{path_uuid}/cancel",
            body=await async_maybe_transform(
                {"body_uuid": body_uuid}, indexing_job_update_cancel_params.IndexingJobUpdateCancelParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexingJobUpdateCancelResponse,
        )

    async def wait_for_completion(
        self,
        uuid: str,
        *,
        poll_interval: float = 5,
        timeout: float | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexingJobRetrieveResponse:
        """
        Wait for an indexing job to complete by polling its status.

        This method polls the indexing job status at regular intervals until it reaches
        a terminal state (succeeded, failed, error, or cancelled). It raises an exception
        if the job fails or times out.

        Args:
          uuid: The UUID of the indexing job to wait for.

          poll_interval: Time in seconds between status checks (default: 5 seconds).

          timeout: Maximum time in seconds to wait for completion. If None, waits indefinitely.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          request_timeout: Override the client-level default timeout for this request, in seconds

        Returns:
          The final IndexingJobRetrieveResponse when the job completes successfully.

        Raises:
          IndexingJobTimeoutError: If the job doesn't complete within the specified timeout.
          IndexingJobError: If the job fails, errors, or is cancelled.
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")

        start_time = time.time()

        while True:
            response = await self.retrieve(
                uuid,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=request_timeout,
            )

            # Check if job is in a terminal state
            if response.job and response.job.phase:
                phase = response.job.phase

                # Success state
                if phase == "BATCH_JOB_PHASE_SUCCEEDED":
                    return response

                # Failure states
                if phase == "BATCH_JOB_PHASE_FAILED":
                    raise IndexingJobError(
                        f"Indexing job {uuid} failed. ",
                        uuid=uuid,
                        phase=phase,
                    )

                if phase == "BATCH_JOB_PHASE_ERROR":
                    raise IndexingJobError(
                        f"Indexing job {uuid} encountered an error",
                        uuid=uuid,
                        phase=phase,
                    )

                if phase == "BATCH_JOB_PHASE_CANCELLED":
                    raise IndexingJobError(
                        f"Indexing job {uuid} was cancelled",
                        uuid=uuid,
                        phase=phase,
                    )

                # Still in progress (UNKNOWN, PENDING, or RUNNING)
                # Check timeout
                if timeout is not None:
                    elapsed = time.time() - start_time
                    if elapsed >= timeout:
                        raise IndexingJobTimeoutError(
                            f"Indexing job {uuid} did not complete within {timeout} seconds. Current phase: {phase}",
                            uuid=uuid,
                            phase=phase,
                            timeout=timeout,
                        )

            # Wait before next poll
            await asyncio.sleep(poll_interval)


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
        self.retrieve_signed_url = to_raw_response_wrapper(
            indexing_jobs.retrieve_signed_url,
        )
        self.update_cancel = to_raw_response_wrapper(
            indexing_jobs.update_cancel,
        )
        self.wait_for_completion = to_raw_response_wrapper(
            indexing_jobs.wait_for_completion,
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
        self.retrieve_signed_url = async_to_raw_response_wrapper(
            indexing_jobs.retrieve_signed_url,
        )
        self.update_cancel = async_to_raw_response_wrapper(
            indexing_jobs.update_cancel,
        )
        self.wait_for_completion = async_to_raw_response_wrapper(
            indexing_jobs.wait_for_completion,
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
        self.retrieve_signed_url = to_streamed_response_wrapper(
            indexing_jobs.retrieve_signed_url,
        )
        self.update_cancel = to_streamed_response_wrapper(
            indexing_jobs.update_cancel,
        )
        self.wait_for_completion = to_streamed_response_wrapper(
            indexing_jobs.wait_for_completion,
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
        self.retrieve_signed_url = async_to_streamed_response_wrapper(
            indexing_jobs.retrieve_signed_url,
        )
        self.update_cancel = async_to_streamed_response_wrapper(
            indexing_jobs.update_cancel,
        )
        self.wait_for_completion = async_to_streamed_response_wrapper(
            indexing_jobs.wait_for_completion,
        )
