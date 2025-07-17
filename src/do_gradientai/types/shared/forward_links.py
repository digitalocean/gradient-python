# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ForwardLinks"]


class ForwardLinks(BaseModel):
    last: Optional[str] = None
    """URI of the last page of the results."""

    next: Optional[str] = None
    """URI of the next page of the results."""
