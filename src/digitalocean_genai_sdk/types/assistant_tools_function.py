# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .function_object import FunctionObject

__all__ = ["AssistantToolsFunction"]


class AssistantToolsFunction(BaseModel):
    function: FunctionObject

    type: Literal["function"]
    """The type of tool being defined: `function`"""
