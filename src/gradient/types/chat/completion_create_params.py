# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "CompletionCreateParamsBase",
    "Message",
    "MessageChatCompletionRequestSystemMessage",
    "MessageChatCompletionRequestSystemMessageContent",
    "MessageChatCompletionRequestSystemMessageContentChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestSystemMessageContentChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestSystemMessageContentArrayOfContentPart",
    "MessageChatCompletionRequestSystemMessageContentArrayOfContentPartChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestSystemMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestDeveloperMessage",
    "MessageChatCompletionRequestDeveloperMessageContent",
    "MessageChatCompletionRequestDeveloperMessageContentChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestDeveloperMessageContentChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPart",
    "MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPartChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestUserMessage",
    "MessageChatCompletionRequestUserMessageContent",
    "MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartImageURL",
    "MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartImageURLImageURL",
    "MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartVideoURL",
    "MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartVideoURLVideoURL",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPart",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartImageURL",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartImageURLImageURL",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartVideoURL",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartVideoURLVideoURL",
    "MessageChatCompletionRequestAssistantMessage",
    "MessageChatCompletionRequestAssistantMessageContent",
    "MessageChatCompletionRequestAssistantMessageContentChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestAssistantMessageContentChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestAssistantMessageContentArrayOfContentPart",
    "MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestAssistantMessageToolCall",
    "MessageChatCompletionRequestAssistantMessageToolCallFunction",
    "MessageChatCompletionRequestToolMessage",
    "MessageChatCompletionRequestToolMessageContent",
    "MessageChatCompletionRequestToolMessageContentChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestToolMessageContentChatCompletionRequestContentPartTextCacheControl",
    "MessageChatCompletionRequestToolMessageContentArrayOfContentPart",
    "MessageChatCompletionRequestToolMessageContentArrayOfContentPartChatCompletionRequestContentPartText",
    "MessageChatCompletionRequestToolMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceChatCompletionNamedToolChoice",
    "ToolChoiceChatCompletionNamedToolChoiceFunction",
    "Tool",
    "ToolFunction",
    "CompletionCreateParamsNonStreaming",
    "CompletionCreateParamsStreaming",
]


class CompletionCreateParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """A list of messages comprising the conversation so far."""

    model: Required[str]
    """Model ID used to generate the response."""

    frequency_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    logit_bias: Optional[Dict[str, int]]
    """Modify the likelihood of specified tokens appearing in the completion.

    Accepts a JSON object that maps tokens (specified by their token ID in the
    tokenizer) to an associated bias value from -100 to 100. Mathematically, the
    bias is added to the logits generated by the model prior to sampling. The exact
    effect will vary per model, but values between -1 and 1 should decrease or
    increase likelihood of selection; values like -100 or 100 should result in a ban
    or exclusive selection of the relevant token.
    """

    logprobs: Optional[bool]
    """Whether to return log probabilities of the output tokens or not.

    If true, returns the log probabilities of each output token returned in the
    `content` of `message`.
    """

    max_completion_tokens: Optional[int]
    """
    The maximum number of completion tokens that may be used over the course of the
    run. The run will make a best effort to use only the number of completion tokens
    specified, across multiple turns of the run.
    """

    max_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the completion.

    The token count of your prompt plus `max_tokens` cannot exceed the model's
    context length.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    n: Optional[int]
    """How many chat completion choices to generate for each input message.

    Note that you will be charged based on the number of generated tokens across all
    of the choices. Keep `n` as `1` to minimize costs.
    """

    presence_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.
    """

    reasoning_effort: Optional[Literal["none", "minimal", "low", "medium", "high", "xhigh"]]
    """Constrains effort on reasoning for reasoning models.

    Reducing reasoning effort can result in faster responses and fewer tokens used
    on reasoning in a response.
    """

    stop: Union[Optional[str], SequenceNotStr[str], None]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
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

    Currently, only functions are supported as a tool.
    """

    top_logprobs: Optional[int]
    """
    An integer between 0 and 20 specifying the number of most likely tokens to
    return at each token position, each with an associated log probability.
    `logprobs` must be set to `true` if this parameter is used.
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


class MessageChatCompletionRequestSystemMessageContentChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestSystemMessageContentChatCompletionRequestContentPartText(TypedDict, total=False):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: MessageChatCompletionRequestSystemMessageContentChatCompletionRequestContentPartTextCacheControl
    """Cache control settings for the content part."""


class MessageChatCompletionRequestSystemMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestSystemMessageContentArrayOfContentPartChatCompletionRequestContentPartText(
    TypedDict, total=False
):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: MessageChatCompletionRequestSystemMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl
    """Cache control settings for the content part."""


MessageChatCompletionRequestSystemMessageContentArrayOfContentPart: TypeAlias = Union[
    str, MessageChatCompletionRequestSystemMessageContentArrayOfContentPartChatCompletionRequestContentPartText
]

MessageChatCompletionRequestSystemMessageContent: TypeAlias = Union[
    str,
    MessageChatCompletionRequestSystemMessageContentChatCompletionRequestContentPartText,
    SequenceNotStr[MessageChatCompletionRequestSystemMessageContentArrayOfContentPart],
]


class MessageChatCompletionRequestSystemMessage(TypedDict, total=False):
    """
    System-provided instructions that the model should follow, regardless of
    messages sent by the user.
    """

    content: Required[MessageChatCompletionRequestSystemMessageContent]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""


class MessageChatCompletionRequestDeveloperMessageContentChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestDeveloperMessageContentChatCompletionRequestContentPartText(TypedDict, total=False):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: MessageChatCompletionRequestDeveloperMessageContentChatCompletionRequestContentPartTextCacheControl
    """Cache control settings for the content part."""


class MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPartChatCompletionRequestContentPartText(
    TypedDict, total=False
):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl
    """Cache control settings for the content part."""


MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPart: TypeAlias = Union[
    str, MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPartChatCompletionRequestContentPartText
]

MessageChatCompletionRequestDeveloperMessageContent: TypeAlias = Union[
    str,
    MessageChatCompletionRequestDeveloperMessageContentChatCompletionRequestContentPartText,
    SequenceNotStr[MessageChatCompletionRequestDeveloperMessageContentArrayOfContentPart],
]


class MessageChatCompletionRequestDeveloperMessage(TypedDict, total=False):
    """
    Developer-provided instructions that the model should follow, regardless of
    messages sent by the user.
    """

    content: Required[MessageChatCompletionRequestDeveloperMessageContent]
    """The contents of the developer message."""

    role: Required[Literal["developer"]]
    """The role of the messages author, in this case `developer`."""


class MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartText(TypedDict, total=False):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartTextCacheControl
    """Cache control settings for the content part."""


class MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartImageURLImageURL(
    TypedDict, total=False
):
    """Image URL settings."""

    url: Required[str]
    """A URL or data URL containing image content."""

    detail: Literal["auto", "low", "high"]
    """Optional detail level for image understanding."""


class MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartImageURL(TypedDict, total=False):
    """Content part with type and image URL."""

    image_url: Required[MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartImageURLImageURL]
    """Image URL settings."""

    type: Required[Literal["image_url"]]
    """The type of content part"""


class MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartVideoURLVideoURL(
    TypedDict, total=False
):
    """Video URL settings."""

    url: Required[str]
    """A URL or data URL containing video content."""


class MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartVideoURL(TypedDict, total=False):
    """Content part with type and video URL."""

    type: Required[Literal["video_url"]]
    """The type of content part"""

    video_url: Required[MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartVideoURLVideoURL]
    """Video URL settings."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartText(
    TypedDict, total=False
):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: (
        MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl
    )
    """Cache control settings for the content part."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartImageURLImageURL(
    TypedDict, total=False
):
    """Image URL settings."""

    url: Required[str]
    """A URL or data URL containing image content."""

    detail: Literal["auto", "low", "high"]
    """Optional detail level for image understanding."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartImageURL(
    TypedDict, total=False
):
    """Content part with type and image URL."""

    image_url: Required[
        MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartImageURLImageURL
    ]
    """Image URL settings."""

    type: Required[Literal["image_url"]]
    """The type of content part"""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartVideoURLVideoURL(
    TypedDict, total=False
):
    """Video URL settings."""

    url: Required[str]
    """A URL or data URL containing video content."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartVideoURL(
    TypedDict, total=False
):
    """Content part with type and video URL."""

    type: Required[Literal["video_url"]]
    """The type of content part"""

    video_url: Required[
        MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartVideoURLVideoURL
    ]
    """Video URL settings."""


MessageChatCompletionRequestUserMessageContentArrayOfContentPart: TypeAlias = Union[
    str,
    MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartText,
    MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartImageURL,
    MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestContentPartVideoURL,
]

MessageChatCompletionRequestUserMessageContent: TypeAlias = Union[
    str,
    MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartText,
    MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartImageURL,
    MessageChatCompletionRequestUserMessageContentChatCompletionRequestContentPartVideoURL,
    SequenceNotStr[MessageChatCompletionRequestUserMessageContentArrayOfContentPart],
]


class MessageChatCompletionRequestUserMessage(TypedDict, total=False):
    """
    Messages sent by an end user, containing prompts or additional context
    information.
    """

    content: Required[MessageChatCompletionRequestUserMessageContent]
    """The contents of the user message."""

    role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""


class MessageChatCompletionRequestAssistantMessageContentChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestAssistantMessageContentChatCompletionRequestContentPartText(TypedDict, total=False):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: MessageChatCompletionRequestAssistantMessageContentChatCompletionRequestContentPartTextCacheControl
    """Cache control settings for the content part."""


class MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestContentPartText(
    TypedDict, total=False
):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl
    """Cache control settings for the content part."""


MessageChatCompletionRequestAssistantMessageContentArrayOfContentPart: TypeAlias = Union[
    str, MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestContentPartText
]

MessageChatCompletionRequestAssistantMessageContent: TypeAlias = Union[
    str,
    MessageChatCompletionRequestAssistantMessageContentChatCompletionRequestContentPartText,
    SequenceNotStr[MessageChatCompletionRequestAssistantMessageContentArrayOfContentPart],
]


class MessageChatCompletionRequestAssistantMessageToolCallFunction(TypedDict, total=False):
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


class MessageChatCompletionRequestAssistantMessageToolCall(TypedDict, total=False):
    id: Required[str]
    """The ID of the tool call."""

    function: Required[MessageChatCompletionRequestAssistantMessageToolCallFunction]
    """The function that the model called."""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class MessageChatCompletionRequestAssistantMessage(TypedDict, total=False):
    """Messages sent by the model in response to user messages."""

    role: Required[Literal["assistant"]]
    """The role of the messages author, in this case `assistant`."""

    content: Optional[MessageChatCompletionRequestAssistantMessageContent]
    """The contents of the assistant message."""

    tool_calls: Iterable[MessageChatCompletionRequestAssistantMessageToolCall]
    """The tool calls generated by the model, such as function calls."""


class MessageChatCompletionRequestToolMessageContentChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestToolMessageContentChatCompletionRequestContentPartText(TypedDict, total=False):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: MessageChatCompletionRequestToolMessageContentChatCompletionRequestContentPartTextCacheControl
    """Cache control settings for the content part."""


class MessageChatCompletionRequestToolMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl(
    TypedDict, total=False
):
    """Cache control settings for the content part."""

    type: Required[Literal["ephemeral"]]
    """The cache control type."""

    ttl: Literal["5m", "1h"]
    """The cache TTL."""


class MessageChatCompletionRequestToolMessageContentArrayOfContentPartChatCompletionRequestContentPartText(
    TypedDict, total=False
):
    """Content part with type and text"""

    text: Required[str]
    """The text content"""

    type: Required[Literal["text"]]
    """The type of content part"""

    cache_control: (
        MessageChatCompletionRequestToolMessageContentArrayOfContentPartChatCompletionRequestContentPartTextCacheControl
    )
    """Cache control settings for the content part."""


MessageChatCompletionRequestToolMessageContentArrayOfContentPart: TypeAlias = Union[
    str, MessageChatCompletionRequestToolMessageContentArrayOfContentPartChatCompletionRequestContentPartText
]

MessageChatCompletionRequestToolMessageContent: TypeAlias = Union[
    str,
    MessageChatCompletionRequestToolMessageContentChatCompletionRequestContentPartText,
    SequenceNotStr[MessageChatCompletionRequestToolMessageContentArrayOfContentPart],
]


class MessageChatCompletionRequestToolMessage(TypedDict, total=False):
    content: Required[MessageChatCompletionRequestToolMessageContent]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""


Message: TypeAlias = Union[
    MessageChatCompletionRequestSystemMessage,
    MessageChatCompletionRequestDeveloperMessage,
    MessageChatCompletionRequestUserMessage,
    MessageChatCompletionRequestAssistantMessage,
    MessageChatCompletionRequestToolMessage,
]


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


class ToolFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](/docs/guides/function-calling) for examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Optional[Literal[False]]
    """
    If set to true, the model response data will be streamed to the client as it is
    generated using server-sent events.
    """


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """
    If set to true, the model response data will be streamed to the client as it is
    generated using server-sent events.
    """


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
