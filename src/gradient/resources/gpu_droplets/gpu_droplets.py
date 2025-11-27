# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, Optional, cast
from typing_extensions import Literal, overload

import httpx

from .sizes import (
    SizesResource,
    AsyncSizesResource,
    SizesResourceWithRawResponse,
    AsyncSizesResourceWithRawResponse,
    SizesResourceWithStreamingResponse,
    AsyncSizesResourceWithStreamingResponse,
)
from ...types import (
    gpu_droplet_list_params,
    gpu_droplet_create_params,
    gpu_droplet_list_kernels_params,
    gpu_droplet_delete_by_tag_params,
    gpu_droplet_list_firewalls_params,
    gpu_droplet_list_snapshots_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from .backups import (
    BackupsResource,
    AsyncBackupsResource,
    BackupsResourceWithRawResponse,
    AsyncBackupsResourceWithRawResponse,
    BackupsResourceWithStreamingResponse,
    AsyncBackupsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .autoscale import (
    AutoscaleResource,
    AsyncAutoscaleResource,
    AutoscaleResourceWithRawResponse,
    AsyncAutoscaleResourceWithRawResponse,
    AutoscaleResourceWithStreamingResponse,
    AsyncAutoscaleResourceWithStreamingResponse,
)
from .snapshots import (
    SnapshotsResource,
    AsyncSnapshotsResource,
    SnapshotsResourceWithRawResponse,
    AsyncSnapshotsResourceWithRawResponse,
    SnapshotsResourceWithStreamingResponse,
    AsyncSnapshotsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .images.images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .account.account import (
    AccountResource,
    AsyncAccountResource,
    AccountResourceWithRawResponse,
    AsyncAccountResourceWithRawResponse,
    AccountResourceWithStreamingResponse,
    AsyncAccountResourceWithStreamingResponse,
)
from .volumes.volumes import (
    VolumesResource,
    AsyncVolumesResource,
    VolumesResourceWithRawResponse,
    AsyncVolumesResourceWithRawResponse,
    VolumesResourceWithStreamingResponse,
    AsyncVolumesResourceWithStreamingResponse,
)
from .firewalls.firewalls import (
    FirewallsResource,
    AsyncFirewallsResource,
    FirewallsResourceWithRawResponse,
    AsyncFirewallsResourceWithRawResponse,
    FirewallsResourceWithStreamingResponse,
    AsyncFirewallsResourceWithStreamingResponse,
)
from .floating_ips.floating_ips import (
    FloatingIPsResource,
    AsyncFloatingIPsResource,
    FloatingIPsResourceWithRawResponse,
    AsyncFloatingIPsResourceWithRawResponse,
    FloatingIPsResourceWithStreamingResponse,
    AsyncFloatingIPsResourceWithStreamingResponse,
)
from .load_balancers.load_balancers import (
    LoadBalancersResource,
    AsyncLoadBalancersResource,
    LoadBalancersResourceWithRawResponse,
    AsyncLoadBalancersResourceWithRawResponse,
    LoadBalancersResourceWithStreamingResponse,
    AsyncLoadBalancersResourceWithStreamingResponse,
)
from ...types.gpu_droplet_list_response import GPUDropletListResponse
from .destroy_with_associated_resources import (
    DestroyWithAssociatedResourcesResource,
    AsyncDestroyWithAssociatedResourcesResource,
    DestroyWithAssociatedResourcesResourceWithRawResponse,
    AsyncDestroyWithAssociatedResourcesResourceWithRawResponse,
    DestroyWithAssociatedResourcesResourceWithStreamingResponse,
    AsyncDestroyWithAssociatedResourcesResourceWithStreamingResponse,
)
from ...types.droplet_backup_policy_param import DropletBackupPolicyParam
from ...types.gpu_droplet_create_response import GPUDropletCreateResponse
from ...types.gpu_droplet_retrieve_response import GPUDropletRetrieveResponse
from ...types.gpu_droplet_list_kernels_response import GPUDropletListKernelsResponse
from ...types.gpu_droplet_list_firewalls_response import GPUDropletListFirewallsResponse
from ...types.gpu_droplet_list_neighbors_response import GPUDropletListNeighborsResponse
from ...types.gpu_droplet_list_snapshots_response import GPUDropletListSnapshotsResponse

__all__ = ["GPUDropletsResource", "AsyncGPUDropletsResource"]


class GPUDropletsResource(SyncAPIResource):
    @cached_property
    def backups(self) -> BackupsResource:
        return BackupsResource(self._client)

    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def destroy_with_associated_resources(self) -> DestroyWithAssociatedResourcesResource:
        return DestroyWithAssociatedResourcesResource(self._client)

    @cached_property
    def autoscale(self) -> AutoscaleResource:
        return AutoscaleResource(self._client)

    @cached_property
    def firewalls(self) -> FirewallsResource:
        return FirewallsResource(self._client)

    @cached_property
    def floating_ips(self) -> FloatingIPsResource:
        return FloatingIPsResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def load_balancers(self) -> LoadBalancersResource:
        return LoadBalancersResource(self._client)

    @cached_property
    def sizes(self) -> SizesResource:
        return SizesResource(self._client)

    @cached_property
    def snapshots(self) -> SnapshotsResource:
        return SnapshotsResource(self._client)

    @cached_property
    def volumes(self) -> VolumesResource:
        return VolumesResource(self._client)

    @cached_property
    def account(self) -> AccountResource:
        return AccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> GPUDropletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return GPUDropletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GPUDropletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return GPUDropletsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        image: Union[str, int],
        name: str,
        size: str,
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        backups: bool | Omit = omit,
        ipv6: bool | Omit = omit,
        monitoring: bool | Omit = omit,
        private_networking: bool | Omit = omit,
        region: str | Omit = omit,
        ssh_keys: SequenceNotStr[Union[str, int]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_data: str | Omit = omit,
        volumes: SequenceNotStr[str] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        with_droplet_agent: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletCreateResponse:
        """
        To create a new Droplet, send a POST request to `/v2/droplets` setting the
        required attributes.

        A Droplet will be created using the provided information. The response body will
        contain a JSON object with a key called `droplet`. The value will be an object
        containing the standard attributes for your new Droplet. The response code, 202
        Accepted, does not indicate the success or failure of the operation, just that
        the request has been accepted for processing. The `actions` returned as part of
        the response's `links` object can be used to check the status of the Droplet
        create event.

        ### Create Multiple Droplets

        Creating multiple Droplets is very similar to creating a single Droplet. Instead
        of sending `name` as a string, send `names` as an array of strings. A Droplet
        will be created for each name you send using the associated information. Up to
        ten Droplets may be created this way at a time.

        Rather than returning a single Droplet, the response body will contain a JSON
        array with a key called `droplets`. This will be set to an array of JSON
        objects, each of which will contain the standard Droplet attributes. The
        response code, 202 Accepted, does not indicate the success or failure of any
        operation, just that the request has been accepted for processing. The array of
        `actions` returned as part of the response's `links` object can be used to check
        the status of each individual Droplet create event.

        Args:
          image: The image ID of a public or private image or the slug identifier for a public
              image. This image will be the base image for your Droplet. Requires `image:read`
              scope.

          name: The human-readable string you wish to use when displaying the Droplet name. The
              name, if set to a domain name managed in the DigitalOcean DNS management system,
              will configure a PTR record for the Droplet. The name set during creation will
              also determine the hostname for the Droplet in its internal configuration.

          size: The slug identifier for the size that you wish to select for this Droplet.

          backup_policy: An object specifying the backup policy for the Droplet. If omitted and `backups`
              is `true`, the backup plan will default to daily.

          backups: A boolean indicating whether automated backups should be enabled for the
              Droplet.

          ipv6: A boolean indicating whether to enable IPv6 on the Droplet.

          monitoring: A boolean indicating whether to install the DigitalOcean agent for monitoring.

          private_networking: This parameter has been deprecated. Use `vpc_uuid` instead to specify a VPC
              network for the Droplet. If no `vpc_uuid` is provided, the Droplet will be
              placed in your account's default VPC for the region.

          region: The slug identifier for the region that you wish to deploy the Droplet in. If
              the specific datacenter is not not important, a slug prefix (e.g. `nyc`) can be
              used to deploy the Droplet in any of the that region's locations (`nyc1`,
              `nyc2`, or `nyc3`). If the region is omitted from the create request completely,
              the Droplet may deploy in any region.

          ssh_keys: An array containing the IDs or fingerprints of the SSH keys that you wish to
              embed in the Droplet's root account upon creation. You must add the keys to your
              team before they can be embedded on a Droplet. Requires `ssh_key:read` scope.

          tags: A flat array of tag names as strings to apply to the Droplet after it is
              created. Tag names can either be existing or new tags. Requires `tag:create`
              scope.

          user_data: A string containing 'user data' which may be used to configure the Droplet on
              first boot, often a 'cloud-config' file or Bash script. It must be plain text
              and may not exceed 64 KiB in size.

          volumes: An array of IDs for block storage volumes that will be attached to the Droplet
              once created. The volumes must not already be attached to an existing Droplet.
              Requires `block_storage:read` scpoe.

          vpc_uuid: A string specifying the UUID of the VPC to which the Droplet will be assigned.
              If excluded, the Droplet will be assigned to your account's default VPC for the
              region. Requires `vpc:read` scope.

          with_droplet_agent: A boolean indicating whether to install the DigitalOcean agent used for
              providing access to the Droplet web console in the control panel. By default,
              the agent is installed on new Droplets but installation errors (i.e. OS not
              supported) are ignored. To prevent it from being installed, set to `false`. To
              make installation errors fatal, explicitly set it to `true`.

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
        image: Union[str, int],
        names: SequenceNotStr[str],
        size: str,
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        backups: bool | Omit = omit,
        ipv6: bool | Omit = omit,
        monitoring: bool | Omit = omit,
        private_networking: bool | Omit = omit,
        region: str | Omit = omit,
        ssh_keys: SequenceNotStr[Union[str, int]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_data: str | Omit = omit,
        volumes: SequenceNotStr[str] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        with_droplet_agent: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletCreateResponse:
        """
        To create a new Droplet, send a POST request to `/v2/droplets` setting the
        required attributes.

        A Droplet will be created using the provided information. The response body will
        contain a JSON object with a key called `droplet`. The value will be an object
        containing the standard attributes for your new Droplet. The response code, 202
        Accepted, does not indicate the success or failure of the operation, just that
        the request has been accepted for processing. The `actions` returned as part of
        the response's `links` object can be used to check the status of the Droplet
        create event.

        ### Create Multiple Droplets

        Creating multiple Droplets is very similar to creating a single Droplet. Instead
        of sending `name` as a string, send `names` as an array of strings. A Droplet
        will be created for each name you send using the associated information. Up to
        ten Droplets may be created this way at a time.

        Rather than returning a single Droplet, the response body will contain a JSON
        array with a key called `droplets`. This will be set to an array of JSON
        objects, each of which will contain the standard Droplet attributes. The
        response code, 202 Accepted, does not indicate the success or failure of any
        operation, just that the request has been accepted for processing. The array of
        `actions` returned as part of the response's `links` object can be used to check
        the status of each individual Droplet create event.

        Args:
          image: The image ID of a public or private image or the slug identifier for a public
              image. This image will be the base image for your Droplet. Requires `image:read`
              scope.

          names: An array of human human-readable strings you wish to use when displaying the
              Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS
              management system, will configure a PTR record for the Droplet. Each name set
              during creation will also determine the hostname for the Droplet in its internal
              configuration.

          size: The slug identifier for the size that you wish to select for this Droplet.

          backup_policy: An object specifying the backup policy for the Droplet. If omitted and `backups`
              is `true`, the backup plan will default to daily.

          backups: A boolean indicating whether automated backups should be enabled for the
              Droplet.

          ipv6: A boolean indicating whether to enable IPv6 on the Droplet.

          monitoring: A boolean indicating whether to install the DigitalOcean agent for monitoring.

          private_networking: This parameter has been deprecated. Use `vpc_uuid` instead to specify a VPC
              network for the Droplet. If no `vpc_uuid` is provided, the Droplet will be
              placed in your account's default VPC for the region.

          region: The slug identifier for the region that you wish to deploy the Droplet in. If
              the specific datacenter is not not important, a slug prefix (e.g. `nyc`) can be
              used to deploy the Droplet in any of the that region's locations (`nyc1`,
              `nyc2`, or `nyc3`). If the region is omitted from the create request completely,
              the Droplet may deploy in any region.

          ssh_keys: An array containing the IDs or fingerprints of the SSH keys that you wish to
              embed in the Droplet's root account upon creation. You must add the keys to your
              team before they can be embedded on a Droplet. Requires `ssh_key:read` scope.

          tags: A flat array of tag names as strings to apply to the Droplet after it is
              created. Tag names can either be existing or new tags. Requires `tag:create`
              scope.

          user_data: A string containing 'user data' which may be used to configure the Droplet on
              first boot, often a 'cloud-config' file or Bash script. It must be plain text
              and may not exceed 64 KiB in size.

          volumes: An array of IDs for block storage volumes that will be attached to the Droplet
              once created. The volumes must not already be attached to an existing Droplet.
              Requires `block_storage:read` scpoe.

          vpc_uuid: A string specifying the UUID of the VPC to which the Droplet will be assigned.
              If excluded, the Droplet will be assigned to your account's default VPC for the
              region. Requires `vpc:read` scope.

          with_droplet_agent: A boolean indicating whether to install the DigitalOcean agent used for
              providing access to the Droplet web console in the control panel. By default,
              the agent is installed on new Droplets but installation errors (i.e. OS not
              supported) are ignored. To prevent it from being installed, set to `false`. To
              make installation errors fatal, explicitly set it to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["image", "name", "size"], ["image", "names", "size"])
    def create(
        self,
        *,
        image: Union[str, int],
        name: str | Omit = omit,
        size: str,
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        backups: bool | Omit = omit,
        ipv6: bool | Omit = omit,
        monitoring: bool | Omit = omit,
        private_networking: bool | Omit = omit,
        region: str | Omit = omit,
        ssh_keys: SequenceNotStr[Union[str, int]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_data: str | Omit = omit,
        volumes: SequenceNotStr[str] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        with_droplet_agent: bool | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletCreateResponse:
        return cast(
            GPUDropletCreateResponse,
            self._post(
                "/v2/droplets" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/droplets",
                body=maybe_transform(
                    {
                        "image": image,
                        "name": name,
                        "size": size,
                        "backup_policy": backup_policy,
                        "backups": backups,
                        "ipv6": ipv6,
                        "monitoring": monitoring,
                        "private_networking": private_networking,
                        "region": region,
                        "ssh_keys": ssh_keys,
                        "tags": tags,
                        "user_data": user_data,
                        "volumes": volumes,
                        "vpc_uuid": vpc_uuid,
                        "with_droplet_agent": with_droplet_agent,
                        "names": names,
                    },
                    gpu_droplet_create_params.GPUDropletCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, GPUDropletCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletRetrieveResponse:
        """
        To show information about an individual Droplet, send a GET request to
        `/v2/droplets/$DROPLET_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUDropletRetrieveResponse,
        )

    def list(
        self,
        *,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        tag_name: str | Omit = omit,
        type: Literal["droplets", "gpus"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListResponse:
        """
        To list all Droplets in your account, send a GET request to `/v2/droplets`.

        The response body will be a JSON object with a key of `droplets`. This will be
        set to an array containing objects each representing a Droplet. These will
        contain the standard Droplet attributes.

        ### Filtering Results by Tag

        It's possible to request filtered results by including certain query parameters.
        To only list Droplets assigned to a specific tag, include the `tag_name` query
        parameter set to the name of the tag in your GET request. For example,
        `/v2/droplets?tag_name=$TAG_NAME`.

        ### GPU Droplets

        By default, only non-GPU Droplets are returned. To list only GPU Droplets, set
        the `type` query parameter to `gpus`. For example, `/v2/droplets?type=gpus`.

        Args:
          name: Used to filter list response by Droplet name returning only exact matches. It is
              case-insensitive and can not be combined with `tag_name`.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          tag_name: Used to filter Droplets by a specific tag. Can not be combined with `name` or
              `type`. Requires `tag:read` scope.

          type: When `type` is set to `gpus`, only GPU Droplets will be returned. By default,
              only non-GPU Droplets are returned. Can not be combined with `tag_name`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/droplets" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/droplets",
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
                        "tag_name": tag_name,
                        "type": type,
                    },
                    gpu_droplet_list_params.GPUDropletListParams,
                ),
            ),
            cast_to=GPUDropletListResponse,
        )

    def delete(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a Droplet, send a DELETE request to `/v2/droplets/$DROPLET_ID`.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/droplets/{droplet_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_by_tag(
        self,
        *,
        tag_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete **all** Droplets assigned to a specific tag, include the `tag_name`
        query parameter set to the name of the tag in your DELETE request. For example,
        `/v2/droplets?tag_name=$TAG_NAME`.

        This endpoint requires `tag:read` scope.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          tag_name: Specifies Droplets to be deleted by tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v2/droplets" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/droplets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tag_name": tag_name}, gpu_droplet_delete_by_tag_params.GPUDropletDeleteByTagParams
                ),
            ),
            cast_to=NoneType,
        )

    def list_firewalls(
        self,
        droplet_id: int,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListFirewallsResponse:
        """
        To retrieve a list of all firewalls available to a Droplet, send a GET request
        to `/v2/droplets/$DROPLET_ID/firewalls`

        The response will be a JSON object that has a key called `firewalls`. This will
        be set to an array of `firewall` objects, each of which contain the standard
        `firewall` attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/firewalls"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/firewalls",
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
                    gpu_droplet_list_firewalls_params.GPUDropletListFirewallsParams,
                ),
            ),
            cast_to=GPUDropletListFirewallsResponse,
        )

    def list_kernels(
        self,
        droplet_id: int,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListKernelsResponse:
        """
        To retrieve a list of all kernels available to a Droplet, send a GET request to
        `/v2/droplets/$DROPLET_ID/kernels`

        The response will be a JSON object that has a key called `kernels`. This will be
        set to an array of `kernel` objects, each of which contain the standard `kernel`
        attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/kernels"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/kernels",
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
                    gpu_droplet_list_kernels_params.GPUDropletListKernelsParams,
                ),
            ),
            cast_to=GPUDropletListKernelsResponse,
        )

    def list_neighbors(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListNeighborsResponse:
        """To retrieve a list of any "neighbors" (i.e.

        Droplets that are co-located on the
        same physical hardware) for a specific Droplet, send a GET request to
        `/v2/droplets/$DROPLET_ID/neighbors`.

        The results will be returned as a JSON object with a key of `droplets`. This
        will be set to an array containing objects representing any other Droplets that
        share the same physical hardware. An empty array indicates that the Droplet is
        not co-located any other Droplets associated with your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/neighbors"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/neighbors",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUDropletListNeighborsResponse,
        )

    def list_snapshots(
        self,
        droplet_id: int,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListSnapshotsResponse:
        """
        To retrieve the snapshots that have been created from a Droplet, send a GET
        request to `/v2/droplets/$DROPLET_ID/snapshots`.

        You will get back a JSON object that has a `snapshots` key. This will be set to
        an array of snapshot objects, each of which contain the standard Droplet
        snapshot attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/snapshots"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/snapshots",
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
                    gpu_droplet_list_snapshots_params.GPUDropletListSnapshotsParams,
                ),
            ),
            cast_to=GPUDropletListSnapshotsResponse,
        )


