# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.organization import (
    usage_images_params,
    usage_embeddings_params,
    usage_completions_params,
    usage_moderations_params,
    usage_vector_stores_params,
    usage_audio_speeches_params,
    usage_audio_transcriptions_params,
    usage_code_interpreter_sessions_params,
)
from ...types.usage_response import UsageResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def audio_speeches(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get audio speeches usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/usage/audio_speeches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_audio_speeches_params.UsageAudioSpeechesParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    def audio_transcriptions(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get audio transcriptions usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/usage/audio_transcriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_audio_transcriptions_params.UsageAudioTranscriptionsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    def code_interpreter_sessions(
        self,
        *,
        start_time: int,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get code interpreter sessions usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/usage/code_interpreter_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "page": page,
                        "project_ids": project_ids,
                    },
                    usage_code_interpreter_sessions_params.UsageCodeInterpreterSessionsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    def completions(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        batch: bool | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model", "batch"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get completions usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          batch: If `true`, return batch jobs only. If `false`, return non-batch jobs only. By
              default, return both.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model`, `batch` or any combination of
              them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/usage/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "batch": batch,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_completions_params.UsageCompletionsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    def embeddings(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get embeddings usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/usage/embeddings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_embeddings_params.UsageEmbeddingsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    def images(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model", "size", "source"]]
        | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        sizes: List[Literal["256x256", "512x512", "1024x1024", "1792x1792", "1024x1792"]] | NotGiven = NOT_GIVEN,
        sources: List[Literal["image.generation", "image.edit", "image.variation"]] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get images usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model`, `size`, `source` or any
              combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          sizes: Return only usages for these image sizes. Possible values are `256x256`,
              `512x512`, `1024x1024`, `1792x1792`, `1024x1792` or any combination of them.

          sources: Return only usages for these sources. Possible values are `image.generation`,
              `image.edit`, `image.variation` or any combination of them.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/usage/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "sizes": sizes,
                        "sources": sources,
                        "user_ids": user_ids,
                    },
                    usage_images_params.UsageImagesParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    def moderations(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get moderations usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/usage/moderations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_moderations_params.UsageModerationsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    def vector_stores(
        self,
        *,
        start_time: int,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get vector stores usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/usage/vector_stores",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "page": page,
                        "project_ids": project_ids,
                    },
                    usage_vector_stores_params.UsageVectorStoresParams,
                ),
            ),
            cast_to=UsageResponse,
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    async def audio_speeches(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get audio speeches usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/usage/audio_speeches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_audio_speeches_params.UsageAudioSpeechesParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    async def audio_transcriptions(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get audio transcriptions usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/usage/audio_transcriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_audio_transcriptions_params.UsageAudioTranscriptionsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    async def code_interpreter_sessions(
        self,
        *,
        start_time: int,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get code interpreter sessions usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/usage/code_interpreter_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "page": page,
                        "project_ids": project_ids,
                    },
                    usage_code_interpreter_sessions_params.UsageCodeInterpreterSessionsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    async def completions(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        batch: bool | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model", "batch"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get completions usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          batch: If `true`, return batch jobs only. If `false`, return non-batch jobs only. By
              default, return both.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model`, `batch` or any combination of
              them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/usage/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "batch": batch,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_completions_params.UsageCompletionsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    async def embeddings(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get embeddings usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/usage/embeddings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_embeddings_params.UsageEmbeddingsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    async def images(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model", "size", "source"]]
        | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        sizes: List[Literal["256x256", "512x512", "1024x1024", "1792x1792", "1024x1792"]] | NotGiven = NOT_GIVEN,
        sources: List[Literal["image.generation", "image.edit", "image.variation"]] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get images usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model`, `size`, `source` or any
              combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          sizes: Return only usages for these image sizes. Possible values are `256x256`,
              `512x512`, `1024x1024`, `1792x1792`, `1024x1792` or any combination of them.

          sources: Return only usages for these sources. Possible values are `image.generation`,
              `image.edit`, `image.variation` or any combination of them.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/usage/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "sizes": sizes,
                        "sources": sources,
                        "user_ids": user_ids,
                    },
                    usage_images_params.UsageImagesParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    async def moderations(
        self,
        *,
        start_time: int,
        api_key_ids: List[str] | NotGiven = NOT_GIVEN,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "user_id", "api_key_id", "model"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get moderations usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          api_key_ids: Return only usage for these API keys.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          models: Return only usage for these models.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          user_ids: Return only usage for these users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/usage/moderations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "api_key_ids": api_key_ids,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "models": models,
                        "page": page,
                        "project_ids": project_ids,
                        "user_ids": user_ids,
                    },
                    usage_moderations_params.UsageModerationsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    async def vector_stores(
        self,
        *,
        start_time: int,
        bucket_width: Literal["1m", "1h", "1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageResponse:
        """
        Get vector stores usage details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          bucket_width: Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
              supported, default to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the usage data by the specified fields. Support fields include
              `project_id`.

          limit: Specifies the number of buckets to return.

              - `bucket_width=1d`: default: 7, max: 31
              - `bucket_width=1h`: default: 24, max: 168
              - `bucket_width=1m`: default: 60, max: 1440

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only usage for these projects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/usage/vector_stores",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "bucket_width": bucket_width,
                        "end_time": end_time,
                        "group_by": group_by,
                        "limit": limit,
                        "page": page,
                        "project_ids": project_ids,
                    },
                    usage_vector_stores_params.UsageVectorStoresParams,
                ),
            ),
            cast_to=UsageResponse,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.audio_speeches = to_raw_response_wrapper(
            usage.audio_speeches,
        )
        self.audio_transcriptions = to_raw_response_wrapper(
            usage.audio_transcriptions,
        )
        self.code_interpreter_sessions = to_raw_response_wrapper(
            usage.code_interpreter_sessions,
        )
        self.completions = to_raw_response_wrapper(
            usage.completions,
        )
        self.embeddings = to_raw_response_wrapper(
            usage.embeddings,
        )
        self.images = to_raw_response_wrapper(
            usage.images,
        )
        self.moderations = to_raw_response_wrapper(
            usage.moderations,
        )
        self.vector_stores = to_raw_response_wrapper(
            usage.vector_stores,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.audio_speeches = async_to_raw_response_wrapper(
            usage.audio_speeches,
        )
        self.audio_transcriptions = async_to_raw_response_wrapper(
            usage.audio_transcriptions,
        )
        self.code_interpreter_sessions = async_to_raw_response_wrapper(
            usage.code_interpreter_sessions,
        )
        self.completions = async_to_raw_response_wrapper(
            usage.completions,
        )
        self.embeddings = async_to_raw_response_wrapper(
            usage.embeddings,
        )
        self.images = async_to_raw_response_wrapper(
            usage.images,
        )
        self.moderations = async_to_raw_response_wrapper(
            usage.moderations,
        )
        self.vector_stores = async_to_raw_response_wrapper(
            usage.vector_stores,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.audio_speeches = to_streamed_response_wrapper(
            usage.audio_speeches,
        )
        self.audio_transcriptions = to_streamed_response_wrapper(
            usage.audio_transcriptions,
        )
        self.code_interpreter_sessions = to_streamed_response_wrapper(
            usage.code_interpreter_sessions,
        )
        self.completions = to_streamed_response_wrapper(
            usage.completions,
        )
        self.embeddings = to_streamed_response_wrapper(
            usage.embeddings,
        )
        self.images = to_streamed_response_wrapper(
            usage.images,
        )
        self.moderations = to_streamed_response_wrapper(
            usage.moderations,
        )
        self.vector_stores = to_streamed_response_wrapper(
            usage.vector_stores,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.audio_speeches = async_to_streamed_response_wrapper(
            usage.audio_speeches,
        )
        self.audio_transcriptions = async_to_streamed_response_wrapper(
            usage.audio_transcriptions,
        )
        self.code_interpreter_sessions = async_to_streamed_response_wrapper(
            usage.code_interpreter_sessions,
        )
        self.completions = async_to_streamed_response_wrapper(
            usage.completions,
        )
        self.embeddings = async_to_streamed_response_wrapper(
            usage.embeddings,
        )
        self.images = async_to_streamed_response_wrapper(
            usage.images,
        )
        self.moderations = async_to_streamed_response_wrapper(
            usage.moderations,
        )
        self.vector_stores = async_to_streamed_response_wrapper(
            usage.vector_stores,
        )
