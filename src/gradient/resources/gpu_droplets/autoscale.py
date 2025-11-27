# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.gpu_droplets import (
    autoscale_list_params,
    autoscale_create_params,
    autoscale_update_params,
    autoscale_list_history_params,
    autoscale_list_members_params,
)
from ...types.gpu_droplets.autoscale_list_response import AutoscaleListResponse
from ...types.gpu_droplets.autoscale_create_response import AutoscaleCreateResponse
from ...types.gpu_droplets.autoscale_update_response import AutoscaleUpdateResponse
from ...types.gpu_droplets.autoscale_retrieve_response import AutoscaleRetrieveResponse
from ...types.gpu_droplets.autoscale_list_history_response import AutoscaleListHistoryResponse
from ...types.gpu_droplets.autoscale_list_members_response import AutoscaleListMembersResponse
from ...types.gpu_droplets.autoscale_pool_droplet_template_param import AutoscalePoolDropletTemplateParam

__all__ = ["AutoscaleResource", "AsyncAutoscaleResource"]


class AutoscaleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoscaleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AutoscaleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoscaleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AutoscaleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: autoscale_create_params.Config,
        droplet_template: AutoscalePoolDropletTemplateParam,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleCreateResponse:
        """
        To create a new autoscale pool, send a POST request to `/v2/droplets/autoscale`
        setting the required attributes.

        The response body will contain a JSON object with a key called `autoscale_pool`
        containing the standard attributes for the new autoscale pool.

        Args:
          config: The scaling configuration for an autoscale pool, which is how the pool scales up
              and down (either by resource utilization or static configuration).

          name: The human-readable name of the autoscale pool. This field cannot be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/droplets/autoscale"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/autoscale",
            body=maybe_transform(
                {
                    "config": config,
                    "droplet_template": droplet_template,
                    "name": name,
                },
                autoscale_create_params.AutoscaleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoscaleCreateResponse,
        )

    def retrieve(
        self,
        autoscale_pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleRetrieveResponse:
        """
        To show information about an individual autoscale pool, send a GET request to
        `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        return self._get(
            f"/v2/droplets/autoscale/{autoscale_pool_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoscaleRetrieveResponse,
        )

    def update(
        self,
        autoscale_pool_id: str,
        *,
        config: autoscale_update_params.Config,
        droplet_template: AutoscalePoolDropletTemplateParam,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleUpdateResponse:
        """
        To update the configuration of an existing autoscale pool, send a PUT request to
        `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID`. The request must contain a full
        representation of the autoscale pool including existing attributes.

        Args:
          config: The scaling configuration for an autoscale pool, which is how the pool scales up
              and down (either by resource utilization or static configuration).

          name: The human-readable name of the autoscale pool. This field cannot be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        return self._put(
            f"/v2/droplets/autoscale/{autoscale_pool_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}",
            body=maybe_transform(
                {
                    "config": config,
                    "droplet_template": droplet_template,
                    "name": name,
                },
                autoscale_update_params.AutoscaleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoscaleUpdateResponse,
        )

    def list(
        self,
        *,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleListResponse:
        """
        To list all autoscale pools in your team, send a GET request to
        `/v2/droplets/autoscale`. The response body will be a JSON object with a key of
        `autoscale_pools` containing an array of autoscale pool objects. These each
        contain the standard autoscale pool attributes.

        Args:
          name: The name of the autoscale pool

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/droplets/autoscale"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/autoscale",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    autoscale_list_params.AutoscaleListParams,
                ),
            ),
            cast_to=AutoscaleListResponse,
        )

    def delete(
        self,
        autoscale_pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy an autoscale pool, send a DELETE request to the
        `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID` endpoint.

        A successful response will include a 202 response code and no content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/droplets/autoscale/{autoscale_pool_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_dangerous(
        self,
        autoscale_pool_id: str,
        *,
        x_dangerous: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy an autoscale pool and its associated resources (Droplets), send a
        DELETE request to the `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID/dangerous`
        endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"X-Dangerous": ("true" if x_dangerous else "false")})
        return self._delete(
            f"/v2/droplets/autoscale/{autoscale_pool_id}/dangerous"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}/dangerous",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_history(
        self,
        autoscale_pool_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleListHistoryResponse:
        """
        To list all of the scaling history events of an autoscale pool, send a GET
        request to `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID/history`.

        The response body will be a JSON object with a key of `history`. This will be
        set to an array containing objects each representing a history event.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        return self._get(
            f"/v2/droplets/autoscale/{autoscale_pool_id}/history"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}/history",
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
                    autoscale_list_history_params.AutoscaleListHistoryParams,
                ),
            ),
            cast_to=AutoscaleListHistoryResponse,
        )

    def list_members(
        self,
        autoscale_pool_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleListMembersResponse:
        """
        To list the Droplets in an autoscale pool, send a GET request to
        `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID/members`.

        The response body will be a JSON object with a key of `droplets`. This will be
        set to an array containing information about each of the Droplets in the
        autoscale pool.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        return self._get(
            f"/v2/droplets/autoscale/{autoscale_pool_id}/members"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}/members",
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
                    autoscale_list_members_params.AutoscaleListMembersParams,
                ),
            ),
            cast_to=AutoscaleListMembersResponse,
        )


class AsyncAutoscaleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoscaleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoscaleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoscaleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncAutoscaleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: autoscale_create_params.Config,
        droplet_template: AutoscalePoolDropletTemplateParam,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleCreateResponse:
        """
        To create a new autoscale pool, send a POST request to `/v2/droplets/autoscale`
        setting the required attributes.

        The response body will contain a JSON object with a key called `autoscale_pool`
        containing the standard attributes for the new autoscale pool.

        Args:
          config: The scaling configuration for an autoscale pool, which is how the pool scales up
              and down (either by resource utilization or static configuration).

          name: The human-readable name of the autoscale pool. This field cannot be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/droplets/autoscale"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/autoscale",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "droplet_template": droplet_template,
                    "name": name,
                },
                autoscale_create_params.AutoscaleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoscaleCreateResponse,
        )

    async def retrieve(
        self,
        autoscale_pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleRetrieveResponse:
        """
        To show information about an individual autoscale pool, send a GET request to
        `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        return await self._get(
            f"/v2/droplets/autoscale/{autoscale_pool_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoscaleRetrieveResponse,
        )

    async def update(
        self,
        autoscale_pool_id: str,
        *,
        config: autoscale_update_params.Config,
        droplet_template: AutoscalePoolDropletTemplateParam,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleUpdateResponse:
        """
        To update the configuration of an existing autoscale pool, send a PUT request to
        `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID`. The request must contain a full
        representation of the autoscale pool including existing attributes.

        Args:
          config: The scaling configuration for an autoscale pool, which is how the pool scales up
              and down (either by resource utilization or static configuration).

          name: The human-readable name of the autoscale pool. This field cannot be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        return await self._put(
            f"/v2/droplets/autoscale/{autoscale_pool_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "droplet_template": droplet_template,
                    "name": name,
                },
                autoscale_update_params.AutoscaleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoscaleUpdateResponse,
        )

    async def list(
        self,
        *,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleListResponse:
        """
        To list all autoscale pools in your team, send a GET request to
        `/v2/droplets/autoscale`. The response body will be a JSON object with a key of
        `autoscale_pools` containing an array of autoscale pool objects. These each
        contain the standard autoscale pool attributes.

        Args:
          name: The name of the autoscale pool

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/droplets/autoscale"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/autoscale",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    autoscale_list_params.AutoscaleListParams,
                ),
            ),
            cast_to=AutoscaleListResponse,
        )

    async def delete(
        self,
        autoscale_pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy an autoscale pool, send a DELETE request to the
        `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID` endpoint.

        A successful response will include a 202 response code and no content.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/droplets/autoscale/{autoscale_pool_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_dangerous(
        self,
        autoscale_pool_id: str,
        *,
        x_dangerous: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To destroy an autoscale pool and its associated resources (Droplets), send a
        DELETE request to the `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID/dangerous`
        endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"X-Dangerous": ("true" if x_dangerous else "false")})
        return await self._delete(
            f"/v2/droplets/autoscale/{autoscale_pool_id}/dangerous"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}/dangerous",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_history(
        self,
        autoscale_pool_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleListHistoryResponse:
        """
        To list all of the scaling history events of an autoscale pool, send a GET
        request to `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID/history`.

        The response body will be a JSON object with a key of `history`. This will be
        set to an array containing objects each representing a history event.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        return await self._get(
            f"/v2/droplets/autoscale/{autoscale_pool_id}/history"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}/history",
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
                    autoscale_list_history_params.AutoscaleListHistoryParams,
                ),
            ),
            cast_to=AutoscaleListHistoryResponse,
        )

    async def list_members(
        self,
        autoscale_pool_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoscaleListMembersResponse:
        """
        To list the Droplets in an autoscale pool, send a GET request to
        `/v2/droplets/autoscale/$AUTOSCALE_POOL_ID/members`.

        The response body will be a JSON object with a key of `droplets`. This will be
        set to an array containing information about each of the Droplets in the
        autoscale pool.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not autoscale_pool_id:
            raise ValueError(f"Expected a non-empty value for `autoscale_pool_id` but received {autoscale_pool_id!r}")
        return await self._get(
            f"/v2/droplets/autoscale/{autoscale_pool_id}/members"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/autoscale/{autoscale_pool_id}/members",
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
                    autoscale_list_members_params.AutoscaleListMembersParams,
                ),
            ),
            cast_to=AutoscaleListMembersResponse,
        )