class AsyncGPUDropletsResource(AsyncAPIResource):
    @cached_property
    def backups(self) -> AsyncBackupsResource:
        return AsyncBackupsResource(self._client)

    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def destroy_with_associated_resources(self) -> AsyncDestroyWithAssociatedResourcesResource:
        return AsyncDestroyWithAssociatedResourcesResource(self._client)

    @cached_property
    def autoscale(self) -> AsyncAutoscaleResource:
        return AsyncAutoscaleResource(self._client)

    @cached_property
    def firewalls(self) -> AsyncFirewallsResource:
        return AsyncFirewallsResource(self._client)

    @cached_property
    def floating_ips(self) -> AsyncFloatingIPsResource:
        return AsyncFloatingIPsResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancersResource:
        return AsyncLoadBalancersResource(self._client)

    @cached_property
    def sizes(self) -> AsyncSizesResource:
        return AsyncSizesResource(self._client)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResource:
        return AsyncSnapshotsResource(self._client)

    @cached_property
    def volumes(self) -> AsyncVolumesResource:
        return AsyncVolumesResource(self._client)

    @cached_property
    def account(self) -> AsyncAccountResource:
        return AsyncAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGPUDropletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGPUDropletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGPUDropletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncGPUDropletsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        image: Union[str, int],
        name: str,
        size: str,
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        backups: bool | Omit = omit,
        ipv6: bool | Omit = omit,
        monitoring: bool | Omit = omit,
        private_networking: bool | Omit = omit,
        region: str | Omit = omit,
        ssh_keys: SequenceNotStr[Union[str, int]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_data: str | Omit = omit,
        volumes: SequenceNotStr[str] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        with_droplet_agent: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletCreateResponse:
        """
        To create a new Droplet, send a POST request to `/v2/droplets` setting the
        required attributes.

        A Droplet will be created using the provided information. The response body will
        contain a JSON object with a key called `droplet`. The value will be an object
        containing the standard attributes for your new Droplet. The response code, 202
        Accepted, does not indicate the success or failure of the operation, just that
        the request has been accepted for processing. The `actions` returned as part of
        the response's `links` object can be used to check the status of the Droplet
        create event.

        ### Create Multiple Droplets

        Creating multiple Droplets is very similar to creating a single Droplet. Instead
        of sending `name` as a string, send `names` as an array of strings. A Droplet
        will be created for each name you send using the associated information. Up to
        ten Droplets may be created this way at a time.

        Rather than returning a single Droplet, the response body will contain a JSON
        array with a key called `droplets`. This will be set to an array of JSON
        objects, each of which will contain the standard Droplet attributes. The
        response code, 202 Accepted, does not indicate the success or failure of any
        operation, just that the request has been accepted for processing. The array of
        `actions` returned as part of the response's `links` object can be used to check
        the status of each individual Droplet create event.

        Args:
          image: The image ID of a public or private image or the slug identifier for a public
              image. This image will be the base image for your Droplet. Requires `image:read`
              scope.

          name: The human-readable string you wish to use when displaying the Droplet name. The
              name, if set to a domain name managed in the DigitalOcean DNS management system,
              will configure a PTR record for the Droplet. The name set during creation will
              also determine the hostname for the Droplet in its internal configuration.

          size: The slug identifier for the size that you wish to select for this Droplet.

          backup_policy: An object specifying the backup policy for the Droplet. If omitted and `backups`
              is `true`, the backup plan will default to daily.

          backups: A boolean indicating whether automated backups should be enabled for the
              Droplet.

          ipv6: A boolean indicating whether to enable IPv6 on the Droplet.

          monitoring: A boolean indicating whether to install the DigitalOcean agent for monitoring.

          private_networking: This parameter has been deprecated. Use `vpc_uuid` instead to specify a VPC
              network for the Droplet. If no `vpc_uuid` is provided, the Droplet will be
              placed in your account's default VPC for the region.

          region: The slug identifier for the region that you wish to deploy the Droplet in. If
              the specific datacenter is not not important, a slug prefix (e.g. `nyc`) can be
              used to deploy the Droplet in any of the that region's locations (`nyc1`,
              `nyc2`, or `nyc3`). If the region is omitted from the create request completely,
              the Droplet may deploy in any region.

          ssh_keys: An array containing the IDs or fingerprints of the SSH keys that you wish to
              embed in the Droplet's root account upon creation. You must add the keys to your
              team before they can be embedded on a Droplet. Requires `ssh_key:read` scope.

          tags: A flat array of tag names as strings to apply to the Droplet after it is
              created. Tag names can either be existing or new tags. Requires `tag:create`
              scope.

          user_data: A string containing 'user data' which may be used to configure the Droplet on
              first boot, often a 'cloud-config' file or Bash script. It must be plain text
              and may not exceed 64 KiB in size.

          volumes: An array of IDs for block storage volumes that will be attached to the Droplet
              once created. The volumes must not already be attached to an existing Droplet.
              Requires `block_storage:read` scpoe.

          vpc_uuid: A string specifying the UUID of the VPC to which the Droplet will be assigned.
              If excluded, the Droplet will be assigned to your account's default VPC for the
              region. Requires `vpc:read` scope.

          with_droplet_agent: A boolean indicating whether to install the DigitalOcean agent used for
              providing access to the Droplet web console in the control panel. By default,
              the agent is installed on new Droplets but installation errors (i.e. OS not
              supported) are ignored. To prevent it from being installed, set to `false`. To
              make installation errors fatal, explicitly set it to `true`.

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
        image: Union[str, int],
        names: SequenceNotStr[str],
        size: str,
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        backups: bool | Omit = omit,
        ipv6: bool | Omit = omit,
        monitoring: bool | Omit = omit,
        private_networking: bool | Omit = omit,
        region: str | Omit = omit,
        ssh_keys: SequenceNotStr[Union[str, int]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_data: str | Omit = omit,
        volumes: SequenceNotStr[str] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        with_droplet_agent: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletCreateResponse:
        """
        To create a new Droplet, send a POST request to `/v2/droplets` setting the
        required attributes.

        A Droplet will be created using the provided information. The response body will
        contain a JSON object with a key called `droplet`. The value will be an object
        containing the standard attributes for your new Droplet. The response code, 202
        Accepted, does not indicate the success or failure of the operation, just that
        the request has been accepted for processing. The `actions` returned as part of
        the response's `links` object can be used to check the status of the Droplet
        create event.

        ### Create Multiple Droplets

        Creating multiple Droplets is very similar to creating a single Droplet. Instead
        of sending `name` as a string, send `names` as an array of strings. A Droplet
        will be created for each name you send using the associated information. Up to
        ten Droplets may be created this way at a time.

        Rather than returning a single Droplet, the response body will contain a JSON
        array with a key called `droplets`. This will be set to an array of JSON
        objects, each of which will contain the standard Droplet attributes. The
        response code, 202 Accepted, does not indicate the success or failure of any
        operation, just that the request has been accepted for processing. The array of
        `actions` returned as part of the response's `links` object can be used to check
        the status of each individual Droplet create event.

        Args:
          image: The image ID of a public or private image or the slug identifier for a public
              image. This image will be the base image for your Droplet. Requires `image:read`
              scope.

          names: An array of human human-readable strings you wish to use when displaying the
              Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS
              management system, will configure a PTR record for the Droplet. Each name set
              during creation will also determine the hostname for the Droplet in its internal
              configuration.

          size: The slug identifier for the size that you wish to select for this Droplet.

          backup_policy: An object specifying the backup policy for the Droplet. If omitted and `backups`
              is `true`, the backup plan will default to daily.

          backups: A boolean indicating whether automated backups should be enabled for the
              Droplet.

          ipv6: A boolean indicating whether to enable IPv6 on the Droplet.

          monitoring: A boolean indicating whether to install the DigitalOcean agent for monitoring.

          private_networking: This parameter has been deprecated. Use `vpc_uuid` instead to specify a VPC
              network for the Droplet. If no `vpc_uuid` is provided, the Droplet will be
              placed in your account's default VPC for the region.

          region: The slug identifier for the region that you wish to deploy the Droplet in. If
              the specific datacenter is not not important, a slug prefix (e.g. `nyc`) can be
              used to deploy the Droplet in any of the that region's locations (`nyc1`,
              `nyc2`, or `nyc3`). If the region is omitted from the create request completely,
              the Droplet may deploy in any region.

          ssh_keys: An array containing the IDs or fingerprints of the SSH keys that you wish to
              embed in the Droplet's root account upon creation. You must add the keys to your
              team before they can be embedded on a Droplet. Requires `ssh_key:read` scope.

          tags: A flat array of tag names as strings to apply to the Droplet after it is
              created. Tag names can either be existing or new tags. Requires `tag:create`
              scope.

          user_data: A string containing 'user data' which may be used to configure the Droplet on
              first boot, often a 'cloud-config' file or Bash script. It must be plain text
              and may not exceed 64 KiB in size.

          volumes: An array of IDs for block storage volumes that will be attached to the Droplet
              once created. The volumes must not already be attached to an existing Droplet.
              Requires `block_storage:read` scpoe.

          vpc_uuid: A string specifying the UUID of the VPC to which the Droplet will be assigned.
              If excluded, the Droplet will be assigned to your account's default VPC for the
              region. Requires `vpc:read` scope.

          with_droplet_agent: A boolean indicating whether to install the DigitalOcean agent used for
              providing access to the Droplet web console in the control panel. By default,
              the agent is installed on new Droplets but installation errors (i.e. OS not
              supported) are ignored. To prevent it from being installed, set to `false`. To
              make installation errors fatal, explicitly set it to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["image", "name", "size"], ["image", "names", "size"])
    async def create(
        self,
        *,
        image: Union[str, int],
        name: str | Omit = omit,
        size: str,
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        backups: bool | Omit = omit,
        ipv6: bool | Omit = omit,
        monitoring: bool | Omit = omit,
        private_networking: bool | Omit = omit,
        region: str | Omit = omit,
        ssh_keys: SequenceNotStr[Union[str, int]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_data: str | Omit = omit,
        volumes: SequenceNotStr[str] | Omit = omit,
        vpc_uuid: str | Omit = omit,
        with_droplet_agent: bool | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletCreateResponse:
        return cast(
            GPUDropletCreateResponse,
            await self._post(
                "/v2/droplets" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/droplets",
                body=await async_maybe_transform(
                    {
                        "image": image,
                        "name": name,
                        "size": size,
                        "backup_policy": backup_policy,
                        "backups": backups,
                        "ipv6": ipv6,
                        "monitoring": monitoring,
                        "private_networking": private_networking,
                        "region": region,
                        "ssh_keys": ssh_keys,
                        "tags": tags,
                        "user_data": user_data,
                        "volumes": volumes,
                        "vpc_uuid": vpc_uuid,
                        "with_droplet_agent": with_droplet_agent,
                        "names": names,
                    },
                    gpu_droplet_create_params.GPUDropletCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, GPUDropletCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletRetrieveResponse:
        """
        To show information about an individual Droplet, send a GET request to
        `/v2/droplets/$DROPLET_ID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUDropletRetrieveResponse,
        )

    async def list(
        self,
        *,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        tag_name: str | Omit = omit,
        type: Literal["droplets", "gpus"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListResponse:
        """
        To list all Droplets in your account, send a GET request to `/v2/droplets`.

        The response body will be a JSON object with a key of `droplets`. This will be
        set to an array containing objects each representing a Droplet. These will
        contain the standard Droplet attributes.

        ### Filtering Results by Tag

        It's possible to request filtered results by including certain query parameters.
        To only list Droplets assigned to a specific tag, include the `tag_name` query
        parameter set to the name of the tag in your GET request. For example,
        `/v2/droplets?tag_name=$TAG_NAME`.

        ### GPU Droplets

        By default, only non-GPU Droplets are returned. To list only GPU Droplets, set
        the `type` query parameter to `gpus`. For example, `/v2/droplets?type=gpus`.

        Args:
          name: Used to filter list response by Droplet name returning only exact matches. It is
              case-insensitive and can not be combined with `tag_name`.

          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          tag_name: Used to filter Droplets by a specific tag. Can not be combined with `name` or
              `type`. Requires `tag:read` scope.

          type: When `type` is set to `gpus`, only GPU Droplets will be returned. By default,
              only non-GPU Droplets are returned. Can not be combined with `tag_name`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/droplets" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/droplets",
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
                        "tag_name": tag_name,
                        "type": type,
                    },
                    gpu_droplet_list_params.GPUDropletListParams,
                ),
            ),
            cast_to=GPUDropletListResponse,
        )

    async def delete(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete a Droplet, send a DELETE request to `/v2/droplets/$DROPLET_ID`.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/droplets/{droplet_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_by_tag(
        self,
        *,
        tag_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        To delete **all** Droplets assigned to a specific tag, include the `tag_name`
        query parameter set to the name of the tag in your DELETE request. For example,
        `/v2/droplets?tag_name=$TAG_NAME`.

        This endpoint requires `tag:read` scope.

        A successful request will receive a 204 status code with no body in response.
        This indicates that the request was processed successfully.

        Args:
          tag_name: Specifies Droplets to be deleted by tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v2/droplets" if self._client._base_url_overridden else "https://api.digitalocean.com/v2/droplets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tag_name": tag_name}, gpu_droplet_delete_by_tag_params.GPUDropletDeleteByTagParams
                ),
            ),
            cast_to=NoneType,
        )

    async def list_firewalls(
        self,
        droplet_id: int,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListFirewallsResponse:
        """
        To retrieve a list of all firewalls available to a Droplet, send a GET request
        to `/v2/droplets/$DROPLET_ID/firewalls`

        The response will be a JSON object that has a key called `firewalls`. This will
        be set to an array of `firewall` objects, each of which contain the standard
        `firewall` attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/firewalls"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/firewalls",
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
                    gpu_droplet_list_firewalls_params.GPUDropletListFirewallsParams,
                ),
            ),
            cast_to=GPUDropletListFirewallsResponse,
        )

    async def list_kernels(
        self,
        droplet_id: int,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListKernelsResponse:
        """
        To retrieve a list of all kernels available to a Droplet, send a GET request to
        `/v2/droplets/$DROPLET_ID/kernels`

        The response will be a JSON object that has a key called `kernels`. This will be
        set to an array of `kernel` objects, each of which contain the standard `kernel`
        attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/kernels"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/kernels",
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
                    gpu_droplet_list_kernels_params.GPUDropletListKernelsParams,
                ),
            ),
            cast_to=GPUDropletListKernelsResponse,
        )

    async def list_neighbors(
        self,
        droplet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListNeighborsResponse:
        """To retrieve a list of any "neighbors" (i.e.

        Droplets that are co-located on the
        same physical hardware) for a specific Droplet, send a GET request to
        `/v2/droplets/$DROPLET_ID/neighbors`.

        The results will be returned as a JSON object with a key of `droplets`. This
        will be set to an array containing objects representing any other Droplets that
        share the same physical hardware. An empty array indicates that the Droplet is
        not co-located any other Droplets associated with your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/neighbors"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/neighbors",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUDropletListNeighborsResponse,
        )

    async def list_snapshots(
        self,
        droplet_id: int,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUDropletListSnapshotsResponse:
        """
        To retrieve the snapshots that have been created from a Droplet, send a GET
        request to `/v2/droplets/$DROPLET_ID/snapshots`.

        You will get back a JSON object that has a `snapshots` key. This will be set to
        an array of snapshot objects, each of which contain the standard Droplet
        snapshot attributes.

        Args:
          page: Which 'page' of paginated results to return.

          per_page: Number of items returned per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/snapshots"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/snapshots",
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
                    gpu_droplet_list_snapshots_params.GPUDropletListSnapshotsParams,
                ),
            ),
            cast_to=GPUDropletListSnapshotsResponse,
        )


