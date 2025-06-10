# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .includable import Includable
from .reasoning_effort import ReasoningEffort
from .input_content_param import InputContentParam
from .input_message_param import InputMessageParam
from .output_message_param import OutputMessageParam
from .reasoning_item_param import ReasoningItemParam
from .compound_filter_param import CompoundFilterParam
from .comparison_filter_param import ComparisonFilterParam
from .computer_tool_call_param import ComputerToolCallParam
from .function_tool_call_param import FunctionToolCallParam
from .web_search_tool_call_param import WebSearchToolCallParam
from .file_search_tool_call_param import FileSearchToolCallParam
from .chat.web_search_context_size import WebSearchContextSize
from .chat.web_search_location_param import WebSearchLocationParam
from .chat.response_format_text_param import ResponseFormatTextParam
from .computer_tool_call_output_param import ComputerToolCallOutputParam
from .function_tool_call_output_param import FunctionToolCallOutputParam
from .chat.response_format_json_object_param import ResponseFormatJsonObjectParam

__all__ = [
    "ResponseCreateParams",
    "InputInputItemList",
    "InputInputItemListMessage",
    "InputInputItemListItemReference",
    "Reasoning",
    "Text",
    "TextFormat",
    "TextFormatTextResponseFormatJsonSchema",
    "ToolChoice",
    "ToolChoiceToolChoiceTypes",
    "ToolChoiceToolChoiceFunction",
    "Tool",
    "ToolFileSearchTool",
    "ToolFileSearchToolFilters",
    "ToolFileSearchToolRankingOptions",
    "ToolFunctionTool",
    "ToolComputerTool",
    "ToolWebSearchTool",
    "ToolWebSearchToolUserLocation",
]


