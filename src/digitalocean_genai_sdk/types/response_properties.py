# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .compound_filter import CompoundFilter
from .reasoning_effort import ReasoningEffort
from .comparison_filter import ComparisonFilter
from .chat.web_search_location import WebSearchLocation
from .chat.response_format_text import ResponseFormatText
from .chat.web_search_context_size import WebSearchContextSize
from .chat.response_format_json_object import ResponseFormatJsonObject

__all__ = [
    "ResponseProperties",
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


class Reasoning(BaseModel):
    effort: Optional[ReasoningEffort] = None
    """**o-series models only**

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
    supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
    result in faster responses and fewer tokens used on reasoning in a response.
    """

    generate_summary: Optional[Literal["concise", "detailed"]] = None
    """**computer_use_preview only**

    A summary of the reasoning performed by the model. This can be useful for
    debugging and understanding the model's reasoning process. One of `concise` or
    `detailed`.
    """


class TextFormatTextResponseFormatJsonSchema(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    type: Literal["json_schema"]
    """The type of response format being defined. Always `json_schema`."""

    description: Optional[str] = None
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    name: Optional[str] = None
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    strict: Optional[bool] = None
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. To
    learn more, read the
    [Structured Outputs guide](/docs/guides/structured-outputs).
    """


TextFormat: TypeAlias = Union[ResponseFormatText, TextFormatTextResponseFormatJsonSchema, ResponseFormatJsonObject]


class Text(BaseModel):
    format: Optional[TextFormat] = None
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


class ToolChoiceToolChoiceTypes(BaseModel):
    type: Literal["file_search", "web_search_preview", "computer_use_preview", "web_search_preview_2025_03_11"]
    """The type of hosted tool the model should to use.

    Learn more about [built-in tools](/docs/guides/tools).

    Allowed values are:

    - `file_search`
    - `web_search_preview`
    - `computer_use_preview`
    """


class ToolChoiceToolChoiceFunction(BaseModel):
    name: str
    """The name of the function to call."""

    type: Literal["function"]
    """For function calling, the type is always `function`."""


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"], ToolChoiceToolChoiceTypes, ToolChoiceToolChoiceFunction
]

ToolFileSearchToolFilters: TypeAlias = Union[ComparisonFilter, CompoundFilter]


class ToolFileSearchToolRankingOptions(BaseModel):
    ranker: Optional[Literal["auto", "default-2024-11-15"]] = None
    """The ranker to use for the file search."""

    score_threshold: Optional[float] = None
    """
    The score threshold for the file search, a number between 0 and 1. Numbers
    closer to 1 will attempt to return only the most relevant results, but may
    return fewer results.
    """


class ToolFileSearchTool(BaseModel):
    type: Literal["file_search"]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: List[str]
    """The IDs of the vector stores to search."""

    filters: Optional[ToolFileSearchToolFilters] = None
    """A filter to apply based on file attributes."""

    max_num_results: Optional[int] = None
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: Optional[ToolFileSearchToolRankingOptions] = None
    """Ranking options for search."""


class ToolFunctionTool(BaseModel):
    name: str
    """The name of the function to call."""

    parameters: Dict[str, object]
    """A JSON schema object describing the parameters of the function."""

    strict: bool
    """Whether to enforce strict parameter validation. Default `true`."""

    type: Literal["function"]
    """The type of the function tool. Always `function`."""

    description: Optional[str] = None
    """A description of the function.

    Used by the model to determine whether or not to call the function.
    """


class ToolComputerTool(BaseModel):
    display_height: float
    """The height of the computer display."""

    display_width: float
    """The width of the computer display."""

    environment: Literal["mac", "windows", "ubuntu", "browser"]
    """The type of computer environment to control."""

    type: Literal["computer_use_preview"]
    """The type of the computer use tool. Always `computer_use_preview`."""


class ToolWebSearchToolUserLocation(WebSearchLocation):
    type: Literal["approximate"]
    """The type of location approximation. Always `approximate`."""


class ToolWebSearchTool(BaseModel):
    type: Literal["web_search_preview", "web_search_preview_2025_03_11"]
    """The type of the web search tool. One of:

    - `web_search_preview`
    - `web_search_preview_2025_03_11`
    """

    search_context_size: Optional[WebSearchContextSize] = None
    """
    High level guidance for the amount of context window space to use for the
    search. One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[ToolWebSearchToolUserLocation] = None
    """Approximate location parameters for the search."""


Tool: TypeAlias = Union[ToolFileSearchTool, ToolFunctionTool, ToolComputerTool, ToolWebSearchTool]


class ResponseProperties(BaseModel):
    instructions: Optional[str] = None
    """
    Inserts a system (or developer) message as the first item in the model's
    context.

    When using along with `previous_response_id`, the instructions from a previous
    response will be not be carried over to the next response. This makes it simple
    to swap out system (or developer) messages in new responses.
    """

    max_output_tokens: Optional[int] = None
    """
    An upper bound for the number of tokens that can be generated for a response,
    including visible output tokens and [reasoning tokens](/docs/guides/reasoning).
    """

    model: Union[
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
        None,
    ] = None
    """Model ID used to generate the response, like `gpt-4o` or `o1`.

    OpenAI offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model guide](/docs/models) to
    browse and compare available models.
    """

    previous_response_id: Optional[str] = None
    """The unique ID of the previous response to the model.

    Use this to create multi-turn conversations. Learn more about
    [conversation state](/docs/guides/conversation-state).
    """

    reasoning: Optional[Reasoning] = None
    """**o-series models only**

    Configuration options for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    """

    text: Optional[Text] = None
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](/docs/guides/text)
    - [Structured Outputs](/docs/guides/structured-outputs)
    """

    tool_choice: Optional[ToolChoice] = None
    """
    How the model should select which tool (or tools) to use when generating a
    response. See the `tools` parameter to see how to specify which tools the model
    can call.
    """

    tools: Optional[List[Tool]] = None
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

    truncation: Optional[Literal["auto", "disabled"]] = None
    """The truncation strategy to use for the model response.

    - `auto`: If the context of this response and previous ones exceeds the model's
      context window size, the model will truncate the response to fit the context
      window by dropping input items in the middle of the conversation.
    - `disabled` (default): If a model response will exceed the context window size
      for a model, the request will fail with a 400 error.
    """
