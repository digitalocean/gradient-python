# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["Region"]


class Region(BaseModel):
    available: bool
    """
    This is a boolean value that represents whether new Droplets can be created in
    this region.
    """

    features: List[str]
    """
    This attribute is set to an array which contains features available in this
    region
    """

    name: str
    """The display name of the region.

    This will be a full name that is used in the control panel and other interfaces.
    """

    sizes: List[str]
    """
    This attribute is set to an array which contains the identifying slugs for the
    sizes available in this region. sizes:read is required to view.
    """

    slug: str
    """A human-readable string that is used as a unique identifier for each region."""
