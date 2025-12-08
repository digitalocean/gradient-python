# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APISpacesDataSource"]


class APISpacesDataSource(BaseModel):
    """Spaces Bucket Data Source"""

    bucket_name: Optional[str] = None
    """Spaces bucket name"""

    item_path: Optional[str] = None

    region: Optional[str] = None
    """Region of bucket"""
