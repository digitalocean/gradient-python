# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DestroyedAssociatedResource"]


class DestroyedAssociatedResource(BaseModel):
    """An object containing information about a resource scheduled for deletion."""

    id: Optional[str] = None
    """The unique identifier for the resource scheduled for deletion."""

    destroyed_at: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format indicating when the
    resource was destroyed if the request was successful.
    """

    error_message: Optional[str] = None
    """
    A string indicating that the resource was not successfully destroyed and
    providing additional information.
    """

    name: Optional[str] = None
    """The name of the resource scheduled for deletion."""
