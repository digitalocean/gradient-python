# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
import asyncio
from typing import Iterable

import httpx

from ...types import (
    knowledge_base_list_params,
    knowledge_base_create_params,
    knowledge_base_update_params,
)
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .data_sources import (
    DataSourcesResource,
    AsyncDataSourcesResource,
    DataSourcesResourceWithRawResponse,
    AsyncDataSourcesResourceWithRawResponse,
    DataSourcesResourceWithStreamingResponse,
    AsyncDataSourcesResourceWithStreamingResponse,
)
from .indexing_jobs import (
    IndexingJobsResource,
    AsyncIndexingJobsResource,
    IndexingJobsResourceWithRawResponse,
    AsyncIndexingJobsResourceWithRawResponse,
    IndexingJobsResourceWithStreamingResponse,
    AsyncIndexingJobsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.knowledge_base_list_response import KnowledgeBaseListResponse
from ...types.knowledge_base_create_response import KnowledgeBaseCreateResponse
from ...types.knowledge_base_delete_response import KnowledgeBaseDeleteResponse
from ...types.knowledge_base_update_response import KnowledgeBaseUpdateResponse
from ...types.knowledge_base_retrieve_response import KnowledgeBaseRetrieveResponse
from ...types.knowledge_base_list_indexing_jobs_response import (
    KnowledgeBaseListIndexingJobsResponse,
)

__all__ = [
    "KnowledgeBasesResource",
    "AsyncKnowledgeBasesResource",
    "KnowledgeBaseDatabaseError",
    "KnowledgeBaseTimeoutError",
]


class KnowledgeBaseDatabaseError(Exception):
    """Raised when a knowledge base database enters a failed state."""

    pass


class KnowledgeBaseTimeoutError(Exception):
    """Raised when waiting for a knowledge base database times out."""

    pass


class KnowledgeBasesResource(SyncAPIResource):
    @cached_property
    def data_sources(self) -> DataSourcesResource:
        return DataSourcesResource(self._client)

    @cached_property
    def indexing_jobs(self) -> IndexingJobsResource:
        return IndexingJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> KnowledgeBasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return KnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeBasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return KnowledgeBasesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        database_id: str | Omit = omit,
        datasources: Iterable[knowledge_base_create_params.Datasource] | Omit = omit,
        embedding_model_uuid: str | Omit = omit,
        name: str | Omit = omit,
        project_id: str | Omit = omit,
        region: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseCreateResponse:
        """
        To create a knowledge base, send a POST request to `/v2/gen-ai/knowledge_bases`.

        Args:
          database_id: Identifier of the DigitalOcean OpenSearch database this knowledge base will use,
              optional. If not provided, we create a new database for the knowledge base in
              the same region as the knowledge base.

          datasources: The data sources to use for this knowledge base. See
              [Organize Data Sources](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#spaces-buckets)
              for more information on data sources best practices.

          embedding_model_uuid: Identifier for the
              [embedding model](https://docs.digitalocean.com/products/genai-platform/details/models/#embedding-models).

          name: Name of the knowledge base.

          project_id: Identifier of the DigitalOcean project this knowledge base will belong to.

          region: The datacenter region to deploy the knowledge base in.

          tags: Tags to organize your knowledge base.

          vpc_uuid: The VPC to deploy the knowledge base database in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            (
                "/v2/gen-ai/knowledge_bases"
                if self._client._base_url_overridden
                else "https://api.digitalocean.com/v2/gen-ai/knowledge_bases"
            ),
            body=maybe_transform(
                {
                    "database_id": database_id,
                    "datasources": datasources,
                    "embedding_model_uuid": embedding_model_uuid,
                    "name": name,
                    "project_id": project_id,
                    "region": region,
                    "tags": tags,
                    "vpc_uuid": vpc_uuid,
                },
                knowledge_base_create_params.KnowledgeBaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseCreateResponse,
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
    ) -> KnowledgeBaseRetrieveResponse:
        """
        To retrive information about an existing knowledge base, send a GET request to
        `/v2/gen-ai/knowledge_bases/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(
                f"Expected a non-empty value for `uuid` but received {uuid!r}"
            )
        return self._get(
            (
                f"/v2/gen-ai/knowledge_bases/{uuid}"
                if self._client._base_url_overridden
                else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{uuid}"
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseRetrieveResponse,
        )

    def update(
        self,
        path_uuid: str,
        *,
        database_id: str | Omit = omit,
        embedding_model_uuid: str | Omit = omit,
        name: str | Omit = omit,
        project_id: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        body_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseUpdateResponse:
        """
        To update a knowledge base, send a PUT request to
        `/v2/gen-ai/knowledge_bases/{uuid}`.

        Args:
          database_id: The id of the DigitalOcean database this knowledge base will use, optiona.

          embedding_model_uuid: Identifier for the foundation model.

          name: Knowledge base name

          project_id: The id of the DigitalOcean project this knowledge base will belong to

          tags: Tags to organize your knowledge base.

          body_uuid: Knowledge base id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_uuid` but received {path_uuid!r}"
            )
        return self._put(
            (
                f"/v2/gen-ai/knowledge_bases/{path_uuid}"
                if self._client._base_url_overridden
                else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{path_uuid}"
            ),
            body=maybe_transform(
                {
                    "database_id": database_id,
                    "embedding_model_uuid": embedding_model_uuid,
                    "name": name,
                    "project_id": project_id,
                    "tags": tags,
                    "body_uuid": body_uuid,
                },
                knowledge_base_update_params.KnowledgeBaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseUpdateResponse,
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
    ) -> KnowledgeBaseListResponse:
        """
        To list all knowledge bases, send a GET request to `/v2/gen-ai/knowledge_bases`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            (
                "/v2/gen-ai/knowledge_bases"
                if self._client._base_url_overridden
                else "https://api.digitalocean.com/v2/gen-ai/knowledge_bases"
            ),
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
                    knowledge_base_list_params.KnowledgeBaseListParams,
                ),
            ),
            cast_to=KnowledgeBaseListResponse,
        )

    def delete(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseDeleteResponse:
        """
        To delete a knowledge base, send a DELETE request to
        `/v2/gen-ai/knowledge_bases/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(
                f"Expected a non-empty value for `uuid` but received {uuid!r}"
            )
        return self._delete(
            (
                f"/v2/gen-ai/knowledge_bases/{uuid}"
                if self._client._base_url_overridden
                else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{uuid}"
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseDeleteResponse,
        )

    def wait_for_database(
        self,
        uuid: str,
        *,
        timeout: float = 600.0,
        poll_interval: float = 5.0,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> KnowledgeBaseRetrieveResponse:
        """
        Poll the knowledge base until the database status is ONLINE or a failed state is reached.

        This helper function repeatedly calls retrieve() to check the database_status field.
        It will wait for the database to become ONLINE, or raise an exception if it enters
        a failed state (DECOMMISSIONED or UNHEALTHY) or if the timeout is exceeded.

        Args:
          uuid: The knowledge base UUID to poll

          timeout: Maximum time to wait in seconds (default: 600 seconds / 10 minutes)

          poll_interval: Time to wait between polls in seconds (default: 5 seconds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

        Returns:
          The final KnowledgeBaseRetrieveResponse when the database status is ONLINE

        Raises:
          KnowledgeBaseDatabaseError: If the database enters a failed state (DECOMMISSIONED, UNHEALTHY)

          KnowledgeBaseTimeoutError: If the timeout is exceeded before the database becomes ONLINE
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")

        start_time = time.time()
        failed_states = {"DECOMMISSIONED", "UNHEALTHY"}

        while True:
            elapsed = time.time() - start_time
            if elapsed >= timeout:
                raise KnowledgeBaseTimeoutError(
                    f"Timeout waiting for knowledge base database to become ready. "
                    f"Database did not reach ONLINE status within {timeout} seconds."
                )

            response = self.retrieve(
                uuid,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

            status = response.database_status

            if status == "ONLINE":
                return response

            if status in failed_states:
                raise KnowledgeBaseDatabaseError(f"Knowledge base database entered failed state: {status}")

            # Sleep before next poll, but don't exceed timeout
            remaining_time = timeout - elapsed
            sleep_time = min(poll_interval, remaining_time)
            if sleep_time > 0:
                time.sleep(sleep_time)

    def list_indexing_jobs(
        self,
        knowledge_base_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseListIndexingJobsResponse:
        """
        To list latest 15 indexing jobs for a knowledge base, send a GET request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/indexing_jobs`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `knowledge_base_uuid` but received {knowledge_base_uuid!r}"
            )
        return self._get(
            (
                f"/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/indexing_jobs"
                if self._client._base_url_overridden
                else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/indexing_jobs"
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseListIndexingJobsResponse,
        )


class AsyncKnowledgeBasesResource(AsyncAPIResource):
    @cached_property
    def data_sources(self) -> AsyncDataSourcesResource:
        return AsyncDataSourcesResource(self._client)

    @cached_property
    def indexing_jobs(self) -> AsyncIndexingJobsResource:
        return AsyncIndexingJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeBasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        database_id: str | Omit = omit,
        datasources: Iterable[knowledge_base_create_params.Datasource] | Omit = omit,
        embedding_model_uuid: str | Omit = omit,
        name: str | Omit = omit,
        project_id: str | Omit = omit,
        region: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseCreateResponse:
        """
        To create a knowledge base, send a POST request to `/v2/gen-ai/knowledge_bases`.

        Args:
          database_id: Identifier of the DigitalOcean OpenSearch database this knowledge base will use,
              optional. If not provided, we create a new database for the knowledge base in
              the same region as the knowledge base.

          datasources: The data sources to use for this knowledge base. See
              [Organize Data Sources](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#spaces-buckets)
              for more information on data sources best practices.

          embedding_model_uuid: Identifier for the
              [embedding model](https://docs.digitalocean.com/products/genai-platform/details/models/#embedding-models).

          name: Name of the knowledge base.

          project_id: Identifier of the DigitalOcean project this knowledge base will belong to.

          region: The datacenter region to deploy the knowledge base in.

          tags: Tags to organize your knowledge base.

          vpc_uuid: The VPC to deploy the knowledge base database in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            (
                "/v2/gen-ai/knowledge_bases"
                if self._client._base_url_overridden
                else "https://api.digitalocean.com/v2/gen-ai/knowledge_bases"
            ),
            body=await async_maybe_transform(
                {
                    "database_id": database_id,
                    "datasources": datasources,
                    "embedding_model_uuid": embedding_model_uuid,
                    "name": name,
                    "project_id": project_id,
                    "region": region,
                    "tags": tags,
                    "vpc_uuid": vpc_uuid,
                },
                knowledge_base_create_params.KnowledgeBaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseCreateResponse,
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
    ) -> KnowledgeBaseRetrieveResponse:
        """
        To retrive information about an existing knowledge base, send a GET request to
        `/v2/gen-ai/knowledge_bases/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(
                f"Expected a non-empty value for `uuid` but received {uuid!r}"
            )
        return await self._get(
            (
                f"/v2/gen-ai/knowledge_bases/{uuid}"
                if self._client._base_url_overridden
                else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{uuid}"
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseRetrieveResponse,
        )

    async def update(
        self,
        path_uuid: str,
        *,
        database_id: str | Omit = omit,
        embedding_model_uuid: str | Omit = omit,
        name: str | Omit = omit,
        project_id: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        body_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseUpdateResponse:
        """
        To update a knowledge base, send a PUT request to
        `/v2/gen-ai/knowledge_bases/{uuid}`.

        Args:
          database_id: The id of the DigitalOcean database this knowledge base will use, optiona.

          embedding_model_uuid: Identifier for the foundation model.

          name: Knowledge base name

          project_id: The id of the DigitalOcean project this knowledge base will belong to

          tags: Tags to organize your knowledge base.

          body_uuid: Knowledge base id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_uuid` but received {path_uuid!r}"
            )
        return await self._put(
            (
                f"/v2/gen-ai/knowledge_bases/{path_uuid}"
                if self._client._base_url_overridden
                else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{path_uuid}"
            ),
            body=await async_maybe_transform(
                {
                    "database_id": database_id,
                    "embedding_model_uuid": embedding_model_uuid,
                    "name": name,
                    "project_id": project_id,
                    "tags": tags,
                    "body_uuid": body_uuid,
                },
                knowledge_base_update_params.KnowledgeBaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseUpdateResponse,
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
    ) -> KnowledgeBaseListResponse:
        """
        To list all knowledge bases, send a GET request to `/v2/gen-ai/knowledge_bases`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            (
                "/v2/gen-ai/knowledge_bases"
                if self._client._base_url_overridden
                else "https://api.digitalocean.com/v2/gen-ai/knowledge_bases"
            ),
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
                    knowledge_base_list_params.KnowledgeBaseListParams,
                ),
            ),
            cast_to=KnowledgeBaseListResponse,
        )

    async def delete(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseDeleteResponse:
        """
        To delete a knowledge base, send a DELETE request to
        `/v2/gen-ai/knowledge_bases/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(
                f"Expected a non-empty value for `uuid` but received {uuid!r}"
            )
        return await self._delete(
            (
                f"/v2/gen-ai/knowledge_bases/{uuid}"
                if self._client._base_url_overridden
                else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{uuid}"
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseDeleteResponse,
        )

    async def wait_for_database(
        self,
        uuid: str,
        *,
        timeout: float = 600.0,
        poll_interval: float = 5.0,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> KnowledgeBaseRetrieveResponse:
        """
        Poll the knowledge base until the database status is ONLINE or a failed state is reached.

        This helper function repeatedly calls retrieve() to check the database_status field.
        It will wait for the database to become ONLINE, or raise an exception if it enters
        a failed state (DECOMMISSIONED or UNHEALTHY) or if the timeout is exceeded.

        Args:
          uuid: The knowledge base UUID to poll

          timeout: Maximum time to wait in seconds (default: 600 seconds / 10 minutes)

          poll_interval: Time to wait between polls in seconds (default: 5 seconds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

        Returns:
          The final KnowledgeBaseRetrieveResponse when the database status is ONLINE

        Raises:
          KnowledgeBaseDatabaseError: If the database enters a failed state (DECOMMISSIONED, UNHEALTHY)

          KnowledgeBaseTimeoutError: If the timeout is exceeded before the database becomes ONLINE
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")

        start_time = time.time()
        failed_states = {"DECOMMISSIONED", "UNHEALTHY"}

        while True:
            elapsed = time.time() - start_time
            if elapsed >= timeout:
                raise KnowledgeBaseTimeoutError(
                    f"Timeout waiting for knowledge base database to become ready. "
                    f"Database did not reach ONLINE status within {timeout} seconds."
                )

            response = await self.retrieve(
                uuid,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

            status = response.database_status

            if status == "ONLINE":
                return response

            if status in failed_states:
                raise KnowledgeBaseDatabaseError(f"Knowledge base database entered failed state: {status}")

            # Sleep before next poll, but don't exceed timeout
            remaining_time = timeout - elapsed
            sleep_time = min(poll_interval, remaining_time)
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)

    async def list_indexing_jobs(
        self,
        knowledge_base_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseListIndexingJobsResponse:
        """
        To list latest 15 indexing jobs for a knowledge base, send a GET request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/indexing_jobs`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `knowledge_base_uuid` but received {knowledge_base_uuid!r}"
            )
        return await self._get(
            (
                f"/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/indexing_jobs"
                if self._client._base_url_overridden
                else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/indexing_jobs"
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KnowledgeBaseListIndexingJobsResponse,
        )


class KnowledgeBasesResourceWithRawResponse:
    def __init__(self, knowledge_bases: KnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.create = to_raw_response_wrapper(
            knowledge_bases.create,
        )
        self.retrieve = to_raw_response_wrapper(
            knowledge_bases.retrieve,
        )
        self.update = to_raw_response_wrapper(
            knowledge_bases.update,
        )
        self.list = to_raw_response_wrapper(
            knowledge_bases.list,
        )
        self.delete = to_raw_response_wrapper(
            knowledge_bases.delete,
        )
        self.wait_for_database = to_raw_response_wrapper(
            knowledge_bases.wait_for_database,
        )
        self.list_indexing_jobs = to_raw_response_wrapper(
            knowledge_bases.list_indexing_jobs,
        )

    @cached_property
    def data_sources(self) -> DataSourcesResourceWithRawResponse:
        return DataSourcesResourceWithRawResponse(self._knowledge_bases.data_sources)

    @cached_property
    def indexing_jobs(self) -> IndexingJobsResourceWithRawResponse:
        return IndexingJobsResourceWithRawResponse(self._knowledge_bases.indexing_jobs)


class AsyncKnowledgeBasesResourceWithRawResponse:
    def __init__(self, knowledge_bases: AsyncKnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.create = async_to_raw_response_wrapper(
            knowledge_bases.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            knowledge_bases.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            knowledge_bases.update,
        )
        self.list = async_to_raw_response_wrapper(
            knowledge_bases.list,
        )
        self.delete = async_to_raw_response_wrapper(
            knowledge_bases.delete,
        )
        self.wait_for_database = async_to_raw_response_wrapper(
            knowledge_bases.wait_for_database,
        )
        self.list_indexing_jobs = async_to_raw_response_wrapper(
            knowledge_bases.list_indexing_jobs,
        )

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResourceWithRawResponse:
        return AsyncDataSourcesResourceWithRawResponse(
            self._knowledge_bases.data_sources
        )

    @cached_property
    def indexing_jobs(self) -> AsyncIndexingJobsResourceWithRawResponse:
        return AsyncIndexingJobsResourceWithRawResponse(
            self._knowledge_bases.indexing_jobs
        )


class KnowledgeBasesResourceWithStreamingResponse:
    def __init__(self, knowledge_bases: KnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.create = to_streamed_response_wrapper(
            knowledge_bases.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            knowledge_bases.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            knowledge_bases.update,
        )
        self.list = to_streamed_response_wrapper(
            knowledge_bases.list,
        )
        self.delete = to_streamed_response_wrapper(
            knowledge_bases.delete,
        )
        self.wait_for_database = to_streamed_response_wrapper(
            knowledge_bases.wait_for_database,
        )
        self.list_indexing_jobs = to_streamed_response_wrapper(
            knowledge_bases.list_indexing_jobs,
        )

    @cached_property
    def data_sources(self) -> DataSourcesResourceWithStreamingResponse:
        return DataSourcesResourceWithStreamingResponse(
            self._knowledge_bases.data_sources
        )

    @cached_property
    def indexing_jobs(self) -> IndexingJobsResourceWithStreamingResponse:
        return IndexingJobsResourceWithStreamingResponse(
            self._knowledge_bases.indexing_jobs
        )


class AsyncKnowledgeBasesResourceWithStreamingResponse:
    def __init__(self, knowledge_bases: AsyncKnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.create = async_to_streamed_response_wrapper(
            knowledge_bases.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            knowledge_bases.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            knowledge_bases.update,
        )
        self.list = async_to_streamed_response_wrapper(
            knowledge_bases.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            knowledge_bases.delete,
        )
        self.wait_for_database = async_to_streamed_response_wrapper(
            knowledge_bases.wait_for_database,
        )
        self.list_indexing_jobs = async_to_streamed_response_wrapper(
            knowledge_bases.list_indexing_jobs,
        )

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResourceWithStreamingResponse:
        return AsyncDataSourcesResourceWithStreamingResponse(
            self._knowledge_bases.data_sources
        )

    @cached_property
    def indexing_jobs(self) -> AsyncIndexingJobsResourceWithStreamingResponse:
        return AsyncIndexingJobsResourceWithStreamingResponse(
            self._knowledge_bases.indexing_jobs
        )
