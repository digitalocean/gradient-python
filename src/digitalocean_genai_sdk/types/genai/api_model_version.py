# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APIModelVersion"]


class APIModelVersion(BaseModel):
    major: Optional[int] = None

    minor: Optional[int] = None

    patch: Optional[int] = None
