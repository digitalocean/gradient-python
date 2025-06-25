# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IndexingJobRetrieveDataSourcesResponse", "IndexedDataSource"]


class IndexedDataSource(BaseModel):
    completed_at: Optional[datetime] = None

    data_source_uuid: Optional[str] = None

    error_details: Optional[str] = None

    error_msg: Optional[str] = None

    failed_item_count: Optional[str] = None

    indexed_file_count: Optional[str] = None

    indexed_item_count: Optional[str] = None

    removed_item_count: Optional[str] = None

    skipped_item_count: Optional[str] = None

    started_at: Optional[datetime] = None

    status: Optional[
        Literal[
            "DATA_SOURCE_STATUS_UNKNOWN",
            "DATA_SOURCE_STATUS_IN_PROGRESS",
            "DATA_SOURCE_STATUS_UPDATED",
            "DATA_SOURCE_STATUS_PARTIALLY_UPDATED",
            "DATA_SOURCE_STATUS_NOT_UPDATED",
            "DATA_SOURCE_STATUS_FAILED",
        ]
    ] = None

    total_bytes: Optional[str] = None

    total_bytes_indexed: Optional[str] = None

    total_file_count: Optional[str] = None


class IndexingJobRetrieveDataSourcesResponse(BaseModel):
    indexed_data_sources: Optional[List[IndexedDataSource]] = None
