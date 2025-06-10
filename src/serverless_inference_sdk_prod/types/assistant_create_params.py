# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .reasoning_effort import ReasoningEffort
from .assistant_supported_models import AssistantSupportedModels
from .assistant_tools_code_param import AssistantToolsCodeParam
from .assistant_tools_function_param import AssistantToolsFunctionParam
from .api_response_format_option_param import APIResponseFormatOptionParam
from .assistant_tools_file_search_param import AssistantToolsFileSearchParam

__all__ = [
    "AssistantCreateParams",
    "ToolResources",
    "ToolResourcesCodeInterpreter",
    "ToolResourcesFileSearch",
    "ToolResourcesFileSearchVectorStore",
    "ToolResourcesFileSearchVectorStoreChunkingStrategy",
    "ToolResourcesFileSearchVectorStoreChunkingStrategyAutoChunkingStrategy",
    "ToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategy",
    "ToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategyStatic",
    "Tool",
]


class AssistantCreateParams(TypedDict, total=False):
    model: Required[Union[str, AssistantSupportedModels]]
    """ID of the model to use.

    You can use the [List models](/docs/api-reference/models/list) API to see all of
    your available models, or see our [Model overview](/docs/models) for
    descriptions of them.
    """

    description: Optional[str]
    """The description of the assistant. The maximum length is 512 characters."""

    instructions: Optional[str]
    """The system instructions that the assistant uses.

    The maximum length is 256,000 characters.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: Optional[str]
    """The name of the assistant. The maximum length is 256 characters."""

    reasoning_effort: Optional[ReasoningEffort]
    """**o-series models only**

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
    supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
    result in faster responses and fewer tokens used on reasoning in a response.
    """

    response_format: Optional[APIResponseFormatOptionParam]
    """Specifies the format that the model must output.

    Compatible with [GPT-4o](/docs/models#gpt-4o),
    [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models
    since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the [Structured Outputs guide](/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
    message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to
    produce JSON yourself via a system or user message. Without this, the model may
    generate an unending stream of whitespace until the generation reaches the token
    limit, resulting in a long-running and seemingly "stuck" request. Also note that
    the message content may be partially cut off if `finish_reason="length"`, which
    indicates the generation exceeded `max_tokens` or the conversation exceeded the
    max context length.
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic.
    """

    tool_resources: Optional[ToolResources]
    """A set of resources that are used by the assistant's tools.

    The resources are specific to the type of tool. For example, the
    `code_interpreter` tool requires a list of file IDs, while the `file_search`
    tool requires a list of vector store IDs.
    """

    tools: Iterable[Tool]
    """A list of tool enabled on the assistant.

    There can be a maximum of 128 tools per assistant. Tools can be of types
    `code_interpreter`, `file_search`, or `function`.
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.
    """


class ToolResourcesCodeInterpreter(TypedDict, total=False):
    file_ids: List[str]
    """
    A list of [file](/docs/api-reference/files) IDs made available to the
    `code_interpreter` tool. There can be a maximum of 20 files associated with the
    tool.
    """


class ToolResourcesFileSearchVectorStoreChunkingStrategyAutoChunkingStrategy(TypedDict, total=False):
    type: Required[Literal["auto"]]
    """Always `auto`."""


class ToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategyStatic(TypedDict, total=False):
    chunk_overlap_tokens: Required[int]
    """The number of tokens that overlap between chunks. The default value is `400`.

    Note that the overlap must not exceed half of `max_chunk_size_tokens`.
    """

    max_chunk_size_tokens: Required[int]
    """The maximum number of tokens in each chunk.

    The default value is `800`. The minimum value is `100` and the maximum value is
    `4096`.
    """


class ToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategy(TypedDict, total=False):
    static: Required[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategyStatic]

    type: Required[Literal["static"]]
    """Always `static`."""


ToolResourcesFileSearchVectorStoreChunkingStrategy: TypeAlias = Union[
    ToolResourcesFileSearchVectorStoreChunkingStrategyAutoChunkingStrategy,
    ToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategy,
]


class ToolResourcesFileSearchVectorStore(TypedDict, total=False):
    chunking_strategy: ToolResourcesFileSearchVectorStoreChunkingStrategy
    """The chunking strategy used to chunk the file(s).

    If not set, will use the `auto` strategy.
    """

    file_ids: List[str]
    """A list of [file](/docs/api-reference/files) IDs to add to the vector store.

    There can be a maximum of 10000 files in a vector store.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


class ToolResourcesFileSearch(TypedDict, total=False):
    vector_store_ids: List[str]
    """
    The [vector store](/docs/api-reference/vector-stores/object) attached to this
    assistant. There can be a maximum of 1 vector store attached to the assistant.
    """

    vector_stores: Iterable[ToolResourcesFileSearchVectorStore]
    """
    A helper to create a [vector store](/docs/api-reference/vector-stores/object)
    with file_ids and attach it to this assistant. There can be a maximum of 1
    vector store attached to the assistant.
    """


class ToolResources(TypedDict, total=False):
    code_interpreter: ToolResourcesCodeInterpreter

    file_search: ToolResourcesFileSearch


Tool: TypeAlias = Union[AssistantToolsCodeParam, AssistantToolsFileSearchParam, AssistantToolsFunctionParam]
