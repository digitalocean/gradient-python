# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InferenceResource", "AsyncInferenceResource"]


class InferenceResource(SyncAPIResource):
    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> InferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return InferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return InferenceResourceWithStreamingResponse(self)


class AsyncInferenceResource(AsyncAPIResource):
    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncInferenceResourceWithStreamingResponse(self)


class InferenceResourceWithRawResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._inference.api_keys)


class AsyncInferenceResourceWithRawResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._inference.api_keys)


class InferenceResourceWithStreamingResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._inference.api_keys)


class AsyncInferenceResourceWithStreamingResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._inference.api_keys)
