# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents.api_link_knowledge_base_output import APILinkKnowledgeBaseOutput
from ...types.agents.knowledge_base_detach_response import KnowledgeBaseDetachResponse

__all__ = ["KnowledgeBasesResource", "AsyncKnowledgeBasesResource"]


class KnowledgeBasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KnowledgeBasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return KnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeBasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return KnowledgeBasesResourceWithStreamingResponse(self)

    def attach(
        self,
        agent_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APILinkKnowledgeBaseOutput:
        """
        To attach knowledge bases to an agent, send a POST request to
        `/v2/gen-ai/agents/{agent_uuid}/knowledge_bases`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        return self._post(
            f"/v2/gen-ai/agents/{agent_uuid}/knowledge_bases"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/knowledge_bases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APILinkKnowledgeBaseOutput,
        )

    def attach_single(
        self,
        knowledge_base_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APILinkKnowledgeBaseOutput:
        """
        To attach a knowledge base to an agent, send a POST request to
        `/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `knowledge_base_uuid` but received {knowledge_base_uuid!r}"
            )
        return self._post(
            f"/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APILinkKnowledgeBaseOutput,
        )

    def detach(
        self,
        knowledge_base_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseDetachResponse:
        """
        To detach a knowledge base from an agent, send a DELETE request to
        `/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `knowledge_base_uuid` but received {knowledge_base_uuid!r}"
            )
        return self._delete(
            f"/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseDetachResponse,
        )


class AsyncKnowledgeBasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeBasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self)

    async def attach(
        self,
        agent_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APILinkKnowledgeBaseOutput:
        """
        To attach knowledge bases to an agent, send a POST request to
        `/v2/gen-ai/agents/{agent_uuid}/knowledge_bases`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        return await self._post(
            f"/v2/gen-ai/agents/{agent_uuid}/knowledge_bases"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/knowledge_bases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APILinkKnowledgeBaseOutput,
        )

    async def attach_single(
        self,
        knowledge_base_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APILinkKnowledgeBaseOutput:
        """
        To attach a knowledge base to an agent, send a POST request to
        `/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `knowledge_base_uuid` but received {knowledge_base_uuid!r}"
            )
        return await self._post(
            f"/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APILinkKnowledgeBaseOutput,
        )

    async def detach(
        self,
        knowledge_base_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseDetachResponse:
        """
        To detach a knowledge base from an agent, send a DELETE request to
        `/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `knowledge_base_uuid` but received {knowledge_base_uuid!r}"
            )
        return await self._delete(
            f"/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseDetachResponse,
        )


class KnowledgeBasesResourceWithRawResponse:
    def __init__(self, knowledge_bases: KnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.attach = to_raw_response_wrapper(
            knowledge_bases.attach,
        )
        self.attach_single = to_raw_response_wrapper(
            knowledge_bases.attach_single,
        )
        self.detach = to_raw_response_wrapper(
            knowledge_bases.detach,
        )


class AsyncKnowledgeBasesResourceWithRawResponse:
    def __init__(self, knowledge_bases: AsyncKnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.attach = async_to_raw_response_wrapper(
            knowledge_bases.attach,
        )
        self.attach_single = async_to_raw_response_wrapper(
            knowledge_bases.attach_single,
        )
        self.detach = async_to_raw_response_wrapper(
            knowledge_bases.detach,
        )


class KnowledgeBasesResourceWithStreamingResponse:
    def __init__(self, knowledge_bases: KnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.attach = to_streamed_response_wrapper(
            knowledge_bases.attach,
        )
        self.attach_single = to_streamed_response_wrapper(
            knowledge_bases.attach_single,
        )
        self.detach = to_streamed_response_wrapper(
            knowledge_bases.detach,
        )


class AsyncKnowledgeBasesResourceWithStreamingResponse:
    def __init__(self, knowledge_bases: AsyncKnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.attach = async_to_streamed_response_wrapper(
            knowledge_bases.attach,
        )
        self.attach_single = async_to_streamed_response_wrapper(
            knowledge_bases.attach_single,
        )
        self.detach = async_to_streamed_response_wrapper(
            knowledge_bases.detach,
        )
