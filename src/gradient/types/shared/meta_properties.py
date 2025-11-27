# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MetaProperties"]


class MetaProperties(BaseModel):
    total: Optional[int] = None
    """Number of objects returned by the request."""
