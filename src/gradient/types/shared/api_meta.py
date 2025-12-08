# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APIMeta"]


class APIMeta(BaseModel):
    """Meta information about the data set"""

    page: Optional[int] = None
    """The current page"""

    pages: Optional[int] = None
    """Total number of pages"""

    total: Optional[int] = None
    """Total amount of items over all pages"""
