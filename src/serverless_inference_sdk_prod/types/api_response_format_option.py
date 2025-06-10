# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .chat.response_format_text import ResponseFormatText
from .chat.response_format_json_object import ResponseFormatJsonObject
from .chat.response_format_json_schema import ResponseFormatJsonSchema

__all__ = ["APIResponseFormatOption"]

APIResponseFormatOption: TypeAlias = Union[
    Literal["auto"], ResponseFormatText, ResponseFormatJsonObject, ResponseFormatJsonSchema
]
