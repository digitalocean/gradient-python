# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.genai.knowledge_bases import (
    data_source_list_params,
    data_source_create_params,
)
from ....types.genai.knowledge_bases.data_source_list_response import DataSourceListResponse
from ....types.genai.knowledge_bases.data_source_create_response import DataSourceCreateResponse
from ....types.genai.knowledge_bases.data_source_delete_response import DataSourceDeleteResponse
from ....types.genai.knowledge_bases.api_spaces_data_source_param import APISpacesDataSourceParam
from ....types.genai.knowledge_bases.api_web_crawler_data_source_param import APIWebCrawlerDataSourceParam

__all__ = ["DataSourcesResource", "AsyncDataSourcesResource"]


class DataSourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return DataSourcesResourceWithStreamingResponse(self)

    def create(
        self,
        path_knowledge_base_uuid: str,
        *,
        aws_data_source: data_source_create_params.AwsDataSource | NotGiven = NOT_GIVEN,
        body_knowledge_base_uuid: str | NotGiven = NOT_GIVEN,
        spaces_data_source: APISpacesDataSourceParam | NotGiven = NOT_GIVEN,
        web_crawler_data_source: APIWebCrawlerDataSourceParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSourceCreateResponse:
        """
        To add a data source to a knowledge base, send a POST request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources`.

        Args:
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
            f"/v2/genai/knowledge_bases/{path_knowledge_base_uuid}/data_sources",
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
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSourceListResponse:
        """
        To list all data sources for a knowledge base, send a GET request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources`.

        Args:
          page: page number.

          per_page: items per page.

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
            f"/v2/genai/knowledge_bases/{knowledge_base_uuid}/data_sources",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v2/genai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceDeleteResponse,
        )


class AsyncDataSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return AsyncDataSourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        path_knowledge_base_uuid: str,
        *,
        aws_data_source: data_source_create_params.AwsDataSource | NotGiven = NOT_GIVEN,
        body_knowledge_base_uuid: str | NotGiven = NOT_GIVEN,
        spaces_data_source: APISpacesDataSourceParam | NotGiven = NOT_GIVEN,
        web_crawler_data_source: APIWebCrawlerDataSourceParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSourceCreateResponse:
        """
        To add a data source to a knowledge base, send a POST request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources`.

        Args:
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
            f"/v2/genai/knowledge_bases/{path_knowledge_base_uuid}/data_sources",
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
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSourceListResponse:
        """
        To list all data sources for a knowledge base, send a GET request to
        `/v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources`.

        Args:
          page: page number.

          per_page: items per page.

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
            f"/v2/genai/knowledge_bases/{knowledge_base_uuid}/data_sources",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/v2/genai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceDeleteResponse,
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
