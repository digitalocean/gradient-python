# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.gpu_droplets import size_list_params
from ...types.gpu_droplets.size_list_response import SizeListResponse

__all__ = ["SizesResource", "AsyncSizesResource"]


class SizesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SizesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return SizesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SizesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return SizesResourceWithStreamingResponse(self)

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
    ) -> SizeListResponse:
        """To list all of available Droplet sizes, send a GET request to `/v2/sizes`.

        The
        response will be a JSON object with a key called `sizes`. The value of this will
        be an array of `size` objects each of which contain the standard size
        attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/sizes" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/sizes",
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
                    size_list_params.SizeListParams,
                ),
            ),
            cast_to=SizeListResponse,
        )


class AsyncSizesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSizesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSizesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSizesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncSizesResourceWithStreamingResponse(self)

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
    ) -> SizeListResponse:
        """To list all of available Droplet sizes, send a GET request to `/v2/sizes`.

        The
        response will be a JSON object with a key called `sizes`. The value of this will
        be an array of `size` objects each of which contain the standard size
        attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/sizes" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/sizes",
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
                    size_list_params.SizeListParams,
                ),
            ),
            cast_to=SizeListResponse,
        )


class SizesResourceWithRawResponse:
    def __init__(self, sizes: SizesResource) -> None:
        self._sizes = sizes

        self.list = to_raw_response_wrapper(
            sizes.list,
        )


class AsyncSizesResourceWithRawResponse:
    def __init__(self, sizes: AsyncSizesResource) -> None:
        self._sizes = sizes

        self.list = async_to_raw_response_wrapper(
            sizes.list,
        )


class SizesResourceWithStreamingResponse:
    def __init__(self, sizes: SizesResource) -> None:
        self._sizes = sizes

        self.list = to_streamed_response_wrapper(
            sizes.list,
        )


class AsyncSizesResourceWithStreamingResponse:
    def __init__(self, sizes: AsyncSizesResource) -> None:
        self._sizes = sizes

        self.list = async_to_streamed_response_wrapper(
            sizes.list,
        )
