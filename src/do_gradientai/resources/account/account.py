# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.account_retrieve_response import AccountRetrieveResponse

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AccountResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """
        To show information about the current user account, send a GET request to
        `/v2/account`.
        """
        return self._get(
            "/v2/account" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )


class AsyncAccountResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AsyncAccountResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """
        To show information about the current user account, send a GET request to
        `/v2/account`.
        """
        return await self._get(
            "/v2/account" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )


class AccountResourceWithRawResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.retrieve = to_raw_response_wrapper(
            account.retrieve,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._account.keys)


class AsyncAccountResourceWithRawResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.retrieve = async_to_raw_response_wrapper(
            account.retrieve,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._account.keys)


class AccountResourceWithStreamingResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.retrieve = to_streamed_response_wrapper(
            account.retrieve,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._account.keys)


class AsyncAccountResourceWithStreamingResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.retrieve = async_to_streamed_response_wrapper(
            account.retrieve,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._account.keys)
