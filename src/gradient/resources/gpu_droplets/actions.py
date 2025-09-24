# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.gpu_droplets import action_list_params, action_initiate_params, action_bulk_initiate_params
from ...types.droplet_backup_policy_param import DropletBackupPolicyParam
from ...types.gpu_droplets.action_list_response import ActionListResponse
from ...types.gpu_droplets.action_initiate_response import ActionInitiateResponse
from ...types.gpu_droplets.action_retrieve_response import ActionRetrieveResponse
from ...types.gpu_droplets.action_bulk_initiate_response import ActionBulkInitiateResponse

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
        droplet_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        """
        To retrieve a Droplet action, send a GET request to
        `/v2/droplets/$DROPLET_ID/actions/$ACTION_ID`.

        The response will be a JSON object with a key called `action`. The value will be
        a Droplet action object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v2/droplets/{droplet_id}/actions/{action_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    def list(
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
    ) -> ActionListResponse:
        """
        To retrieve a list of all actions that have been executed for a Droplet, send a
        GET request to `/v2/droplets/$DROPLET_ID/actions`.

        The results will be returned as a JSON object with an `actions` key. This will
        be set to an array filled with `action` objects containing the standard `action`
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
            f"/v2/droplets/{droplet_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/actions",
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
    def bulk_initiate(
        self,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        tag_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionBulkInitiateResponse:
        """Some actions can be performed in bulk on tagged Droplets.

        The actions can be
        initiated by sending a POST to `/v2/droplets/actions?tag_name=$TAG_NAME` with
        the action arguments.

        Only a sub-set of action types are supported:

        - `power_cycle`
        - `power_on`
        - `power_off`
        - `shutdown`
        - `enable_ipv6`
        - `enable_backups`
        - `disable_backups`
        - `snapshot` (also requires `image:create` permission)

        Args:
          type: The type of action to initiate for the Droplet.

          tag_name: Used to filter Droplets by a specific tag. Can not be combined with `name` or
              `type`. Requires `tag:read` scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def bulk_initiate(
        self,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        tag_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionBulkInitiateResponse:
        """Some actions can be performed in bulk on tagged Droplets.

        The actions can be
        initiated by sending a POST to `/v2/droplets/actions?tag_name=$TAG_NAME` with
        the action arguments.

        Only a sub-set of action types are supported:

        - `power_cycle`
        - `power_on`
        - `power_off`
        - `shutdown`
        - `enable_ipv6`
        - `enable_backups`
        - `disable_backups`
        - `snapshot` (also requires `image:create` permission)

        Args:
          type: The type of action to initiate for the Droplet.

          tag_name: Used to filter Droplets by a specific tag. Can not be combined with `name` or
              `type`. Requires `tag:read` scope.

          name: The name to give the new snapshot of the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    def bulk_initiate(
        self,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        tag_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionBulkInitiateResponse:
        return self._post(
            "/v2/droplets/actions"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/actions",
            body=maybe_transform(
                {
                    "type": type,
                    "name": name,
                },
                action_bulk_initiate_params.ActionBulkInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tag_name": tag_name}, action_bulk_initiate_params.ActionBulkInitiateParams),
            ),
            cast_to=ActionBulkInitiateResponse,
        )

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          backup_policy: An object specifying the backup policy for the Droplet. If omitted, the backup
              plan will default to daily.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          backup_policy: An object specifying the backup policy for the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        image: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          image: The ID of a backup of the current Droplet instance to restore from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        disk: bool | Omit = omit,
        size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          disk: When `true`, the Droplet's disk will be resized in addition to its RAM and CPU.
              This is a permanent change and cannot be reversed as a Droplet's disk size
              cannot be decreased.

          size: The slug identifier for the size to which you wish to resize the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        image: Union[str, int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          image: The image ID of a public or private image or the slug identifier for a public
              image. The Droplet will be rebuilt using this image as its base.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          name: The new name for the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        kernel: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          kernel: A unique number used to identify and reference a specific kernel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          name: The name to give the new snapshot of the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        image: int | Union[str, int] | Omit = omit,
        disk: bool | Omit = omit,
        size: str | Omit = omit,
        name: str | Omit = omit,
        kernel: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        return self._post(
            f"/v2/droplets/{droplet_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/actions",
            body=maybe_transform(
                {
                    "type": type,
                    "backup_policy": backup_policy,
                    "image": image,
                    "disk": disk,
                    "size": size,
                    "name": name,
                    "kernel": kernel,
                },
                action_initiate_params.ActionInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionInitiateResponse,
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
        droplet_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        """
        To retrieve a Droplet action, send a GET request to
        `/v2/droplets/$DROPLET_ID/actions/$ACTION_ID`.

        The response will be a JSON object with a key called `action`. The value will be
        a Droplet action object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v2/droplets/{droplet_id}/actions/{action_id}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    async def list(
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
    ) -> ActionListResponse:
        """
        To retrieve a list of all actions that have been executed for a Droplet, send a
        GET request to `/v2/droplets/$DROPLET_ID/actions`.

        The results will be returned as a JSON object with an `actions` key. This will
        be set to an array filled with `action` objects containing the standard `action`
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
            f"/v2/droplets/{droplet_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/actions",
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
    async def bulk_initiate(
        self,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        tag_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionBulkInitiateResponse:
        """Some actions can be performed in bulk on tagged Droplets.

        The actions can be
        initiated by sending a POST to `/v2/droplets/actions?tag_name=$TAG_NAME` with
        the action arguments.

        Only a sub-set of action types are supported:

        - `power_cycle`
        - `power_on`
        - `power_off`
        - `shutdown`
        - `enable_ipv6`
        - `enable_backups`
        - `disable_backups`
        - `snapshot` (also requires `image:create` permission)

        Args:
          type: The type of action to initiate for the Droplet.

          tag_name: Used to filter Droplets by a specific tag. Can not be combined with `name` or
              `type`. Requires `tag:read` scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def bulk_initiate(
        self,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        tag_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionBulkInitiateResponse:
        """Some actions can be performed in bulk on tagged Droplets.

        The actions can be
        initiated by sending a POST to `/v2/droplets/actions?tag_name=$TAG_NAME` with
        the action arguments.

        Only a sub-set of action types are supported:

        - `power_cycle`
        - `power_on`
        - `power_off`
        - `shutdown`
        - `enable_ipv6`
        - `enable_backups`
        - `disable_backups`
        - `snapshot` (also requires `image:create` permission)

        Args:
          type: The type of action to initiate for the Droplet.

          tag_name: Used to filter Droplets by a specific tag. Can not be combined with `name` or
              `type`. Requires `tag:read` scope.

          name: The name to give the new snapshot of the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    async def bulk_initiate(
        self,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        tag_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionBulkInitiateResponse:
        return await self._post(
            "/v2/droplets/actions"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/droplets/actions",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "name": name,
                },
                action_bulk_initiate_params.ActionBulkInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tag_name": tag_name}, action_bulk_initiate_params.ActionBulkInitiateParams
                ),
            ),
            cast_to=ActionBulkInitiateResponse,
        )

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          backup_policy: An object specifying the backup policy for the Droplet. If omitted, the backup
              plan will default to daily.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          backup_policy: An object specifying the backup policy for the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        image: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          image: The ID of a backup of the current Droplet instance to restore from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        disk: bool | Omit = omit,
        size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          disk: When `true`, the Droplet's disk will be resized in addition to its RAM and CPU.
              This is a permanent change and cannot be reversed as a Droplet's disk size
              cannot be decreased.

          size: The slug identifier for the size to which you wish to resize the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        image: Union[str, int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          image: The image ID of a public or private image or the slug identifier for a public
              image. The Droplet will be rebuilt using this image as its base.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          name: The new name for the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        kernel: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          kernel: A unique number used to identify and reference a specific kernel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        """
        To initiate an action on a Droplet send a POST request to
        `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the
        `type` attribute to on of the supported action types:

        | Action                              | Details                                                                                                                                                                                                                                                                                                                                                                                                                             | Additionally Required Permission |
        | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
        | <nobr>`enable_backups`</nobr>       | Enables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                       |                                  |
        | <nobr>`disable_backups`</nobr>      | Disables backups for a Droplet                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
        | <nobr>`change_backup_policy`</nobr> | Update the backup policy for a Droplet                                                                                                                                                                                                                                                                                                                                                                                              |                                  |
        | <nobr>`reboot`</nobr>               | Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console.                                                                                                                                                                                                                                                                                 |                                  |
        | <nobr>`power_cycle`</nobr>          | Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.                                                                                                                                                                                                                                                                                   |                                  |
        | <nobr>`shutdown`</nobr>             | Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. |                                  |
        | <nobr>`power_off`</nobr>            | Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications.                                                                                                                                                                                                                    |                                  |
        | <nobr>`power_on`</nobr>             | Powers on a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
        | <nobr>`restore`</nobr>              | Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.                                                                                                                                                                                                                                                     | droplet:admin                    |
        | <nobr>`password_reset`</nobr>       | Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use.                                                                                                                                                                                                                                                                                                              | droplet:admin                    |
        | <nobr>`resize`</nobr>               | Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`.                                                                                                                                                                                                                                                                        | droplet:create                   |
        | <nobr>`rebuild`</nobr>              | Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug.                                                                                                                                                                                                                                                                                                                                         | droplet:admin                    |
        | <nobr>`rename`</nobr>               | Renames a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
        | <nobr>`change_kernel`</nobr>        | Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default.                                                                                                                                                                                                                                                                        |                                  |
        | <nobr>`enable_ipv6`</nobr>          | Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required.                                                                                                                                                           |                                  |
        | <nobr>`snapshot`</nobr>             | Takes a snapshot of a Droplet.                                                                                                                                                                                                                                                                                                                                                                                                      | image:create                     |

        Args:
          type: The type of action to initiate for the Droplet.

          name: The name to give the new snapshot of the Droplet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    async def initiate(
        self,
        droplet_id: int,
        *,
        type: Literal[
            "enable_backups",
            "disable_backups",
            "reboot",
            "power_cycle",
            "shutdown",
            "power_off",
            "power_on",
            "restore",
            "password_reset",
            "resize",
            "rebuild",
            "rename",
            "change_kernel",
            "enable_ipv6",
            "snapshot",
        ],
        backup_policy: DropletBackupPolicyParam | Omit = omit,
        image: int | Union[str, int] | Omit = omit,
        disk: bool | Omit = omit,
        size: str | Omit = omit,
        name: str | Omit = omit,
        kernel: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionInitiateResponse:
        return await self._post(
            f"/v2/droplets/{droplet_id}/actions"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/droplets/{droplet_id}/actions",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "backup_policy": backup_policy,
                    "image": image,
                    "disk": disk,
                    "size": size,
                    "name": name,
                    "kernel": kernel,
                },
                action_initiate_params.ActionInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionInitiateResponse,
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
        self.bulk_initiate = to_raw_response_wrapper(
            actions.bulk_initiate,
        )
        self.initiate = to_raw_response_wrapper(
            actions.initiate,
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
        self.bulk_initiate = async_to_raw_response_wrapper(
            actions.bulk_initiate,
        )
        self.initiate = async_to_raw_response_wrapper(
            actions.initiate,
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
        self.bulk_initiate = to_streamed_response_wrapper(
            actions.bulk_initiate,
        )
        self.initiate = to_streamed_response_wrapper(
            actions.initiate,
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
        self.bulk_initiate = async_to_streamed_response_wrapper(
            actions.bulk_initiate,
        )
        self.initiate = async_to_streamed_response_wrapper(
            actions.initiate,
        )
