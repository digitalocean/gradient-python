# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.organization.projects import rate_limit_list_params, rate_limit_update_params
from ....types.organization.projects.project_rate_limit import ProjectRateLimit
from ....types.organization.projects.rate_limit_list_response import RateLimitListResponse

__all__ = ["RateLimitsResource", "AsyncRateLimitsResource"]


class RateLimitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RateLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return RateLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RateLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return RateLimitsResourceWithStreamingResponse(self)

    def update(
        self,
        rate_limit_id: str,
        *,
        project_id: str,
        batch_1_day_max_input_tokens: int | NotGiven = NOT_GIVEN,
        max_audio_megabytes_per_1_minute: int | NotGiven = NOT_GIVEN,
        max_images_per_1_minute: int | NotGiven = NOT_GIVEN,
        max_requests_per_1_day: int | NotGiven = NOT_GIVEN,
        max_requests_per_1_minute: int | NotGiven = NOT_GIVEN,
        max_tokens_per_1_minute: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRateLimit:
        """
        Updates a project rate limit.

        Args:
          batch_1_day_max_input_tokens: The maximum batch input tokens per day. Only relevant for certain models.

          max_audio_megabytes_per_1_minute: The maximum audio megabytes per minute. Only relevant for certain models.

          max_images_per_1_minute: The maximum images per minute. Only relevant for certain models.

          max_requests_per_1_day: The maximum requests per day. Only relevant for certain models.

          max_requests_per_1_minute: The maximum requests per minute.

          max_tokens_per_1_minute: The maximum tokens per minute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not rate_limit_id:
            raise ValueError(f"Expected a non-empty value for `rate_limit_id` but received {rate_limit_id!r}")
        return self._post(
            f"/organization/projects/{project_id}/rate_limits/{rate_limit_id}",
            body=maybe_transform(
                {
                    "batch_1_day_max_input_tokens": batch_1_day_max_input_tokens,
                    "max_audio_megabytes_per_1_minute": max_audio_megabytes_per_1_minute,
                    "max_images_per_1_minute": max_images_per_1_minute,
                    "max_requests_per_1_day": max_requests_per_1_day,
                    "max_requests_per_1_minute": max_requests_per_1_minute,
                    "max_tokens_per_1_minute": max_tokens_per_1_minute,
                },
                rate_limit_update_params.RateLimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRateLimit,
        )

    def list(
        self,
        project_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateLimitListResponse:
        """
        Returns the rate limits per model for a project.

        Args:
          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              beginning with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          limit: A limit on the number of objects to be returned. The default is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/organization/projects/{project_id}/rate_limits",
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
                    },
                    rate_limit_list_params.RateLimitListParams,
                ),
            ),
            cast_to=RateLimitListResponse,
        )


class AsyncRateLimitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRateLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRateLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRateLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncRateLimitsResourceWithStreamingResponse(self)

    async def update(
        self,
        rate_limit_id: str,
        *,
        project_id: str,
        batch_1_day_max_input_tokens: int | NotGiven = NOT_GIVEN,
        max_audio_megabytes_per_1_minute: int | NotGiven = NOT_GIVEN,
        max_images_per_1_minute: int | NotGiven = NOT_GIVEN,
        max_requests_per_1_day: int | NotGiven = NOT_GIVEN,
        max_requests_per_1_minute: int | NotGiven = NOT_GIVEN,
        max_tokens_per_1_minute: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRateLimit:
        """
        Updates a project rate limit.

        Args:
          batch_1_day_max_input_tokens: The maximum batch input tokens per day. Only relevant for certain models.

          max_audio_megabytes_per_1_minute: The maximum audio megabytes per minute. Only relevant for certain models.

          max_images_per_1_minute: The maximum images per minute. Only relevant for certain models.

          max_requests_per_1_day: The maximum requests per day. Only relevant for certain models.

          max_requests_per_1_minute: The maximum requests per minute.

          max_tokens_per_1_minute: The maximum tokens per minute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not rate_limit_id:
            raise ValueError(f"Expected a non-empty value for `rate_limit_id` but received {rate_limit_id!r}")
        return await self._post(
            f"/organization/projects/{project_id}/rate_limits/{rate_limit_id}",
            body=await async_maybe_transform(
                {
                    "batch_1_day_max_input_tokens": batch_1_day_max_input_tokens,
                    "max_audio_megabytes_per_1_minute": max_audio_megabytes_per_1_minute,
                    "max_images_per_1_minute": max_images_per_1_minute,
                    "max_requests_per_1_day": max_requests_per_1_day,
                    "max_requests_per_1_minute": max_requests_per_1_minute,
                    "max_tokens_per_1_minute": max_tokens_per_1_minute,
                },
                rate_limit_update_params.RateLimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRateLimit,
        )

    async def list(
        self,
        project_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateLimitListResponse:
        """
        Returns the rate limits per model for a project.

        Args:
          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              beginning with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          limit: A limit on the number of objects to be returned. The default is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/organization/projects/{project_id}/rate_limits",
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
                    },
                    rate_limit_list_params.RateLimitListParams,
                ),
            ),
            cast_to=RateLimitListResponse,
        )


class RateLimitsResourceWithRawResponse:
    def __init__(self, rate_limits: RateLimitsResource) -> None:
        self._rate_limits = rate_limits

        self.update = to_raw_response_wrapper(
            rate_limits.update,
        )
        self.list = to_raw_response_wrapper(
            rate_limits.list,
        )


class AsyncRateLimitsResourceWithRawResponse:
    def __init__(self, rate_limits: AsyncRateLimitsResource) -> None:
        self._rate_limits = rate_limits

        self.update = async_to_raw_response_wrapper(
            rate_limits.update,
        )
        self.list = async_to_raw_response_wrapper(
            rate_limits.list,
        )


class RateLimitsResourceWithStreamingResponse:
    def __init__(self, rate_limits: RateLimitsResource) -> None:
        self._rate_limits = rate_limits

        self.update = to_streamed_response_wrapper(
            rate_limits.update,
        )
        self.list = to_streamed_response_wrapper(
            rate_limits.list,
        )


class AsyncRateLimitsResourceWithStreamingResponse:
    def __init__(self, rate_limits: AsyncRateLimitsResource) -> None:
        self._rate_limits = rate_limits

        self.update = async_to_streamed_response_wrapper(
            rate_limits.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rate_limits.list,
        )
