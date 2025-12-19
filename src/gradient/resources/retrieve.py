# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import retrieve_documents_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.retrieve_documents_response import RetrieveDocumentsResponse

__all__ = ["RetrieveResource", "AsyncRetrieveResource"]


class RetrieveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrieveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return RetrieveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrieveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return RetrieveResourceWithStreamingResponse(self)

    def documents(
        self,
        knowledge_base_id: str,
        *,
        num_results: int,
        query: str,
        alpha: float | Omit = omit,
        filters: retrieve_documents_params.Filters | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrieveDocumentsResponse:
        """
        Retrieve relevant documents from a knowledge base using semantic search.

        This endpoint:

        1. Authenticates the request using the provided bearer token
        2. Generates embeddings for the query using the knowledge base's configured
           model
        3. Performs vector similarity search in the knowledge base
        4. Returns the most relevant document chunks

        Args:
          num_results: Number of results to return

          query: The search query text

          alpha:
              Weight for hybrid search (0-1):

              - 0 = pure keyword search (BM25)
              - 1 = pure vector search (default)
              - 0.5 = balanced hybrid search

          filters: Metadata filters to apply to the search

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._post(
            (
                f"/{knowledge_base_id}/retrieve"
                if self._client._base_url_overridden
                else f"https://kbaas.do-ai.run/v1/{knowledge_base_id}/retrieve"
            ),
            body=maybe_transform(
                {
                    "num_results": num_results,
                    "query": query,
                    "alpha": alpha,
                    "filters": filters,
                },
                retrieve_documents_params.RetrieveDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=RetrieveDocumentsResponse,
        )


class AsyncRetrieveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrieveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrieveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrieveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncRetrieveResourceWithStreamingResponse(self)

    async def documents(
        self,
        knowledge_base_id: str,
        *,
        num_results: int,
        query: str,
        alpha: float | Omit = omit,
        filters: retrieve_documents_params.Filters | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrieveDocumentsResponse:
        """
        Retrieve relevant documents from a knowledge base using semantic search.

        This endpoint:

        1. Authenticates the request using the provided bearer token
        2. Generates embeddings for the query using the knowledge base's configured
           model
        3. Performs vector similarity search in the knowledge base
        4. Returns the most relevant document chunks

        Args:
          num_results: Number of results to return

          query: The search query text

          alpha:
              Weight for hybrid search (0-1):

              - 0 = pure keyword search (BM25)
              - 1 = pure vector search (default)
              - 0.5 = balanced hybrid search

          filters: Metadata filters to apply to the search

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._post(
            (
                f"/{knowledge_base_id}/retrieve"
                if self._client._base_url_overridden
                else f"https://kbaas.do-ai.run/v1/{knowledge_base_id}/retrieve"
            ),
            body=await async_maybe_transform(
                {
                    "num_results": num_results,
                    "query": query,
                    "alpha": alpha,
                    "filters": filters,
                },
                retrieve_documents_params.RetrieveDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=RetrieveDocumentsResponse,
        )


class RetrieveResourceWithRawResponse:
    def __init__(self, retrieve: RetrieveResource) -> None:
        self._retrieve = retrieve

        self.documents = to_raw_response_wrapper(
            retrieve.documents,
        )


class AsyncRetrieveResourceWithRawResponse:
    def __init__(self, retrieve: AsyncRetrieveResource) -> None:
        self._retrieve = retrieve

        self.documents = async_to_raw_response_wrapper(
            retrieve.documents,
        )


class RetrieveResourceWithStreamingResponse:
    def __init__(self, retrieve: RetrieveResource) -> None:
        self._retrieve = retrieve

        self.documents = to_streamed_response_wrapper(
            retrieve.documents,
        )


class AsyncRetrieveResourceWithStreamingResponse:
    def __init__(self, retrieve: AsyncRetrieveResource) -> None:
        self._retrieve = retrieve

        self.documents = async_to_streamed_response_wrapper(
            retrieve.documents,
        )
