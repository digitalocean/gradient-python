# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from ..types import image_generate_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.image_generate_response import ImageGenerateResponse
from ..types.shared.image_gen_stream_event import ImageGenStreamEvent

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
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

    @overload
    def generate(
        self,
        *,
        prompt: str,
        background: Optional[str] | Omit = omit,
        model: str | Omit = omit,
        moderation: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_compression: Optional[int] | Omit = omit,
        output_format: Optional[str] | Omit = omit,
        partial_images: Optional[int] | Omit = omit,
        quality: Optional[str] | Omit = omit,
        size: Optional[str] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageGenerateResponse:
        """
        Creates a high-quality image from a text prompt using GPT-IMAGE-1, the latest
        image generation model with automatic prompt optimization and enhanced visual
        capabilities.

        Args:
          prompt: A text description of the desired image(s). GPT-IMAGE-1 supports up to 32,000
              characters and provides automatic prompt optimization for best results.

          background:
              The background setting for the image generation. GPT-IMAGE-1 supports:
              transparent, opaque, auto.

          model: The model to use for image generation. GPT-IMAGE-1 is the latest model offering
              the best quality with automatic optimization and enhanced capabilities.

          moderation: The moderation setting for the image generation. GPT-IMAGE-1 supports: low,
              auto.

          n: The number of images to generate. GPT-IMAGE-1 only supports n=1.

          output_compression: The output compression for the image generation. GPT-IMAGE-1 supports: 0-100.

          output_format: The output format for the image generation. GPT-IMAGE-1 supports: png, webp,
              jpeg.

          partial_images: The number of partial image chunks to return during streaming generation. This
              parameter is optional with a default of 0. When stream=true, this must be
              greater than 0 to receive progressive updates of the image as it's being
              generated. Higher values provide more frequent updates but may increase response
              overhead.

          quality: The quality of the image that will be generated. GPT-IMAGE-1 supports: auto
              (automatically select best quality), high, medium, low.

          size: The size of the generated images. GPT-IMAGE-1 supports: auto (automatically
              select best size), 1536x1024 (landscape), 1024x1536 (portrait).

          stream: If set to true, partial image data will be streamed as the image is being
              generated. When streaming, the response will be sent as server-sent events with
              partial image chunks. When stream is true, partial_images must be greater
              than 0.

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generate(
        self,
        *,
        prompt: str,
        stream: Literal[True],
        background: Optional[str] | Omit = omit,
        model: str | Omit = omit,
        moderation: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_compression: Optional[int] | Omit = omit,
        output_format: Optional[str] | Omit = omit,
        partial_images: Optional[int] | Omit = omit,
        quality: Optional[str] | Omit = omit,
        size: Optional[str] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ImageGenStreamEvent]:
        """
        Creates a high-quality image from a text prompt using GPT-IMAGE-1, the latest
        image generation model with automatic prompt optimization and enhanced visual
        capabilities.

        Args:
          prompt: A text description of the desired image(s). GPT-IMAGE-1 supports up to 32,000
              characters and provides automatic prompt optimization for best results.

          stream: If set to true, partial image data will be streamed as the image is being
              generated. When streaming, the response will be sent as server-sent events with
              partial image chunks. When stream is true, partial_images must be greater
              than 0.

          background:
              The background setting for the image generation. GPT-IMAGE-1 supports:
              transparent, opaque, auto.

          model: The model to use for image generation. GPT-IMAGE-1 is the latest model offering
              the best quality with automatic optimization and enhanced capabilities.

          moderation: The moderation setting for the image generation. GPT-IMAGE-1 supports: low,
              auto.

          n: The number of images to generate. GPT-IMAGE-1 only supports n=1.

          output_compression: The output compression for the image generation. GPT-IMAGE-1 supports: 0-100.

          output_format: The output format for the image generation. GPT-IMAGE-1 supports: png, webp,
              jpeg.

          partial_images: The number of partial image chunks to return during streaming generation. This
              parameter is optional with a default of 0. When stream=true, this must be
              greater than 0 to receive progressive updates of the image as it's being
              generated. Higher values provide more frequent updates but may increase response
              overhead.

          quality: The quality of the image that will be generated. GPT-IMAGE-1 supports: auto
              (automatically select best quality), high, medium, low.

          size: The size of the generated images. GPT-IMAGE-1 supports: auto (automatically
              select best size), 1536x1024 (landscape), 1024x1536 (portrait).

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generate(
        self,
        *,
        prompt: str,
        stream: bool,
        background: Optional[str] | Omit = omit,
        model: str | Omit = omit,
        moderation: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_compression: Optional[int] | Omit = omit,
        output_format: Optional[str] | Omit = omit,
        partial_images: Optional[int] | Omit = omit,
        quality: Optional[str] | Omit = omit,
        size: Optional[str] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageGenerateResponse | Stream[ImageGenStreamEvent]:
        """
        Creates a high-quality image from a text prompt using GPT-IMAGE-1, the latest
        image generation model with automatic prompt optimization and enhanced visual
        capabilities.

        Args:
          prompt: A text description of the desired image(s). GPT-IMAGE-1 supports up to 32,000
              characters and provides automatic prompt optimization for best results.

          stream: If set to true, partial image data will be streamed as the image is being
              generated. When streaming, the response will be sent as server-sent events with
              partial image chunks. When stream is true, partial_images must be greater
              than 0.

          background:
              The background setting for the image generation. GPT-IMAGE-1 supports:
              transparent, opaque, auto.

          model: The model to use for image generation. GPT-IMAGE-1 is the latest model offering
              the best quality with automatic optimization and enhanced capabilities.

          moderation: The moderation setting for the image generation. GPT-IMAGE-1 supports: low,
              auto.

          n: The number of images to generate. GPT-IMAGE-1 only supports n=1.

          output_compression: The output compression for the image generation. GPT-IMAGE-1 supports: 0-100.

          output_format: The output format for the image generation. GPT-IMAGE-1 supports: png, webp,
              jpeg.

          partial_images: The number of partial image chunks to return during streaming generation. This
              parameter is optional with a default of 0. When stream=true, this must be
              greater than 0 to receive progressive updates of the image as it's being
              generated. Higher values provide more frequent updates but may increase response
              overhead.

          quality: The quality of the image that will be generated. GPT-IMAGE-1 supports: auto
              (automatically select best quality), high, medium, low.

          size: The size of the generated images. GPT-IMAGE-1 supports: auto (automatically
              select best size), 1536x1024 (landscape), 1024x1536 (portrait).

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["prompt"], ["prompt", "stream"])
    def generate(
        self,
        *,
        prompt: str,
        background: Optional[str] | Omit = omit,
        model: str | Omit = omit,
        moderation: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_compression: Optional[int] | Omit = omit,
        output_format: Optional[str] | Omit = omit,
        partial_images: Optional[int] | Omit = omit,
        quality: Optional[str] | Omit = omit,
        size: Optional[str] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageGenerateResponse | Stream[ImageGenStreamEvent]:
        if not self._client.model_access_key:
            raise TypeError(
                "Could not resolve authentication method. Expected model_access_key to be set for chat completions."
            )
        headers = extra_headers or {}
        headers = {
            "Authorization": f"Bearer {self._client.model_access_key}",
            **headers,
        }

        return self._post(
            "/images/generations",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "background": background,
                    "model": model,
                    "moderation": moderation,
                    "n": n,
                    "output_compression": output_compression,
                    "output_format": output_format,
                    "partial_images": partial_images,
                    "quality": quality,
                    "size": size,
                    "stream": stream,
                    "user": user,
                },
                image_generate_params.ImageGenerateParamsStreaming
                if stream
                else image_generate_params.ImageGenerateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageGenerateResponse,
            stream=stream or False,
            stream_cls=Stream[ImageGenStreamEvent],
        )


class AsyncImagesResource(AsyncAPIResource):
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

    @overload
    async def generate(
        self,
        *,
        prompt: str,
        background: Optional[str] | Omit = omit,
        model: str | Omit = omit,
        moderation: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_compression: Optional[int] | Omit = omit,
        output_format: Optional[str] | Omit = omit,
        partial_images: Optional[int] | Omit = omit,
        quality: Optional[str] | Omit = omit,
        size: Optional[str] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageGenerateResponse:
        """
        Creates a high-quality image from a text prompt using GPT-IMAGE-1, the latest
        image generation model with automatic prompt optimization and enhanced visual
        capabilities.

        Args:
          prompt: A text description of the desired image(s). GPT-IMAGE-1 supports up to 32,000
              characters and provides automatic prompt optimization for best results.

          background:
              The background setting for the image generation. GPT-IMAGE-1 supports:
              transparent, opaque, auto.

          model: The model to use for image generation. GPT-IMAGE-1 is the latest model offering
              the best quality with automatic optimization and enhanced capabilities.

          moderation: The moderation setting for the image generation. GPT-IMAGE-1 supports: low,
              auto.

          n: The number of images to generate. GPT-IMAGE-1 only supports n=1.

          output_compression: The output compression for the image generation. GPT-IMAGE-1 supports: 0-100.

          output_format: The output format for the image generation. GPT-IMAGE-1 supports: png, webp,
              jpeg.

          partial_images: The number of partial image chunks to return during streaming generation. This
              parameter is optional with a default of 0. When stream=true, this must be
              greater than 0 to receive progressive updates of the image as it's being
              generated. Higher values provide more frequent updates but may increase response
              overhead.

          quality: The quality of the image that will be generated. GPT-IMAGE-1 supports: auto
              (automatically select best quality), high, medium, low.

          size: The size of the generated images. GPT-IMAGE-1 supports: auto (automatically
              select best size), 1536x1024 (landscape), 1024x1536 (portrait).

          stream: If set to true, partial image data will be streamed as the image is being
              generated. When streaming, the response will be sent as server-sent events with
              partial image chunks. When stream is true, partial_images must be greater
              than 0.

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generate(
        self,
        *,
        prompt: str,
        stream: Literal[True],
        background: Optional[str] | Omit = omit,
        model: str | Omit = omit,
        moderation: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_compression: Optional[int] | Omit = omit,
        output_format: Optional[str] | Omit = omit,
        partial_images: Optional[int] | Omit = omit,
        quality: Optional[str] | Omit = omit,
        size: Optional[str] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ImageGenStreamEvent]:
        """
        Creates a high-quality image from a text prompt using GPT-IMAGE-1, the latest
        image generation model with automatic prompt optimization and enhanced visual
        capabilities.

        Args:
          prompt: A text description of the desired image(s). GPT-IMAGE-1 supports up to 32,000
              characters and provides automatic prompt optimization for best results.

          stream: If set to true, partial image data will be streamed as the image is being
              generated. When streaming, the response will be sent as server-sent events with
              partial image chunks. When stream is true, partial_images must be greater
              than 0.

          background:
              The background setting for the image generation. GPT-IMAGE-1 supports:
              transparent, opaque, auto.

          model: The model to use for image generation. GPT-IMAGE-1 is the latest model offering
              the best quality with automatic optimization and enhanced capabilities.

          moderation: The moderation setting for the image generation. GPT-IMAGE-1 supports: low,
              auto.

          n: The number of images to generate. GPT-IMAGE-1 only supports n=1.

          output_compression: The output compression for the image generation. GPT-IMAGE-1 supports: 0-100.

          output_format: The output format for the image generation. GPT-IMAGE-1 supports: png, webp,
              jpeg.

          partial_images: The number of partial image chunks to return during streaming generation. This
              parameter is optional with a default of 0. When stream=true, this must be
              greater than 0 to receive progressive updates of the image as it's being
              generated. Higher values provide more frequent updates but may increase response
              overhead.

          quality: The quality of the image that will be generated. GPT-IMAGE-1 supports: auto
              (automatically select best quality), high, medium, low.

          size: The size of the generated images. GPT-IMAGE-1 supports: auto (automatically
              select best size), 1536x1024 (landscape), 1024x1536 (portrait).

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generate(
        self,
        *,
        prompt: str,
        stream: bool,
        background: Optional[str] | Omit = omit,
        model: str | Omit = omit,
        moderation: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_compression: Optional[int] | Omit = omit,
        output_format: Optional[str] | Omit = omit,
        partial_images: Optional[int] | Omit = omit,
        quality: Optional[str] | Omit = omit,
        size: Optional[str] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageGenerateResponse | AsyncStream[ImageGenStreamEvent]:
        """
        Creates a high-quality image from a text prompt using GPT-IMAGE-1, the latest
        image generation model with automatic prompt optimization and enhanced visual
        capabilities.

        Args:
          prompt: A text description of the desired image(s). GPT-IMAGE-1 supports up to 32,000
              characters and provides automatic prompt optimization for best results.

          stream: If set to true, partial image data will be streamed as the image is being
              generated. When streaming, the response will be sent as server-sent events with
              partial image chunks. When stream is true, partial_images must be greater
              than 0.

          background:
              The background setting for the image generation. GPT-IMAGE-1 supports:
              transparent, opaque, auto.

          model: The model to use for image generation. GPT-IMAGE-1 is the latest model offering
              the best quality with automatic optimization and enhanced capabilities.

          moderation: The moderation setting for the image generation. GPT-IMAGE-1 supports: low,
              auto.

          n: The number of images to generate. GPT-IMAGE-1 only supports n=1.

          output_compression: The output compression for the image generation. GPT-IMAGE-1 supports: 0-100.

          output_format: The output format for the image generation. GPT-IMAGE-1 supports: png, webp,
              jpeg.

          partial_images: The number of partial image chunks to return during streaming generation. This
              parameter is optional with a default of 0. When stream=true, this must be
              greater than 0 to receive progressive updates of the image as it's being
              generated. Higher values provide more frequent updates but may increase response
              overhead.

          quality: The quality of the image that will be generated. GPT-IMAGE-1 supports: auto
              (automatically select best quality), high, medium, low.

          size: The size of the generated images. GPT-IMAGE-1 supports: auto (automatically
              select best size), 1536x1024 (landscape), 1024x1536 (portrait).

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["prompt"], ["prompt", "stream"])
    async def generate(
        self,
        *,
        prompt: str,
        background: Optional[str] | Omit = omit,
        model: str | Omit = omit,
        moderation: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_compression: Optional[int] | Omit = omit,
        output_format: Optional[str] | Omit = omit,
        partial_images: Optional[int] | Omit = omit,
        quality: Optional[str] | Omit = omit,
        size: Optional[str] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageGenerateResponse | AsyncStream[ImageGenStreamEvent]:
        if not self._client.model_access_key:
            raise TypeError(
                "Could not resolve authentication method. Expected model_access_key to be set for chat completions."
            )
        headers = extra_headers or {}
        headers = {
            "Authorization": f"Bearer {self._client.model_access_key}",
            **headers,
        }
        return await self._post(
            "/images/generations",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "background": background,
                    "model": model,
                    "moderation": moderation,
                    "n": n,
                    "output_compression": output_compression,
                    "output_format": output_format,
                    "partial_images": partial_images,
                    "quality": quality,
                    "size": size,
                    "stream": stream,
                    "user": user,
                },
                image_generate_params.ImageGenerateParamsStreaming
                if stream
                else image_generate_params.ImageGenerateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageGenerateResponse,
            stream=stream or False,
            stream_cls=AsyncStream[ImageGenStreamEvent],
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.generate = to_raw_response_wrapper(
            images.generate,
        )


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.generate = async_to_raw_response_wrapper(
            images.generate,
        )


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.generate = to_streamed_response_wrapper(
            images.generate,
        )


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.generate = async_to_streamed_response_wrapper(
            images.generate,
        )