class GPUDropletsResourceWithRawResponse:
    def __init__(self, gpu_droplets: GPUDropletsResource) -> None:
        self._gpu_droplets = gpu_droplets

        self.create = to_raw_response_wrapper(
            gpu_droplets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            gpu_droplets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            gpu_droplets.list,
        )
        self.delete = to_raw_response_wrapper(
            gpu_droplets.delete,
        )
        self.delete_by_tag = to_raw_response_wrapper(
            gpu_droplets.delete_by_tag,
        )
        self.list_firewalls = to_raw_response_wrapper(
            gpu_droplets.list_firewalls,
        )
        self.list_kernels = to_raw_response_wrapper(
            gpu_droplets.list_kernels,
        )
        self.list_neighbors = to_raw_response_wrapper(
            gpu_droplets.list_neighbors,
        )
        self.list_snapshots = to_raw_response_wrapper(
            gpu_droplets.list_snapshots,
        )

    @cached_property
    def backups(self) -> BackupsResourceWithRawResponse:
        return BackupsResourceWithRawResponse(self._gpu_droplets.backups)

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._gpu_droplets.actions)

    @cached_property
    def destroy_with_associated_resources(self) -> DestroyWithAssociatedResourcesResourceWithRawResponse:
        return DestroyWithAssociatedResourcesResourceWithRawResponse(
            self._gpu_droplets.destroy_with_associated_resources
        )

    @cached_property
    def autoscale(self) -> AutoscaleResourceWithRawResponse:
        return AutoscaleResourceWithRawResponse(self._gpu_droplets.autoscale)

    @cached_property
    def firewalls(self) -> FirewallsResourceWithRawResponse:
        return FirewallsResourceWithRawResponse(self._gpu_droplets.firewalls)

    @cached_property
    def floating_ips(self) -> FloatingIPsResourceWithRawResponse:
        return FloatingIPsResourceWithRawResponse(self._gpu_droplets.floating_ips)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._gpu_droplets.images)

    @cached_property
    def load_balancers(self) -> LoadBalancersResourceWithRawResponse:
        return LoadBalancersResourceWithRawResponse(self._gpu_droplets.load_balancers)

    @cached_property
    def sizes(self) -> SizesResourceWithRawResponse:
        return SizesResourceWithRawResponse(self._gpu_droplets.sizes)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithRawResponse:
        return SnapshotsResourceWithRawResponse(self._gpu_droplets.snapshots)

    @cached_property
    def volumes(self) -> VolumesResourceWithRawResponse:
        return VolumesResourceWithRawResponse(self._gpu_droplets.volumes)

    @cached_property
    def account(self) -> AccountResourceWithRawResponse:
        return AccountResourceWithRawResponse(self._gpu_droplets.account)


class AsyncGPUDropletsResourceWithRawResponse:
    def __init__(self, gpu_droplets: AsyncGPUDropletsResource) -> None:
        self._gpu_droplets = gpu_droplets

        self.create = async_to_raw_response_wrapper(
            gpu_droplets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            gpu_droplets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            gpu_droplets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gpu_droplets.delete,
        )
        self.delete_by_tag = async_to_raw_response_wrapper(
            gpu_droplets.delete_by_tag,
        )
        self.list_firewalls = async_to_raw_response_wrapper(
            gpu_droplets.list_firewalls,
        )
        self.list_kernels = async_to_raw_response_wrapper(
            gpu_droplets.list_kernels,
        )
        self.list_neighbors = async_to_raw_response_wrapper(
            gpu_droplets.list_neighbors,
        )
        self.list_snapshots = async_to_raw_response_wrapper(
            gpu_droplets.list_snapshots,
        )

    @cached_property
    def backups(self) -> AsyncBackupsResourceWithRawResponse:
        return AsyncBackupsResourceWithRawResponse(self._gpu_droplets.backups)

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._gpu_droplets.actions)

    @cached_property
    def destroy_with_associated_resources(self) -> AsyncDestroyWithAssociatedResourcesResourceWithRawResponse:
        return AsyncDestroyWithAssociatedResourcesResourceWithRawResponse(
            self._gpu_droplets.destroy_with_associated_resources
        )

    @cached_property
    def autoscale(self) -> AsyncAutoscaleResourceWithRawResponse:
        return AsyncAutoscaleResourceWithRawResponse(self._gpu_droplets.autoscale)

    @cached_property
    def firewalls(self) -> AsyncFirewallsResourceWithRawResponse:
        return AsyncFirewallsResourceWithRawResponse(self._gpu_droplets.firewalls)

    @cached_property
    def floating_ips(self) -> AsyncFloatingIPsResourceWithRawResponse:
        return AsyncFloatingIPsResourceWithRawResponse(self._gpu_droplets.floating_ips)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._gpu_droplets.images)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancersResourceWithRawResponse:
        return AsyncLoadBalancersResourceWithRawResponse(self._gpu_droplets.load_balancers)

    @cached_property
    def sizes(self) -> AsyncSizesResourceWithRawResponse:
        return AsyncSizesResourceWithRawResponse(self._gpu_droplets.sizes)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithRawResponse:
        return AsyncSnapshotsResourceWithRawResponse(self._gpu_droplets.snapshots)

    @cached_property
    def volumes(self) -> AsyncVolumesResourceWithRawResponse:
        return AsyncVolumesResourceWithRawResponse(self._gpu_droplets.volumes)

    @cached_property
    def account(self) -> AsyncAccountResourceWithRawResponse:
        return AsyncAccountResourceWithRawResponse(self._gpu_droplets.account)


