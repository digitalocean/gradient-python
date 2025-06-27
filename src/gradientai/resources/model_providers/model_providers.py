# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .openai.openai import (
    OpenAIResource,
    AsyncOpenAIResource,
    OpenAIResourceWithRawResponse,
    AsyncOpenAIResourceWithRawResponse,
    OpenAIResourceWithStreamingResponse,
    AsyncOpenAIResourceWithStreamingResponse,
)
from .anthropic.anthropic import (
    AnthropicResource,
    AsyncAnthropicResource,
    AnthropicResourceWithRawResponse,
    AsyncAnthropicResourceWithRawResponse,
    AnthropicResourceWithStreamingResponse,
    AsyncAnthropicResourceWithStreamingResponse,
)

__all__ = ["ModelProvidersResource", "AsyncModelProvidersResource"]


class ModelProvidersResource(SyncAPIResource):
    @cached_property
    def anthropic(self) -> AnthropicResource:
        return AnthropicResource(self._client)

    @cached_property
    def openai(self) -> OpenAIResource:
        return OpenAIResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return ModelProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return ModelProvidersResourceWithStreamingResponse(self)


class AsyncModelProvidersResource(AsyncAPIResource):
    @cached_property
    def anthropic(self) -> AsyncAnthropicResource:
        return AsyncAnthropicResource(self._client)

    @cached_property
    def openai(self) -> AsyncOpenAIResource:
        return AsyncOpenAIResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradientai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradientai-python#with_streaming_response
        """
        return AsyncModelProvidersResourceWithStreamingResponse(self)


class ModelProvidersResourceWithRawResponse:
    def __init__(self, model_providers: ModelProvidersResource) -> None:
        self._model_providers = model_providers

    @cached_property
    def anthropic(self) -> AnthropicResourceWithRawResponse:
        return AnthropicResourceWithRawResponse(self._model_providers.anthropic)

    @cached_property
    def openai(self) -> OpenAIResourceWithRawResponse:
        return OpenAIResourceWithRawResponse(self._model_providers.openai)


class AsyncModelProvidersResourceWithRawResponse:
    def __init__(self, model_providers: AsyncModelProvidersResource) -> None:
        self._model_providers = model_providers

    @cached_property
    def anthropic(self) -> AsyncAnthropicResourceWithRawResponse:
        return AsyncAnthropicResourceWithRawResponse(self._model_providers.anthropic)

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithRawResponse:
        return AsyncOpenAIResourceWithRawResponse(self._model_providers.openai)


class ModelProvidersResourceWithStreamingResponse:
    def __init__(self, model_providers: ModelProvidersResource) -> None:
        self._model_providers = model_providers

    @cached_property
    def anthropic(self) -> AnthropicResourceWithStreamingResponse:
        return AnthropicResourceWithStreamingResponse(self._model_providers.anthropic)

    @cached_property
    def openai(self) -> OpenAIResourceWithStreamingResponse:
        return OpenAIResourceWithStreamingResponse(self._model_providers.openai)


class AsyncModelProvidersResourceWithStreamingResponse:
    def __init__(self, model_providers: AsyncModelProvidersResource) -> None:
        self._model_providers = model_providers

    @cached_property
    def anthropic(self) -> AsyncAnthropicResourceWithStreamingResponse:
        return AsyncAnthropicResourceWithStreamingResponse(self._model_providers.anthropic)

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithStreamingResponse:
        return AsyncOpenAIResourceWithStreamingResponse(self._model_providers.openai)
