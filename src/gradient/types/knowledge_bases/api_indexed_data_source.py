# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIIndexedDataSource"]


class APIIndexedDataSource(BaseModel):
    completed_at: Optional[datetime] = None
    """Timestamp when data source completed indexing"""

    data_source_uuid: Optional[str] = None
    """Uuid of the indexed data source"""

    error_details: Optional[str] = None
    """A detailed error description"""

    error_msg: Optional[str] = None
    """A string code provinding a hint which part of the system experienced an error"""

    failed_item_count: Optional[str] = None
    """Total count of files that have failed"""

    indexed_file_count: Optional[str] = None
    """Total count of files that have been indexed"""

    indexed_item_count: Optional[str] = None
    """Total count of files that have been indexed"""

    removed_item_count: Optional[str] = None
    """Total count of files that have been removed"""

    skipped_item_count: Optional[str] = None
    """Total count of files that have been skipped"""

    started_at: Optional[datetime] = None
    """Timestamp when data source started indexing"""

    status: Optional[
        Literal[
            "DATA_SOURCE_STATUS_UNKNOWN",
            "DATA_SOURCE_STATUS_IN_PROGRESS",
            "DATA_SOURCE_STATUS_UPDATED",
            "DATA_SOURCE_STATUS_PARTIALLY_UPDATED",
            "DATA_SOURCE_STATUS_NOT_UPDATED",
            "DATA_SOURCE_STATUS_FAILED",
            "DATA_SOURCE_STATUS_CANCELLED",
        ]
    ] = None

    total_bytes: Optional[str] = None
    """Total size of files in data source in bytes"""

    total_bytes_indexed: Optional[str] = None
    """Total size of files in data source in bytes that have been indexed"""

    total_file_count: Optional[str] = None
    """Total file count in the data source"""
