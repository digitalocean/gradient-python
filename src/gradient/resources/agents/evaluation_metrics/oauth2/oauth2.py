# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .dropbox import (
    DropboxResource,
    AsyncDropboxResource,
    DropboxResourceWithRawResponse,
    AsyncDropboxResourceWithRawResponse,
    DropboxResourceWithStreamingResponse,
    AsyncDropboxResourceWithStreamingResponse,
)
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
from .....types.agents.evaluation_metrics import oauth2_generate_url_params
from .....types.agents.evaluation_metrics.oauth2_generate_url_response import Oauth2GenerateURLResponse

__all__ = ["Oauth2Resource", "AsyncOauth2Resource"]


class Oauth2Resource(SyncAPIResource):
    @cached_property
    def dropbox(self) -> DropboxResource:
        return DropboxResource(self._client)

    @cached_property
    def with_raw_response(self) -> Oauth2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return Oauth2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Oauth2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return Oauth2ResourceWithStreamingResponse(self)

    def generate_url(
        self,
        *,
        redirect_url: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Oauth2GenerateURLResponse:
        """
        To generate an Oauth2-URL for use with your localhost, send a GET request to
        `/v2/gen-ai/oauth2/url`. Pass 'http://localhost:3000 as redirect_url

        Args:
          redirect_url: The redirect url.

          type: Type "google" / "dropbox".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gen-ai/oauth2/url"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/oauth2/url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "redirect_url": redirect_url,
                        "type": type,
                    },
                    oauth2_generate_url_params.Oauth2GenerateURLParams,
                ),
            ),
            cast_to=Oauth2GenerateURLResponse,
        )


class AsyncOauth2Resource(AsyncAPIResource):
    @cached_property
    def dropbox(self) -> AsyncDropboxResource:
        return AsyncDropboxResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOauth2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOauth2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOauth2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncOauth2ResourceWithStreamingResponse(self)

    async def generate_url(
        self,
        *,
        redirect_url: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Oauth2GenerateURLResponse:
        """
        To generate an Oauth2-URL for use with your localhost, send a GET request to
        `/v2/gen-ai/oauth2/url`. Pass 'http://localhost:3000 as redirect_url

        Args:
          redirect_url: The redirect url.

          type: Type "google" / "dropbox".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gen-ai/oauth2/url"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/oauth2/url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "redirect_url": redirect_url,
                        "type": type,
                    },
                    oauth2_generate_url_params.Oauth2GenerateURLParams,
                ),
            ),
            cast_to=Oauth2GenerateURLResponse,
        )


class Oauth2ResourceWithRawResponse:
    def __init__(self, oauth2: Oauth2Resource) -> None:
        self._oauth2 = oauth2

        self.generate_url = to_raw_response_wrapper(
            oauth2.generate_url,
        )

    @cached_property
    def dropbox(self) -> DropboxResourceWithRawResponse:
        return DropboxResourceWithRawResponse(self._oauth2.dropbox)


class AsyncOauth2ResourceWithRawResponse:
    def __init__(self, oauth2: AsyncOauth2Resource) -> None:
        self._oauth2 = oauth2

        self.generate_url = async_to_raw_response_wrapper(
            oauth2.generate_url,
        )

    @cached_property
    def dropbox(self) -> AsyncDropboxResourceWithRawResponse:
        return AsyncDropboxResourceWithRawResponse(self._oauth2.dropbox)


class Oauth2ResourceWithStreamingResponse:
    def __init__(self, oauth2: Oauth2Resource) -> None:
        self._oauth2 = oauth2

        self.generate_url = to_streamed_response_wrapper(
            oauth2.generate_url,
        )

    @cached_property
    def dropbox(self) -> DropboxResourceWithStreamingResponse:
        return DropboxResourceWithStreamingResponse(self._oauth2.dropbox)


class AsyncOauth2ResourceWithStreamingResponse:
    def __init__(self, oauth2: AsyncOauth2Resource) -> None:
        self._oauth2 = oauth2

        self.generate_url = async_to_streamed_response_wrapper(
            oauth2.generate_url,
        )

    @cached_property
    def dropbox(self) -> AsyncDropboxResourceWithStreamingResponse:
        return AsyncDropboxResourceWithStreamingResponse(self._oauth2.dropbox)
