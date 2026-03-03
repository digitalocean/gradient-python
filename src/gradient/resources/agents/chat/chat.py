# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .completions import (
    CompletionsResource,
    AsyncCompletionsResource,
    CompletionsResourceWithRawResponse,
    AsyncCompletionsResourceWithRawResponse,
    CompletionsResourceWithStreamingResponse,
    AsyncCompletionsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def completions(self) -> CompletionsResource:
        """
        Given a list of messages comprising a conversation, the model will return a response.
        """
        return CompletionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def completions(self) -> AsyncCompletionsResource:
        """
        Given a list of messages comprising a conversation, the model will return a response.
        """
        return AsyncCompletionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

    @cached_property
    def completions(self) -> CompletionsResourceWithRawResponse:
        """
        Given a list of messages comprising a conversation, the model will return a response.
        """
        return CompletionsResourceWithRawResponse(self._chat.completions)


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        Given a list of messages comprising a conversation, the model will return a response.
        """
        return AsyncCompletionsResourceWithRawResponse(self._chat.completions)


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

    @cached_property
    def completions(self) -> CompletionsResourceWithStreamingResponse:
        """
        Given a list of messages comprising a conversation, the model will return a response.
        """
        return CompletionsResourceWithStreamingResponse(self._chat.completions)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        Given a list of messages comprising a conversation, the model will return a response.
        """
        return AsyncCompletionsResourceWithStreamingResponse(self._chat.completions)
