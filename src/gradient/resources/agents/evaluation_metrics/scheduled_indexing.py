# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ....types.agents.evaluation_metrics import scheduled_indexing_create_params
from ....types.agents.evaluation_metrics.scheduled_indexing_create_response import ScheduledIndexingCreateResponse
from ....types.agents.evaluation_metrics.scheduled_indexing_delete_response import ScheduledIndexingDeleteResponse
from ....types.agents.evaluation_metrics.scheduled_indexing_retrieve_response import ScheduledIndexingRetrieveResponse

__all__ = ["ScheduledIndexingResource", "AsyncScheduledIndexingResource"]


class ScheduledIndexingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduledIndexingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ScheduledIndexingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduledIndexingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ScheduledIndexingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        days: Iterable[int] | Omit = omit,
        knowledge_base_uuid: str | Omit = omit,
        time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledIndexingCreateResponse:
        """
        To create scheduled indexing for a knowledge base, send a POST request to
        `/v2/gen-ai/scheduled-indexing`.

        Args:
          days: Days for execution (day is represented same as in a cron expression, e.g. Monday
              begins with 1 )

          knowledge_base_uuid: Knowledge base uuid for which the schedule is created

          time: Time of execution (HH:MM) UTC

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/scheduled-indexing"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/scheduled-indexing",
            body=maybe_transform(
                {
                    "days": days,
                    "knowledge_base_uuid": knowledge_base_uuid,
                    "time": time,
                },
                scheduled_indexing_create_params.ScheduledIndexingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledIndexingCreateResponse,
        )

    def retrieve(
        self,
        knowledge_base_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledIndexingRetrieveResponse:
        """
        Get Scheduled Indexing for knowledge base using knoweldge base uuid, send a GET
        request to `/v2/gen-ai/scheduled-indexing/knowledge-base/{knowledge_base_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `knowledge_base_uuid` but received {knowledge_base_uuid!r}"
            )
        return self._get(
            f"/v2/gen-ai/scheduled-indexing/knowledge-base/{knowledge_base_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/scheduled-indexing/knowledge-base/{knowledge_base_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledIndexingRetrieveResponse,
        )

    def delete(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledIndexingDeleteResponse:
        """
        Delete Scheduled Indexing for knowledge base, send a DELETE request to
        `/v2/gen-ai/scheduled-indexing/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/v2/gen-ai/scheduled-indexing/{uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/scheduled-indexing/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledIndexingDeleteResponse,
        )


class AsyncScheduledIndexingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduledIndexingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduledIndexingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduledIndexingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncScheduledIndexingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        days: Iterable[int] | Omit = omit,
        knowledge_base_uuid: str | Omit = omit,
        time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledIndexingCreateResponse:
        """
        To create scheduled indexing for a knowledge base, send a POST request to
        `/v2/gen-ai/scheduled-indexing`.

        Args:
          days: Days for execution (day is represented same as in a cron expression, e.g. Monday
              begins with 1 )

          knowledge_base_uuid: Knowledge base uuid for which the schedule is created

          time: Time of execution (HH:MM) UTC

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/scheduled-indexing"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/scheduled-indexing",
            body=await async_maybe_transform(
                {
                    "days": days,
                    "knowledge_base_uuid": knowledge_base_uuid,
                    "time": time,
                },
                scheduled_indexing_create_params.ScheduledIndexingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledIndexingCreateResponse,
        )

    async def retrieve(
        self,
        knowledge_base_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledIndexingRetrieveResponse:
        """
        Get Scheduled Indexing for knowledge base using knoweldge base uuid, send a GET
        request to `/v2/gen-ai/scheduled-indexing/knowledge-base/{knowledge_base_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_uuid:
            raise ValueError(
                f"Expected a non-empty value for `knowledge_base_uuid` but received {knowledge_base_uuid!r}"
            )
        return await self._get(
            f"/v2/gen-ai/scheduled-indexing/knowledge-base/{knowledge_base_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/scheduled-indexing/knowledge-base/{knowledge_base_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledIndexingRetrieveResponse,
        )

    async def delete(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledIndexingDeleteResponse:
        """
        Delete Scheduled Indexing for knowledge base, send a DELETE request to
        `/v2/gen-ai/scheduled-indexing/{uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/scheduled-indexing/{uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/scheduled-indexing/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledIndexingDeleteResponse,
        )


class ScheduledIndexingResourceWithRawResponse:
    def __init__(self, scheduled_indexing: ScheduledIndexingResource) -> None:
        self._scheduled_indexing = scheduled_indexing

        self.create = to_raw_response_wrapper(
            scheduled_indexing.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scheduled_indexing.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            scheduled_indexing.delete,
        )


class AsyncScheduledIndexingResourceWithRawResponse:
    def __init__(self, scheduled_indexing: AsyncScheduledIndexingResource) -> None:
        self._scheduled_indexing = scheduled_indexing

        self.create = async_to_raw_response_wrapper(
            scheduled_indexing.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scheduled_indexing.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            scheduled_indexing.delete,
        )


class ScheduledIndexingResourceWithStreamingResponse:
    def __init__(self, scheduled_indexing: ScheduledIndexingResource) -> None:
        self._scheduled_indexing = scheduled_indexing

        self.create = to_streamed_response_wrapper(
            scheduled_indexing.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scheduled_indexing.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            scheduled_indexing.delete,
        )


class AsyncScheduledIndexingResourceWithStreamingResponse:
    def __init__(self, scheduled_indexing: AsyncScheduledIndexingResource) -> None:
        self._scheduled_indexing = scheduled_indexing

        self.create = async_to_streamed_response_wrapper(
            scheduled_indexing.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scheduled_indexing.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            scheduled_indexing.delete,
        )