class AutoscaleResourceWithRawResponse:
    def __init__(self, autoscale: AutoscaleResource) -> None:
        self._autoscale = autoscale

        self.create = to_raw_response_wrapper(
            autoscale.create,
        )
        self.retrieve = to_raw_response_wrapper(
            autoscale.retrieve,
        )
        self.update = to_raw_response_wrapper(
            autoscale.update,
        )
        self.list = to_raw_response_wrapper(
            autoscale.list,
        )
        self.delete = to_raw_response_wrapper(
            autoscale.delete,
        )
        self.delete_dangerous = to_raw_response_wrapper(
            autoscale.delete_dangerous,
        )
        self.list_history = to_raw_response_wrapper(
            autoscale.list_history,
        )
        self.list_members = to_raw_response_wrapper(
            autoscale.list_members,
        )


class AsyncAutoscaleResourceWithRawResponse:
    def __init__(self, autoscale: AsyncAutoscaleResource) -> None:
        self._autoscale = autoscale

        self.create = async_to_raw_response_wrapper(
            autoscale.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            autoscale.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            autoscale.update,
        )
        self.list = async_to_raw_response_wrapper(
            autoscale.list,
        )
        self.delete = async_to_raw_response_wrapper(
            autoscale.delete,
        )
        self.delete_dangerous = async_to_raw_response_wrapper(
            autoscale.delete_dangerous,
        )
        self.list_history = async_to_raw_response_wrapper(
            autoscale.list_history,
        )
        self.list_members = async_to_raw_response_wrapper(
            autoscale.list_members,
        )


