# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AssistantsAPIToolChoiceOptionParam", "AssistantsNamedToolChoice", "AssistantsNamedToolChoiceFunction"]


class AssistantsNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


class AssistantsNamedToolChoice(TypedDict, total=False):
    type: Required[Literal["function", "code_interpreter", "file_search"]]
    """The type of the tool. If type is `function`, the function name must be set"""

    function: AssistantsNamedToolChoiceFunction


AssistantsAPIToolChoiceOptionParam: TypeAlias = Union[Literal["none", "auto", "required"], AssistantsNamedToolChoice]
