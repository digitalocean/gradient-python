# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ...file_search_ranker import FileSearchRanker

__all__ = [
    "RunStepObject",
    "LastError",
    "StepDetails",
    "StepDetailsRunStepDetailsMessageCreationObject",
    "StepDetailsRunStepDetailsMessageCreationObjectMessageCreation",
    "StepDetailsRunStepDetailsToolCallsObject",
    "StepDetailsRunStepDetailsToolCallsObjectToolCall",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObject",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreter",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutput",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputLogsObject",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObject",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObjectImage",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObject",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearch",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchRankingOptions",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResult",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResultContent",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObject",
    "StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObjectFunction",
    "Usage",
]


class LastError(BaseModel):
    code: Literal["server_error", "rate_limit_exceeded"]
    """One of `server_error` or `rate_limit_exceeded`."""

    message: str
    """A human-readable description of the error."""


class StepDetailsRunStepDetailsMessageCreationObjectMessageCreation(BaseModel):
    message_id: str
    """The ID of the message that was created by this run step."""


class StepDetailsRunStepDetailsMessageCreationObject(BaseModel):
    message_creation: StepDetailsRunStepDetailsMessageCreationObjectMessageCreation

    type: Literal["message_creation"]
    """Always `message_creation`."""


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputLogsObject(
    BaseModel
):
    logs: str
    """The text output from the Code Interpreter tool call."""

    type: Literal["logs"]
    """Always `logs`."""


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObjectImage(
    BaseModel
):
    file_id: str
    """The [file](/docs/api-reference/files) ID of the image."""


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObject(
    BaseModel
):
    image: StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObjectImage

    type: Literal["image"]
    """Always `image`."""


StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutput: TypeAlias = Union[
    StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputLogsObject,
    StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObject,
]


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreter(BaseModel):
    input: str
    """The input to the Code Interpreter tool call."""

    outputs: List[
        StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutput
    ]
    """The outputs from the Code Interpreter tool call.

    Code Interpreter can output one or more items, including text (`logs`) or images
    (`image`). Each of these are represented by a different object type.
    """


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObject(BaseModel):
    id: str
    """The ID of the tool call."""

    code_interpreter: StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreter
    """The Code Interpreter tool call definition."""

    type: Literal["code_interpreter"]
    """The type of tool call.

    This is always going to be `code_interpreter` for this type of tool call.
    """


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchRankingOptions(
    BaseModel
):
    ranker: FileSearchRanker
    """The ranker to use for the file search.

    If not specified will use the `auto` ranker.
    """

    score_threshold: float
    """The score threshold for the file search.

    All values must be a floating point number between 0 and 1.
    """


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResultContent(
    BaseModel
):
    text: Optional[str] = None
    """The text content of the file."""

    type: Optional[Literal["text"]] = None
    """The type of the content."""


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResult(
    BaseModel
):
    file_id: str
    """The ID of the file that result was found in."""

    file_name: str
    """The name of the file that result was found in."""

    score: float
    """The score of the result.

    All values must be a floating point number between 0 and 1.
    """

    content: Optional[
        List[
            StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResultContent
        ]
    ] = None
    """The content of the result that was found.

    The content is only included if requested via the include query parameter.
    """


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearch(BaseModel):
    ranking_options: Optional[
        StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchRankingOptions
    ] = None
    """The ranking options for the file search."""

    results: Optional[
        List[StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResult]
    ] = None
    """The results of the file search."""


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObject(BaseModel):
    id: str
    """The ID of the tool call object."""

    file_search: StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearch
    """For now, this is always going to be an empty object."""

    type: Literal["file_search"]
    """The type of tool call.

    This is always going to be `file_search` for this type of tool call.
    """


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObjectFunction(BaseModel):
    arguments: str
    """The arguments passed to the function."""

    name: str
    """The name of the function."""

    output: Optional[str] = None
    """The output of the function.

    This will be `null` if the outputs have not been
    [submitted](/docs/api-reference/runs/submitToolOutputs) yet.
    """


class StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObject(BaseModel):
    id: str
    """The ID of the tool call object."""

    function: StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObjectFunction
    """The definition of the function that was called."""

    type: Literal["function"]
    """The type of tool call.

    This is always going to be `function` for this type of tool call.
    """


StepDetailsRunStepDetailsToolCallsObjectToolCall: TypeAlias = Union[
    StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObject,
    StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObject,
    StepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObject,
]


class StepDetailsRunStepDetailsToolCallsObject(BaseModel):
    tool_calls: List[StepDetailsRunStepDetailsToolCallsObjectToolCall]
    """An array of tool calls the run step was involved in.

    These can be associated with one of three types of tools: `code_interpreter`,
    `file_search`, or `function`.
    """

    type: Literal["tool_calls"]
    """Always `tool_calls`."""


StepDetails: TypeAlias = Union[StepDetailsRunStepDetailsMessageCreationObject, StepDetailsRunStepDetailsToolCallsObject]


class Usage(BaseModel):
    completion_tokens: int
    """Number of completion tokens used over the course of the run step."""

    prompt_tokens: int
    """Number of prompt tokens used over the course of the run step."""

    total_tokens: int
    """Total number of tokens used (prompt + completion)."""


class RunStepObject(BaseModel):
    id: str
    """The identifier of the run step, which can be referenced in API endpoints."""

    assistant_id: str
    """
    The ID of the [assistant](/docs/api-reference/assistants) associated with the
    run step.
    """

    cancelled_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run step was cancelled."""

    completed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run step completed."""

    created_at: int
    """The Unix timestamp (in seconds) for when the run step was created."""

    expired_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run step expired.

    A step is considered expired if the parent run is expired.
    """

    failed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run step failed."""

    last_error: Optional[LastError] = None
    """The last error associated with this run step.

    Will be `null` if there are no errors.
    """

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    object: Literal["thread.run.step"]
    """The object type, which is always `thread.run.step`."""

    run_id: str
    """The ID of the [run](/docs/api-reference/runs) that this run step is a part of."""

    status: Literal["in_progress", "cancelled", "failed", "completed", "expired"]
    """
    The status of the run step, which can be either `in_progress`, `cancelled`,
    `failed`, `completed`, or `expired`.
    """

    step_details: StepDetails
    """The details of the run step."""

    thread_id: str
    """The ID of the [thread](/docs/api-reference/threads) that was run."""

    type: Literal["message_creation", "tool_calls"]
    """The type of run step, which can be either `message_creation` or `tool_calls`."""

    usage: Optional[Usage] = None
    """Usage statistics related to the run step.

    This value will be `null` while the run step's status is `in_progress`.
    """
