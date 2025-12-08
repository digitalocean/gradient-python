# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NfInitiateActionResponse", "Action"]


class Action(BaseModel):
    """The action that was submitted."""

    region_slug: str
    """The DigitalOcean region slug where the resource is located."""

    resource_id: str
    """The unique identifier of the resource on which the action is being performed."""

    resource_type: Literal["network_file_share", "network_file_share_snapshot"]
    """The type of resource on which the action is being performed."""

    started_at: datetime
    """The timestamp when the action was started."""

    status: Literal["in-progress", "completed", "errored"]
    """The current status of the action."""

    type: str
    """The type of action being performed."""


class NfInitiateActionResponse(BaseModel):
    """Action response of an NFS share."""

    action: Action
    """The action that was submitted."""
