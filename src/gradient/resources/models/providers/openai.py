# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.models.providers import (
    openai_list_params,
    openai_create_params,
    openai_update_params,
    openai_retrieve_agents_params,
)
from ....types.models.providers.openai_list_response import OpenAIListResponse
from ....types.models.providers.openai_create_response import OpenAICreateResponse
from ....types.models.providers.openai_delete_response import OpenAIDeleteResponse
from ....types.models.providers.openai_update_response import OpenAIUpdateResponse
from ....types.models.providers.openai_retrieve_response import OpenAIRetrieveResponse
from ....types.models.providers.openai_retrieve_agents_response import OpenAIRetrieveAgentsResponse

__all__ = ["OpenAIResource", "AsyncOpenAIResource"]


class OpenAIResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpenAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return OpenAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return OpenAIResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        api_key: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAICreateResponse:
        """
        To create an OpenAI API key, send a POST request to `/v2/gen-ai/openai/keys`.

        Args:
          api_key: OpenAI API key

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/openai/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/openai/keys",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "name": name,
                },
                openai_create_params.OpenAICreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAICreateResponse,
        )

    def retrieve(
        self,
        api_key_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIRetrieveResponse:
        """
        To retrieve details of an OpenAI API key, send a GET request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return self._get(
            f"/v2/gen-ai/openai/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIRetrieveResponse,
        )

    def update(
        self,
        path_api_key_uuid: str,
        *,
        api_key: str | Omit = omit,
        body_api_key_uuid: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIUpdateResponse:
        """
        To update an OpenAI API key, send a PUT request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          api_key: OpenAI API key

          body_api_key_uuid: API key ID

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `path_api_key_uuid` but received {path_api_key_uuid!r}")
        return self._put(
            f"/v2/gen-ai/openai/keys/{path_api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{path_api_key_uuid}",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "body_api_key_uuid": body_api_key_uuid,
                    "name": name,
                },
                openai_update_params.OpenAIUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIListResponse:
        """
        To list all OpenAI API keys, send a GET request to `/v2/gen-ai/openai/keys`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gen-ai/openai/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/openai/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    openai_list_params.OpenAIListParams,
                ),
            ),
            cast_to=OpenAIListResponse,
        )

    def delete(
        self,
        api_key_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIDeleteResponse:
        """
        To delete an OpenAI API key, send a DELETE request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return self._delete(
            f"/v2/gen-ai/openai/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIDeleteResponse,
        )

    def retrieve_agents(
        self,
        uuid: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIRetrieveAgentsResponse:
        """
        List Agents by OpenAI Key.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/v2/gen-ai/openai/keys/{uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{uuid}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    openai_retrieve_agents_params.OpenAIRetrieveAgentsParams,
                ),
            ),
            cast_to=OpenAIRetrieveAgentsResponse,
        )


class AsyncOpenAIResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpenAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncOpenAIResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        api_key: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAICreateResponse:
        """
        To create an OpenAI API key, send a POST request to `/v2/gen-ai/openai/keys`.

        Args:
          api_key: OpenAI API key

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/openai/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/openai/keys",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "name": name,
                },
                openai_create_params.OpenAICreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAICreateResponse,
        )

    async def retrieve(
        self,
        api_key_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIRetrieveResponse:
        """
        To retrieve details of an OpenAI API key, send a GET request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/openai/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIRetrieveResponse,
        )

    async def update(
        self,
        path_api_key_uuid: str,
        *,
        api_key: str | Omit = omit,
        body_api_key_uuid: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIUpdateResponse:
        """
        To update an OpenAI API key, send a PUT request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          api_key: OpenAI API key

          body_api_key_uuid: API key ID

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `path_api_key_uuid` but received {path_api_key_uuid!r}")
        return await self._put(
            f"/v2/gen-ai/openai/keys/{path_api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{path_api_key_uuid}",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "body_api_key_uuid": body_api_key_uuid,
                    "name": name,
                },
                openai_update_params.OpenAIUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIListResponse:
        """
        To list all OpenAI API keys, send a GET request to `/v2/gen-ai/openai/keys`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gen-ai/openai/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/openai/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    openai_list_params.OpenAIListParams,
                ),
            ),
            cast_to=OpenAIListResponse,
        )

    async def delete(
        self,
        api_key_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIDeleteResponse:
        """
        To delete an OpenAI API key, send a DELETE request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/openai/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIDeleteResponse,
        )

    async def retrieve_agents(
        self,
        uuid: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIRetrieveAgentsResponse:
        """
        List Agents by OpenAI Key.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/v2/gen-ai/openai/keys/{uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{uuid}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    openai_retrieve_agents_params.OpenAIRetrieveAgentsParams,
                ),
            ),
            cast_to=OpenAIRetrieveAgentsResponse,
        )


class OpenAIResourceWithRawResponse:
    def __init__(self, openai: OpenAIResource) -> None:
        self._openai = openai

        self.create = to_raw_response_wrapper(
            openai.create,
        )
        self.retrieve = to_raw_response_wrapper(
            openai.retrieve,
        )
        self.update = to_raw_response_wrapper(
            openai.update,
        )
        self.list = to_raw_response_wrapper(
            openai.list,
        )
        self.delete = to_raw_response_wrapper(
            openai.delete,
        )
        self.retrieve_agents = to_raw_response_wrapper(
            openai.retrieve_agents,
        )


class AsyncOpenAIResourceWithRawResponse:
    def __init__(self, openai: AsyncOpenAIResource) -> None:
        self._openai = openai

        self.create = async_to_raw_response_wrapper(
            openai.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            openai.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            openai.update,
        )
        self.list = async_to_raw_response_wrapper(
            openai.list,
        )
        self.delete = async_to_raw_response_wrapper(
            openai.delete,
        )
        self.retrieve_agents = async_to_raw_response_wrapper(
            openai.retrieve_agents,
        )


class OpenAIResourceWithStreamingResponse:
    def __init__(self, openai: OpenAIResource) -> None:
        self._openai = openai

        self.create = to_streamed_response_wrapper(
            openai.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            openai.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            openai.update,
        )
        self.list = to_streamed_response_wrapper(
            openai.list,
        )
        self.delete = to_streamed_response_wrapper(
            openai.delete,
        )
        self.retrieve_agents = to_streamed_response_wrapper(
            openai.retrieve_agents,
        )


class AsyncOpenAIResourceWithStreamingResponse:
    def __init__(self, openai: AsyncOpenAIResource) -> None:
        self._openai = openai

        self.create = async_to_streamed_response_wrapper(
            openai.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            openai.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            openai.update,
        )
        self.list = async_to_streamed_response_wrapper(
            openai.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            openai.delete,
        )
        self.retrieve_agents = async_to_streamed_response_wrapper(
            openai.retrieve_agents,
        )
