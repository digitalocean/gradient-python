# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .function_object_param import FunctionObjectParam

__all__ = ["AssistantToolsFunctionParam"]


class AssistantToolsFunctionParam(TypedDict, total=False):
    function: Required[FunctionObjectParam]

    type: Required[Literal["function"]]
    """The type of tool being defined: `function`"""
