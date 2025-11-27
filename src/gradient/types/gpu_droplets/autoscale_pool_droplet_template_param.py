# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AutoscalePoolDropletTemplateParam"]


class AutoscalePoolDropletTemplateParam(TypedDict, total=False):
    image: Required[str]
    """The Droplet image to be used for all Droplets in the autoscale pool.

    You may specify the slug or the image ID.
    """

    region: Required[
        Literal[
            "nyc1",
            "nyc2",
            "nyc3",
            "ams2",
            "ams3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "lon1",
            "fra1",
            "tor1",
            "blr1",
            "syd1",
        ]
    ]
    """The datacenter in which all of the Droplets will be created."""

    size: Required[str]
    """The Droplet size to be used for all Droplets in the autoscale pool."""

    ssh_keys: Required[SequenceNotStr[str]]
    """The SSH keys to be installed on the Droplets in the autoscale pool.

    You can either specify the key ID or the fingerprint. Requires `ssh_key:read`
    scope.
    """

    ipv6: bool
    """Assigns a unique IPv6 address to each of the Droplets in the autoscale pool."""

    name: str
    """The name(s) to be applied to all Droplets in the autoscale pool."""

    project_id: str
    """
    The project that the Droplets in the autoscale pool will belong to. Requires
    `project:read` scope.
    """

    tags: SequenceNotStr[str]
    """
    The tags to apply to each of the Droplets in the autoscale pool. Requires
    `tag:read` scope.
    """

    user_data: str
    """
    A string containing user data that cloud-init consumes to configure a Droplet on
    first boot. User data is often a cloud-config file or Bash script. It must be
    plain text and may not exceed 64 KiB in size.
    """

    vpc_uuid: str
    """The VPC where the Droplets in the autoscale pool will be created.

    The VPC must be in the region where you want to create the Droplets. Requires
    `vpc:read` scope.
    """

    with_droplet_agent: bool
    """Installs the Droplet agent.

    This must be set to true to monitor Droplets for resource utilization scaling.
    """
