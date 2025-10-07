# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageGenerateParamsBase", "ImageGenerateParamsNonStreaming", "ImageGenerateParamsStreaming"]


class ImageGenerateParamsBase(TypedDict, total=False):
    prompt: Required[str]
    """A text description of the desired image(s).

    GPT-IMAGE-1 supports up to 32,000 characters and provides automatic prompt
    optimization for best results.
    """

    background: Optional[str]
    """The background setting for the image generation.

    GPT-IMAGE-1 supports: transparent, opaque, auto.
    """

    model: str
    """The model to use for image generation.

    GPT-IMAGE-1 is the latest model offering the best quality with automatic
    optimization and enhanced capabilities.
    """

    moderation: Optional[str]
    """The moderation setting for the image generation.

    GPT-IMAGE-1 supports: low, auto.
    """

    n: Optional[int]
    """The number of images to generate. GPT-IMAGE-1 only supports n=1."""

    output_compression: Optional[int]
    """The output compression for the image generation. GPT-IMAGE-1 supports: 0-100."""

    output_format: Optional[str]
    """The output format for the image generation.

    GPT-IMAGE-1 supports: png, webp, jpeg.
    """

    partial_images: Optional[int]
    """The number of partial image chunks to return during streaming generation.

    This parameter is optional with a default of 0. When stream=true, this must be
    greater than 0 to receive progressive updates of the image as it's being
    generated. Higher values provide more frequent updates but may increase response
    overhead.
    """

    quality: Optional[str]
    """The quality of the image that will be generated.

    GPT-IMAGE-1 supports: auto (automatically select best quality), high, medium,
    low.
    """

    size: Optional[str]
    """The size of the generated images.

    GPT-IMAGE-1 supports: auto (automatically select best size), 1536x1024
    (landscape), 1024x1536 (portrait).
    """

    user: Optional[str]
    """
    A unique identifier representing your end-user, which can help DigitalOcean to
    monitor and detect abuse.
    """


class ImageGenerateParamsNonStreaming(ImageGenerateParamsBase, total=False):
    stream: Optional[Literal[False]]
    """
    If set to true, partial image data will be streamed as the image is being
    generated. When streaming, the response will be sent as server-sent events with
    partial image chunks. When stream is true, partial_images must be greater
    than 0.
    """


class ImageGenerateParamsStreaming(ImageGenerateParamsBase):
    stream: Required[Literal[True]]
    """
    If set to true, partial image data will be streamed as the image is being
    generated. When streaming, the response will be sent as server-sent events with
    partial image chunks. When stream is true, partial_images must be greater
    than 0.
    """


ImageGenerateParams = Union[ImageGenerateParamsNonStreaming, ImageGenerateParamsStreaming]
