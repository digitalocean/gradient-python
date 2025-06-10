# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .permissions import (
    PermissionsResource,
    AsyncPermissionsResource,
    PermissionsResourceWithRawResponse,
    AsyncPermissionsResourceWithRawResponse,
    PermissionsResourceWithStreamingResponse,
    AsyncPermissionsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CheckpointsResource", "AsyncCheckpointsResource"]


class CheckpointsResource(SyncAPIResource):
    @cached_property
    def permissions(self) -> PermissionsResource:
        return PermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CheckpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return CheckpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return CheckpointsResourceWithStreamingResponse(self)


class AsyncCheckpointsResource(AsyncAPIResource):
    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        return AsyncPermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCheckpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncCheckpointsResourceWithStreamingResponse(self)


class CheckpointsResourceWithRawResponse:
    def __init__(self, checkpoints: CheckpointsResource) -> None:
        self._checkpoints = checkpoints

    @cached_property
    def permissions(self) -> PermissionsResourceWithRawResponse:
        return PermissionsResourceWithRawResponse(self._checkpoints.permissions)


class AsyncCheckpointsResourceWithRawResponse:
    def __init__(self, checkpoints: AsyncCheckpointsResource) -> None:
        self._checkpoints = checkpoints

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithRawResponse:
        return AsyncPermissionsResourceWithRawResponse(self._checkpoints.permissions)


class CheckpointsResourceWithStreamingResponse:
    def __init__(self, checkpoints: CheckpointsResource) -> None:
        self._checkpoints = checkpoints

    @cached_property
    def permissions(self) -> PermissionsResourceWithStreamingResponse:
        return PermissionsResourceWithStreamingResponse(self._checkpoints.permissions)


class AsyncCheckpointsResourceWithStreamingResponse:
    def __init__(self, checkpoints: AsyncCheckpointsResource) -> None:
        self._checkpoints = checkpoints

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithStreamingResponse:
        return AsyncPermissionsResourceWithStreamingResponse(self._checkpoints.permissions)
