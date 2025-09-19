# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.gpu_droplets.account import key_list_params, key_create_params, key_update_params
from ....types.gpu_droplets.account.key_list_response import KeyListResponse
from ....types.gpu_droplets.account.key_create_response import KeyCreateResponse
from ....types.gpu_droplets.account.key_update_response import KeyUpdateResponse
from ....types.gpu_droplets.account.key_retrieve_response import KeyRetrieveResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        public_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyCreateResponse:
        """
        To add a new SSH public key to your DigitalOcean account, send a POST request to
        `/v2/account/keys`. Set the `name` attribute to the name you wish to use and the
        `public_key` attribute to the full public key you are adding.

        Args:
          name: A human-readable display name for this key, used to easily identify the SSH keys
              when they are displayed.

          public_key: The entire public key string that was uploaded. Embedded into the root user's
              `authorized_keys` file if you include this key during Droplet creation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/account/keys" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/account/keys",
            body=maybe_transform(
                {
                    "name": name,
                    "public_key": public_key,
                },
                key_create_params.KeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyCreateResponse,
        )

    def retrieve(
        self,
        ssh_key_identifier: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyRetrieveResponse:
        """
        To get information about a key, send a GET request to `/v2/account/keys/$KEY_ID`
        or `/v2/account/keys/$KEY_FINGERPRINT`. The response will be a JSON object with
        the key `ssh_key` and value an ssh_key object which contains the standard
        ssh_key attributes.

        Args:
          ssh_key_identifier: A unique identification number for this key. Can be used to embed a specific SSH
              key into a Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/account/keys/{ssh_key_identifier}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/account/keys/{ssh_key_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyRetrieveResponse,
        )

    def update(
        self,
        ssh_key_identifier: Union[int, str],
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyUpdateResponse:
        """
        To update the name of an SSH key, send a PUT request to either
        `/v2/account/keys/$SSH_KEY_ID` or `/v2/account/keys/$SSH_KEY_FINGERPRINT`. Set
        the `name` attribute to the new name you want to use.

        Args:
          ssh_key_identifier: A unique identification number for this key. Can be used to embed a specific SSH
              key into a Droplet.

          name: A human-readable display name for this key, used to easily identify the SSH keys
              when they are displayed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/v2/account/keys/{ssh_key_identifier}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/account/keys/{ssh_key_identifier}",
            body=maybe_transform({"name": name}, key_update_params.KeyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyUpdateResponse,
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
    ) -> KeyListResponse:
        """
        To list all of the keys in your account, send a GET request to
        `/v2/account/keys`. The response will be a JSON object with a key set to
        `ssh_keys`. The value of this will be an array of ssh_key objects, each of which
        contains the standard ssh_key attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/account/keys" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/account/keys",
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
                    key_list_params.KeyListParams,
                ),
            ),
            cast_to=KeyListResponse,
        )

    def delete(
        self,
        ssh_key_identifier: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy a public SSH key that you have in your account, send a DELETE request
        to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`. A 204
        status will be returned, indicating that the action was successful and that the
        response body is empty.

        Args:
          ssh_key_identifier: A unique identification number for this key. Can be used to embed a specific SSH
              key into a Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/account/keys/{ssh_key_identifier}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/account/keys/{ssh_key_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        public_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyCreateResponse:
        """
        To add a new SSH public key to your DigitalOcean account, send a POST request to
        `/v2/account/keys`. Set the `name` attribute to the name you wish to use and the
        `public_key` attribute to the full public key you are adding.

        Args:
          name: A human-readable display name for this key, used to easily identify the SSH keys
              when they are displayed.

          public_key: The entire public key string that was uploaded. Embedded into the root user's
              `authorized_keys` file if you include this key during Droplet creation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/account/keys" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/account/keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "public_key": public_key,
                },
                key_create_params.KeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyCreateResponse,
        )

    async def retrieve(
        self,
        ssh_key_identifier: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyRetrieveResponse:
        """
        To get information about a key, send a GET request to `/v2/account/keys/$KEY_ID`
        or `/v2/account/keys/$KEY_FINGERPRINT`. The response will be a JSON object with
        the key `ssh_key` and value an ssh_key object which contains the standard
        ssh_key attributes.

        Args:
          ssh_key_identifier: A unique identification number for this key. Can be used to embed a specific SSH
              key into a Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/account/keys/{ssh_key_identifier}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/account/keys/{ssh_key_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyRetrieveResponse,
        )

    async def update(
        self,
        ssh_key_identifier: Union[int, str],
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyUpdateResponse:
        """
        To update the name of an SSH key, send a PUT request to either
        `/v2/account/keys/$SSH_KEY_ID` or `/v2/account/keys/$SSH_KEY_FINGERPRINT`. Set
        the `name` attribute to the new name you want to use.

        Args:
          ssh_key_identifier: A unique identification number for this key. Can be used to embed a specific SSH
              key into a Droplet.

          name: A human-readable display name for this key, used to easily identify the SSH keys
              when they are displayed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/v2/account/keys/{ssh_key_identifier}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/account/keys/{ssh_key_identifier}",
            body=await async_maybe_transform({"name": name}, key_update_params.KeyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyUpdateResponse,
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
    ) -> KeyListResponse:
        """
        To list all of the keys in your account, send a GET request to
        `/v2/account/keys`. The response will be a JSON object with a key set to
        `ssh_keys`. The value of this will be an array of ssh_key objects, each of which
        contains the standard ssh_key attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/account/keys" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/account/keys",
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
                    key_list_params.KeyListParams,
                ),
            ),
            cast_to=KeyListResponse,
        )

    async def delete(
        self,
        ssh_key_identifier: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy a public SSH key that you have in your account, send a DELETE request
        to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`. A 204
        status will be returned, indicating that the action was successful and that the
        response body is empty.

        Args:
          ssh_key_identifier: A unique identification number for this key. Can be used to embed a specific SSH
              key into a Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/account/keys/{ssh_key_identifier}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/account/keys/{ssh_key_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_raw_response_wrapper(
            keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            keys.update,
        )
        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.delete = to_raw_response_wrapper(
            keys.delete,
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_raw_response_wrapper(
            keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            keys.delete,
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_streamed_response_wrapper(
            keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            keys.update,
        )
        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            keys.delete,
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_streamed_response_wrapper(
            keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            keys.delete,
        )
