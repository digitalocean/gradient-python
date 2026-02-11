# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import billing_list_insights_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.billing_list_insights_response import BillingListInsightsResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def list_insights(
        self,
        end_date: Union[str, date],
        *,
        account_urn: str,
        start_date: Union[str, date],
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListInsightsResponse:
        """
        This endpoint returns day-over-day changes in billing resource usage based on
        nightly invoice items, including total amount, region, SKU, and description for
        a specified date range. It is important to note that the daily resource usage
        may not reflect month-end billing totals when totaled for a given month as
        nightly invoice item estimates do not necessarily encompass all invoicing
        factors for the entire month.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_urn:
            raise ValueError(f"Expected a non-empty value for `account_urn` but received {account_urn!r}")
        if not start_date:
            raise ValueError(f"Expected a non-empty value for `start_date` but received {start_date!r}")
        if not end_date:
            raise ValueError(f"Expected a non-empty value for `end_date` but received {end_date!r}")
        return self._get(
            f"/v2/billing/{account_urn}/insights/{start_date}/{end_date}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/billing/{account_urn}/insights/{start_date}/{end_date}",
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
                    billing_list_insights_params.BillingListInsightsParams,
                ),
            ),
            cast_to=BillingListInsightsResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def list_insights(
        self,
        end_date: Union[str, date],
        *,
        account_urn: str,
        start_date: Union[str, date],
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListInsightsResponse:
        """
        This endpoint returns day-over-day changes in billing resource usage based on
        nightly invoice items, including total amount, region, SKU, and description for
        a specified date range. It is important to note that the daily resource usage
        may not reflect month-end billing totals when totaled for a given month as
        nightly invoice item estimates do not necessarily encompass all invoicing
        factors for the entire month.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_urn:
            raise ValueError(f"Expected a non-empty value for `account_urn` but received {account_urn!r}")
        if not start_date:
            raise ValueError(f"Expected a non-empty value for `start_date` but received {start_date!r}")
        if not end_date:
            raise ValueError(f"Expected a non-empty value for `end_date` but received {end_date!r}")
        return await self._get(
            f"/v2/billing/{account_urn}/insights/{start_date}/{end_date}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/billing/{account_urn}/insights/{start_date}/{end_date}",
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
                    billing_list_insights_params.BillingListInsightsParams,
                ),
            ),
            cast_to=BillingListInsightsResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.list_insights = to_raw_response_wrapper(
            billing.list_insights,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.list_insights = async_to_raw_response_wrapper(
            billing.list_insights,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.list_insights = to_streamed_response_wrapper(
            billing.list_insights,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.list_insights = async_to_streamed_response_wrapper(
            billing.list_insights,
        )
