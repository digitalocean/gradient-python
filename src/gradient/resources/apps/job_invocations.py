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
from ...types.apps import job_invocation_cancel_params
from ..._base_client import make_request_options
from ...types.apps.job_invocation_cancel_response import JobInvocationCancelResponse

__all__ = ["JobInvocationsResource", "AsyncJobInvocationsResource"]


class JobInvocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobInvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return JobInvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobInvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return JobInvocationsResourceWithStreamingResponse(self)

    def cancel(
        self,
        job_invocation_id: str,
        *,
        app_id: str,
        job_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobInvocationCancelResponse:
        """
        Cancel a specific job invocation for an app.

        Args:
          job_name: The job name to list job invocations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not job_invocation_id:
            raise ValueError(f"Expected a non-empty value for `job_invocation_id` but received {job_invocation_id!r}")
        return self._post(
            f"/v2/apps/{app_id}/job-invocations/{job_invocation_id}/cancel"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/apps/{app_id}/job-invocations/{job_invocation_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"job_name": job_name}, job_invocation_cancel_params.JobInvocationCancelParams),
            ),
            cast_to=JobInvocationCancelResponse,
        )


class AsyncJobInvocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobInvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobInvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobInvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncJobInvocationsResourceWithStreamingResponse(self)

    async def cancel(
        self,
        job_invocation_id: str,
        *,
        app_id: str,
        job_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobInvocationCancelResponse:
        """
        Cancel a specific job invocation for an app.

        Args:
          job_name: The job name to list job invocations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not job_invocation_id:
            raise ValueError(f"Expected a non-empty value for `job_invocation_id` but received {job_invocation_id!r}")
        return await self._post(
            f"/v2/apps/{app_id}/job-invocations/{job_invocation_id}/cancel"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/apps/{app_id}/job-invocations/{job_invocation_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"job_name": job_name}, job_invocation_cancel_params.JobInvocationCancelParams
                ),
            ),
            cast_to=JobInvocationCancelResponse,
        )


class JobInvocationsResourceWithRawResponse:
    def __init__(self, job_invocations: JobInvocationsResource) -> None:
        self._job_invocations = job_invocations

        self.cancel = to_raw_response_wrapper(
            job_invocations.cancel,
        )


class AsyncJobInvocationsResourceWithRawResponse:
    def __init__(self, job_invocations: AsyncJobInvocationsResource) -> None:
        self._job_invocations = job_invocations

        self.cancel = async_to_raw_response_wrapper(
            job_invocations.cancel,
        )


class JobInvocationsResourceWithStreamingResponse:
    def __init__(self, job_invocations: JobInvocationsResource) -> None:
        self._job_invocations = job_invocations

        self.cancel = to_streamed_response_wrapper(
            job_invocations.cancel,
        )


class AsyncJobInvocationsResourceWithStreamingResponse:
    def __init__(self, job_invocations: AsyncJobInvocationsResource) -> None:
        self._job_invocations = job_invocations

        self.cancel = async_to_streamed_response_wrapper(
            job_invocations.cancel,
        )
