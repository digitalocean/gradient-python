# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import organization_get_costs_params, organization_list_audit_logs_params
from .invites import (
    InvitesResource,
    AsyncInvitesResource,
    InvitesResourceWithRawResponse,
    AsyncInvitesResourceWithRawResponse,
    InvitesResourceWithStreamingResponse,
    AsyncInvitesResourceWithStreamingResponse,
)
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
from .admin_api_keys import (
    AdminAPIKeysResource,
    AsyncAdminAPIKeysResource,
    AdminAPIKeysResourceWithRawResponse,
    AsyncAdminAPIKeysResourceWithRawResponse,
    AdminAPIKeysResourceWithStreamingResponse,
    AsyncAdminAPIKeysResourceWithStreamingResponse,
)
from .projects.projects import (
    ProjectsResource,
    AsyncProjectsResource,
    ProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
    AsyncProjectsResourceWithStreamingResponse,
)
from ...types.usage_response import UsageResponse
from ...types.audit_log_event_type import AuditLogEventType
from ...types.organization_list_audit_logs_response import OrganizationListAuditLogsResponse

__all__ = ["OrganizationResource", "AsyncOrganizationResource"]


class OrganizationResource(SyncAPIResource):
    @cached_property
    def admin_api_keys(self) -> AdminAPIKeysResource:
        return AdminAPIKeysResource(self._client)

    @cached_property
    def invites(self) -> InvitesResource:
        return InvitesResource(self._client)

    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        return UsageResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return OrganizationResourceWithStreamingResponse(self)

    def get_costs(
        self,
        *,
        start_time: int,
        bucket_width: Literal["1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "line_item"]] | NotGiven = NOT_GIVEN,
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
        Get costs details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          bucket_width: Width of each time bucket in response. Currently only `1d` is supported, default
              to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the costs by the specified fields. Support fields include `project_id`,
              `line_item` and any combination of them.

          limit: A limit on the number of buckets to be returned. Limit can range between 1 and
              180, and the default is 7.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only costs for these projects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/costs",
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
                    organization_get_costs_params.OrganizationGetCostsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    def list_audit_logs(
        self,
        *,
        actor_emails: List[str] | NotGiven = NOT_GIVEN,
        actor_ids: List[str] | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        effective_at: organization_list_audit_logs_params.EffectiveAt | NotGiven = NOT_GIVEN,
        event_types: List[AuditLogEventType] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        resource_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationListAuditLogsResponse:
        """
        List user actions and configuration changes within this organization.

        Args:
          actor_emails: Return only events performed by users with these emails.

          actor_ids: Return only events performed by these actors. Can be a user ID, a service
              account ID, or an api key tracking ID.

          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          effective_at: Return only events whose `effective_at` (Unix seconds) is in this range.

          event_types: Return only events with a `type` in one of these values. For example,
              `project.created`. For all options, see the documentation for the
              [audit log object](/docs/api-reference/audit-logs/object).

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          project_ids: Return only events for these projects.

          resource_ids: Return only events performed on these targets. For example, a project ID
              updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organization/audit_logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "actor_emails": actor_emails,
                        "actor_ids": actor_ids,
                        "after": after,
                        "before": before,
                        "effective_at": effective_at,
                        "event_types": event_types,
                        "limit": limit,
                        "project_ids": project_ids,
                        "resource_ids": resource_ids,
                    },
                    organization_list_audit_logs_params.OrganizationListAuditLogsParams,
                ),
            ),
            cast_to=OrganizationListAuditLogsResponse,
        )


class AsyncOrganizationResource(AsyncAPIResource):
    @cached_property
    def admin_api_keys(self) -> AsyncAdminAPIKeysResource:
        return AsyncAdminAPIKeysResource(self._client)

    @cached_property
    def invites(self) -> AsyncInvitesResource:
        return AsyncInvitesResource(self._client)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        return AsyncUsageResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return AsyncOrganizationResourceWithStreamingResponse(self)

    async def get_costs(
        self,
        *,
        start_time: int,
        bucket_width: Literal["1d"] | NotGiven = NOT_GIVEN,
        end_time: int | NotGiven = NOT_GIVEN,
        group_by: List[Literal["project_id", "line_item"]] | NotGiven = NOT_GIVEN,
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
        Get costs details for the organization.

        Args:
          start_time: Start time (Unix seconds) of the query time range, inclusive.

          bucket_width: Width of each time bucket in response. Currently only `1d` is supported, default
              to `1d`.

          end_time: End time (Unix seconds) of the query time range, exclusive.

          group_by: Group the costs by the specified fields. Support fields include `project_id`,
              `line_item` and any combination of them.

          limit: A limit on the number of buckets to be returned. Limit can range between 1 and
              180, and the default is 7.

          page: A cursor for use in pagination. Corresponding to the `next_page` field from the
              previous response.

          project_ids: Return only costs for these projects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/costs",
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
                    organization_get_costs_params.OrganizationGetCostsParams,
                ),
            ),
            cast_to=UsageResponse,
        )

    async def list_audit_logs(
        self,
        *,
        actor_emails: List[str] | NotGiven = NOT_GIVEN,
        actor_ids: List[str] | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        effective_at: organization_list_audit_logs_params.EffectiveAt | NotGiven = NOT_GIVEN,
        event_types: List[AuditLogEventType] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        project_ids: List[str] | NotGiven = NOT_GIVEN,
        resource_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationListAuditLogsResponse:
        """
        List user actions and configuration changes within this organization.

        Args:
          actor_emails: Return only events performed by users with these emails.

          actor_ids: Return only events performed by these actors. Can be a user ID, a service
              account ID, or an api key tracking ID.

          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          effective_at: Return only events whose `effective_at` (Unix seconds) is in this range.

          event_types: Return only events with a `type` in one of these values. For example,
              `project.created`. For all options, see the documentation for the
              [audit log object](/docs/api-reference/audit-logs/object).

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          project_ids: Return only events for these projects.

          resource_ids: Return only events performed on these targets. For example, a project ID
              updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organization/audit_logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "actor_emails": actor_emails,
                        "actor_ids": actor_ids,
                        "after": after,
                        "before": before,
                        "effective_at": effective_at,
                        "event_types": event_types,
                        "limit": limit,
                        "project_ids": project_ids,
                        "resource_ids": resource_ids,
                    },
                    organization_list_audit_logs_params.OrganizationListAuditLogsParams,
                ),
            ),
            cast_to=OrganizationListAuditLogsResponse,
        )


class OrganizationResourceWithRawResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.get_costs = to_raw_response_wrapper(
            organization.get_costs,
        )
        self.list_audit_logs = to_raw_response_wrapper(
            organization.list_audit_logs,
        )

    @cached_property
    def admin_api_keys(self) -> AdminAPIKeysResourceWithRawResponse:
        return AdminAPIKeysResourceWithRawResponse(self._organization.admin_api_keys)

    @cached_property
    def invites(self) -> InvitesResourceWithRawResponse:
        return InvitesResourceWithRawResponse(self._organization.invites)

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._organization.projects)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self._organization.usage)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._organization.users)


class AsyncOrganizationResourceWithRawResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.get_costs = async_to_raw_response_wrapper(
            organization.get_costs,
        )
        self.list_audit_logs = async_to_raw_response_wrapper(
            organization.list_audit_logs,
        )

    @cached_property
    def admin_api_keys(self) -> AsyncAdminAPIKeysResourceWithRawResponse:
        return AsyncAdminAPIKeysResourceWithRawResponse(self._organization.admin_api_keys)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithRawResponse:
        return AsyncInvitesResourceWithRawResponse(self._organization.invites)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._organization.projects)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self._organization.usage)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._organization.users)


class OrganizationResourceWithStreamingResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.get_costs = to_streamed_response_wrapper(
            organization.get_costs,
        )
        self.list_audit_logs = to_streamed_response_wrapper(
            organization.list_audit_logs,
        )

    @cached_property
    def admin_api_keys(self) -> AdminAPIKeysResourceWithStreamingResponse:
        return AdminAPIKeysResourceWithStreamingResponse(self._organization.admin_api_keys)

    @cached_property
    def invites(self) -> InvitesResourceWithStreamingResponse:
        return InvitesResourceWithStreamingResponse(self._organization.invites)

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._organization.projects)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self._organization.usage)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._organization.users)


class AsyncOrganizationResourceWithStreamingResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.get_costs = async_to_streamed_response_wrapper(
            organization.get_costs,
        )
        self.list_audit_logs = async_to_streamed_response_wrapper(
            organization.list_audit_logs,
        )

    @cached_property
    def admin_api_keys(self) -> AsyncAdminAPIKeysResourceWithStreamingResponse:
        return AsyncAdminAPIKeysResourceWithStreamingResponse(self._organization.admin_api_keys)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self._organization.invites)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._organization.projects)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._organization.usage)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._organization.users)