class AutoscaleResourceWithStreamingResponse:
    def __init__(self, autoscale: AutoscaleResource) -> None:
        self._autoscale = autoscale

        self.create = to_streamed_response_wrapper(
            autoscale.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            autoscale.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            autoscale.update,
        )
        self.list = to_streamed_response_wrapper(
            autoscale.list,
        )
        self.delete = to_streamed_response_wrapper(
            autoscale.delete,
        )
        self.delete_dangerous = to_streamed_response_wrapper(
            autoscale.delete_dangerous,
        )
        self.list_history = to_streamed_response_wrapper(
            autoscale.list_history,
        )
        self.list_members = to_streamed_response_wrapper(
            autoscale.list_members,
        )


class AsyncAutoscaleResourceWithStreamingResponse:
    def __init__(self, autoscale: AsyncAutoscaleResource) -> None:
        self._autoscale = autoscale

        self.create = async_to_streamed_response_wrapper(
            autoscale.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            autoscale.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            autoscale.update,
        )
        self.list = async_to_streamed_response_wrapper(
            autoscale.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            autoscale.delete,
        )
        self.delete_dangerous = async_to_streamed_response_wrapper(
            autoscale.delete_dangerous,
        )
        self.list_history = async_to_streamed_response_wrapper(
            autoscale.list_history,
        )
        self.list_members = async_to_streamed_response_wrapper(
            autoscale.list_members,
        )
