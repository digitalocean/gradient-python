# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .job_invocations import (
    JobInvocationsResource,
    AsyncJobInvocationsResource,
    JobInvocationsResourceWithRawResponse,
    AsyncJobInvocationsResourceWithRawResponse,
    JobInvocationsResourceWithStreamingResponse,
    AsyncJobInvocationsResourceWithStreamingResponse,
)

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def job_invocations(self) -> JobInvocationsResource:
        return JobInvocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def job_invocations(self) -> AsyncJobInvocationsResource:
        return AsyncJobInvocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

    @cached_property
    def job_invocations(self) -> JobInvocationsResourceWithRawResponse:
        return JobInvocationsResourceWithRawResponse(self._apps.job_invocations)


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

    @cached_property
    def job_invocations(self) -> AsyncJobInvocationsResourceWithRawResponse:
        return AsyncJobInvocationsResourceWithRawResponse(self._apps.job_invocations)


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

    @cached_property
    def job_invocations(self) -> JobInvocationsResourceWithStreamingResponse:
        return JobInvocationsResourceWithStreamingResponse(self._apps.job_invocations)


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

    @cached_property
    def job_invocations(self) -> AsyncJobInvocationsResourceWithStreamingResponse:
        return AsyncJobInvocationsResourceWithStreamingResponse(self._apps.job_invocations)
