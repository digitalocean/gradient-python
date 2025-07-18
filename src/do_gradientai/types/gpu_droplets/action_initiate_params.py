# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..droplet_backup_policy_param import DropletBackupPolicyParam

__all__ = [
    "ActionInitiateParams",
    "DropletAction",
    "DropletActionEnableBackups",
    "DropletActionChangeBackupPolicy",
    "DropletActionRestore",
    "DropletActionResize",
    "DropletActionRebuild",
    "DropletActionRename",
    "DropletActionChangeKernel",
    "DropletActionSnapshot",
]


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


class DropletActionEnableBackups(TypedDict, total=False):
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

    backup_policy: DropletBackupPolicyParam
    """An object specifying the backup policy for the Droplet.

    If omitted, the backup plan will default to daily.
    """


class DropletActionChangeBackupPolicy(TypedDict, total=False):
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

    backup_policy: DropletBackupPolicyParam
    """An object specifying the backup policy for the Droplet."""


class DropletActionRestore(TypedDict, total=False):
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

    image: int
    """The ID of a backup of the current Droplet instance to restore from."""


class DropletActionResize(TypedDict, total=False):
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

    disk: bool
    """When `true`, the Droplet's disk will be resized in addition to its RAM and CPU.

    This is a permanent change and cannot be reversed as a Droplet's disk size
    cannot be decreased.
    """

    size: str
    """The slug identifier for the size to which you wish to resize the Droplet."""


class DropletActionRebuild(TypedDict, total=False):
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

    image: Union[str, int]
    """
    The image ID of a public or private image or the slug identifier for a public
    image. The Droplet will be rebuilt using this image as its base.
    """


class DropletActionRename(TypedDict, total=False):
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

    name: str
    """The new name for the Droplet."""


class DropletActionChangeKernel(TypedDict, total=False):
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

    kernel: int
    """A unique number used to identify and reference a specific kernel."""


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

    name: str
    """The name to give the new snapshot of the Droplet."""


ActionInitiateParams: TypeAlias = Union[
    DropletAction,
    DropletActionEnableBackups,
    DropletActionChangeBackupPolicy,
    DropletActionRestore,
    DropletActionResize,
    DropletActionRebuild,
    DropletActionRename,
    DropletActionChangeKernel,
    DropletActionSnapshot,
]
