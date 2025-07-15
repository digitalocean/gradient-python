# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BackwardLinks"]


class BackwardLinks(BaseModel):
    first: Optional[str] = None
    """URI of the first page of the results."""

    prev: Optional[str] = None
    """URI of the previous page of the results."""
