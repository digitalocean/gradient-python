# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["AssistantsAPIToolChoiceOption", "AssistantsNamedToolChoice", "AssistantsNamedToolChoiceFunction"]


class AssistantsNamedToolChoiceFunction(BaseModel):
    name: str
    """The name of the function to call."""


class AssistantsNamedToolChoice(BaseModel):
    type: Literal["function", "code_interpreter", "file_search"]
    """The type of the tool. If type is `function`, the function name must be set"""

    function: Optional[AssistantsNamedToolChoiceFunction] = None


AssistantsAPIToolChoiceOption: TypeAlias = Union[Literal["none", "auto", "required"], AssistantsNamedToolChoice]
