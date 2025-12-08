# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APIFileUploadDataSource"]


class APIFileUploadDataSource(BaseModel):
    """File to upload as data source for knowledge base."""

    original_file_name: Optional[str] = None
    """The original file name"""

    size_in_bytes: Optional[str] = None
    """The size of the file in bytes"""

    stored_object_key: Optional[str] = None
    """The object key the file was stored as"""
