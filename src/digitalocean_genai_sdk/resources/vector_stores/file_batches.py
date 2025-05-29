# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.vector_stores import ChunkingStrategyRequestParam, file_batch_create_params, file_batch_list_files_params
from ...types.vector_stores.vector_store_file_batch_object import VectorStoreFileBatchObject
from ...types.vector_stores.chunking_strategy_request_param import ChunkingStrategyRequestParam
from ...types.vector_stores.list_vector_store_files_response import ListVectorStoreFilesResponse

__all__ = ["FileBatchesResource", "AsyncFileBatchesResource"]


class FileBatchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return FileBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return FileBatchesResourceWithStreamingResponse(self)

    def create(
        self,
        vector_store_id: str,
        *,
        file_ids: List[str],
        attributes: Optional[Dict[str, Union[str, float, bool]]] | NotGiven = NOT_GIVEN,
        chunking_strategy: ChunkingStrategyRequestParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileBatchObject:
        """
        Create a vector store file batch.

        Args:
          file_ids: A list of [File](/docs/api-reference/files) IDs that the vector store should
              use. Useful for tools like `file_search` that can access files.

          attributes: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard. Keys are strings with a maximum
              length of 64 characters. Values are strings with a maximum length of 512
              characters, booleans, or numbers.

          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._post(
            f"/vector_stores/{vector_store_id}/file_batches",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "attributes": attributes,
                    "chunking_strategy": chunking_strategy,
                },
                file_batch_create_params.FileBatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatchObject,
        )

    def retrieve(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileBatchObject:
        """
        Retrieves a vector store file batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            f"/vector_stores/{vector_store_id}/file_batches/{batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatchObject,
        )

    def cancel(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileBatchObject:
        """Cancel a vector store file batch.

        This attempts to cancel the processing of
        files in this batch as soon as possible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._post(
            f"/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatchObject,
        )

    def list_files(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        filter: Literal["in_progress", "completed", "failed", "cancelled"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListVectorStoreFilesResponse:
        """
        Returns a list of vector store files in a batch.

        Args:
          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          filter: Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            f"/vector_stores/{vector_store_id}/file_batches/{batch_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "filter": filter,
                        "limit": limit,
                        "order": order,
                    },
                    file_batch_list_files_params.FileBatchListFilesParams,
                ),
            ),
            cast_to=ListVectorStoreFilesResponse,
        )


class AsyncFileBatchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncFileBatchesResourceWithStreamingResponse(self)

    async def create(
        self,
        vector_store_id: str,
        *,
        file_ids: List[str],
        attributes: Optional[Dict[str, Union[str, float, bool]]] | NotGiven = NOT_GIVEN,
        chunking_strategy: ChunkingStrategyRequestParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileBatchObject:
        """
        Create a vector store file batch.

        Args:
          file_ids: A list of [File](/docs/api-reference/files) IDs that the vector store should
              use. Useful for tools like `file_search` that can access files.

          attributes: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard. Keys are strings with a maximum
              length of 64 characters. Values are strings with a maximum length of 512
              characters, booleans, or numbers.

          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._post(
            f"/vector_stores/{vector_store_id}/file_batches",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "attributes": attributes,
                    "chunking_strategy": chunking_strategy,
                },
                file_batch_create_params.FileBatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatchObject,
        )

    async def retrieve(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileBatchObject:
        """
        Retrieves a vector store file batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            f"/vector_stores/{vector_store_id}/file_batches/{batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatchObject,
        )

    async def cancel(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileBatchObject:
        """Cancel a vector store file batch.

        This attempts to cancel the processing of
        files in this batch as soon as possible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._post(
            f"/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileBatchObject,
        )

    async def list_files(
        self,
        batch_id: str,
        *,
        vector_store_id: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        filter: Literal["in_progress", "completed", "failed", "cancelled"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListVectorStoreFilesResponse:
        """
        Returns a list of vector store files in a batch.

        Args:
          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          filter: Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            f"/vector_stores/{vector_store_id}/file_batches/{batch_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "filter": filter,
                        "limit": limit,
                        "order": order,
                    },
                    file_batch_list_files_params.FileBatchListFilesParams,
                ),
            ),
            cast_to=ListVectorStoreFilesResponse,
        )


class FileBatchesResourceWithRawResponse:
    def __init__(self, file_batches: FileBatchesResource) -> None:
        self._file_batches = file_batches

        self.create = to_raw_response_wrapper(
            file_batches.create,
        )
        self.retrieve = to_raw_response_wrapper(
            file_batches.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            file_batches.cancel,
        )
        self.list_files = to_raw_response_wrapper(
            file_batches.list_files,
        )


class AsyncFileBatchesResourceWithRawResponse:
    def __init__(self, file_batches: AsyncFileBatchesResource) -> None:
        self._file_batches = file_batches

        self.create = async_to_raw_response_wrapper(
            file_batches.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            file_batches.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            file_batches.cancel,
        )
        self.list_files = async_to_raw_response_wrapper(
            file_batches.list_files,
        )


class FileBatchesResourceWithStreamingResponse:
    def __init__(self, file_batches: FileBatchesResource) -> None:
        self._file_batches = file_batches

        self.create = to_streamed_response_wrapper(
            file_batches.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            file_batches.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            file_batches.cancel,
        )
        self.list_files = to_streamed_response_wrapper(
            file_batches.list_files,
        )


class AsyncFileBatchesResourceWithStreamingResponse:
    def __init__(self, file_batches: AsyncFileBatchesResource) -> None:
        self._file_batches = file_batches

        self.create = async_to_streamed_response_wrapper(
            file_batches.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            file_batches.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            file_batches.cancel,
        )
        self.list_files = async_to_streamed_response_wrapper(
            file_batches.list_files,
        )
