# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.agents import function_create_params, function_update_params
from ...types.agents.function_create_response import FunctionCreateResponse
from ...types.agents.function_delete_response import FunctionDeleteResponse
from ...types.agents.function_update_response import FunctionUpdateResponse

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)

    def create(
        self,
        path_agent_uuid: str,
        *,
        body_agent_uuid: str | Omit = omit,
        description: str | Omit = omit,
        faas_name: str | Omit = omit,
        faas_namespace: str | Omit = omit,
        function_name: str | Omit = omit,
        input_schema: object | Omit = omit,
        output_schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionCreateResponse:
        """
        To create a function route for an agent, send a POST request to
        `/v2/gen-ai/agents/{agent_uuid}/functions`.

        Args:
          body_agent_uuid: Agent id

          description: Function description

          faas_name: The name of the function in the DigitalOcean functions platform

          faas_namespace: The namespace of the function in the DigitalOcean functions platform

          function_name: Function name

          input_schema: Describe the input schema for the function so the agent may call it

          output_schema: Describe the output schema for the function so the agent handle its response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `path_agent_uuid` but received {path_agent_uuid!r}")
        return self._post(
            f"/v2/gen-ai/agents/{path_agent_uuid}/functions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_agent_uuid}/functions",
            body=maybe_transform(
                {
                    "body_agent_uuid": body_agent_uuid,
                    "description": description,
                    "faas_name": faas_name,
                    "faas_namespace": faas_namespace,
                    "function_name": function_name,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionCreateResponse,
        )

    def update(
        self,
        path_function_uuid: str,
        *,
        path_agent_uuid: str,
        body_agent_uuid: str | Omit = omit,
        description: str | Omit = omit,
        faas_name: str | Omit = omit,
        faas_namespace: str | Omit = omit,
        function_name: str | Omit = omit,
        body_function_uuid: str | Omit = omit,
        input_schema: object | Omit = omit,
        output_schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionUpdateResponse:
        """
        To update the function route, send a PUT request to
        `/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}`.

        Args:
          body_agent_uuid: Agent id

          description: Funciton description

          faas_name: The name of the function in the DigitalOcean functions platform

          faas_namespace: The namespace of the function in the DigitalOcean functions platform

          function_name: Function name

          body_function_uuid: Function id

          input_schema: Describe the input schema for the function so the agent may call it

          output_schema: Describe the output schema for the function so the agent handle its response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `path_agent_uuid` but received {path_agent_uuid!r}")
        if not path_function_uuid:
            raise ValueError(f"Expected a non-empty value for `path_function_uuid` but received {path_function_uuid!r}")
        return self._put(
            f"/v2/gen-ai/agents/{path_agent_uuid}/functions/{path_function_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_agent_uuid}/functions/{path_function_uuid}",
            body=maybe_transform(
                {
                    "body_agent_uuid": body_agent_uuid,
                    "description": description,
                    "faas_name": faas_name,
                    "faas_namespace": faas_namespace,
                    "function_name": function_name,
                    "body_function_uuid": body_function_uuid,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionUpdateResponse,
        )

    def delete(
        self,
        function_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionDeleteResponse:
        """
        To delete a function route from an agent, send a DELETE request to
        `/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not function_uuid:
            raise ValueError(f"Expected a non-empty value for `function_uuid` but received {function_uuid!r}")
        return self._delete(
            f"/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionDeleteResponse,
        )


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)

    async def create(
        self,
        path_agent_uuid: str,
        *,
        body_agent_uuid: str | Omit = omit,
        description: str | Omit = omit,
        faas_name: str | Omit = omit,
        faas_namespace: str | Omit = omit,
        function_name: str | Omit = omit,
        input_schema: object | Omit = omit,
        output_schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionCreateResponse:
        """
        To create a function route for an agent, send a POST request to
        `/v2/gen-ai/agents/{agent_uuid}/functions`.

        Args:
          body_agent_uuid: Agent id

          description: Function description

          faas_name: The name of the function in the DigitalOcean functions platform

          faas_namespace: The namespace of the function in the DigitalOcean functions platform

          function_name: Function name

          input_schema: Describe the input schema for the function so the agent may call it

          output_schema: Describe the output schema for the function so the agent handle its response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `path_agent_uuid` but received {path_agent_uuid!r}")
        return await self._post(
            f"/v2/gen-ai/agents/{path_agent_uuid}/functions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_agent_uuid}/functions",
            body=await async_maybe_transform(
                {
                    "body_agent_uuid": body_agent_uuid,
                    "description": description,
                    "faas_name": faas_name,
                    "faas_namespace": faas_namespace,
                    "function_name": function_name,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionCreateResponse,
        )

    async def update(
        self,
        path_function_uuid: str,
        *,
        path_agent_uuid: str,
        body_agent_uuid: str | Omit = omit,
        description: str | Omit = omit,
        faas_name: str | Omit = omit,
        faas_namespace: str | Omit = omit,
        function_name: str | Omit = omit,
        body_function_uuid: str | Omit = omit,
        input_schema: object | Omit = omit,
        output_schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionUpdateResponse:
        """
        To update the function route, send a PUT request to
        `/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}`.

        Args:
          body_agent_uuid: Agent id

          description: Funciton description

          faas_name: The name of the function in the DigitalOcean functions platform

          faas_namespace: The namespace of the function in the DigitalOcean functions platform

          function_name: Function name

          body_function_uuid: Function id

          input_schema: Describe the input schema for the function so the agent may call it

          output_schema: Describe the output schema for the function so the agent handle its response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `path_agent_uuid` but received {path_agent_uuid!r}")
        if not path_function_uuid:
            raise ValueError(f"Expected a non-empty value for `path_function_uuid` but received {path_function_uuid!r}")
        return await self._put(
            f"/v2/gen-ai/agents/{path_agent_uuid}/functions/{path_function_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_agent_uuid}/functions/{path_function_uuid}",
            body=await async_maybe_transform(
                {
                    "body_agent_uuid": body_agent_uuid,
                    "description": description,
                    "faas_name": faas_name,
                    "faas_namespace": faas_namespace,
                    "function_name": function_name,
                    "body_function_uuid": body_function_uuid,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionUpdateResponse,
        )

    async def delete(
        self,
        function_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionDeleteResponse:
        """
        To delete a function route from an agent, send a DELETE request to
        `/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not function_uuid:
            raise ValueError(f"Expected a non-empty value for `function_uuid` but received {function_uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionDeleteResponse,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_raw_response_wrapper(
            functions.create,
        )
        self.update = to_raw_response_wrapper(
            functions.update,
        )
        self.delete = to_raw_response_wrapper(
            functions.delete,
        )


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_raw_response_wrapper(
            functions.create,
        )
        self.update = async_to_raw_response_wrapper(
            functions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            functions.delete,
        )


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_streamed_response_wrapper(
            functions.create,
        )
        self.update = to_streamed_response_wrapper(
            functions.update,
        )
        self.delete = to_streamed_response_wrapper(
            functions.delete,
        )


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_streamed_response_wrapper(
            functions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            functions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            functions.delete,
        )
