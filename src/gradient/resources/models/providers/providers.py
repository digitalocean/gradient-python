# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .openai import (
    OpenAIResource,
    AsyncOpenAIResource,
    OpenAIResourceWithRawResponse,
    AsyncOpenAIResourceWithRawResponse,
    OpenAIResourceWithStreamingResponse,
    AsyncOpenAIResourceWithStreamingResponse,
)
from .anthropic import (
    AnthropicResource,
    AsyncAnthropicResource,
    AnthropicResourceWithRawResponse,
    AsyncAnthropicResourceWithRawResponse,
    AnthropicResourceWithStreamingResponse,
    AsyncAnthropicResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def anthropic(self) -> AnthropicResource:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AnthropicResource(self._client)

    @cached_property
    def openai(self) -> OpenAIResource:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return OpenAIResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ProvidersResourceWithStreamingResponse(self)


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def anthropic(self) -> AsyncAnthropicResource:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AsyncAnthropicResource(self._client)

    @cached_property
    def openai(self) -> AsyncOpenAIResource:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AsyncOpenAIResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncProvidersResourceWithStreamingResponse(self)


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

    @cached_property
    def anthropic(self) -> AnthropicResourceWithRawResponse:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AnthropicResourceWithRawResponse(self._providers.anthropic)

    @cached_property
    def openai(self) -> OpenAIResourceWithRawResponse:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return OpenAIResourceWithRawResponse(self._providers.openai)


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

    @cached_property
    def anthropic(self) -> AsyncAnthropicResourceWithRawResponse:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AsyncAnthropicResourceWithRawResponse(self._providers.anthropic)

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithRawResponse:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AsyncOpenAIResourceWithRawResponse(self._providers.openai)


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

    @cached_property
    def anthropic(self) -> AnthropicResourceWithStreamingResponse:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AnthropicResourceWithStreamingResponse(self._providers.anthropic)

    @cached_property
    def openai(self) -> OpenAIResourceWithStreamingResponse:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return OpenAIResourceWithStreamingResponse(self._providers.openai)


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

    @cached_property
    def anthropic(self) -> AsyncAnthropicResourceWithStreamingResponse:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AsyncAnthropicResourceWithStreamingResponse(self._providers.anthropic)

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithStreamingResponse:
        """
        The API lets you build GPU-powered AI agents with pre-built or custom foundation models, function and agent routes, and RAG pipelines with knowledge bases.
        """
        return AsyncOpenAIResourceWithStreamingResponse(self._providers.openai)