class GPUDropletsResourceWithStreamingResponse:
    def __init__(self, gpu_droplets: GPUDropletsResource) -> None:
        self._gpu_droplets = gpu_droplets

        self.create = to_streamed_response_wrapper(
            gpu_droplets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            gpu_droplets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            gpu_droplets.list,
        )
        self.delete = to_streamed_response_wrapper(
            gpu_droplets.delete,
        )
        self.delete_by_tag = to_streamed_response_wrapper(
            gpu_droplets.delete_by_tag,
        )
        self.list_firewalls = to_streamed_response_wrapper(
            gpu_droplets.list_firewalls,
        )
        self.list_kernels = to_streamed_response_wrapper(
            gpu_droplets.list_kernels,
        )
        self.list_neighbors = to_streamed_response_wrapper(
            gpu_droplets.list_neighbors,
        )
        self.list_snapshots = to_streamed_response_wrapper(
            gpu_droplets.list_snapshots,
        )

    @cached_property
    def backups(self) -> BackupsResourceWithStreamingResponse:
        return BackupsResourceWithStreamingResponse(self._gpu_droplets.backups)

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._gpu_droplets.actions)

    @cached_property
    def destroy_with_associated_resources(self) -> DestroyWithAssociatedResourcesResourceWithStreamingResponse:
        return DestroyWithAssociatedResourcesResourceWithStreamingResponse(
            self._gpu_droplets.destroy_with_associated_resources
        )

    @cached_property
    def autoscale(self) -> AutoscaleResourceWithStreamingResponse:
        return AutoscaleResourceWithStreamingResponse(self._gpu_droplets.autoscale)

    @cached_property
    def firewalls(self) -> FirewallsResourceWithStreamingResponse:
        return FirewallsResourceWithStreamingResponse(self._gpu_droplets.firewalls)

    @cached_property
    def floating_ips(self) -> FloatingIPsResourceWithStreamingResponse:
        return FloatingIPsResourceWithStreamingResponse(self._gpu_droplets.floating_ips)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._gpu_droplets.images)

    @cached_property
    def load_balancers(self) -> LoadBalancersResourceWithStreamingResponse:
        return LoadBalancersResourceWithStreamingResponse(self._gpu_droplets.load_balancers)

    @cached_property
    def sizes(self) -> SizesResourceWithStreamingResponse:
        return SizesResourceWithStreamingResponse(self._gpu_droplets.sizes)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithStreamingResponse:
        return SnapshotsResourceWithStreamingResponse(self._gpu_droplets.snapshots)

    @cached_property
    def volumes(self) -> VolumesResourceWithStreamingResponse:
        return VolumesResourceWithStreamingResponse(self._gpu_droplets.volumes)

    @cached_property
    def account(self) -> AccountResourceWithStreamingResponse:
        return AccountResourceWithStreamingResponse(self._gpu_droplets.account)


