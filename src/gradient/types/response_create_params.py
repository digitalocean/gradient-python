# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ResponseCreateParams",
    "InputUnionMember1",
    "InputUnionMember1UnionMember0",
    "InputUnionMember1UnionMember0Content",
    "InputUnionMember1UnionMember1",
    "InputUnionMember1UnionMember1ContentUnionMember1",
    "InputUnionMember1UnionMember1ContentUnionMember1UnionMember0",
    "InputUnionMember1UnionMember1ToolCall",
    "InputUnionMember1UnionMember1ToolCallFunction",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceChatCompletionNamedToolChoice",
    "ToolChoiceChatCompletionNamedToolChoiceFunction",
    "Tool",
]


class ResponseCreateParams(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputUnionMember1]]]
    """The input text prompt or conversation history.

    Can be a string or an array of message objects for conversation context.
    """

    model: Required[str]
    """Model ID used to generate the response. Must be a VLLM model."""

    instructions: Optional[str]
    """System-level instructions for the model.

    This sets the behavior and context for the response generation.
    """

    max_output_tokens: Optional[int]
    """Maximum number of tokens to generate in the response.

    If not specified, the model will use a default value.
    """

    max_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the completion.

    Alias for max_output_tokens for compatibility.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    modalities: Optional[List[Literal["text"]]]
    """Specifies the output types the model should generate.

    For text-to-text, this should be ["text"].
    """

    parallel_tool_calls: Optional[bool]
    """Whether to enable parallel tool calls.

    When true, the model can make multiple tool calls in parallel.
    """

    stop: Union[Optional[str], SequenceNotStr[str], None]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    stream: Optional[bool]
    """
    If set to true, the model response data will be streamed to the client as it is
    generated using server-sent events.
    """

    stream_options: Optional[StreamOptions]
    """Options for streaming response. Only set this when you set `stream: true`."""

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or `top_p` but not both.
    """

    tool_choice: ToolChoice
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tool and instead generates a message. `auto` means the model can
    pick between generating a message or calling one or more tools. `required` means
    the model must call one or more tools. Specifying a particular tool via
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that tool.

    `none` is the default when no tools are present. `auto` is the default if tools
    are present.
    """

    tools: Iterable[Tool]
    """A list of tools the model may call.

    Currently, only functions are supported as a tool. Uses Responses API format
    (with `name`, `description`, `parameters` at top level).
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """

    user: str
    """
    A unique identifier representing your end-user, which can help DigitalOcean to
    monitor and detect abuse.
    """


class InputUnionMember1UnionMember0ContentTyped(TypedDict, total=False):
    text: str
    """The reasoning text content"""

    type: Literal["reasoning_text"]
    """The type of content"""


InputUnionMember1UnionMember0Content: TypeAlias = Union[InputUnionMember1UnionMember0ContentTyped, Dict[str, object]]


class InputUnionMember1UnionMember0Typed(TypedDict, total=False):
    type: Required[Literal["function_call", "function_call_output", "reasoning"]]
    """
    The type of input item (must be function_call, function_call_output, or
    reasoning)
    """

    id: str
    """The unique ID of the reasoning item (optional for reasoning)"""

    arguments: str
    """JSON string of function arguments (required for function_call)"""

    call_id: str
    """The call ID (required for function_call and function_call_output)"""

    content: Optional[Iterable[InputUnionMember1UnionMember0Content]]
    """Array of reasoning content parts (optional for reasoning, can be null)"""

    encrypted_content: Optional[str]
    """Encrypted content (optional)"""

    name: str
    """The function name (required for function_call)"""

    output: str
    """JSON string of function output (required for function_call_output)"""

    status: Optional[str]
    """Status of the item (optional, can be null)"""

    summary: Iterable[object]
    """Summary of the reasoning (optional for reasoning)"""


InputUnionMember1UnionMember0: TypeAlias = Union[InputUnionMember1UnionMember0Typed, Dict[str, object]]


class InputUnionMember1UnionMember1ContentUnionMember1UnionMember0(TypedDict, total=False):
    text: Required[str]
    """The text content"""

    type: Required[Literal["input_text"]]
    """The type of content part"""


InputUnionMember1UnionMember1ContentUnionMember1: TypeAlias = Union[
    InputUnionMember1UnionMember1ContentUnionMember1UnionMember0, Dict[str, object]
]


class InputUnionMember1UnionMember1ToolCallFunction(TypedDict, total=False):
    """The function that the model called."""

    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class InputUnionMember1UnionMember1ToolCall(TypedDict, total=False):
    id: Required[str]
    """The ID of the tool call."""

    function: Required[InputUnionMember1UnionMember1ToolCallFunction]
    """The function that the model called."""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class InputUnionMember1UnionMember1Typed(TypedDict, total=False):
    content: Required[Union[str, Iterable[InputUnionMember1UnionMember1ContentUnionMember1]]]
    """The content of the message (string or content parts array)"""

    role: Literal["user", "assistant", "system", "tool", "developer"]
    """The role of the message author"""

    tool_call_id: str
    """Tool call ID that this message is responding to (required for tool role)"""

    tool_calls: Iterable[InputUnionMember1UnionMember1ToolCall]
    """Tool calls made by the assistant (for assistant role messages)"""

    type: Literal["message"]
    """Optional type identifier for message items (used by some clients like Codex)"""


InputUnionMember1UnionMember1: TypeAlias = Union[InputUnionMember1UnionMember1Typed, Dict[str, object]]

InputUnionMember1: TypeAlias = Union[InputUnionMember1UnionMember0, InputUnionMember1UnionMember1]


class StreamOptions(TypedDict, total=False):
    """Options for streaming response. Only set this when you set `stream: true`."""

    include_usage: bool
    """If set, an additional chunk will be streamed before the `data: [DONE]` message.

    The `usage` field on this chunk shows the token usage statistics for the entire
    request, and the `choices` field will always be an empty array.

    All other chunks will also include a `usage` field, but with a null value.
    **NOTE:** If the stream is interrupted, you may not receive the final usage
    chunk which contains the total token usage for the request.
    """


class ToolChoiceChatCompletionNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


class ToolChoiceChatCompletionNamedToolChoice(TypedDict, total=False):
    """Specifies a tool the model should use.

    Use to force the model to call a specific function.
    """

    function: Required[ToolChoiceChatCompletionNamedToolChoiceFunction]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceChatCompletionNamedToolChoice]


class Tool(TypedDict, total=False):
    """Tool definition for Responses API (flat format).

    This format is used by VLLM's Responses API where name, description, and parameters are at the top level of the tool object.
    """

    type: Required[Literal["function", "web_search", "web_search_2025_08_26"]]
    """The type of the tool.

    Supported values are `function` (custom tools), `web_search`, and
    `web_search_2025_08_26` (built-in web search).
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    name: str
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](/docs/guides/function-calling) for examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """
