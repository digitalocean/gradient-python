# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ActionBulkInitiateParams", "DropletAction", "DropletActionSnapshot"]


class DropletAction(TypedDict, total=False):
    type: Required[
        Literal[
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
        ]
    ]
    """The type of action to initiate for the Droplet."""

    tag_name: str
    """Used to filter Droplets by a specific tag.

    Can not be combined with `name` or `type`. Requires `tag:read` scope.
    """


class DropletActionSnapshot(TypedDict, total=False):
    type: Required[
        Literal[
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
        ]
    ]
    """The type of action to initiate for the Droplet."""

    tag_name: str
    """Used to filter Droplets by a specific tag.

    Can not be combined with `name` or `type`. Requires `tag:read` scope.
    """

    name: str
    """The name to give the new snapshot of the Droplet."""


ActionBulkInitiateParams: TypeAlias = Union[DropletAction, DropletActionSnapshot]
