# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.agents.evaluation_metrics.oauth2 import dropbox_create_tokens_params
from .....types.agents.evaluation_metrics.oauth2.dropbox_create_tokens_response import DropboxCreateTokensResponse

__all__ = ["DropboxResource", "AsyncDropboxResource"]


class DropboxResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DropboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return DropboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DropboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return DropboxResourceWithStreamingResponse(self)

    def create_tokens(
        self,
        *,
        code: str | Omit = omit,
        redirect_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DropboxCreateTokensResponse:
        """
        To obtain the refresh token, needed for creation of data sources, send a GET
        request to `/v2/gen-ai/oauth2/dropbox/tokens`. Pass the code you obtrained from
        the oauth flow in the field 'code'

        Args:
          code: The oauth2 code from google

          redirect_url: Redirect url

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/oauth2/dropbox/tokens"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/oauth2/dropbox/tokens",
            body=maybe_transform(
                {
                    "code": code,
                    "redirect_url": redirect_url,
                },
                dropbox_create_tokens_params.DropboxCreateTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DropboxCreateTokensResponse,
        )


class AsyncDropboxResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDropboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDropboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDropboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncDropboxResourceWithStreamingResponse(self)

    async def create_tokens(
        self,
        *,
        code: str | Omit = omit,
        redirect_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DropboxCreateTokensResponse:
        """
        To obtain the refresh token, needed for creation of data sources, send a GET
        request to `/v2/gen-ai/oauth2/dropbox/tokens`. Pass the code you obtrained from
        the oauth flow in the field 'code'

        Args:
          code: The oauth2 code from google

          redirect_url: Redirect url

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/oauth2/dropbox/tokens"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/oauth2/dropbox/tokens",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "redirect_url": redirect_url,
                },
                dropbox_create_tokens_params.DropboxCreateTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DropboxCreateTokensResponse,
        )


class DropboxResourceWithRawResponse:
    def __init__(self, dropbox: DropboxResource) -> None:
        self._dropbox = dropbox

        self.create_tokens = to_raw_response_wrapper(
            dropbox.create_tokens,
        )


class AsyncDropboxResourceWithRawResponse:
    def __init__(self, dropbox: AsyncDropboxResource) -> None:
        self._dropbox = dropbox

        self.create_tokens = async_to_raw_response_wrapper(
            dropbox.create_tokens,
        )


class DropboxResourceWithStreamingResponse:
    def __init__(self, dropbox: DropboxResource) -> None:
        self._dropbox = dropbox

        self.create_tokens = to_streamed_response_wrapper(
            dropbox.create_tokens,
        )


class AsyncDropboxResourceWithStreamingResponse:
    def __init__(self, dropbox: AsyncDropboxResource) -> None:
        self._dropbox = dropbox

        self.create_tokens = async_to_streamed_response_wrapper(
            dropbox.create_tokens,
        )
