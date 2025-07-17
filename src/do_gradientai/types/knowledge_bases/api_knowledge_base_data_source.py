# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .api_indexing_job import APIIndexingJob
from .api_spaces_data_source import APISpacesDataSource
from .api_indexed_data_source import APIIndexedDataSource
from .api_file_upload_data_source import APIFileUploadDataSource
from .api_web_crawler_data_source import APIWebCrawlerDataSource

__all__ = ["APIKnowledgeBaseDataSource", "AwsDataSource"]


class AwsDataSource(BaseModel):
    bucket_name: Optional[str] = None
    """Spaces bucket name"""

    item_path: Optional[str] = None

    region: Optional[str] = None
    """Region of bucket"""


class APIKnowledgeBaseDataSource(BaseModel):
    aws_data_source: Optional[AwsDataSource] = None
    """AWS S3 Data Source for Display"""

    bucket_name: Optional[str] = None
    """Name of storage bucket - Deprecated, moved to data_source_details"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    file_upload_data_source: Optional[APIFileUploadDataSource] = None
    """File to upload as data source for knowledge base."""

    item_path: Optional[str] = None
    """Path of folder or object in bucket - Deprecated, moved to data_source_details"""

    last_datasource_indexing_job: Optional[APIIndexedDataSource] = None

    last_indexing_job: Optional[APIIndexingJob] = None
    """IndexingJob description"""

    region: Optional[str] = None
    """Region code - Deprecated, moved to data_source_details"""

    spaces_data_source: Optional[APISpacesDataSource] = None
    """Spaces Bucket Data Source"""

    updated_at: Optional[datetime] = None
    """Last modified"""

    uuid: Optional[str] = None
    """Unique id of knowledge base"""

    web_crawler_data_source: Optional[APIWebCrawlerDataSource] = None
    """WebCrawlerDataSource"""
