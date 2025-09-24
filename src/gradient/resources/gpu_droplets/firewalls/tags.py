# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, SequenceNotStr, not_given
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
from ....types.gpu_droplets.firewalls import tag_add_params, tag_remove_params

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return TagsResourceWithStreamingResponse(self)

    def add(
        self,
        firewall_id: str,
        *,
        tags: Optional[SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To assign a tag representing a group of Droplets to a firewall, send a POST
        request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request, there
        should be a `tags` attribute containing a list of tag names.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              must exist in order to be referenced in a request.

              Requires `tag:create` and `tag:read` scopes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v2/firewalls/{firewall_id}/tags"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/tags",
            body=maybe_transform({"tags": tags}, tag_add_params.TagAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        firewall_id: str,
        *,
        tags: Optional[SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To remove a tag representing a group of Droplets from a firewall, send a DELETE
        request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request, there
        should be a `tags` attribute containing a list of tag names.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              must exist in order to be referenced in a request.

              Requires `tag:create` and `tag:read` scopes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/firewalls/{firewall_id}/tags"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/tags",
            body=maybe_transform({"tags": tags}, tag_remove_params.TagRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncTagsResourceWithStreamingResponse(self)

    async def add(
        self,
        firewall_id: str,
        *,
        tags: Optional[SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To assign a tag representing a group of Droplets to a firewall, send a POST
        request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request, there
        should be a `tags` attribute containing a list of tag names.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              must exist in order to be referenced in a request.

              Requires `tag:create` and `tag:read` scopes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v2/firewalls/{firewall_id}/tags"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/tags",
            body=await async_maybe_transform({"tags": tags}, tag_add_params.TagAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        firewall_id: str,
        *,
        tags: Optional[SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To remove a tag representing a group of Droplets from a firewall, send a DELETE
        request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request, there
        should be a `tags` attribute containing a list of tag names.

        No response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              must exist in order to be referenced in a request.

              Requires `tag:create` and `tag:read` scopes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not firewall_id:
            raise ValueError(f"Expected a non-empty value for `firewall_id` but received {firewall_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/firewalls/{firewall_id}/tags"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/firewalls/{firewall_id}/tags",
            body=await async_maybe_transform({"tags": tags}, tag_remove_params.TagRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.add = to_raw_response_wrapper(
            tags.add,
        )
        self.remove = to_raw_response_wrapper(
            tags.remove,
        )


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.add = async_to_raw_response_wrapper(
            tags.add,
        )
        self.remove = async_to_raw_response_wrapper(
            tags.remove,
        )


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.add = to_streamed_response_wrapper(
            tags.add,
        )
        self.remove = to_streamed_response_wrapper(
            tags.remove,
        )


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.add = async_to_streamed_response_wrapper(
            tags.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            tags.remove,
        )