class ResponseCreateParams(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputInputItemList]]]
    """Text, image, or file inputs to the model, used to generate a response.

    Learn more:

    - [Text inputs and outputs](/docs/guides/text)
    - [Image inputs](/docs/guides/images)
    - [File inputs](/docs/guides/pdf-files)
    - [Conversation state](/docs/guides/conversation-state)
    - [Function calling](/docs/guides/function-calling)
    """

    model: Required[
        Union[
            Literal[
                "o3-mini",
                "o3-mini-2025-01-31",
                "o1",
                "o1-2024-12-17",
                "o1-preview",
                "o1-preview-2024-09-12",
                "o1-mini",
                "o1-mini-2024-09-12",
                "gpt-4o",
                "gpt-4o-2024-11-20",
                "gpt-4o-2024-08-06",
                "gpt-4o-2024-05-13",
                "gpt-4o-audio-preview",
                "gpt-4o-audio-preview-2024-10-01",
                "gpt-4o-audio-preview-2024-12-17",
                "gpt-4o-mini-audio-preview",
                "gpt-4o-mini-audio-preview-2024-12-17",
                "gpt-4o-search-preview",
                "gpt-4o-mini-search-preview",
                "gpt-4o-search-preview-2025-03-11",
                "gpt-4o-mini-search-preview-2025-03-11",
                "chatgpt-4o-latest",
                "gpt-4o-mini",
                "gpt-4o-mini-2024-07-18",
                "gpt-4-turbo",
                "gpt-4-turbo-2024-04-09",
                "gpt-4-0125-preview",
                "gpt-4-turbo-preview",
                "gpt-4-1106-preview",
                "gpt-4-vision-preview",
                "gpt-4",
                "gpt-4-0314",
                "gpt-4-0613",
                "gpt-4-32k",
                "gpt-4-32k-0314",
                "gpt-4-32k-0613",
                "gpt-3.5-turbo",
                "gpt-3.5-turbo-16k",
                "gpt-3.5-turbo-0301",
                "gpt-3.5-turbo-0613",
                "gpt-3.5-turbo-1106",
                "gpt-3.5-turbo-0125",
                "gpt-3.5-turbo-16k-0613",
                "o1-pro",
                "o1-pro-2025-03-19",
                "computer-use-preview",
                "computer-use-preview-2025-03-11",
            ],
            str,
        ]
    ]
    """Model ID used to generate the response, like `gpt-4o` or `o1`.

    OpenAI offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model guide](/docs/models) to
    browse and compare available models.
    """

    include: Optional[List[Includable]]
    """Specify additional output data to include in the model response.

    Currently supported values are:

    - `file_search_call.results`: Include the search results of

      the file search tool call.

    - `message.input_image.image_url`: Include image urls from the input message.
    - `computer_call_output.output.image_url`: Include image urls from the computer
      call output.
    """

    instructions: Optional[str]
    """
    Inserts a system (or developer) message as the first item in the model's
    context.

    When using along with `previous_response_id`, the instructions from a previous
    response will be not be carried over to the next response. This makes it simple
    to swap out system (or developer) messages in new responses.
    """

    max_output_tokens: Optional[int]
    """
    An upper bound for the number of tokens that can be generated for a response,
    including visible output tokens and [reasoning tokens](/docs/guides/reasoning).
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    parallel_tool_calls: Optional[bool]
    """Whether to allow the model to run tool calls in parallel."""

    previous_response_id: Optional[str]
    """The unique ID of the previous response to the model.

    Use this to create multi-turn conversations. Learn more about
    [conversation state](/docs/guides/conversation-state).
    """

    reasoning: Optional[Reasoning]
    """**o-series models only**

    Configuration options for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    """

    store: Optional[bool]
    """Whether to store the generated model response for later retrieval via API."""

    stream: Optional[bool]
    """
    If set to true, the model response data will be streamed to the client as it is
    generated using
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
    See the [Streaming section below](/docs/api-reference/responses-streaming) for
    more information.
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or `top_p` but not both.
    """

    text: Text
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](/docs/guides/text)
    - [Structured Outputs](/docs/guides/structured-outputs)
    """

    tool_choice: ToolChoice
    """
    How the model should select which tool (or tools) to use when generating a
    response. See the `tools` parameter to see how to specify which tools the model
    can call.
    """

    tools: Iterable[Tool]
    """An array of tools the model may call while generating a response.

    You can specify which tool to use by setting the `tool_choice` parameter.

    The two categories of tools you can provide the model are:

    - **Built-in tools**: Tools that are provided by OpenAI that extend the model's
      capabilities, like [web search](/docs/guides/tools-web-search) or
      [file search](/docs/guides/tools-file-search). Learn more about
      [built-in tools](/docs/guides/tools).
    - **Function calls (custom tools)**: Functions that are defined by you, enabling
      the model to call your own code. Learn more about
      [function calling](/docs/guides/function-calling).
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """

    truncation: Optional[Literal["auto", "disabled"]]
    """The truncation strategy to use for the model response.

    - `auto`: If the context of this response and previous ones exceeds the model's
      context window size, the model will truncate the response to fit the context
      window by dropping input items in the middle of the conversation.
    - `disabled` (default): If a model response will exceed the context window size
      for a model, the request will fail with a 400 error.
    """

    user: str
    """
    A unique identifier representing your end-user, which can help OpenAI to monitor
    and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids).
    """


class InputInputItemListMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[InputContentParam]]]
    """
    Text, image, or audio input to the model, used to generate a response. Can also
    contain previous assistant responses.
    """

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class InputInputItemListItemReference(TypedDict, total=False):
    id: Required[str]
    """The ID of the item to reference."""

    type: Required[Literal["item_reference"]]
    """The type of item to reference. Always `item_reference`."""


InputInputItemList: TypeAlias = Union[
    InputInputItemListMessage,
    InputMessageParam,
    OutputMessageParam,
    FileSearchToolCallParam,
    ComputerToolCallParam,
    ComputerToolCallOutputParam,
    WebSearchToolCallParam,
    FunctionToolCallParam,
    FunctionToolCallOutputParam,
    ReasoningItemParam,
    InputInputItemListItemReference,
]


class Reasoning(TypedDict, total=False):
    effort: Optional[ReasoningEffort]
    """**o-series models only**

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
    supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
    result in faster responses and fewer tokens used on reasoning in a response.
    """

    generate_summary: Optional[Literal["concise", "detailed"]]
    """**computer_use_preview only**

    A summary of the reasoning performed by the model. This can be useful for
    debugging and understanding the model's reasoning process. One of `concise` or
    `detailed`.
    """


