# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APIMeta"]


class APIMeta(BaseModel):
    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
