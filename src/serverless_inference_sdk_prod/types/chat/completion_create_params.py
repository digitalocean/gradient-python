# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..reasoning_effort import ReasoningEffort
from ..function_object_param import FunctionObjectParam
from .model_ids_shared_param import ModelIDsSharedParam
from ..voice_ids_shared_param import VoiceIDsSharedParam
from .message_tool_call_param import MessageToolCallParam
from .web_search_context_size import WebSearchContextSize
from ..stop_configuration_param import StopConfigurationParam
from .web_search_location_param import WebSearchLocationParam
from .response_format_text_param import ResponseFormatTextParam
from .response_format_json_object_param import ResponseFormatJsonObjectParam
from .response_format_json_schema_param import ResponseFormatJsonSchemaParam
from ..chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
from .request_message_content_part_text_param import RequestMessageContentPartTextParam

__all__ = [
    "CompletionCreateParams",
    "Message",
    "MessageChatCompletionRequestDeveloperMessage",
    "MessageChatCompletionRequestSystemMessage",
    "MessageChatCompletionRequestUserMessage",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPart",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImage",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImageImageURL",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartAudio",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartAudioInputAudio",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartFile",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartFileFile",
    "MessageChatCompletionRequestAssistantMessage",
    "MessageChatCompletionRequestAssistantMessageAudio",
    "MessageChatCompletionRequestAssistantMessageContentArrayOfContentPart",
    "MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartRefusal",
    "MessageChatCompletionRequestAssistantMessageFunctionCall",
    "MessageChatCompletionRequestToolMessage",
    "MessageChatCompletionRequestFunctionMessage",
    "Audio",
    "FunctionCall",
    "FunctionCallChatCompletionFunctionCallOption",
    "Function",
    "Prediction",
    "ResponseFormat",
    "ToolChoice",
    "ToolChoiceChatCompletionNamedToolChoice",
    "ToolChoiceChatCompletionNamedToolChoiceFunction",
    "Tool",
    "WebSearchOptions",
    "WebSearchOptionsUserLocation",
]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """A list of messages comprising the conversation so far.

    Depending on the [model](/docs/models) you use, different message types
    (modalities) are supported, like [text](/docs/guides/text-generation),
    [images](/docs/guides/vision), and [audio](/docs/guides/audio).
    """

    model: Required[ModelIDsSharedParam]
    """Model ID used to generate the response, like `gpt-4o` or `o1`.

    OpenAI offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model guide](/docs/models) to
    browse and compare available models.
    """

    audio: Optional[Audio]
    """Parameters for audio output.

    Required when audio output is requested with `modalities: ["audio"]`.
    [Learn more](/docs/guides/audio).
    """

    frequency_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    function_call: FunctionCall
    """Deprecated in favor of `tool_choice`.

    Controls which (if any) function is called by the model.

    `none` means the model will not call a function and instead generates a message.

    `auto` means the model can pick between generating a message or calling a
    function.

    Specifying a particular function via `{"name": "my_function"}` forces the model
    to call that function.

    `none` is the default when no functions are present. `auto` is the default if
    functions are present.
    """

    functions: Iterable[Function]
    """Deprecated in favor of `tools`.

    A list of functions the model may generate JSON inputs for.
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
    An upper bound for the number of tokens that can be generated for a completion,
    including visible output tokens and [reasoning tokens](/docs/guides/reasoning).
    """

    max_tokens: Optional[int]
    """
    The maximum number of [tokens](/tokenizer) that can be generated in the chat
    completion. This value can be used to control
    [costs](https://openai.com/api/pricing/) for text generated via API.

    This value is now deprecated in favor of `max_completion_tokens`, and is not
    compatible with [o1 series models](/docs/guides/reasoning).
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    modalities: Optional[List[Literal["text", "audio"]]]
    """
    Output types that you would like the model to generate. Most models are capable
    of generating text, which is the default:

    `["text"]`

    The `gpt-4o-audio-preview` model can also be used to
    [generate audio](/docs/guides/audio). To request that this model generate both
    text and audio responses, you can use:

    `["text", "audio"]`
    """

    n: Optional[int]
    """How many chat completion choices to generate for each input message.

    Note that you will be charged based on the number of generated tokens across all
    of the choices. Keep `n` as `1` to minimize costs.
    """

    parallel_tool_calls: bool
    """
    Whether to enable
    [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling)
    during tool use.
    """

    prediction: Optional[Prediction]
    """
    Static predicted output content, such as the content of a text file that is
    being regenerated.
    """

    presence_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.
    """

    reasoning_effort: Optional[ReasoningEffort]
    """**o-series models only**

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
    supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
    result in faster responses and fewer tokens used on reasoning in a response.
    """

    response_format: ResponseFormat
    """An object specifying the format that the model must output.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the [Structured Outputs guide](/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """

    seed: Optional[int]
    """
    This feature is in Beta. If specified, our system will make a best effort to
    sample deterministically, such that repeated requests with the same `seed` and
    parameters should return the same result. Determinism is not guaranteed, and you
    should refer to the `system_fingerprint` response parameter to monitor changes
    in the backend.
    """

    service_tier: Optional[Literal["auto", "default"]]
    """Specifies the latency tier to use for processing the request.

    This parameter is relevant for customers subscribed to the scale tier service:

    - If set to 'auto', and the Project is Scale tier enabled, the system will
      utilize scale tier credits until they are exhausted.
    - If set to 'auto', and the Project is not Scale tier enabled, the request will
      be processed using the default service tier with a lower uptime SLA and no
      latency guarentee.
    - If set to 'default', the request will be processed using the default service
      tier with a lower uptime SLA and no latency guarentee.
    - When not set, the default behavior is 'auto'.

    When this parameter is set, the response body will include the `service_tier`
    utilized.
    """

    stop: Optional[StopConfigurationParam]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    store: Optional[bool]
    """
    Whether or not to store the output of this chat completion request for use in
    our [model distillation](/docs/guides/distillation) or
    [evals](/docs/guides/evals) products.
    """

    stream: Optional[bool]
    """
    If set to true, the model response data will be streamed to the client as it is
    generated using
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
    See the [Streaming section below](/docs/api-reference/chat/streaming) for more
    information, along with the
    [streaming responses](/docs/guides/streaming-responses) guide for more
    information on how to handle the streaming events.
    """

    stream_options: Optional[ChatCompletionStreamOptionsParam]
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

    Currently, only functions are supported as a tool. Use this to provide a list of
    functions the model may generate JSON inputs for. A max of 128 functions are
    supported.
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
    A unique identifier representing your end-user, which can help OpenAI to monitor
    and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids).
    """

    web_search_options: WebSearchOptions
    """
    This tool searches the web for relevant results to use in a response. Learn more
    about the [web search tool](/docs/guides/tools-web-search?api-mode=chat).
    """


class MessageChatCompletionRequestDeveloperMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[RequestMessageContentPartTextParam]]]
    """The contents of the developer message."""

    role: Required[Literal["developer"]]
    """The role of the messages author, in this case `developer`."""

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """


class MessageChatCompletionRequestSystemMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[RequestMessageContentPartTextParam]]]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImageImageURL(
    TypedDict, total=False
):
    url: Required[str]
    """Either a URL of the image or the base64 encoded image data."""

    detail: Literal["auto", "low", "high"]
    """Specifies the detail level of the image.

    Learn more in the
    [Vision guide](/docs/guides/vision#low-or-high-fidelity-image-understanding).
    """


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImage(
    TypedDict, total=False
):
    image_url: Required[
        MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImageImageURL
    ]

    type: Required[Literal["image_url"]]
    """The type of the content part."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartAudioInputAudio(
    TypedDict, total=False
):
    data: Required[str]
    """Base64 encoded audio data."""

    format: Required[Literal["wav", "mp3"]]
    """The format of the encoded audio data. Currently supports "wav" and "mp3"."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartAudio(
    TypedDict, total=False
):
    input_audio: Required[
        MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartAudioInputAudio
    ]

    type: Required[Literal["input_audio"]]
    """The type of the content part. Always `input_audio`."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartFileFile(
    TypedDict, total=False
):
    file_data: str
    """
    The base64 encoded file data, used when passing the file to the model as a
    string.
    """

    file_id: str
    """The ID of an uploaded file to use as input."""

    filename: str
    """The name of the file, used when passing the file to the model as a string."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartFile(
    TypedDict, total=False
):
    file: Required[
        MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartFileFile
    ]

    type: Required[Literal["file"]]
    """The type of the content part. Always `file`."""


MessageChatCompletionRequestUserMessageContentArrayOfContentPart: TypeAlias = Union[
    RequestMessageContentPartTextParam,
    MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImage,
    MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartAudio,
    MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartFile,
]


class MessageChatCompletionRequestUserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionRequestUserMessageContentArrayOfContentPart]]]
    """The contents of the user message."""

    role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """


class MessageChatCompletionRequestAssistantMessageAudio(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for a previous audio response from the model."""


class MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartRefusal(
    TypedDict, total=False
):
    refusal: Required[str]
    """The refusal message generated by the model."""

    type: Required[Literal["refusal"]]
    """The type of the content part."""


MessageChatCompletionRequestAssistantMessageContentArrayOfContentPart: TypeAlias = Union[
    RequestMessageContentPartTextParam,
    MessageChatCompletionRequestAssistantMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartRefusal,
]


class MessageChatCompletionRequestAssistantMessageFunctionCall(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class MessageChatCompletionRequestAssistantMessage(TypedDict, total=False):
    role: Required[Literal["assistant"]]
    """The role of the messages author, in this case `assistant`."""

    audio: Optional[MessageChatCompletionRequestAssistantMessageAudio]
    """Data about a previous audio response from the model.

    [Learn more](/docs/guides/audio).
    """

    content: Union[str, Iterable[MessageChatCompletionRequestAssistantMessageContentArrayOfContentPart], None]
    """The contents of the assistant message.

    Required unless `tool_calls` or `function_call` is specified.
    """

    function_call: Optional[MessageChatCompletionRequestAssistantMessageFunctionCall]
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

    refusal: Optional[str]
    """The refusal message by the assistant."""

    tool_calls: Iterable[MessageToolCallParam]
    """The tool calls generated by the model, such as function calls."""


class MessageChatCompletionRequestToolMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[RequestMessageContentPartTextParam]]]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""


class MessageChatCompletionRequestFunctionMessage(TypedDict, total=False):
    content: Required[Optional[str]]
    """The contents of the function message."""

    name: Required[str]
    """The name of the function to call."""

    role: Required[Literal["function"]]
    """The role of the messages author, in this case `function`."""


Message: TypeAlias = Union[
    MessageChatCompletionRequestDeveloperMessage,
    MessageChatCompletionRequestSystemMessage,
    MessageChatCompletionRequestUserMessage,
    MessageChatCompletionRequestAssistantMessage,
    MessageChatCompletionRequestToolMessage,
    MessageChatCompletionRequestFunctionMessage,
]


class Audio(TypedDict, total=False):
    format: Required[Literal["wav", "mp3", "flac", "opus", "pcm16"]]
    """Specifies the output audio format.

    Must be one of `wav`, `mp3`, `flac`, `opus`, or `pcm16`.
    """

    voice: Required[VoiceIDsSharedParam]
    """The voice the model uses to respond.

    Supported voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, and
    `shimmer`.
    """


class FunctionCallChatCompletionFunctionCallOption(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


FunctionCall: TypeAlias = Union[Literal["none", "auto"], FunctionCallChatCompletionFunctionCallOption]


class Function(TypedDict, total=False):
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


class Prediction(TypedDict, total=False):
    content: Required[Union[str, Iterable[RequestMessageContentPartTextParam]]]
    """
    The content that should be matched when generating a model response. If
    generated tokens would match this content, the entire model response can be
    returned much more quickly.
    """

    type: Required[Literal["content"]]
    """The type of the predicted content you want to provide.

    This type is currently always `content`.
    """


ResponseFormat: TypeAlias = Union[ResponseFormatTextParam, ResponseFormatJsonSchemaParam, ResponseFormatJsonObjectParam]


class ToolChoiceChatCompletionNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


class ToolChoiceChatCompletionNamedToolChoice(TypedDict, total=False):
    function: Required[ToolChoiceChatCompletionNamedToolChoiceFunction]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceChatCompletionNamedToolChoice]


class Tool(TypedDict, total=False):
    function: Required[FunctionObjectParam]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class WebSearchOptionsUserLocation(TypedDict, total=False):
    approximate: Required[WebSearchLocationParam]
    """Approximate location parameters for the search."""

    type: Required[Literal["approximate"]]
    """The type of location approximation. Always `approximate`."""


class WebSearchOptions(TypedDict, total=False):
    search_context_size: WebSearchContextSize
    """
    High level guidance for the amount of context window space to use for the
    search. One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[WebSearchOptionsUserLocation]
    """Approximate location parameters for the search."""
