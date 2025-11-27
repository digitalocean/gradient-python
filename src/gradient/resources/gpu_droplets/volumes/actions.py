# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.gpu_droplets.volumes import (
    action_list_params,
    action_retrieve_params,
    action_initiate_by_id_params,
    action_initiate_by_name_params,
)
from ....types.gpu_droplets.volumes.action_list_response import ActionListResponse
from ....types.gpu_droplets.volumes.action_retrieve_response import ActionRetrieveResponse
from ....types.gpu_droplets.volumes.action_initiate_by_id_response import ActionInitiateByIDResponse
from ....types.gpu_droplets.volumes.action_initiate_by_name_response import ActionInitiateByNameResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        action_id: int,
        *,
        volume_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        """
        To retrieve the status of a volume action, send a GET request to
        `/v2/volumes/$VOLUME_ID/actions/$ACTION_ID`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._get(
            f"/v2/volumes/{volume_id}/actions/{action_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/actions/{action_id}",
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
                    action_retrieve_params.ActionRetrieveParams,
                ),
            ),
            cast_to=ActionRetrieveResponse,
        )

    def list(
        self,
        volume_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionListResponse:
        """
        To retrieve all actions that have been executed on a volume, send a GET request
        to `/v2/volumes/$VOLUME_ID/actions`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._get(
            f"/v2/volumes/{volume_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/actions",
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
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    @overload
    def initiate_by_id(
        self,
        volume_id: str,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateByIDResponse:
        """
        To initiate an action on a block storage volume by Id, send a POST request to
        `~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate
        attributes for the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `attach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `detach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        ## Resize a Volume

        | Attribute      | Details                                                             |
        | -------------- | ------------------------------------------------------------------- |
        | type           | This must be `resize`                                               |
        | size_gigabytes | The new size of the block storage volume in GiB (1024^3)            |
        | region         | Set to the slug representing the region where the volume is located |

        Volumes may only be resized upwards. The maximum size for a volume is 16TiB.

        Args:
          droplet_id: The unique identifier for the Droplet the volume will be attached or detached
              from.

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

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
    def initiate_by_id(
        self,
        volume_id: str,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
    ) -> ActionInitiateByIDResponse:
        """
        To initiate an action on a block storage volume by Id, send a POST request to
        `~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate
        attributes for the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `attach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `detach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        ## Resize a Volume

        | Attribute      | Details                                                             |
        | -------------- | ------------------------------------------------------------------- |
        | type           | This must be `resize`                                               |
        | size_gigabytes | The new size of the block storage volume in GiB (1024^3)            |
        | region         | Set to the slug representing the region where the volume is located |

        Volumes may only be resized upwards. The maximum size for a volume is 16TiB.

        Args:
          droplet_id: The unique identifier for the Droplet the volume will be attached or detached
              from.

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate_by_id(
        self,
        volume_id: str,
        *,
        size_gigabytes: int,
        type: Literal["attach", "detach", "resize"],
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
    ) -> ActionInitiateByIDResponse:
        """
        To initiate an action on a block storage volume by Id, send a POST request to
        `~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate
        attributes for the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `attach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `detach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        ## Resize a Volume

        | Attribute      | Details                                                             |
        | -------------- | ------------------------------------------------------------------- |
        | type           | This must be `resize`                                               |
        | size_gigabytes | The new size of the block storage volume in GiB (1024^3)            |
        | region         | Set to the slug representing the region where the volume is located |

        Volumes may only be resized upwards. The maximum size for a volume is 16TiB.

        Args:
          size_gigabytes: The new size of the block storage volume in GiB (1024^3).

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["droplet_id", "type"], ["size_gigabytes", "type"])
    def initiate_by_id(
        self,
        volume_id: str,
        *,
        droplet_id: int | Omit = omit,
        type: Literal["attach", "detach", "resize"],
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        size_gigabytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateByIDResponse:
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._post(
            f"/v2/volumes/{volume_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/actions",
            body=maybe_transform(
                {
                    "droplet_id": droplet_id,
                    "type": type,
                    "region": region,
                    "tags": tags,
                    "size_gigabytes": size_gigabytes,
                },
                action_initiate_by_id_params.ActionInitiateByIDParams,
            ),
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
                    action_initiate_by_id_params.ActionInitiateByIDParams,
                ),
            ),
            cast_to=ActionInitiateByIDResponse,
        )

    @overload
    def initiate_by_name(
        self,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateByNameResponse:
        """
        To initiate an action on a block storage volume by Name, send a POST request to
        `~/v2/volumes/actions`. The body should contain the appropriate attributes for
        the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute   | Details                                                             |
        | ----------- | ------------------------------------------------------------------- |
        | type        | This must be `attach`                                               |
        | volume_name | The name of the block storage volume                                |
        | droplet_id  | Set to the Droplet's ID                                             |
        | region      | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute   | Details                                                             |
        | ----------- | ------------------------------------------------------------------- |
        | type        | This must be `detach`                                               |
        | volume_name | The name of the block storage volume                                |
        | droplet_id  | Set to the Droplet's ID                                             |
        | region      | Set to the slug representing the region where the volume is located |

        Args:
          droplet_id: The unique identifier for the Droplet the volume will be attached or detached
              from.

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

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
    def initiate_by_name(
        self,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
    ) -> ActionInitiateByNameResponse:
        """
        To initiate an action on a block storage volume by Name, send a POST request to
        `~/v2/volumes/actions`. The body should contain the appropriate attributes for
        the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute   | Details                                                             |
        | ----------- | ------------------------------------------------------------------- |
        | type        | This must be `attach`                                               |
        | volume_name | The name of the block storage volume                                |
        | droplet_id  | Set to the Droplet's ID                                             |
        | region      | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute   | Details                                                             |
        | ----------- | ------------------------------------------------------------------- |
        | type        | This must be `detach`                                               |
        | volume_name | The name of the block storage volume                                |
        | droplet_id  | Set to the Droplet's ID                                             |
        | region      | Set to the slug representing the region where the volume is located |

        Args:
          droplet_id: The unique identifier for the Droplet the volume will be attached or detached
              from.

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["droplet_id", "type"])
    def initiate_by_name(
        self,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateByNameResponse:
        return self._post(
            "/v2/volumes/actions"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/volumes/actions",
            body=maybe_transform(
                {
                    "droplet_id": droplet_id,
                    "type": type,
                    "region": region,
                    "tags": tags,
                },
                action_initiate_by_name_params.ActionInitiateByNameParams,
            ),
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
                    action_initiate_by_name_params.ActionInitiateByNameParams,
                ),
            ),
            cast_to=ActionInitiateByNameResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        action_id: int,
        *,
        volume_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        """
        To retrieve the status of a volume action, send a GET request to
        `/v2/volumes/$VOLUME_ID/actions/$ACTION_ID`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._get(
            f"/v2/volumes/{volume_id}/actions/{action_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/actions/{action_id}",
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
                    action_retrieve_params.ActionRetrieveParams,
                ),
            ),
            cast_to=ActionRetrieveResponse,
        )

    async def list(
        self,
        volume_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionListResponse:
        """
        To retrieve all actions that have been executed on a volume, send a GET request
        to `/v2/volumes/$VOLUME_ID/actions`.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._get(
            f"/v2/volumes/{volume_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/actions",
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
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    @overload
    async def initiate_by_id(
        self,
        volume_id: str,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateByIDResponse:
        """
        To initiate an action on a block storage volume by Id, send a POST request to
        `~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate
        attributes for the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `attach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `detach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        ## Resize a Volume

        | Attribute      | Details                                                             |
        | -------------- | ------------------------------------------------------------------- |
        | type           | This must be `resize`                                               |
        | size_gigabytes | The new size of the block storage volume in GiB (1024^3)            |
        | region         | Set to the slug representing the region where the volume is located |

        Volumes may only be resized upwards. The maximum size for a volume is 16TiB.

        Args:
          droplet_id: The unique identifier for the Droplet the volume will be attached or detached
              from.

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

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
    async def initiate_by_id(
        self,
        volume_id: str,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
    ) -> ActionInitiateByIDResponse:
        """
        To initiate an action on a block storage volume by Id, send a POST request to
        `~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate
        attributes for the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `attach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `detach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        ## Resize a Volume

        | Attribute      | Details                                                             |
        | -------------- | ------------------------------------------------------------------- |
        | type           | This must be `resize`                                               |
        | size_gigabytes | The new size of the block storage volume in GiB (1024^3)            |
        | region         | Set to the slug representing the region where the volume is located |

        Volumes may only be resized upwards. The maximum size for a volume is 16TiB.

        Args:
          droplet_id: The unique identifier for the Droplet the volume will be attached or detached
              from.

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate_by_id(
        self,
        volume_id: str,
        *,
        size_gigabytes: int,
        type: Literal["attach", "detach", "resize"],
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
    ) -> ActionInitiateByIDResponse:
        """
        To initiate an action on a block storage volume by Id, send a POST request to
        `~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate
        attributes for the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `attach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute  | Details                                                             |
        | ---------- | ------------------------------------------------------------------- |
        | type       | This must be `detach`                                               |
        | droplet_id | Set to the Droplet's ID                                             |
        | region     | Set to the slug representing the region where the volume is located |

        ## Resize a Volume

        | Attribute      | Details                                                             |
        | -------------- | ------------------------------------------------------------------- |
        | type           | This must be `resize`                                               |
        | size_gigabytes | The new size of the block storage volume in GiB (1024^3)            |
        | region         | Set to the slug representing the region where the volume is located |

        Volumes may only be resized upwards. The maximum size for a volume is 16TiB.

        Args:
          size_gigabytes: The new size of the block storage volume in GiB (1024^3).

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["droplet_id", "type"], ["size_gigabytes", "type"])
    async def initiate_by_id(
        self,
        volume_id: str,
        *,
        droplet_id: int | Omit = omit,
        type: Literal["attach", "detach", "resize"],
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        size_gigabytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateByIDResponse:
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._post(
            f"/v2/volumes/{volume_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/volumes/{volume_id}/actions",
            body=await async_maybe_transform(
                {
                    "droplet_id": droplet_id,
                    "type": type,
                    "region": region,
                    "tags": tags,
                    "size_gigabytes": size_gigabytes,
                },
                action_initiate_by_id_params.ActionInitiateByIDParams,
            ),
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
                    action_initiate_by_id_params.ActionInitiateByIDParams,
                ),
            ),
            cast_to=ActionInitiateByIDResponse,
        )

    @overload
    async def initiate_by_name(
        self,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateByNameResponse:
        """
        To initiate an action on a block storage volume by Name, send a POST request to
        `~/v2/volumes/actions`. The body should contain the appropriate attributes for
        the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute   | Details                                                             |
        | ----------- | ------------------------------------------------------------------- |
        | type        | This must be `attach`                                               |
        | volume_name | The name of the block storage volume                                |
        | droplet_id  | Set to the Droplet's ID                                             |
        | region      | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute   | Details                                                             |
        | ----------- | ------------------------------------------------------------------- |
        | type        | This must be `detach`                                               |
        | volume_name | The name of the block storage volume                                |
        | droplet_id  | Set to the Droplet's ID                                             |
        | region      | Set to the slug representing the region where the volume is located |

        Args:
          droplet_id: The unique identifier for the Droplet the volume will be attached or detached
              from.

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

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
    async def initiate_by_name(
        self,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
    ) -> ActionInitiateByNameResponse:
        """
        To initiate an action on a block storage volume by Name, send a POST request to
        `~/v2/volumes/actions`. The body should contain the appropriate attributes for
        the respective action.

        ## Attach a Block Storage Volume to a Droplet

        | Attribute   | Details                                                             |
        | ----------- | ------------------------------------------------------------------- |
        | type        | This must be `attach`                                               |
        | volume_name | The name of the block storage volume                                |
        | droplet_id  | Set to the Droplet's ID                                             |
        | region      | Set to the slug representing the region where the volume is located |

        Each volume may only be attached to a single Droplet. However, up to fifteen
        volumes may be attached to a Droplet at a time. Pre-formatted volumes will be
        automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS
        Droplets created on or after April 26, 2018 when attached. On older Droplets,
        [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/)
        is required.

        ## Remove a Block Storage Volume from a Droplet

        | Attribute   | Details                                                             |
        | ----------- | ------------------------------------------------------------------- |
        | type        | This must be `detach`                                               |
        | volume_name | The name of the block storage volume                                |
        | droplet_id  | Set to the Droplet's ID                                             |
        | region      | Set to the slug representing the region where the volume is located |

        Args:
          droplet_id: The unique identifier for the Droplet the volume will be attached or detached
              from.

          type: The volume action to initiate.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          region: The slug identifier for the region where the resource will initially be
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["droplet_id", "type"])
    async def initiate_by_name(
        self,
        *,
        droplet_id: int,
        type: Literal["attach", "detach", "resize"],
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateByNameResponse:
        return await self._post(
            "/v2/volumes/actions"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/volumes/actions",
            body=await async_maybe_transform(
                {
                    "droplet_id": droplet_id,
                    "type": type,
                    "region": region,
                    "tags": tags,
                },
                action_initiate_by_name_params.ActionInitiateByNameParams,
            ),
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
                    action_initiate_by_name_params.ActionInitiateByNameParams,
                ),
            ),
            cast_to=ActionInitiateByNameResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            actions.list,
        )
        self.initiate_by_id = to_raw_response_wrapper(
            actions.initiate_by_id,
        )
        self.initiate_by_name = to_raw_response_wrapper(
            actions.initiate_by_name,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            actions.list,
        )
        self.initiate_by_id = async_to_raw_response_wrapper(
            actions.initiate_by_id,
        )
        self.initiate_by_name = async_to_raw_response_wrapper(
            actions.initiate_by_name,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            actions.list,
        )
        self.initiate_by_id = to_streamed_response_wrapper(
            actions.initiate_by_id,
        )
        self.initiate_by_name = to_streamed_response_wrapper(
            actions.initiate_by_name,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
        self.initiate_by_id = async_to_streamed_response_wrapper(
            actions.initiate_by_id,
        )
        self.initiate_by_name = async_to_streamed_response_wrapper(
            actions.initiate_by_name,
        )
