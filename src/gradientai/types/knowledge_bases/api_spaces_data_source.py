# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APISpacesDataSource"]


class APISpacesDataSource(BaseModel):
    bucket_name: Optional[str] = None

    item_path: Optional[str] = None

    region: Optional[str] = None
