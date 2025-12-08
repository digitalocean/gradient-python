# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ImageGenerateResponse", "Data", "Usage", "UsageInputTokensDetails"]


class Data(BaseModel):
    """Represents the content of a generated image from GPT-IMAGE-1"""

    b64_json: str
    """The base64-encoded JSON of the generated image.

    GPT-IMAGE-1 returns images in b64_json format only.
    """

    revised_prompt: Optional[str] = None
    """The optimized prompt that was used to generate the image.

    GPT-IMAGE-1 automatically optimizes prompts for best results.
    """


class UsageInputTokensDetails(BaseModel):
    """Detailed breakdown of input tokens"""

    text_tokens: Optional[int] = None
    """Number of text tokens in the input"""


class Usage(BaseModel):
    """Usage statistics for the image generation request"""

    input_tokens: int
    """Number of tokens in the input prompt"""

    total_tokens: int
    """Total number of tokens used (input + output)"""

    input_tokens_details: Optional[UsageInputTokensDetails] = None
    """Detailed breakdown of input tokens"""

    output_tokens: Optional[int] = None
    """Number of tokens in the generated output"""


class ImageGenerateResponse(BaseModel):
    """The response from the image generation endpoint"""

    created: int
    """The Unix timestamp (in seconds) of when the images were created"""

    data: List[Data]
    """The list of generated images"""

    background: Optional[str] = None
    """The background setting used for the image generation"""

    output_format: Optional[str] = None
    """The output format of the generated image"""

    quality: Optional[str] = None
    """The quality setting used for the image generation"""

    size: Optional[str] = None
    """The size of the generated image"""

    usage: Optional[Usage] = None
    """Usage statistics for the image generation request"""
