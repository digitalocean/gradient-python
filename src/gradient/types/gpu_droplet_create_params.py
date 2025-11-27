# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .droplet_backup_policy_param import DropletBackupPolicyParam

__all__ = ["GPUDropletCreateParams", "DropletSingleCreate", "DropletMultiCreate"]


class DropletSingleCreate(TypedDict, total=False):
    image: Required[Union[str, int]]
    """
    The image ID of a public or private image or the slug identifier for a public
    image. This image will be the base image for your Droplet. Requires `image:read`
    scope.
    """

    name: Required[str]
    """The human-readable string you wish to use when displaying the Droplet name.

    The name, if set to a domain name managed in the DigitalOcean DNS management
    system, will configure a PTR record for the Droplet. The name set during
    creation will also determine the hostname for the Droplet in its internal
    configuration.
    """

    size: Required[str]
    """The slug identifier for the size that you wish to select for this Droplet."""

    backup_policy: DropletBackupPolicyParam
    """An object specifying the backup policy for the Droplet.

    If omitted and `backups` is `true`, the backup plan will default to daily.
    """

    backups: bool
    """
    A boolean indicating whether automated backups should be enabled for the
    Droplet.
    """

    ipv6: bool
    """A boolean indicating whether to enable IPv6 on the Droplet."""

    monitoring: bool
    """A boolean indicating whether to install the DigitalOcean agent for monitoring."""

    private_networking: bool
    """This parameter has been deprecated.

    Use `vpc_uuid` instead to specify a VPC network for the Droplet. If no
    `vpc_uuid` is provided, the Droplet will be placed in your account's default VPC
    for the region.
    """

    region: str
    """The slug identifier for the region that you wish to deploy the Droplet in.

    If the specific datacenter is not not important, a slug prefix (e.g. `nyc`) can
    be used to deploy the Droplet in any of the that region's locations (`nyc1`,
    `nyc2`, or `nyc3`). If the region is omitted from the create request completely,
    the Droplet may deploy in any region.
    """

    ssh_keys: SequenceNotStr[Union[str, int]]
    """
    An array containing the IDs or fingerprints of the SSH keys that you wish to
    embed in the Droplet's root account upon creation. You must add the keys to your
    team before they can be embedded on a Droplet. Requires `ssh_key:read` scope.
    """

    tags: Optional[SequenceNotStr[str]]
    """A flat array of tag names as strings to apply to the Droplet after it is
    created.

    Tag names can either be existing or new tags. Requires `tag:create` scope.
    """

    user_data: str
    """
    A string containing 'user data' which may be used to configure the Droplet on
    first boot, often a 'cloud-config' file or Bash script. It must be plain text
    and may not exceed 64 KiB in size.
    """

    volumes: SequenceNotStr[str]
    """
    An array of IDs for block storage volumes that will be attached to the Droplet
    once created. The volumes must not already be attached to an existing Droplet.
    Requires `block_storage:read` scpoe.
    """

    vpc_uuid: str
    """A string specifying the UUID of the VPC to which the Droplet will be assigned.

    If excluded, the Droplet will be assigned to your account's default VPC for the
    region. Requires `vpc:read` scope.
    """

    with_droplet_agent: bool
    """
    A boolean indicating whether to install the DigitalOcean agent used for
    providing access to the Droplet web console in the control panel. By default,
    the agent is installed on new Droplets but installation errors (i.e. OS not
    supported) are ignored. To prevent it from being installed, set to `false`. To
    make installation errors fatal, explicitly set it to `true`.
    """


class DropletMultiCreate(TypedDict, total=False):
    image: Required[Union[str, int]]
    """
    The image ID of a public or private image or the slug identifier for a public
    image. This image will be the base image for your Droplet. Requires `image:read`
    scope.
    """

    names: Required[SequenceNotStr[str]]
    """
    An array of human human-readable strings you wish to use when displaying the
    Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS
    management system, will configure a PTR record for the Droplet. Each name set
    during creation will also determine the hostname for the Droplet in its internal
    configuration.
    """

    size: Required[str]
    """The slug identifier for the size that you wish to select for this Droplet."""

    backup_policy: DropletBackupPolicyParam
    """An object specifying the backup policy for the Droplet.

    If omitted and `backups` is `true`, the backup plan will default to daily.
    """

    backups: bool
    """
    A boolean indicating whether automated backups should be enabled for the
    Droplet.
    """

    ipv6: bool
    """A boolean indicating whether to enable IPv6 on the Droplet."""

    monitoring: bool
    """A boolean indicating whether to install the DigitalOcean agent for monitoring."""

    private_networking: bool
    """This parameter has been deprecated.

    Use `vpc_uuid` instead to specify a VPC network for the Droplet. If no
    `vpc_uuid` is provided, the Droplet will be placed in your account's default VPC
    for the region.
    """

    region: str
    """The slug identifier for the region that you wish to deploy the Droplet in.

    If the specific datacenter is not not important, a slug prefix (e.g. `nyc`) can
    be used to deploy the Droplet in any of the that region's locations (`nyc1`,
    `nyc2`, or `nyc3`). If the region is omitted from the create request completely,
    the Droplet may deploy in any region.
    """

    ssh_keys: SequenceNotStr[Union[str, int]]
    """
    An array containing the IDs or fingerprints of the SSH keys that you wish to
    embed in the Droplet's root account upon creation. You must add the keys to your
    team before they can be embedded on a Droplet. Requires `ssh_key:read` scope.
    """

    tags: Optional[SequenceNotStr[str]]
    """A flat array of tag names as strings to apply to the Droplet after it is
    created.

    Tag names can either be existing or new tags. Requires `tag:create` scope.
    """

    user_data: str
    """
    A string containing 'user data' which may be used to configure the Droplet on
    first boot, often a 'cloud-config' file or Bash script. It must be plain text
    and may not exceed 64 KiB in size.
    """

    volumes: SequenceNotStr[str]
    """
    An array of IDs for block storage volumes that will be attached to the Droplet
    once created. The volumes must not already be attached to an existing Droplet.
    Requires `block_storage:read` scpoe.
    """

    vpc_uuid: str
    """A string specifying the UUID of the VPC to which the Droplet will be assigned.

    If excluded, the Droplet will be assigned to your account's default VPC for the
    region. Requires `vpc:read` scope.
    """

    with_droplet_agent: bool
    """
    A boolean indicating whether to install the DigitalOcean agent used for
    providing access to the Droplet web console in the control panel. By default,
    the agent is installed on new Droplets but installation errors (i.e. OS not
    supported) are ignored. To prevent it from being installed, set to `false`. To
    make installation errors fatal, explicitly set it to `true`.
    """


GPUDropletCreateParams: TypeAlias = Union[DropletSingleCreate, DropletMultiCreate]
