# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .region import Region
from ..._models import BaseModel

__all__ = ["Action"]


class Action(BaseModel):
    id: Optional[int] = None
    """A unique numeric ID that can be used to identify and reference an action."""

    completed_at: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format that represents when
    the action was completed.
    """

    region: Optional[Region] = None

    region_slug: Optional[str] = None
    """A human-readable string that is used as a unique identifier for each region."""

    resource_id: Optional[int] = None
    """A unique identifier for the resource that the action is associated with."""

    resource_type: Optional[str] = None
    """The type of resource that the action is associated with."""

    started_at: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format that represents when
    the action was initiated.
    """

    status: Optional[Literal["in-progress", "completed", "errored"]] = None
    """The current status of the action.

    This can be "in-progress", "completed", or "errored".
    """

    type: Optional[str] = None
    """This is the type of action that the object represents.

    For example, this could be "transfer" to represent the state of an image
    transfer action.
    """
