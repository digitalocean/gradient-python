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
from ...types.knowledge_bases import (
    data_source_list_params,
    data_source_create_params,
    data_source_create_presigned_urls_params,
)
from ...types.knowledge_bases.aws_data_source_param import AwsDataSourceParam
from ...types.knowledge_bases.data_source_list_response import DataSourceListResponse
from ...types.knowledge_bases.data_source_create_response import DataSourceCreateResponse
from ...types.knowledge_bases.data_source_delete_response import DataSourceDeleteResponse
from ...types.knowledge_bases.api_spaces_data_source_param import APISpacesDataSourceParam
from ...types.knowledge_bases.api_web_crawler_data_source_param import APIWebCrawlerDataSourceParam
from ...types.knowledge_bases.data_source_create_presigned_urls_response import DataSourceCreatePresignedURLsResponse

__all__ = ["DataSourcesResource", "AsyncDataSourcesResource"]


class DataSourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return DataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return DataSourcesResourceWithStreamingResponse(self)

    def create(
        self,
        path_knowledge_base_uuid: str,
        *,
        aws_data_source: AwsDataSourceParam | Omit = omit,
        body_knowledge_base_uuid: str | Omit = omit,
        spaces_data_source: APISpacesDataSourceParam | Omit = omit,
        web_crawler_data_source: APIWebCrawlerDataSourceParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceCreateResponse:
        """
        To add a data source to a knowledge base, send a POST request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources`.

        Args:
          aws_data_source: AWS S3 Data Source

          body_knowledge_base_uuid: Knowledge base id

          spaces_data_source: Spaces Bucket Data Source

          web_crawler_data_source: WebCrawlerDataSource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_knowledge_base_uuid` but received {path_knowledge_base_uuid!r}"
            )
        return self._post(
            f"/v2/gen-ai/knowledge_bases/{path_knowledge_base_uuid}/data_sources"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{path_knowledge_base_uuid}/data_sources",
            body=maybe_transform(
                {
                    "aws_data_source": aws_data_source,
                    "body_knowledge_base_uuid": body_knowledge_base_uuid,
                    "spaces_data_source": spaces_data_source,
                    "web_crawler_data_source": web_crawler_data_source,
                },
                data_source_create_params.DataSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceCreateResponse,
        )

    def list(
        self,
        knowledge_base_uuid: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceListResponse:
        """
        To list all data sources for a knowledge base, send a GET request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources`.

        Args:
          page: Page number.

          per_page: Items per page.

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
            f"/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources",
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
                    data_source_list_params.DataSourceListParams,
                ),
            ),
            cast_to=DataSourceListResponse,
        )

    def delete(
        self,
        data_source_uuid: str,
        *,
        knowledge_base_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceDeleteResponse:
        """
        To delete a data source from a knowledge base, send a DELETE request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}`.

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
        if not data_source_uuid:
            raise ValueError(f"Expected a non-empty value for `data_source_uuid` but received {data_source_uuid!r}")
        return self._delete(
            f"/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceDeleteResponse,
        )

    def create_presigned_urls(
        self,
        *,
        files: Iterable[data_source_create_presigned_urls_params.File] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceCreatePresignedURLsResponse:
        """
        To create presigned URLs for knowledge base data source file upload, send a POST
        request to `/v2/gen-ai/knowledge_bases/data_sources/file_upload_presigned_urls`.

        Args:
          files: A list of files to generate presigned URLs for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/knowledge_bases/data_sources/file_upload_presigned_urls"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/knowledge_bases/data_sources/file_upload_presigned_urls",
            body=maybe_transform(
                {"files": files}, data_source_create_presigned_urls_params.DataSourceCreatePresignedURLsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceCreatePresignedURLsResponse,
        )


class AsyncDataSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncDataSourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        path_knowledge_base_uuid: str,
        *,
        aws_data_source: AwsDataSourceParam | Omit = omit,
        body_knowledge_base_uuid: str | Omit = omit,
        spaces_data_source: APISpacesDataSourceParam | Omit = omit,
        web_crawler_data_source: APIWebCrawlerDataSourceParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceCreateResponse:
        """
        To add a data source to a knowledge base, send a POST request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources`.

        Args:
          aws_data_source: AWS S3 Data Source

          body_knowledge_base_uuid: Knowledge base id

          spaces_data_source: Spaces Bucket Data Source

          web_crawler_data_source: WebCrawlerDataSource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_knowledge_base_uuid` but received {path_knowledge_base_uuid!r}"
            )
        return await self._post(
            f"/v2/gen-ai/knowledge_bases/{path_knowledge_base_uuid}/data_sources"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{path_knowledge_base_uuid}/data_sources",
            body=await async_maybe_transform(
                {
                    "aws_data_source": aws_data_source,
                    "body_knowledge_base_uuid": body_knowledge_base_uuid,
                    "spaces_data_source": spaces_data_source,
                    "web_crawler_data_source": web_crawler_data_source,
                },
                data_source_create_params.DataSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceCreateResponse,
        )

    async def list(
        self,
        knowledge_base_uuid: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceListResponse:
        """
        To list all data sources for a knowledge base, send a GET request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources`.

        Args:
          page: Page number.

          per_page: Items per page.

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
            f"/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources",
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
                    data_source_list_params.DataSourceListParams,
                ),
            ),
            cast_to=DataSourceListResponse,
        )

    async def delete(
        self,
        data_source_uuid: str,
        *,
        knowledge_base_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceDeleteResponse:
        """
        To delete a data source from a knowledge base, send a DELETE request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}`.

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
        if not data_source_uuid:
            raise ValueError(f"Expected a non-empty value for `data_source_uuid` but received {data_source_uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceDeleteResponse,
        )

    async def create_presigned_urls(
        self,
        *,
        files: Iterable[data_source_create_presigned_urls_params.File] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceCreatePresignedURLsResponse:
        """
        To create presigned URLs for knowledge base data source file upload, send a POST
        request to `/v2/gen-ai/knowledge_bases/data_sources/file_upload_presigned_urls`.

        Args:
          files: A list of files to generate presigned URLs for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/knowledge_bases/data_sources/file_upload_presigned_urls"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/knowledge_bases/data_sources/file_upload_presigned_urls",
            body=await async_maybe_transform(
                {"files": files}, data_source_create_presigned_urls_params.DataSourceCreatePresignedURLsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceCreatePresignedURLsResponse,
        )


class DataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = to_raw_response_wrapper(
            data_sources.create,
        )
        self.list = to_raw_response_wrapper(
            data_sources.list,
        )
        self.delete = to_raw_response_wrapper(
            data_sources.delete,
        )
        self.create_presigned_urls = to_raw_response_wrapper(
            data_sources.create_presigned_urls,
        )


class AsyncDataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = async_to_raw_response_wrapper(
            data_sources.create,
        )
        self.list = async_to_raw_response_wrapper(
            data_sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            data_sources.delete,
        )
        self.create_presigned_urls = async_to_raw_response_wrapper(
            data_sources.create_presigned_urls,
        )


class DataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = to_streamed_response_wrapper(
            data_sources.create,
        )
        self.list = to_streamed_response_wrapper(
            data_sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            data_sources.delete,
        )
        self.create_presigned_urls = to_streamed_response_wrapper(
            data_sources.create_presigned_urls,
        )


class AsyncDataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = async_to_streamed_response_wrapper(
            data_sources.create,
        )
        self.list = async_to_streamed_response_wrapper(
            data_sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            data_sources.delete,
        )
        self.create_presigned_urls = async_to_streamed_response_wrapper(
            data_sources.create_presigned_urls,
        )
