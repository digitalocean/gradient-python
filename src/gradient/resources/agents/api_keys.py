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
from ...types.agents import api_key_list_params, api_key_create_params, api_key_update_params
from ...types.agents.api_key_list_response import APIKeyListResponse
from ...types.agents.api_key_create_response import APIKeyCreateResponse
from ...types.agents.api_key_delete_response import APIKeyDeleteResponse
from ...types.agents.api_key_update_response import APIKeyUpdateResponse
from ...types.agents.api_key_regenerate_response import APIKeyRegenerateResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def create(
        self,
        path_agent_uuid: str,
        *,
        body_agent_uuid: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyCreateResponse:
        """
        To create an agent API key, send a POST request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys`.

        Args:
          body_agent_uuid: Agent id

          name: A human friendly name to identify the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `path_agent_uuid` but received {path_agent_uuid!r}")
        return self._post(
            f"/v2/gen-ai/agents/{path_agent_uuid}/api_keys"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_agent_uuid}/api_keys",
            body=maybe_transform(
                {
                    "body_agent_uuid": body_agent_uuid,
                    "name": name,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyCreateResponse,
        )

    def update(
        self,
        path_api_key_uuid: str,
        *,
        path_agent_uuid: str,
        body_agent_uuid: str | Omit = omit,
        body_api_key_uuid: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyUpdateResponse:
        """
        To update an agent API key, send a PUT request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}`.

        Args:
          body_agent_uuid: Agent id

          body_api_key_uuid: API key ID

          name: Name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `path_agent_uuid` but received {path_agent_uuid!r}")
        if not path_api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `path_api_key_uuid` but received {path_api_key_uuid!r}")
        return self._put(
            f"/v2/gen-ai/agents/{path_agent_uuid}/api_keys/{path_api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_agent_uuid}/api_keys/{path_api_key_uuid}",
            body=maybe_transform(
                {
                    "body_agent_uuid": body_agent_uuid,
                    "body_api_key_uuid": body_api_key_uuid,
                    "name": name,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyUpdateResponse,
        )

    def list(
        self,
        agent_uuid: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListResponse:
        """
        To list all agent API keys, send a GET request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        return self._get(
            f"/v2/gen-ai/agents/{agent_uuid}/api_keys"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/api_keys",
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
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            cast_to=APIKeyListResponse,
        )

    def delete(
        self,
        api_key_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyDeleteResponse:
        """
        To delete an API key for an agent, send a DELETE request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return self._delete(
            f"/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyDeleteResponse,
        )

    def regenerate(
        self,
        api_key_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyRegenerateResponse:
        """
        To regenerate an agent API key, send a PUT request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return self._put(
            f"/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRegenerateResponse,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        path_agent_uuid: str,
        *,
        body_agent_uuid: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyCreateResponse:
        """
        To create an agent API key, send a POST request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys`.

        Args:
          body_agent_uuid: Agent id

          name: A human friendly name to identify the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `path_agent_uuid` but received {path_agent_uuid!r}")
        return await self._post(
            f"/v2/gen-ai/agents/{path_agent_uuid}/api_keys"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_agent_uuid}/api_keys",
            body=await async_maybe_transform(
                {
                    "body_agent_uuid": body_agent_uuid,
                    "name": name,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyCreateResponse,
        )

    async def update(
        self,
        path_api_key_uuid: str,
        *,
        path_agent_uuid: str,
        body_agent_uuid: str | Omit = omit,
        body_api_key_uuid: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyUpdateResponse:
        """
        To update an agent API key, send a PUT request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}`.

        Args:
          body_agent_uuid: Agent id

          body_api_key_uuid: API key ID

          name: Name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `path_agent_uuid` but received {path_agent_uuid!r}")
        if not path_api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `path_api_key_uuid` but received {path_api_key_uuid!r}")
        return await self._put(
            f"/v2/gen-ai/agents/{path_agent_uuid}/api_keys/{path_api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_agent_uuid}/api_keys/{path_api_key_uuid}",
            body=await async_maybe_transform(
                {
                    "body_agent_uuid": body_agent_uuid,
                    "body_api_key_uuid": body_api_key_uuid,
                    "name": name,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyUpdateResponse,
        )

    async def list(
        self,
        agent_uuid: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListResponse:
        """
        To list all agent API keys, send a GET request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/agents/{agent_uuid}/api_keys"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/api_keys",
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
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            cast_to=APIKeyListResponse,
        )

    async def delete(
        self,
        api_key_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyDeleteResponse:
        """
        To delete an API key for an agent, send a DELETE request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyDeleteResponse,
        )

    async def regenerate(
        self,
        api_key_uuid: str,
        *,
        agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyRegenerateResponse:
        """
        To regenerate an agent API key, send a PUT request to
        `/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return await self._put(
            f"/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRegenerateResponse,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_raw_response_wrapper(
            api_keys.create,
        )
        self.update = to_raw_response_wrapper(
            api_keys.update,
        )
        self.list = to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            api_keys.delete,
        )
        self.regenerate = to_raw_response_wrapper(
            api_keys.regenerate,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )
        self.update = async_to_raw_response_wrapper(
            api_keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_keys.delete,
        )
        self.regenerate = async_to_raw_response_wrapper(
            api_keys.regenerate,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )
        self.update = to_streamed_response_wrapper(
            api_keys.update,
        )
        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.regenerate = to_streamed_response_wrapper(
            api_keys.regenerate,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
        self.update = async_to_streamed_response_wrapper(
            api_keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.regenerate = async_to_streamed_response_wrapper(
            api_keys.regenerate,
        )