class AsyncGPUDropletsResourceWithStreamingResponse:
    def __init__(self, gpu_droplets: AsyncGPUDropletsResource) -> None:
        self._gpu_droplets = gpu_droplets

        self.create = async_to_streamed_response_wrapper(
            gpu_droplets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            gpu_droplets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            gpu_droplets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gpu_droplets.delete,
        )
        self.delete_by_tag = async_to_streamed_response_wrapper(
            gpu_droplets.delete_by_tag,
        )
        self.list_firewalls = async_to_streamed_response_wrapper(
            gpu_droplets.list_firewalls,
        )
        self.list_kernels = async_to_streamed_response_wrapper(
            gpu_droplets.list_kernels,
        )
        self.list_neighbors = async_to_streamed_response_wrapper(
            gpu_droplets.list_neighbors,
        )
        self.list_snapshots = async_to_streamed_response_wrapper(
            gpu_droplets.list_snapshots,
        )

    @cached_property
    def backups(self) -> AsyncBackupsResourceWithStreamingResponse:
        return AsyncBackupsResourceWithStreamingResponse(self._gpu_droplets.backups)

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._gpu_droplets.actions)

    @cached_property
    def destroy_with_associated_resources(self) -> AsyncDestroyWithAssociatedResourcesResourceWithStreamingResponse:
        return AsyncDestroyWithAssociatedResourcesResourceWithStreamingResponse(
            self._gpu_droplets.destroy_with_associated_resources
        )

    @cached_property
    def autoscale(self) -> AsyncAutoscaleResourceWithStreamingResponse:
        return AsyncAutoscaleResourceWithStreamingResponse(self._gpu_droplets.autoscale)

    @cached_property
    def firewalls(self) -> AsyncFirewallsResourceWithStreamingResponse:
        return AsyncFirewallsResourceWithStreamingResponse(self._gpu_droplets.firewalls)

    @cached_property
    def floating_ips(self) -> AsyncFloatingIPsResourceWithStreamingResponse:
        return AsyncFloatingIPsResourceWithStreamingResponse(self._gpu_droplets.floating_ips)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._gpu_droplets.images)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancersResourceWithStreamingResponse:
        return AsyncLoadBalancersResourceWithStreamingResponse(self._gpu_droplets.load_balancers)

    @cached_property
    def sizes(self) -> AsyncSizesResourceWithStreamingResponse:
        return AsyncSizesResourceWithStreamingResponse(self._gpu_droplets.sizes)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        return AsyncSnapshotsResourceWithStreamingResponse(self._gpu_droplets.snapshots)

    @cached_property
    def volumes(self) -> AsyncVolumesResourceWithStreamingResponse:
        return AsyncVolumesResourceWithStreamingResponse(self._gpu_droplets.volumes)

    @cached_property
    def account(self) -> AsyncAccountResourceWithStreamingResponse:
        return AsyncAccountResourceWithStreamingResponse(self._gpu_droplets.account)
