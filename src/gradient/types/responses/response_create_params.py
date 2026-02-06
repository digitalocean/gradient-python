# Types for the Responses API (POST /v1/responses). See docs/RESPONSES_API_PR_BREAKDOWN.md.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ResponseCreateParams",
    "ResponseInputItem",
    "ResponseInputUserMessage",
    "ResponseInputFunctionCall",
    "ResponseInputFunctionCallOutput",
    "ResponseToolChoice",
    "ResponseToolChoiceFunction",
    "ResponseTool",
    "ResponseToolFunction",
]


class ResponseInputUserMessage(TypedDict, total=False):
    """User message in the request input list."""

    type: Required[Literal["message"]]
    role: Required[Literal["user"]]
    content: Required[str]


class ResponseInputFunctionCall(TypedDict, total=False):
    """Function call (assistant turn) in the request input list."""

    type: Required[Literal["function_call"]]
    id: Required[str]
    name: Required[str]
    arguments: Required[str]


class ResponseInputFunctionCallOutput(TypedDict, total=False):
    """Function call result (tool output) in the request input list."""

    type: Required[Literal["function_call_output"]]
    call_id: Required[str]
    output: Required[str]


ResponseInputItem: TypeAlias = Union[
    ResponseInputUserMessage,
    ResponseInputFunctionCall,
    ResponseInputFunctionCallOutput,
]


class ResponseToolFunction(TypedDict, total=False):
    """Function definition for a tool."""

    name: Required[str]
    description: str
    parameters: Dict[str, object]


class ResponseTool(TypedDict, total=False):
    """Tool the model may call (e.g. a function)."""

    type: Required[Literal["function"]]
    function: Required[ResponseToolFunction]


class ResponseToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class ResponseToolChoiceNamed(TypedDict, total=False):
    type: Required[Literal["function"]]
    function: Required[ResponseToolChoiceFunction]


ResponseToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    ResponseToolChoiceNamed,
]


class ResponseCreateParams(TypedDict, total=False):
    """Request body for POST /v1/responses."""

    model: Required[str]
    """Model ID (e.g. openai-gpt-5.2-pro)."""

    input: Required[Iterable[ResponseInputItem]]
    """List of input items: user messages, function_call, function_call_output."""

    tools: Iterable[ResponseTool]
    """Optional list of tools the model may call."""

    max_output_tokens: Optional[int]
    """Maximum tokens to generate."""

    instructions: Optional[str]
    """System or developer instructions."""

    temperature: Optional[float]
    """Sampling temperature."""

    tool_choice: ResponseToolChoice
    """Which tool (if any) the model must or may call."""
