# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

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
from ....types.gpu_droplets import image_list_params, image_create_params, image_update_params
from ....types.gpu_droplets.image_list_response import ImageListResponse
from ....types.gpu_droplets.image_create_response import ImageCreateResponse
from ....types.gpu_droplets.image_update_response import ImageUpdateResponse
from ....types.gpu_droplets.image_retrieve_response import ImageRetrieveResponse

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | Omit = omit,
        distribution: Literal[
            "Arch Linux",
            "CentOS",
            "CoreOS",
            "Debian",
            "Fedora",
            "Fedora Atomic",
            "FreeBSD",
            "Gentoo",
            "openSUSE",
            "RancherOS",
            "Rocky Linux",
            "Ubuntu",
            "Unknown",
        ]
        | Omit = omit,
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageCreateResponse:
        """To create a new custom image, send a POST request to /v2/images.

        The body must
        contain a url attribute pointing to a Linux virtual machine image to be imported
        into DigitalOcean. The image must be in the raw, qcow2, vhdx, vdi, or vmdk
        format. It may be compressed using gzip or bzip2 and must be smaller than 100 GB
        after being decompressed.

        Args:
          description: An optional free-form text field to describe an image.

          distribution: The name of a custom image's distribution. Currently, the valid values are
              `Arch Linux`, `CentOS`, `CoreOS`, `Debian`, `Fedora`, `Fedora Atomic`,
              `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`, `Rocky Linux`, `Ubuntu`, and
              `Unknown`. Any other value will be accepted but ignored, and `Unknown` will be
              used in its place.

          name: The display name that has been given to an image. This is what is shown in the
              control panel and is generally a descriptive title for the image in question.

          region: The slug identifier for the region where the resource will initially be
              available.

          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              may be for either existing or new tags.

              Requires `tag:create` scope.

          url: A URL from which the custom Linux virtual machine image may be retrieved. The
              image it points to must be in the raw, qcow2, vhdx, vdi, or vmdk format. It may
              be compressed using gzip or bzip2 and must be smaller than 100 GB after being
              decompressed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/images" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/images",
            body=maybe_transform(
                {
                    "description": description,
                    "distribution": distribution,
                    "name": name,
                    "region": region,
                    "tags": tags,
                    "url": url,
                },
                image_create_params.ImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageCreateResponse,
        )

    def retrieve(
        self,
        image_id: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageRetrieveResponse:
        """
        To retrieve information about an image, send a `GET` request to
        `/v2/images/$IDENTIFIER`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/images/{image_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageRetrieveResponse,
        )

    def update(
        self,
        image_id: int,
        *,
        description: str | Omit = omit,
        distribution: Literal[
            "Arch Linux",
            "CentOS",
            "CoreOS",
            "Debian",
            "Fedora",
            "Fedora Atomic",
            "FreeBSD",
            "Gentoo",
            "openSUSE",
            "RancherOS",
            "Rocky Linux",
            "Ubuntu",
            "Unknown",
        ]
        | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageUpdateResponse:
        """To update an image, send a `PUT` request to `/v2/images/$IMAGE_ID`.

        Set the
        `name` attribute to the new value you would like to use. For custom images, the
        `description` and `distribution` attributes may also be updated.

        Args:
          description: An optional free-form text field to describe an image.

          distribution: The name of a custom image's distribution. Currently, the valid values are
              `Arch Linux`, `CentOS`, `CoreOS`, `Debian`, `Fedora`, `Fedora Atomic`,
              `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`, `Rocky Linux`, `Ubuntu`, and
              `Unknown`. Any other value will be accepted but ignored, and `Unknown` will be
              used in its place.

          name: The display name that has been given to an image. This is what is shown in the
              control panel and is generally a descriptive title for the image in question.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/v2/images/{image_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "distribution": distribution,
                    "name": name,
                },
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        private: bool | Omit = omit,
        tag_name: str | Omit = omit,
        type: Literal["application", "distribution"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageListResponse:
        """
        To list all of the images available on your account, send a GET request to
        /v2/images.

        ## Filtering Results

        ---

        It's possible to request filtered results by including certain query parameters.

        **Image Type**

        Either 1-Click Application or OS Distribution images can be filtered by using
        the `type` query parameter.

        > Important: The `type` query parameter does not directly relate to the `type`
        > attribute.

        To retrieve only **_distribution_** images, include the `type` query parameter
        set to distribution, `/v2/images?type=distribution`.

        To retrieve only **_application_** images, include the `type` query parameter
        set to application, `/v2/images?type=application`.

        **User Images**

        To retrieve only the private images of a user, include the `private` query
        parameter set to true, `/v2/images?private=true`.

        **Tags**

        To list all images assigned to a specific tag, include the `tag_name` query
        parameter set to the name of the tag in your GET request. For example,
        `/v2/images?tag_name=$TAG_NAME`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          private: Used to filter only user images.

          tag_name: Used to filter images by a specific tag.

          type: Filters results based on image type which can be either `application` or
              `distribution`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/images" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "private": private,
                        "tag_name": tag_name,
                        "type": type,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageListResponse,
        )

    def delete(
        self,
        image_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a snapshot or custom image, send a `DELETE` request to
        `/v2/images/$IMAGE_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/images/{image_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | Omit = omit,
        distribution: Literal[
            "Arch Linux",
            "CentOS",
            "CoreOS",
            "Debian",
            "Fedora",
            "Fedora Atomic",
            "FreeBSD",
            "Gentoo",
            "openSUSE",
            "RancherOS",
            "Rocky Linux",
            "Ubuntu",
            "Unknown",
        ]
        | Omit = omit,
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageCreateResponse:
        """To create a new custom image, send a POST request to /v2/images.

        The body must
        contain a url attribute pointing to a Linux virtual machine image to be imported
        into DigitalOcean. The image must be in the raw, qcow2, vhdx, vdi, or vmdk
        format. It may be compressed using gzip or bzip2 and must be smaller than 100 GB
        after being decompressed.

        Args:
          description: An optional free-form text field to describe an image.

          distribution: The name of a custom image's distribution. Currently, the valid values are
              `Arch Linux`, `CentOS`, `CoreOS`, `Debian`, `Fedora`, `Fedora Atomic`,
              `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`, `Rocky Linux`, `Ubuntu`, and
              `Unknown`. Any other value will be accepted but ignored, and `Unknown` will be
              used in its place.

          name: The display name that has been given to an image. This is what is shown in the
              control panel and is generally a descriptive title for the image in question.

          region: The slug identifier for the region where the resource will initially be
              available.

          tags: A flat array of tag names as strings to be applied to the resource. Tag names
              may be for either existing or new tags.

              Requires `tag:create` scope.

          url: A URL from which the custom Linux virtual machine image may be retrieved. The
              image it points to must be in the raw, qcow2, vhdx, vdi, or vmdk format. It may
              be compressed using gzip or bzip2 and must be smaller than 100 GB after being
              decompressed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/images" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/images",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "distribution": distribution,
                    "name": name,
                    "region": region,
                    "tags": tags,
                    "url": url,
                },
                image_create_params.ImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageCreateResponse,
        )

    async def retrieve(
        self,
        image_id: Union[int, str],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageRetrieveResponse:
        """
        To retrieve information about an image, send a `GET` request to
        `/v2/images/$IDENTIFIER`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/images/{image_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageRetrieveResponse,
        )

    async def update(
        self,
        image_id: int,
        *,
        description: str | Omit = omit,
        distribution: Literal[
            "Arch Linux",
            "CentOS",
            "CoreOS",
            "Debian",
            "Fedora",
            "Fedora Atomic",
            "FreeBSD",
            "Gentoo",
            "openSUSE",
            "RancherOS",
            "Rocky Linux",
            "Ubuntu",
            "Unknown",
        ]
        | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageUpdateResponse:
        """To update an image, send a `PUT` request to `/v2/images/$IMAGE_ID`.

        Set the
        `name` attribute to the new value you would like to use. For custom images, the
        `description` and `distribution` attributes may also be updated.

        Args:
          description: An optional free-form text field to describe an image.

          distribution: The name of a custom image's distribution. Currently, the valid values are
              `Arch Linux`, `CentOS`, `CoreOS`, `Debian`, `Fedora`, `Fedora Atomic`,
              `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`, `Rocky Linux`, `Ubuntu`, and
              `Unknown`. Any other value will be accepted but ignored, and `Unknown` will be
              used in its place.

          name: The display name that has been given to an image. This is what is shown in the
              control panel and is generally a descriptive title for the image in question.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/v2/images/{image_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "distribution": distribution,
                    "name": name,
                },
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        private: bool | Omit = omit,
        tag_name: str | Omit = omit,
        type: Literal["application", "distribution"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageListResponse:
        """
        To list all of the images available on your account, send a GET request to
        /v2/images.

        ## Filtering Results

        ---

        It's possible to request filtered results by including certain query parameters.

        **Image Type**

        Either 1-Click Application or OS Distribution images can be filtered by using
        the `type` query parameter.

        > Important: The `type` query parameter does not directly relate to the `type`
        > attribute.

        To retrieve only **_distribution_** images, include the `type` query parameter
        set to distribution, `/v2/images?type=distribution`.

        To retrieve only **_application_** images, include the `type` query parameter
        set to application, `/v2/images?type=application`.

        **User Images**

        To retrieve only the private images of a user, include the `private` query
        parameter set to true, `/v2/images?private=true`.

        **Tags**

        To list all images assigned to a specific tag, include the `tag_name` query
        parameter set to the name of the tag in your GET request. For example,
        `/v2/images?tag_name=$TAG_NAME`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          private: Used to filter only user images.

          tag_name: Used to filter images by a specific tag.

          type: Filters results based on image type which can be either `application` or
              `distribution`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/images" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "private": private,
                        "tag_name": tag_name,
                        "type": type,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageListResponse,
        )

    async def delete(
        self,
        image_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a snapshot or custom image, send a `DELETE` request to
        `/v2/images/$IMAGE_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/images/{image_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/images/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.create = to_raw_response_wrapper(
            images.create,
        )
        self.retrieve = to_raw_response_wrapper(
            images.retrieve,
        )
        self.update = to_raw_response_wrapper(
            images.update,
        )
        self.list = to_raw_response_wrapper(
            images.list,
        )
        self.delete = to_raw_response_wrapper(
            images.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._images.actions)


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.create = async_to_raw_response_wrapper(
            images.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            images.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            images.update,
        )
        self.list = async_to_raw_response_wrapper(
            images.list,
        )
        self.delete = async_to_raw_response_wrapper(
            images.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._images.actions)


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.create = to_streamed_response_wrapper(
            images.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            images.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            images.update,
        )
        self.list = to_streamed_response_wrapper(
            images.list,
        )
        self.delete = to_streamed_response_wrapper(
            images.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._images.actions)


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.create = async_to_streamed_response_wrapper(
            images.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            images.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            images.update,
        )
        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            images.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._images.actions)