class TextFormatTextResponseFormatJsonSchema(TypedDict, total=False):
    schema: Required[Dict[str, object]]
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    type: Required[Literal["json_schema"]]
    """The type of response format being defined. Always `json_schema`."""

    description: str
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    name: str
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    strict: Optional[bool]
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. To
    learn more, read the
    [Structured Outputs guide](/docs/guides/structured-outputs).
    """


TextFormat: TypeAlias = Union[
    ResponseFormatTextParam, TextFormatTextResponseFormatJsonSchema, ResponseFormatJsonObjectParam
]


class Text(TypedDict, total=False):
    format: TextFormat
    """An object specifying the format that the model must output.

    Configuring `{ "type": "json_schema" }` enables Structured Outputs, which
    ensures the model will match your supplied JSON schema. Learn more in the
    [Structured Outputs guide](/docs/guides/structured-outputs).

    The default format is `{ "type": "text" }` with no additional options.

    **Not recommended for gpt-4o and newer models:**

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """


class ToolChoiceToolChoiceTypes(TypedDict, total=False):
    type: Required[
        Literal["file_search", "web_search_preview", "computer_use_preview", "web_search_preview_2025_03_11"]
    ]
    """The type of hosted tool the model should to use.

    Learn more about [built-in tools](/docs/guides/tools).

    Allowed values are:

    - `file_search`
    - `web_search_preview`
    - `computer_use_preview`
    """


class ToolChoiceToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""

    type: Required[Literal["function"]]
    """For function calling, the type is always `function`."""


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"], ToolChoiceToolChoiceTypes, ToolChoiceToolChoiceFunction
]

ToolFileSearchToolFilters: TypeAlias = Union[ComparisonFilterParam, CompoundFilterParam]


class ToolFileSearchToolRankingOptions(TypedDict, total=False):
    ranker: Literal["auto", "default-2024-11-15"]
    """The ranker to use for the file search."""

    score_threshold: float
    """
    The score threshold for the file search, a number between 0 and 1. Numbers
    closer to 1 will attempt to return only the most relevant results, but may
    return fewer results.
    """


class ToolFileSearchTool(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: Required[List[str]]
    """The IDs of the vector stores to search."""

    filters: ToolFileSearchToolFilters
    """A filter to apply based on file attributes."""

    max_num_results: int
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: ToolFileSearchToolRankingOptions
    """Ranking options for search."""


class ToolFunctionTool(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""

    parameters: Required[Dict[str, object]]
    """A JSON schema object describing the parameters of the function."""

    strict: Required[bool]
    """Whether to enforce strict parameter validation. Default `true`."""

    type: Required[Literal["function"]]
    """The type of the function tool. Always `function`."""

    description: Optional[str]
    """A description of the function.

    Used by the model to determine whether or not to call the function.
    """


class ToolComputerTool(TypedDict, total=False):
    display_height: Required[float]
    """The height of the computer display."""

    display_width: Required[float]
    """The width of the computer display."""

    environment: Required[Literal["mac", "windows", "ubuntu", "browser"]]
    """The type of computer environment to control."""

    type: Required[Literal["computer_use_preview"]]
    """The type of the computer use tool. Always `computer_use_preview`."""


class ToolWebSearchToolUserLocation(WebSearchLocationParam, total=False):
    type: Required[Literal["approximate"]]
    """The type of location approximation. Always `approximate`."""


class ToolWebSearchTool(TypedDict, total=False):
    type: Required[Literal["web_search_preview", "web_search_preview_2025_03_11"]]
    """The type of the web search tool. One of:

    - `web_search_preview`
    - `web_search_preview_2025_03_11`
    """

    search_context_size: WebSearchContextSize
    """
    High level guidance for the amount of context window space to use for the
    search. One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[ToolWebSearchToolUserLocation]
    """Approximate location parameters for the search."""


Tool: TypeAlias = Union[ToolFileSearchTool, ToolFunctionTool, ToolComputerTool, ToolWebSearchTool]
