# Responses API (POST /v1/responses). See docs/RESPONSES_API_PR_BREAKDOWN.md.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.responses import response_create_params
from ...types.responses.response_create_response import ResponseCreateResponse

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.
        """
        return ResponsesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: str,
        input: Iterable[response_create_params.ResponseInputItem],
        tools: Iterable[response_create_params.ResponseTool] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ResponseToolChoice | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse:
        """
        Create a response from the Responses API (POST /v1/responses).

        Args:
            model: Model ID (e.g. openai-gpt-5.2-pro).
            input: List of input items: user messages, function_call, function_call_output.
            tools: Optional list of tools the model may call.
            max_output_tokens: Maximum tokens to generate.
            instructions: System or developer instructions.
            temperature: Sampling temperature.
            tool_choice: Which tool (if any) the model must or may call.
        """
        if not self._client.model_access_key:
            raise TypeError(
                "Could not resolve authentication method. Expected model_access_key to be set for the Responses API."
            )
        headers = extra_headers or {}
        headers = {
            "Authorization": f"Bearer {self._client.model_access_key}",
            **headers,
        }

        return self._post(
            "/v1/responses" if self._client._base_url_overridden else f"{self._client.inference_endpoint}/v1/responses",
            body=maybe_transform(
                {
                    "model": model,
                    "input": input,
                    "tools": tools,
                    "max_output_tokens": max_output_tokens,
                    "instructions": instructions,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ResponseCreateResponse,
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: str,
        input: Iterable[response_create_params.ResponseInputItem],
        tools: Iterable[response_create_params.ResponseTool] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: response_create_params.ResponseToolChoice | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse:
        """
        Create a response from the Responses API (POST /v1/responses).

        Args:
            model: Model ID (e.g. openai-gpt-5.2-pro).
            input: List of input items: user messages, function_call, function_call_output.
            tools: Optional list of tools the model may call.
            max_output_tokens: Maximum tokens to generate.
            instructions: System or developer instructions.
            temperature: Sampling temperature.
            tool_choice: Which tool (if any) the model must or may call.
        """
        if not getattr(self._client, "model_access_key", None) or not self._client.model_access_key:
            raise TypeError(
                "Could not resolve authentication method. Expected model_access_key to be set for the Responses API."
            )
        headers = extra_headers or {}
        headers = {
            "Authorization": f"Bearer {self._client.model_access_key}",
            **headers,
        }

        return await self._post(
            "/v1/responses" if self._client._base_url_overridden else f"{self._client.inference_endpoint}/v1/responses",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "input": input,
                    "tools": tools,
                    "max_output_tokens": max_output_tokens,
                    "instructions": instructions,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=ResponseCreateResponse,
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses
        self.create = to_raw_response_wrapper(responses.create)


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses
        self.create = async_to_raw_response_wrapper(responses.create)


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses
        self.create = to_streamed_response_wrapper(responses.create)


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses
        self.create = async_to_streamed_response_wrapper(responses.create)
