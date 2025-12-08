# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionLink"]


class ActionLink(BaseModel):
    """The linked actions can be used to check the status of a Droplet's create event."""

    id: Optional[int] = None
    """A unique numeric ID that can be used to identify and reference an action."""

    href: Optional[str] = None
    """A URL that can be used to access the action."""

    rel: Optional[str] = None
    """A string specifying the type of the related action."""
