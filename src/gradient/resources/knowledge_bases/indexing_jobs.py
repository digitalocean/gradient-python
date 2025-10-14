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
from ...types.knowledge_bases import (
    indexing_job_list_params,
    indexing_job_create_params,
    indexing_job_update_cancel_params,
)
from ...types.knowledge_bases.indexing_job_list_response import IndexingJobListResponse
from ...types.knowledge_bases.indexing_job_create_response import IndexingJobCreateResponse
from ...types.knowledge_bases.indexing_job_retrieve_response import IndexingJobRetrieveResponse
from ...types.knowledge_bases.indexing_job_update_cancel_response import IndexingJobUpdateCancelResponse
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
        timeout: float | None = 300.0,
        poll_interval: float = 2.0,
        raise_on_failure: bool = True,
    ) -> IndexingJobRetrieveResponse:
        """
        Poll the indexing job until it reaches a terminal state.

        Args:
          uuid: The indexing job uuid to poll.
          timeout: Maximum time in seconds to wait (None for no timeout). Defaults to 300s.
          poll_interval: Seconds between polls. Defaults to 2.0s.
          raise_on_failure: If True, raise a RuntimeError when the job reaches a failed/cancelled/error state.

        Returns:
          The final `IndexingJobRetrieveResponse` when the job is in a terminal state.

        Raises:
          TimeoutError: If the timeout is exceeded.
          RuntimeError: If `raise_on_failure` is True and the job failed/cancelled/errored.
        """
        import time

        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")

        start = time.time()
        while True:
            resp = self.retrieve(uuid)
            job = getattr(resp, "job", None)
            phase = getattr(job, "phase", None) if job is not None else None
            status = getattr(job, "status", None) if job is not None else None

            # Terminal phases
            if phase == "BATCH_JOB_PHASE_SUCCEEDED" or status in ("INDEX_JOB_STATUS_COMPLETED",):
                return resp

            # Failure phases
            if phase in ("BATCH_JOB_PHASE_FAILED", "BATCH_JOB_PHASE_ERROR", "BATCH_JOB_PHASE_CANCELLED") or (
                status in ("INDEX_JOB_STATUS_FAILED",)
            ):
                if raise_on_failure:
                    raise RuntimeError(f"Indexing job {uuid} finished with failure phase={phase} status={status}")
                return resp

            # Still running or pending
            if timeout is not None and (time.time() - start) > timeout:
                raise TimeoutError(f"Timed out waiting for indexing job {uuid} after {timeout} seconds")

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
        timeout: float | None = 300.0,
        poll_interval: float = 2.0,
        raise_on_failure: bool = True,
    ) -> IndexingJobRetrieveResponse:
        """
        Asynchronously poll the indexing job until it reaches a terminal state.

        Args:
          uuid: The indexing job uuid to poll.
          timeout: Maximum time in seconds to wait (None for no timeout). Defaults to 300s.
          poll_interval: Seconds between polls. Defaults to 2.0s.
          raise_on_failure: If True, raise a RuntimeError when the job reaches a failed/cancelled/error state.

        Returns:
          The final `IndexingJobRetrieveResponse` when the job is in a terminal state.

        Raises:
          TimeoutError: If the timeout is exceeded.
          RuntimeError: If `raise_on_failure` is True and the job failed/cancelled/errored.
        """
        import time
        import asyncio

        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")

        start = time.time()
        while True:
            resp = await self.retrieve(uuid)
            job = getattr(resp, "job", None)
            phase = getattr(job, "phase", None) if job is not None else None
            status = getattr(job, "status", None) if job is not None else None

            # Terminal phases
            if phase == "BATCH_JOB_PHASE_SUCCEEDED" or status in ("INDEX_JOB_STATUS_COMPLETED",):
                return resp

            # Failure phases
            if phase in ("BATCH_JOB_PHASE_FAILED", "BATCH_JOB_PHASE_ERROR", "BATCH_JOB_PHASE_CANCELLED") or (
                status in ("INDEX_JOB_STATUS_FAILED",)
            ):
                if raise_on_failure:
                    raise RuntimeError(f"Indexing job {uuid} finished with failure phase={phase} status={status}")
                return resp

            # Still running or pending
            if timeout is not None and (time.time() - start) > timeout:
                raise TimeoutError(f"Timed out waiting for indexing job {uuid} after {timeout} seconds")

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
