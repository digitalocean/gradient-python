# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

from .chat.response_format_text_param import ResponseFormatTextParam
from .chat.response_format_json_object_param import ResponseFormatJsonObjectParam
from .chat.response_format_json_schema_param import ResponseFormatJsonSchemaParam

__all__ = ["AssistantsAPIResponseFormatOptionParam"]

AssistantsAPIResponseFormatOptionParam: TypeAlias = Union[
    Literal["auto"], ResponseFormatTextParam, ResponseFormatJsonObjectParam, ResponseFormatJsonSchemaParam
]
