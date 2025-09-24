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
from ...types.agents import route_add_params, route_update_params
from ...types.agents.route_add_response import RouteAddResponse
from ...types.agents.route_view_response import RouteViewResponse
from ...types.agents.route_delete_response import RouteDeleteResponse
from ...types.agents.route_update_response import RouteUpdateResponse

__all__ = ["RoutesResource", "AsyncRoutesResource"]


class RoutesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return RoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return RoutesResourceWithStreamingResponse(self)

    def update(
        self,
        path_child_agent_uuid: str,
        *,
        path_parent_agent_uuid: str,
        body_child_agent_uuid: str | Omit = omit,
        if_case: str | Omit = omit,
        body_parent_agent_uuid: str | Omit = omit,
        route_name: str | Omit = omit,
        uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteUpdateResponse:
        """
        To update an agent route for an agent, send a PUT request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          body_child_agent_uuid: Routed agent id

          if_case: Describes the case in which the child agent should be used

          body_parent_agent_uuid: A unique identifier for the parent agent.

          route_name: Route name

          uuid: Unique id of linkage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_parent_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_parent_agent_uuid` but received {path_parent_agent_uuid!r}"
            )
        if not path_child_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_child_agent_uuid` but received {path_child_agent_uuid!r}"
            )
        return self._put(
            f"/v2/gen-ai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}",
            body=maybe_transform(
                {
                    "body_child_agent_uuid": body_child_agent_uuid,
                    "if_case": if_case,
                    "body_parent_agent_uuid": body_parent_agent_uuid,
                    "route_name": route_name,
                    "uuid": uuid,
                },
                route_update_params.RouteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteUpdateResponse,
        )

    def delete(
        self,
        child_agent_uuid: str,
        *,
        parent_agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteDeleteResponse:
        """
        To delete an agent route from a parent agent, send a DELETE request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not parent_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `parent_agent_uuid` but received {parent_agent_uuid!r}")
        if not child_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `child_agent_uuid` but received {child_agent_uuid!r}")
        return self._delete(
            f"/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteDeleteResponse,
        )

    def add(
        self,
        path_child_agent_uuid: str,
        *,
        path_parent_agent_uuid: str,
        body_child_agent_uuid: str | Omit = omit,
        if_case: str | Omit = omit,
        body_parent_agent_uuid: str | Omit = omit,
        route_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteAddResponse:
        """
        To add an agent route to an agent, send a POST request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          body_child_agent_uuid: Routed agent id

          body_parent_agent_uuid: A unique identifier for the parent agent.

          route_name: Name of route

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_parent_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_parent_agent_uuid` but received {path_parent_agent_uuid!r}"
            )
        if not path_child_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_child_agent_uuid` but received {path_child_agent_uuid!r}"
            )
        return self._post(
            f"/v2/gen-ai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}",
            body=maybe_transform(
                {
                    "body_child_agent_uuid": body_child_agent_uuid,
                    "if_case": if_case,
                    "body_parent_agent_uuid": body_parent_agent_uuid,
                    "route_name": route_name,
                },
                route_add_params.RouteAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteAddResponse,
        )

    def view(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteViewResponse:
        """
        To view agent routes for an agent, send a GET requtest to
        `/v2/gen-ai/agents/{uuid}/child_agents`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/v2/gen-ai/agents/{uuid}/child_agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{uuid}/child_agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteViewResponse,
        )


class AsyncRoutesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncRoutesResourceWithStreamingResponse(self)

    async def update(
        self,
        path_child_agent_uuid: str,
        *,
        path_parent_agent_uuid: str,
        body_child_agent_uuid: str | Omit = omit,
        if_case: str | Omit = omit,
        body_parent_agent_uuid: str | Omit = omit,
        route_name: str | Omit = omit,
        uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteUpdateResponse:
        """
        To update an agent route for an agent, send a PUT request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          body_child_agent_uuid: Routed agent id

          if_case: Describes the case in which the child agent should be used

          body_parent_agent_uuid: A unique identifier for the parent agent.

          route_name: Route name

          uuid: Unique id of linkage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_parent_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_parent_agent_uuid` but received {path_parent_agent_uuid!r}"
            )
        if not path_child_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_child_agent_uuid` but received {path_child_agent_uuid!r}"
            )
        return await self._put(
            f"/v2/gen-ai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}",
            body=await async_maybe_transform(
                {
                    "body_child_agent_uuid": body_child_agent_uuid,
                    "if_case": if_case,
                    "body_parent_agent_uuid": body_parent_agent_uuid,
                    "route_name": route_name,
                    "uuid": uuid,
                },
                route_update_params.RouteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteUpdateResponse,
        )

    async def delete(
        self,
        child_agent_uuid: str,
        *,
        parent_agent_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteDeleteResponse:
        """
        To delete an agent route from a parent agent, send a DELETE request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not parent_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `parent_agent_uuid` but received {parent_agent_uuid!r}")
        if not child_agent_uuid:
            raise ValueError(f"Expected a non-empty value for `child_agent_uuid` but received {child_agent_uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteDeleteResponse,
        )

    async def add(
        self,
        path_child_agent_uuid: str,
        *,
        path_parent_agent_uuid: str,
        body_child_agent_uuid: str | Omit = omit,
        if_case: str | Omit = omit,
        body_parent_agent_uuid: str | Omit = omit,
        route_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteAddResponse:
        """
        To add an agent route to an agent, send a POST request to
        `/v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}`.

        Args:
          body_child_agent_uuid: Routed agent id

          body_parent_agent_uuid: A unique identifier for the parent agent.

          route_name: Name of route

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_parent_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_parent_agent_uuid` but received {path_parent_agent_uuid!r}"
            )
        if not path_child_agent_uuid:
            raise ValueError(
                f"Expected a non-empty value for `path_child_agent_uuid` but received {path_child_agent_uuid!r}"
            )
        return await self._post(
            f"/v2/gen-ai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{path_parent_agent_uuid}/child_agents/{path_child_agent_uuid}",
            body=await async_maybe_transform(
                {
                    "body_child_agent_uuid": body_child_agent_uuid,
                    "if_case": if_case,
                    "body_parent_agent_uuid": body_parent_agent_uuid,
                    "route_name": route_name,
                },
                route_add_params.RouteAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteAddResponse,
        )

    async def view(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteViewResponse:
        """
        To view agent routes for an agent, send a GET requtest to
        `/v2/gen-ai/agents/{uuid}/child_agents`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/v2/gen-ai/agents/{uuid}/child_agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/agents/{uuid}/child_agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteViewResponse,
        )


class RoutesResourceWithRawResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.update = to_raw_response_wrapper(
            routes.update,
        )
        self.delete = to_raw_response_wrapper(
            routes.delete,
        )
        self.add = to_raw_response_wrapper(
            routes.add,
        )
        self.view = to_raw_response_wrapper(
            routes.view,
        )


class AsyncRoutesResourceWithRawResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.update = async_to_raw_response_wrapper(
            routes.update,
        )
        self.delete = async_to_raw_response_wrapper(
            routes.delete,
        )
        self.add = async_to_raw_response_wrapper(
            routes.add,
        )
        self.view = async_to_raw_response_wrapper(
            routes.view,
        )


class RoutesResourceWithStreamingResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.update = to_streamed_response_wrapper(
            routes.update,
        )
        self.delete = to_streamed_response_wrapper(
            routes.delete,
        )
        self.add = to_streamed_response_wrapper(
            routes.add,
        )
        self.view = to_streamed_response_wrapper(
            routes.view,
        )


class AsyncRoutesResourceWithStreamingResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.update = async_to_streamed_response_wrapper(
            routes.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            routes.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            routes.add,
        )
        self.view = async_to_streamed_response_wrapper(
            routes.view,
        )
