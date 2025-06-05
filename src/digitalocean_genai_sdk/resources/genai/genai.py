# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import genai_retrieve_regions_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .auth.auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .agents.agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)
from .indexing_jobs import (
    IndexingJobsResource,
    AsyncIndexingJobsResource,
    IndexingJobsResourceWithRawResponse,
    AsyncIndexingJobsResourceWithRawResponse,
    IndexingJobsResourceWithStreamingResponse,
    AsyncIndexingJobsResourceWithStreamingResponse,
)
from .models.models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .providers.providers import (
    ProvidersResource,
    AsyncProvidersResource,
    ProvidersResourceWithRawResponse,
    AsyncProvidersResourceWithRawResponse,
    ProvidersResourceWithStreamingResponse,
    AsyncProvidersResourceWithStreamingResponse,
)
from .knowledge_bases.knowledge_bases import (
    KnowledgeBasesResource,
    AsyncKnowledgeBasesResource,
    KnowledgeBasesResourceWithRawResponse,
    AsyncKnowledgeBasesResourceWithRawResponse,
    KnowledgeBasesResourceWithStreamingResponse,
    AsyncKnowledgeBasesResourceWithStreamingResponse,
)
from ...types.genai_retrieve_regions_response import GenaiRetrieveRegionsResponse

__all__ = ["GenaiResource", "AsyncGenaiResource"]


class GenaiResource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

    @cached_property
    def providers(self) -> ProvidersResource:
        return ProvidersResource(self._client)

    @cached_property
    def auth(self) -> AuthResource:
        return AuthResource(self._client)

    @cached_property
    def indexing_jobs(self) -> IndexingJobsResource:
        return IndexingJobsResource(self._client)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResource:
        return KnowledgeBasesResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenaiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return GenaiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenaiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return GenaiResourceWithStreamingResponse(self)

    def retrieve_regions(
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
    ) -> GenaiRetrieveRegionsResponse:
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
            "/v2/genai/regions",
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
                    genai_retrieve_regions_params.GenaiRetrieveRegionsParams,
                ),
            ),
            cast_to=GenaiRetrieveRegionsResponse,
        )


class AsyncGenaiResource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

    @cached_property
    def providers(self) -> AsyncProvidersResource:
        return AsyncProvidersResource(self._client)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        return AsyncAuthResource(self._client)

    @cached_property
    def indexing_jobs(self) -> AsyncIndexingJobsResource:
        return AsyncIndexingJobsResource(self._client)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResource:
        return AsyncKnowledgeBasesResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenaiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenaiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenaiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return AsyncGenaiResourceWithStreamingResponse(self)

    async def retrieve_regions(
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
    ) -> GenaiRetrieveRegionsResponse:
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
            "/v2/genai/regions",
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
                    genai_retrieve_regions_params.GenaiRetrieveRegionsParams,
                ),
            ),
            cast_to=GenaiRetrieveRegionsResponse,
        )


class GenaiResourceWithRawResponse:
    def __init__(self, genai: GenaiResource) -> None:
        self._genai = genai

        self.retrieve_regions = to_raw_response_wrapper(
            genai.retrieve_regions,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._genai.agents)

    @cached_property
    def providers(self) -> ProvidersResourceWithRawResponse:
        return ProvidersResourceWithRawResponse(self._genai.providers)

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._genai.auth)

    @cached_property
    def indexing_jobs(self) -> IndexingJobsResourceWithRawResponse:
        return IndexingJobsResourceWithRawResponse(self._genai.indexing_jobs)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResourceWithRawResponse:
        return KnowledgeBasesResourceWithRawResponse(self._genai.knowledge_bases)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._genai.models)


class AsyncGenaiResourceWithRawResponse:
    def __init__(self, genai: AsyncGenaiResource) -> None:
        self._genai = genai

        self.retrieve_regions = async_to_raw_response_wrapper(
            genai.retrieve_regions,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._genai.agents)

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithRawResponse:
        return AsyncProvidersResourceWithRawResponse(self._genai.providers)

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._genai.auth)

    @cached_property
    def indexing_jobs(self) -> AsyncIndexingJobsResourceWithRawResponse:
        return AsyncIndexingJobsResourceWithRawResponse(self._genai.indexing_jobs)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResourceWithRawResponse:
        return AsyncKnowledgeBasesResourceWithRawResponse(self._genai.knowledge_bases)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._genai.models)


class GenaiResourceWithStreamingResponse:
    def __init__(self, genai: GenaiResource) -> None:
        self._genai = genai

        self.retrieve_regions = to_streamed_response_wrapper(
            genai.retrieve_regions,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._genai.agents)

    @cached_property
    def providers(self) -> ProvidersResourceWithStreamingResponse:
        return ProvidersResourceWithStreamingResponse(self._genai.providers)

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._genai.auth)

    @cached_property
    def indexing_jobs(self) -> IndexingJobsResourceWithStreamingResponse:
        return IndexingJobsResourceWithStreamingResponse(self._genai.indexing_jobs)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResourceWithStreamingResponse:
        return KnowledgeBasesResourceWithStreamingResponse(self._genai.knowledge_bases)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._genai.models)


class AsyncGenaiResourceWithStreamingResponse:
    def __init__(self, genai: AsyncGenaiResource) -> None:
        self._genai = genai

        self.retrieve_regions = async_to_streamed_response_wrapper(
            genai.retrieve_regions,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._genai.agents)

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithStreamingResponse:
        return AsyncProvidersResourceWithStreamingResponse(self._genai.providers)

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._genai.auth)

    @cached_property
    def indexing_jobs(self) -> AsyncIndexingJobsResourceWithStreamingResponse:
        return AsyncIndexingJobsResourceWithStreamingResponse(self._genai.indexing_jobs)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self._genai.knowledge_bases)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._genai.models)
