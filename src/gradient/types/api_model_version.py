# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["APIModelVersion"]


class APIModelVersion(BaseModel):
    """Version Information about a Model"""

    major: Optional[int] = None
    """Major version number"""

    minor: Optional[int] = None
    """Minor version number"""

    patch: Optional[int] = None
    """Patch version number"""
