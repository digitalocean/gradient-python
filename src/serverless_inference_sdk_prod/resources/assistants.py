# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    ReasoningEffort,
    assistant_list_params,
    assistant_create_params,
    assistant_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.assistant_object import AssistantObject
from ..types.reasoning_effort import ReasoningEffort
from ..types.assistant_list_response import AssistantListResponse
from ..types.assistant_delete_response import AssistantDeleteResponse
from ..types.assistant_supported_models import AssistantSupportedModels
from ..types.api_response_format_option_param import APIResponseFormatOptionParam

__all__ = ["AssistantsResource", "AsyncAssistantsResource"]


class AssistantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssistantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AssistantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssistantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AssistantsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Union[str, AssistantSupportedModels],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: Optional[APIResponseFormatOptionParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_resources: Optional[assistant_create_params.ToolResources] | NotGiven = NOT_GIVEN,
        tools: Iterable[assistant_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantObject:
        """
        Create an assistant with a model and instructions.

        Args:
          model: ID of the model to use. You can use the
              [List models](/docs/api-reference/models/list) API to see all of your available
              models, or see our [Model overview](/docs/models) for descriptions of them.

          description: The description of the assistant. The maximum length is 512 characters.

          instructions: The system instructions that the assistant uses. The maximum length is 256,000
              characters.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the assistant. The maximum length is 256 characters.

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: Specifies the format that the model must output. Compatible with
              [GPT-4o](/docs/models#gpt-4o),
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

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

          tool_resources: A set of resources that are used by the assistant's tools. The resources are
              specific to the type of tool. For example, the `code_interpreter` tool requires
              a list of file IDs, while the `file_search` tool requires a list of vector store
              IDs.

          tools: A list of tool enabled on the assistant. There can be a maximum of 128 tools per
              assistant. Tools can be of types `code_interpreter`, `file_search`, or
              `function`.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or temperature but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/assistants",
            body=maybe_transform(
                {
                    "model": model,
                    "description": description,
                    "instructions": instructions,
                    "metadata": metadata,
                    "name": name,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "temperature": temperature,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                },
                assistant_create_params.AssistantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantObject,
        )

    def retrieve(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantObject:
        """
        Retrieves an assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            f"/assistants/{assistant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantObject,
        )

    def update(
        self,
        assistant_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        model: Union[str, AssistantSupportedModels] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: Optional[APIResponseFormatOptionParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_resources: Optional[assistant_update_params.ToolResources] | NotGiven = NOT_GIVEN,
        tools: Iterable[assistant_update_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantObject:
        """Modifies an assistant.

        Args:
          description: The description of the assistant.

        The maximum length is 512 characters.

          instructions: The system instructions that the assistant uses. The maximum length is 256,000
              characters.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          model: ID of the model to use. You can use the
              [List models](/docs/api-reference/models/list) API to see all of your available
              models, or see our [Model overview](/docs/models) for descriptions of them.

          name: The name of the assistant. The maximum length is 256 characters.

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: Specifies the format that the model must output. Compatible with
              [GPT-4o](/docs/models#gpt-4o),
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

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

          tool_resources: A set of resources that are used by the assistant's tools. The resources are
              specific to the type of tool. For example, the `code_interpreter` tool requires
              a list of file IDs, while the `file_search` tool requires a list of vector store
              IDs.

          tools: A list of tool enabled on the assistant. There can be a maximum of 128 tools per
              assistant. Tools can be of types `code_interpreter`, `file_search`, or
              `function`.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or temperature but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._post(
            f"/assistants/{assistant_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "temperature": temperature,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                },
                assistant_update_params.AssistantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantObject,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantListResponse:
        """Returns a list of assistants.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/assistants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    assistant_list_params.AssistantListParams,
                ),
            ),
            cast_to=AssistantListResponse,
        )

    def delete(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantDeleteResponse:
        """
        Delete an assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._delete(
            f"/assistants/{assistant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantDeleteResponse,
        )


class AsyncAssistantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssistantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssistantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssistantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncAssistantsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Union[str, AssistantSupportedModels],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: Optional[APIResponseFormatOptionParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_resources: Optional[assistant_create_params.ToolResources] | NotGiven = NOT_GIVEN,
        tools: Iterable[assistant_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantObject:
        """
        Create an assistant with a model and instructions.

        Args:
          model: ID of the model to use. You can use the
              [List models](/docs/api-reference/models/list) API to see all of your available
              models, or see our [Model overview](/docs/models) for descriptions of them.

          description: The description of the assistant. The maximum length is 512 characters.

          instructions: The system instructions that the assistant uses. The maximum length is 256,000
              characters.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the assistant. The maximum length is 256 characters.

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: Specifies the format that the model must output. Compatible with
              [GPT-4o](/docs/models#gpt-4o),
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

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

          tool_resources: A set of resources that are used by the assistant's tools. The resources are
              specific to the type of tool. For example, the `code_interpreter` tool requires
              a list of file IDs, while the `file_search` tool requires a list of vector store
              IDs.

          tools: A list of tool enabled on the assistant. There can be a maximum of 128 tools per
              assistant. Tools can be of types `code_interpreter`, `file_search`, or
              `function`.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or temperature but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/assistants",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "description": description,
                    "instructions": instructions,
                    "metadata": metadata,
                    "name": name,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "temperature": temperature,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                },
                assistant_create_params.AssistantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantObject,
        )

    async def retrieve(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantObject:
        """
        Retrieves an assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            f"/assistants/{assistant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantObject,
        )

    async def update(
        self,
        assistant_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        model: Union[str, AssistantSupportedModels] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: Optional[APIResponseFormatOptionParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_resources: Optional[assistant_update_params.ToolResources] | NotGiven = NOT_GIVEN,
        tools: Iterable[assistant_update_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantObject:
        """Modifies an assistant.

        Args:
          description: The description of the assistant.

        The maximum length is 512 characters.

          instructions: The system instructions that the assistant uses. The maximum length is 256,000
              characters.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          model: ID of the model to use. You can use the
              [List models](/docs/api-reference/models/list) API to see all of your available
              models, or see our [Model overview](/docs/models) for descriptions of them.

          name: The name of the assistant. The maximum length is 256 characters.

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: Specifies the format that the model must output. Compatible with
              [GPT-4o](/docs/models#gpt-4o),
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

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

          tool_resources: A set of resources that are used by the assistant's tools. The resources are
              specific to the type of tool. For example, the `code_interpreter` tool requires
              a list of file IDs, while the `file_search` tool requires a list of vector store
              IDs.

          tools: A list of tool enabled on the assistant. There can be a maximum of 128 tools per
              assistant. Tools can be of types `code_interpreter`, `file_search`, or
              `function`.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or temperature but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._post(
            f"/assistants/{assistant_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "temperature": temperature,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                },
                assistant_update_params.AssistantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantObject,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantListResponse:
        """Returns a list of assistants.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/assistants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    assistant_list_params.AssistantListParams,
                ),
            ),
            cast_to=AssistantListResponse,
        )

    async def delete(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantDeleteResponse:
        """
        Delete an assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._delete(
            f"/assistants/{assistant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantDeleteResponse,
        )


class AssistantsResourceWithRawResponse:
    def __init__(self, assistants: AssistantsResource) -> None:
        self._assistants = assistants

        self.create = to_raw_response_wrapper(
            assistants.create,
        )
        self.retrieve = to_raw_response_wrapper(
            assistants.retrieve,
        )
        self.update = to_raw_response_wrapper(
            assistants.update,
        )
        self.list = to_raw_response_wrapper(
            assistants.list,
        )
        self.delete = to_raw_response_wrapper(
            assistants.delete,
        )


class AsyncAssistantsResourceWithRawResponse:
    def __init__(self, assistants: AsyncAssistantsResource) -> None:
        self._assistants = assistants

        self.create = async_to_raw_response_wrapper(
            assistants.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            assistants.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            assistants.update,
        )
        self.list = async_to_raw_response_wrapper(
            assistants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            assistants.delete,
        )


class AssistantsResourceWithStreamingResponse:
    def __init__(self, assistants: AssistantsResource) -> None:
        self._assistants = assistants

        self.create = to_streamed_response_wrapper(
            assistants.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            assistants.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            assistants.update,
        )
        self.list = to_streamed_response_wrapper(
            assistants.list,
        )
        self.delete = to_streamed_response_wrapper(
            assistants.delete,
        )


class AsyncAssistantsResourceWithStreamingResponse:
    def __init__(self, assistants: AsyncAssistantsResource) -> None:
        self._assistants = assistants

        self.create = async_to_streamed_response_wrapper(
            assistants.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            assistants.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            assistants.update,
        )
        self.list = async_to_streamed_response_wrapper(
            assistants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            assistants.delete,
        )
