# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .truncation_object_param import TruncationObjectParam
from ..assistant_tools_code_param import AssistantToolsCodeParam
from ..create_thread_request_param import CreateThreadRequestParam
from ..assistant_tools_function_param import AssistantToolsFunctionParam
from ..api_response_format_option_param import APIResponseFormatOptionParam
from ..assistant_tools_file_search_param import AssistantToolsFileSearchParam
from .assistants_api_tool_choice_option_param import AssistantsAPIToolChoiceOptionParam

__all__ = ["RunCreateParams", "ToolResources", "ToolResourcesCodeInterpreter", "ToolResourcesFileSearch", "Tool"]


class RunCreateParams(TypedDict, total=False):
    assistant_id: Required[str]
    """
    The ID of the [assistant](/docs/api-reference/assistants) to use to execute this
    run.
    """

    instructions: Optional[str]
    """Override the default system message of the assistant.

    This is useful for modifying the behavior on a per-run basis.
    """

    max_completion_tokens: Optional[int]
    """
    The maximum number of completion tokens that may be used over the course of the
    run. The run will make a best effort to use only the number of completion tokens
    specified, across multiple turns of the run. If the run exceeds the number of
    completion tokens specified, the run will end with status `incomplete`. See
    `incomplete_details` for more info.
    """

    max_prompt_tokens: Optional[int]
    """The maximum number of prompt tokens that may be used over the course of the run.

    The run will make a best effort to use only the number of prompt tokens
    specified, across multiple turns of the run. If the run exceeds the number of
    prompt tokens specified, the run will end with status `incomplete`. See
    `incomplete_details` for more info.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: Union[
        str,
        Literal[
            "gpt-4o",
            "gpt-4o-2024-11-20",
            "gpt-4o-2024-08-06",
            "gpt-4o-2024-05-13",
            "gpt-4o-mini",
            "gpt-4o-mini-2024-07-18",
            "gpt-4.5-preview",
            "gpt-4.5-preview-2025-02-27",
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
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo-0125",
            "gpt-3.5-turbo-16k-0613",
        ],
        None,
    ]
    """The ID of the [Model](/docs/api-reference/models) to be used to execute this
    run.

    If a value is provided here, it will override the model associated with the
    assistant. If not, the model associated with the assistant will be used.
    """

    parallel_tool_calls: bool
    """
    Whether to enable
    [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling)
    during tool use.
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

    stream: Optional[bool]
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic.
    """

    thread: CreateThreadRequestParam
    """Options to create a new thread.

    If no thread is provided when running a request, an empty thread will be
    created.
    """

    tool_choice: Optional[AssistantsAPIToolChoiceOptionParam]
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tools and instead generates a message. `auto` is the default value
    and means the model can pick between generating a message or calling one or more
    tools. `required` means the model must call one or more tools before responding
    to the user. Specifying a particular tool like `{"type": "file_search"}` or
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that tool.
    """

    tool_resources: Optional[ToolResources]
    """A set of resources that are used by the assistant's tools.

    The resources are specific to the type of tool. For example, the
    `code_interpreter` tool requires a list of file IDs, while the `file_search`
    tool requires a list of vector store IDs.
    """

    tools: Optional[Iterable[Tool]]
    """Override the tools the assistant can use for this run.

    This is useful for modifying the behavior on a per-run basis.
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.
    """

    truncation_strategy: Optional[TruncationObjectParam]
    """Controls for how a thread will be truncated prior to the run.

    Use this to control the intial context window of the run.
    """


class ToolResourcesCodeInterpreter(TypedDict, total=False):
    file_ids: List[str]
    """
    A list of [file](/docs/api-reference/files) IDs made available to the
    `code_interpreter` tool. There can be a maximum of 20 files associated with the
    tool.
    """


class ToolResourcesFileSearch(TypedDict, total=False):
    vector_store_ids: List[str]
    """
    The ID of the [vector store](/docs/api-reference/vector-stores/object) attached
    to this assistant. There can be a maximum of 1 vector store attached to the
    assistant.
    """


class ToolResources(TypedDict, total=False):
    code_interpreter: ToolResourcesCodeInterpreter

    file_search: ToolResourcesFileSearch


Tool: TypeAlias = Union[AssistantToolsCodeParam, AssistantToolsFileSearchParam, AssistantToolsFunctionParam]
