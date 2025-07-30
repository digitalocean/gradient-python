# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AnthropicResource", "AsyncAnthropicResource"]


class AnthropicResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnthropicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AnthropicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnthropicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AnthropicResourceWithStreamingResponse(self)


class AsyncAnthropicResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnthropicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnthropicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnthropicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncAnthropicResourceWithStreamingResponse(self)


class AnthropicResourceWithRawResponse:
    def __init__(self, anthropic: AnthropicResource) -> None:
        self._anthropic = anthropic

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._anthropic.keys)


class AsyncAnthropicResourceWithRawResponse:
    def __init__(self, anthropic: AsyncAnthropicResource) -> None:
        self._anthropic = anthropic

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._anthropic.keys)


class AnthropicResourceWithStreamingResponse:
    def __init__(self, anthropic: AnthropicResource) -> None:
        self._anthropic = anthropic

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._anthropic.keys)


class AsyncAnthropicResourceWithStreamingResponse:
    def __init__(self, anthropic: AsyncAnthropicResource) -> None:
        self._anthropic = anthropic

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._anthropic.keys)
