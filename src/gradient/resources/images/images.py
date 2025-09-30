# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .generations import (
    GenerationsResource,
    AsyncGenerationsResource,
    GenerationsResourceWithRawResponse,
    AsyncGenerationsResourceWithRawResponse,
    GenerationsResourceWithStreamingResponse,
    AsyncGenerationsResourceWithStreamingResponse,
)

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._images.generations)


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._images.generations)


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._images.generations)


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._images.generations)
