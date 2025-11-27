# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from .snapshots import (
    SnapshotsResource,
    AsyncSnapshotsResource,
    SnapshotsResourceWithRawResponse,
    AsyncSnapshotsResourceWithRawResponse,
    SnapshotsResourceWithStreamingResponse,
    AsyncSnapshotsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.gpu_droplets import volume_list_params, volume_create_params, volume_delete_by_name_params
from ....types.gpu_droplets.volume_list_response import VolumeListResponse
from ....types.gpu_droplets.volume_create_response import VolumeCreateResponse
from ....types.gpu_droplets.volume_retrieve_response import VolumeRetrieveResponse

__all__ = ["VolumesResource", "AsyncVolumesResource"]


class VolumesResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def snapshots(self) -> SnapshotsResource:
        return SnapshotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return VolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return VolumesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        name: str,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ],
        size_gigabytes: int,
        description: str | Omit = omit,
        filesystem_label: str | Omit = omit,
        filesystem_type: str | Omit = omit,
        snapshot_id: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeCreateResponse:
        """To create a new volume, send a POST request to `/v2/volumes`.

        Optionally, a
        `filesystem_type` attribute may be provided in order to automatically format the
        volume's filesystem. Pre-formatted volumes are automatically mounted when
        attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created
        on or after April 26, 2018. Attaching pre-formatted volumes to Droplets without
        support for auto-mounting is not recommended.

        Args:
          name: A human-readable name for the block storage volume. Must be lowercase and be
              composed only of numbers, letters and "-", up to a limit of 64 characters. The
              name must begin with a letter.

          region: The slug identifier for the region where the resource will initially be
              available.

          size_gigabytes: The size of the block storage volume in GiB (1024^3). This field does not apply
              when creating a volume from a snapshot.

          description: An optional free-form text field to describe a block storage volume.

          filesystem_label: The label applied to the filesystem. Labels for ext4 type filesystems may
              contain 16 characters while labels for xfs type filesystems are limited to 12
              characters. May only be used in conjunction with filesystem_type.

          filesystem_type: The name of the filesystem type to be used on the volume. When provided, the
              volume will automatically be formatted to the specified filesystem type.
              Currently, the available options are `ext4` and `xfs`. Pre-formatted volumes are
              automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic,
              and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted
              volumes to other Droplets is not recommended.

          snapshot_id: The unique identifier for the volume snapshot from which to create the volume.

          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              may be for either existing or new tags.

              Requires `tag:create` scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        name: str,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ],
        size_gigabytes: int,
        description: str | Omit = omit,
        filesystem_label: str | Omit = omit,
        filesystem_type: str | Omit = omit,
        snapshot_id: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeCreateResponse:
        """To create a new volume, send a POST request to `/v2/volumes`.

        Optionally, a
        `filesystem_type` attribute may be provided in order to automatically format the
        volume's filesystem. Pre-formatted volumes are automatically mounted when
        attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created
        on or after April 26, 2018. Attaching pre-formatted volumes to Droplets without
        support for auto-mounting is not recommended.

        Args:
          name: A human-readable name for the block storage volume. Must be lowercase and be
              composed only of numbers, letters and "-", up to a limit of 64 characters. The
              name must begin with a letter.

          region: The slug identifier for the region where the resource will initially be
              available.

          size_gigabytes: The size of the block storage volume in GiB (1024^3). This field does not apply
              when creating a volume from a snapshot.

          description: An optional free-form text field to describe a block storage volume.

          filesystem_label: The label applied to the filesystem. Labels for ext4 type filesystems may
              contain 16 characters while labels for xfs type filesystems are limited to 12
              characters. May only be used in conjunction with filesystem_type.

          filesystem_type: The name of the filesystem type to be used on the volume. When provided, the
              volume will automatically be formatted to the specified filesystem type.
              Currently, the available options are `ext4` and `xfs`. Pre-formatted volumes are
              automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic,
              and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted
              volumes to other Droplets is not recommended.

          snapshot_id: The unique identifier for the volume snapshot from which to create the volume.

          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              may be for either existing or new tags.

              Requires `tag:create` scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "region", "size_gigabytes"])
    def create(
        self,
        *,
        name: str,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ],
        size_gigabytes: int,
        description: str | Omit = omit,
        filesystem_label: str | Omit = omit,
        filesystem_type: str | Omit = omit,
        snapshot_id: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeCreateResponse:
        return self._post(
            "/v2/volumes" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/volumes",
            body=maybe_transform(
                {
                    "name": name,
                    "region": region,
                    "size_gigabytes": size_gigabytes,
                    "description": description,
                    "filesystem_label": filesystem_label,
                    "filesystem_type": filesystem_type,
                    "snapshot_id": snapshot_id,
                    "tags": tags,
                },
                volume_create_params.VolumeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeCreateResponse,
        )

    def retrieve(
        self,
        volume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeRetrieveResponse:
        """
        To show information about a block storage volume, send a GET request to
        `/v2/volumes/$VOLUME_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._get(
            f"/v2/volumes/{volume_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeRetrieveResponse,
        )

    def list(
        self,
        *,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeListResponse:
        """
        To list all of the block storage volumes available on your account, send a GET
        request to `/v2/volumes`.

        ## Filtering Results

        ### By Region

        The `region` may be provided as query parameter in order to restrict results to
        volumes available in a specific region. For example: `/v2/volumes?region=nyc1`

        ### By Name

        It is also possible to list volumes on your account that match a specified name.
        To do so, send a GET request with the volume's name as a query parameter to
        `/v2/volumes?name=$VOLUME_NAME`. **Note:** You can only create one volume per
        region with the same name.

        ### By Name and Region

        It is also possible to retrieve information about a block storage volume by
        name. To do so, send a GET request with the volume's name and the region slug
        for the region it is located in as query parameters to
        `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.

        Args:
          name: The block storage volume's name.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource is available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/volumes" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/volumes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "region": region,
                    },
                    volume_list_params.VolumeListParams,
                ),
            ),
            cast_to=VolumeListResponse,
        )

    def delete(
        self,
        volume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a block storage volume, destroying all data and removing it from your
        account, send a DELETE request to `/v2/volumes/$VOLUME_ID`. No response body
        will be sent back, but the response code will indicate success. Specifically,
        the response code will be a 204, which means that the action was successful with
        no returned body data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/volumes/{volume_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_by_name(
        self,
        *,
        name: str | Omit = omit,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Block storage volumes may also be deleted by name by sending a DELETE request
        with the volume's **name** and the **region slug** for the region it is located
        in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`. No
        response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          name: The block storage volume's name.

          region: The slug identifier for the region where the resource is available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v2/volumes" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/volumes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "region": region,
                    },
                    volume_delete_by_name_params.VolumeDeleteByNameParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncVolumesResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResource:
        return AsyncSnapshotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncVolumesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        name: str,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ],
        size_gigabytes: int,
        description: str | Omit = omit,
        filesystem_label: str | Omit = omit,
        filesystem_type: str | Omit = omit,
        snapshot_id: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeCreateResponse:
        """To create a new volume, send a POST request to `/v2/volumes`.

        Optionally, a
        `filesystem_type` attribute may be provided in order to automatically format the
        volume's filesystem. Pre-formatted volumes are automatically mounted when
        attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created
        on or after April 26, 2018. Attaching pre-formatted volumes to Droplets without
        support for auto-mounting is not recommended.

        Args:
          name: A human-readable name for the block storage volume. Must be lowercase and be
              composed only of numbers, letters and "-", up to a limit of 64 characters. The
              name must begin with a letter.

          region: The slug identifier for the region where the resource will initially be
              available.

          size_gigabytes: The size of the block storage volume in GiB (1024^3). This field does not apply
              when creating a volume from a snapshot.

          description: An optional free-form text field to describe a block storage volume.

          filesystem_label: The label applied to the filesystem. Labels for ext4 type filesystems may
              contain 16 characters while labels for xfs type filesystems are limited to 12
              characters. May only be used in conjunction with filesystem_type.

          filesystem_type: The name of the filesystem type to be used on the volume. When provided, the
              volume will automatically be formatted to the specified filesystem type.
              Currently, the available options are `ext4` and `xfs`. Pre-formatted volumes are
              automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic,
              and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted
              volumes to other Droplets is not recommended.

          snapshot_id: The unique identifier for the volume snapshot from which to create the volume.

          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              may be for either existing or new tags.

              Requires `tag:create` scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        name: str,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ],
        size_gigabytes: int,
        description: str | Omit = omit,
        filesystem_label: str | Omit = omit,
        filesystem_type: str | Omit = omit,
        snapshot_id: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeCreateResponse:
        """To create a new volume, send a POST request to `/v2/volumes`.

        Optionally, a
        `filesystem_type` attribute may be provided in order to automatically format the
        volume's filesystem. Pre-formatted volumes are automatically mounted when
        attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created
        on or after April 26, 2018. Attaching pre-formatted volumes to Droplets without
        support for auto-mounting is not recommended.

        Args:
          name: A human-readable name for the block storage volume. Must be lowercase and be
              composed only of numbers, letters and "-", up to a limit of 64 characters. The
              name must begin with a letter.

          region: The slug identifier for the region where the resource will initially be
              available.

          size_gigabytes: The size of the block storage volume in GiB (1024^3). This field does not apply
              when creating a volume from a snapshot.

          description: An optional free-form text field to describe a block storage volume.

          filesystem_label: The label applied to the filesystem. Labels for ext4 type filesystems may
              contain 16 characters while labels for xfs type filesystems are limited to 12
              characters. May only be used in conjunction with filesystem_type.

          filesystem_type: The name of the filesystem type to be used on the volume. When provided, the
              volume will automatically be formatted to the specified filesystem type.
              Currently, the available options are `ext4` and `xfs`. Pre-formatted volumes are
              automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic,
              and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted
              volumes to other Droplets is not recommended.

          snapshot_id: The unique identifier for the volume snapshot from which to create the volume.

          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              may be for either existing or new tags.

              Requires `tag:create` scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "region", "size_gigabytes"])
    async def create(
        self,
        *,
        name: str,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ],
        size_gigabytes: int,
        description: str | Omit = omit,
        filesystem_label: str | Omit = omit,
        filesystem_type: str | Omit = omit,
        snapshot_id: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeCreateResponse:
        return await self._post(
            "/v2/volumes" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/volumes",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "region": region,
                    "size_gigabytes": size_gigabytes,
                    "description": description,
                    "filesystem_label": filesystem_label,
                    "filesystem_type": filesystem_type,
                    "snapshot_id": snapshot_id,
                    "tags": tags,
                },
                volume_create_params.VolumeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeCreateResponse,
        )

    async def retrieve(
        self,
        volume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeRetrieveResponse:
        """
        To show information about a block storage volume, send a GET request to
        `/v2/volumes/$VOLUME_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._get(
            f"/v2/volumes/{volume_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeRetrieveResponse,
        )

    async def list(
        self,
        *,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeListResponse:
        """
        To list all of the block storage volumes available on your account, send a GET
        request to `/v2/volumes`.

        ## Filtering Results

        ### By Region

        The `region` may be provided as query parameter in order to restrict results to
        volumes available in a specific region. For example: `/v2/volumes?region=nyc1`

        ### By Name

        It is also possible to list volumes on your account that match a specified name.
        To do so, send a GET request with the volume's name as a query parameter to
        `/v2/volumes?name=$VOLUME_NAME`. **Note:** You can only create one volume per
        region with the same name.

        ### By Name and Region

        It is also possible to retrieve information about a block storage volume by
        name. To do so, send a GET request with the volume's name and the region slug
        for the region it is located in as query parameters to
        `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.

        Args:
          name: The block storage volume's name.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource is available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/volumes" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/volumes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "region": region,
                    },
                    volume_list_params.VolumeListParams,
                ),
            ),
            cast_to=VolumeListResponse,
        )

    async def delete(
        self,
        volume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a block storage volume, destroying all data and removing it from your
        account, send a DELETE request to `/v2/volumes/$VOLUME_ID`. No response body
        will be sent back, but the response code will indicate success. Specifically,
        the response code will be a 204, which means that the action was successful with
        no returned body data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/volumes/{volume_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_by_name(
        self,
        *,
        name: str | Omit = omit,
        region: Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Block storage volumes may also be deleted by name by sending a DELETE request
        with the volume's **name** and the **region slug** for the region it is located
        in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`. No
        response body will be sent back, but the response code will indicate success.
        Specifically, the response code will be a 204, which means that the action was
        successful with no returned body data.

        Args:
          name: The block storage volume's name.

          region: The slug identifier for the region where the resource is available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v2/volumes" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/volumes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "region": region,
                    },
                    volume_delete_by_name_params.VolumeDeleteByNameParams,
                ),
            ),
            cast_to=NoneType,
        )


