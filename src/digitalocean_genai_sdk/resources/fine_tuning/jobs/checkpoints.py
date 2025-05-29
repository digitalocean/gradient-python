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
from ....types.fine_tuning.jobs import checkpoint_retrieve_params
from ....types.fine_tuning.jobs.checkpoint_retrieve_response import CheckpointRetrieveResponse

__all__ = ["CheckpointsResource", "AsyncCheckpointsResource"]


class CheckpointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CheckpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return CheckpointsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        fine_tuning_job_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckpointRetrieveResponse:
        """
        List checkpoints for a fine-tuning job.

        Args:
          after: Identifier for the last checkpoint ID from the previous pagination request.

          limit: Number of checkpoints to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tuning_job_id:
            raise ValueError(f"Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}")
        return self._get(
            f"/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    checkpoint_retrieve_params.CheckpointRetrieveParams,
                ),
            ),
            cast_to=CheckpointRetrieveResponse,
        )


class AsyncCheckpointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return AsyncCheckpointsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        fine_tuning_job_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckpointRetrieveResponse:
        """
        List checkpoints for a fine-tuning job.

        Args:
          after: Identifier for the last checkpoint ID from the previous pagination request.

          limit: Number of checkpoints to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tuning_job_id:
            raise ValueError(f"Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}")
        return await self._get(
            f"/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    checkpoint_retrieve_params.CheckpointRetrieveParams,
                ),
            ),
            cast_to=CheckpointRetrieveResponse,
        )


class CheckpointsResourceWithRawResponse:
    def __init__(self, checkpoints: CheckpointsResource) -> None:
        self._checkpoints = checkpoints

        self.retrieve = to_raw_response_wrapper(
            checkpoints.retrieve,
        )


class AsyncCheckpointsResourceWithRawResponse:
    def __init__(self, checkpoints: AsyncCheckpointsResource) -> None:
        self._checkpoints = checkpoints

        self.retrieve = async_to_raw_response_wrapper(
            checkpoints.retrieve,
        )


class CheckpointsResourceWithStreamingResponse:
    def __init__(self, checkpoints: CheckpointsResource) -> None:
        self._checkpoints = checkpoints

        self.retrieve = to_streamed_response_wrapper(
            checkpoints.retrieve,
        )


class AsyncCheckpointsResourceWithStreamingResponse:
    def __init__(self, checkpoints: AsyncCheckpointsResource) -> None:
        self._checkpoints = checkpoints

        self.retrieve = async_to_streamed_response_wrapper(
            checkpoints.retrieve,
        )
