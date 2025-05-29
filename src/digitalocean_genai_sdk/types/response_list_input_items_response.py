# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .input_message import InputMessage
from .output_message import OutputMessage
from .computer_tool_call import ComputerToolCall
from .function_tool_call import FunctionToolCall
from .web_search_tool_call import WebSearchToolCall
from .file_search_tool_call import FileSearchToolCall
from .computer_tool_call_output import ComputerToolCallOutput
from .function_tool_call_output import FunctionToolCallOutput

__all__ = [
    "ResponseListInputItemsResponse",
    "Data",
    "DataMessage",
    "DataComputerCallOutput",
    "DataFunctionCall",
    "DataFunctionCallOutput",
]


class DataMessage(InputMessage):
    id: str
    """The unique ID of the message input."""


class DataComputerCallOutput(ComputerToolCallOutput):
    id: str  # type: ignore
    """The unique ID of the computer call tool output."""


class DataFunctionCall(FunctionToolCall):
    id: str  # type: ignore
    """The unique ID of the function tool call."""


class DataFunctionCallOutput(FunctionToolCallOutput):
    id: str  # type: ignore
    """The unique ID of the function call tool output."""


Data: TypeAlias = Annotated[
    Union[
        DataMessage,
        OutputMessage,
        FileSearchToolCall,
        ComputerToolCall,
        DataComputerCallOutput,
        WebSearchToolCall,
        DataFunctionCall,
        DataFunctionCallOutput,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseListInputItemsResponse(BaseModel):
    data: List[Data]
    """A list of items used to generate this response."""

    first_id: str
    """The ID of the first item in the list."""

    has_more: bool
    """Whether there are more items available."""

    last_id: str
    """The ID of the last item in the list."""

    object: Literal["list"]
    """The type of object returned, must be `list`."""