class VolumesResourceWithRawResponse:
    def __init__(self, volumes: VolumesResource) -> None:
        self._volumes = volumes

        self.create = to_raw_response_wrapper(
            volumes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            volumes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            volumes.list,
        )
        self.delete = to_raw_response_wrapper(
            volumes.delete,
        )
        self.delete_by_name = to_raw_response_wrapper(
            volumes.delete_by_name,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._volumes.actions)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithRawResponse:
        return SnapshotsResourceWithRawResponse(self._volumes.snapshots)


class AsyncVolumesResourceWithRawResponse:
    def __init__(self, volumes: AsyncVolumesResource) -> None:
        self._volumes = volumes

        self.create = async_to_raw_response_wrapper(
            volumes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            volumes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            volumes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            volumes.delete,
        )
        self.delete_by_name = async_to_raw_response_wrapper(
            volumes.delete_by_name,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._volumes.actions)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithRawResponse:
        return AsyncSnapshotsResourceWithRawResponse(self._volumes.snapshots)


class VolumesResourceWithStreamingResponse:
    def __init__(self, volumes: VolumesResource) -> None:
        self._volumes = volumes

        self.create = to_streamed_response_wrapper(
            volumes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            volumes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            volumes.list,
        )
        self.delete = to_streamed_response_wrapper(
            volumes.delete,
        )
        self.delete_by_name = to_streamed_response_wrapper(
            volumes.delete_by_name,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._volumes.actions)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithStreamingResponse:
        return SnapshotsResourceWithStreamingResponse(self._volumes.snapshots)


class AsyncVolumesResourceWithStreamingResponse:
    def __init__(self, volumes: AsyncVolumesResource) -> None:
        self._volumes = volumes

        self.create = async_to_streamed_response_wrapper(
            volumes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            volumes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            volumes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            volumes.delete,
        )
        self.delete_by_name = async_to_streamed_response_wrapper(
            volumes.delete_by_name,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._volumes.actions)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        return AsyncSnapshotsResourceWithStreamingResponse(self._volumes.snapshots)
