# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from ..shared.page_links import PageLinks
from ..droplet_backup_policy import DropletBackupPolicy
from ..shared.meta_properties import MetaProperties
from ..shared.droplet_next_backup_window import DropletNextBackupWindow

__all__ = ["BackupListPoliciesResponse", "Policies"]


class Policies(BaseModel):
    backup_enabled: Optional[bool] = None
    """A boolean value indicating whether backups are enabled for the Droplet."""

    backup_policy: Optional[DropletBackupPolicy] = None
    """An object specifying the backup policy for the Droplet."""

    droplet_id: Optional[int] = None
    """The unique identifier for the Droplet."""

    next_backup_window: Optional[DropletNextBackupWindow] = None
    """
    An object containing keys with the start and end times of the window during
    which the backup will occur.
    """


class BackupListPoliciesResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    links: Optional[PageLinks] = None

    policies: Optional[Dict[str, Policies]] = None
    """
    A map where the keys are the Droplet IDs and the values are objects containing
    the backup policy information for each Droplet.
    """
