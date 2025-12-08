# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AssociatedResource"]


class AssociatedResource(BaseModel):
    """An objects containing information about a resource associated with a Droplet."""

    id: Optional[str] = None
    """The unique identifier for the resource associated with the Droplet."""

    cost: Optional[str] = None
    """
    The cost of the resource in USD per month if the resource is retained after the
    Droplet is destroyed.
    """

    name: Optional[str] = None
    """The name of the resource associated with the Droplet."""
