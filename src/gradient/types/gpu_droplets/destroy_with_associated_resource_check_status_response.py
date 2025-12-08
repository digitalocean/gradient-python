# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .destroyed_associated_resource import DestroyedAssociatedResource

__all__ = ["DestroyWithAssociatedResourceCheckStatusResponse", "Resources"]


class Resources(BaseModel):
    """
    An object containing additional information about resource related to a Droplet requested to be destroyed.
    """

    floating_ips: Optional[List[DestroyedAssociatedResource]] = None

    reserved_ips: Optional[List[DestroyedAssociatedResource]] = None

    snapshots: Optional[List[DestroyedAssociatedResource]] = None

    volume_snapshots: Optional[List[DestroyedAssociatedResource]] = None

    volumes: Optional[List[DestroyedAssociatedResource]] = None


class DestroyWithAssociatedResourceCheckStatusResponse(BaseModel):
    """An objects containing information about a resources scheduled for deletion."""

    completed_at: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format indicating when the
    requested action was completed.
    """

    droplet: Optional[DestroyedAssociatedResource] = None
    """An object containing information about a resource scheduled for deletion."""

    failures: Optional[int] = None
    """A count of the associated resources that failed to be destroyed, if any."""

    resources: Optional[Resources] = None
    """
    An object containing additional information about resource related to a Droplet
    requested to be destroyed.
    """
