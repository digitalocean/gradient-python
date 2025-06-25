# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APIFileUploadDataSource"]


class APIFileUploadDataSource(BaseModel):
    original_file_name: Optional[str] = None

    size_in_bytes: Optional[str] = None

    stored_object_key: Optional[str] = None
