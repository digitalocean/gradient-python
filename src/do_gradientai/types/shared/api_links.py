# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APILinks", "Pages"]


class Pages(BaseModel):
    first: Optional[str] = None

    last: Optional[str] = None

    next: Optional[str] = None

    previous: Optional[str] = None


class APILinks(BaseModel):
    pages: Optional[Pages] = None
