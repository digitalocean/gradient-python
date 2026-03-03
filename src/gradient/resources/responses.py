# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import response_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.shared.create_response_response import CreateResponseResponse
from ..types.shared.create_response_stream_response import CreateResponseStreamResponse

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    """Generate text-to-text responses from text prompts."""

    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text"]]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateResponseResponse:
        """Generate text responses from text prompts.

        This endpoint supports both streaming
        and non-streaming responses for VLLM models only.

        Args:
          input: The input text prompt or conversation history. Can be a string or an array of
              message objects for conversation context.

          model: Model ID used to generate the response. Must be a VLLM model.

          instructions: System-level instructions for the model. This sets the behavior and context for
              the response generation.

          max_output_tokens: Maximum number of tokens to generate in the response. If not specified, the
              model will use a default value.

          max_tokens: The maximum number of tokens that can be generated in the completion. Alias for
              max_output_tokens for compatibility.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Specifies the output types the model should generate. For text-to-text, this
              should be ["text"].

          parallel_tool_calls: Whether to enable parallel tool calls. When true, the model can make multiple
              tool calls in parallel.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using server-sent events.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Uses Responses API format (with `name`, `description`, `parameters` at top
              level).

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: Literal[True],
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text"]]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[CreateResponseStreamResponse]:
        """Generate text responses from text prompts.

        This endpoint supports both streaming
        and non-streaming responses for VLLM models only.

        Args:
          input: The input text prompt or conversation history. Can be a string or an array of
              message objects for conversation context.

          model: Model ID used to generate the response. Must be a VLLM model.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using server-sent events.

          instructions: System-level instructions for the model. This sets the behavior and context for
              the response generation.

          max_output_tokens: Maximum number of tokens to generate in the response. If not specified, the
              model will use a default value.

          max_tokens: The maximum number of tokens that can be generated in the completion. Alias for
              max_output_tokens for compatibility.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Specifies the output types the model should generate. For text-to-text, this
              should be ["text"].

          parallel_tool_calls: Whether to enable parallel tool calls. When true, the model can make multiple
              tool calls in parallel.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Uses Responses API format (with `name`, `description`, `parameters` at top
              level).

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: bool,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text"]]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateResponseResponse | Stream[CreateResponseStreamResponse]:
        """Generate text responses from text prompts.

        This endpoint supports both streaming
        and non-streaming responses for VLLM models only.

        Args:
          input: The input text prompt or conversation history. Can be a string or an array of
              message objects for conversation context.

          model: Model ID used to generate the response. Must be a VLLM model.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using server-sent events.

          instructions: System-level instructions for the model. This sets the behavior and context for
              the response generation.

          max_output_tokens: Maximum number of tokens to generate in the response. If not specified, the
              model will use a default value.

          max_tokens: The maximum number of tokens that can be generated in the completion. Alias for
              max_output_tokens for compatibility.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Specifies the output types the model should generate. For text-to-text, this
              should be ["text"].

          parallel_tool_calls: Whether to enable parallel tool calls. When true, the model can make multiple
              tool calls in parallel.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Uses Responses API format (with `name`, `description`, `parameters` at top
              level).

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text"]]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateResponseResponse | Stream[CreateResponseStreamResponse]:
        return self._post(
            "/responses" if self._client._base_url_overridden else f"{self._client.inference_endpoint}/v1/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "instructions": instructions,
                    "max_output_tokens": max_output_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "parallel_tool_calls": parallel_tool_calls,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                    "user": user,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateResponseResponse,
            stream=stream or False,
            stream_cls=Stream[CreateResponseStreamResponse],
        )


class AsyncResponsesResource(AsyncAPIResource):
    """Generate text-to-text responses from text prompts."""

    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text"]]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateResponseResponse:
        """Generate text responses from text prompts.

        This endpoint supports both streaming
        and non-streaming responses for VLLM models only.

        Args:
          input: The input text prompt or conversation history. Can be a string or an array of
              message objects for conversation context.

          model: Model ID used to generate the response. Must be a VLLM model.

          instructions: System-level instructions for the model. This sets the behavior and context for
              the response generation.

          max_output_tokens: Maximum number of tokens to generate in the response. If not specified, the
              model will use a default value.

          max_tokens: The maximum number of tokens that can be generated in the completion. Alias for
              max_output_tokens for compatibility.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Specifies the output types the model should generate. For text-to-text, this
              should be ["text"].

          parallel_tool_calls: Whether to enable parallel tool calls. When true, the model can make multiple
              tool calls in parallel.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using server-sent events.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Uses Responses API format (with `name`, `description`, `parameters` at top
              level).

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: Literal[True],
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text"]]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[CreateResponseStreamResponse]:
        """Generate text responses from text prompts.

        This endpoint supports both streaming
        and non-streaming responses for VLLM models only.

        Args:
          input: The input text prompt or conversation history. Can be a string or an array of
              message objects for conversation context.

          model: Model ID used to generate the response. Must be a VLLM model.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using server-sent events.

          instructions: System-level instructions for the model. This sets the behavior and context for
              the response generation.

          max_output_tokens: Maximum number of tokens to generate in the response. If not specified, the
              model will use a default value.

          max_tokens: The maximum number of tokens that can be generated in the completion. Alias for
              max_output_tokens for compatibility.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Specifies the output types the model should generate. For text-to-text, this
              should be ["text"].

          parallel_tool_calls: Whether to enable parallel tool calls. When true, the model can make multiple
              tool calls in parallel.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Uses Responses API format (with `name`, `description`, `parameters` at top
              level).

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: bool,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text"]]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateResponseResponse | AsyncStream[CreateResponseStreamResponse]:
        """Generate text responses from text prompts.

        This endpoint supports both streaming
        and non-streaming responses for VLLM models only.

        Args:
          input: The input text prompt or conversation history. Can be a string or an array of
              message objects for conversation context.

          model: Model ID used to generate the response. Must be a VLLM model.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using server-sent events.

          instructions: System-level instructions for the model. This sets the behavior and context for
              the response generation.

          max_output_tokens: Maximum number of tokens to generate in the response. If not specified, the
              model will use a default value.

          max_tokens: The maximum number of tokens that can be generated in the completion. Alias for
              max_output_tokens for compatibility.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Specifies the output types the model should generate. For text-to-text, this
              should be ["text"].

          parallel_tool_calls: Whether to enable parallel tool calls. When true, the model can make multiple
              tool calls in parallel.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Uses Responses API format (with `name`, `description`, `parameters` at top
              level).

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help DigitalOcean to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text"]]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        stream_options: Optional[response_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateResponseResponse | AsyncStream[CreateResponseStreamResponse]:
        return await self._post(
            "/responses" if self._client._base_url_overridden else f"{self._client.inference_endpoint}/v1/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "instructions": instructions,
                    "max_output_tokens": max_output_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "parallel_tool_calls": parallel_tool_calls,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                    "user": user,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateResponseResponse,
            stream=stream or False,
            stream_cls=AsyncStream[CreateResponseStreamResponse],
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
