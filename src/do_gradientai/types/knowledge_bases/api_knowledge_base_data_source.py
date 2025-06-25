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

    item_path: Optional[str] = None

    region: Optional[str] = None


class APIKnowledgeBaseDataSource(BaseModel):
    aws_data_source: Optional[AwsDataSource] = None

    bucket_name: Optional[str] = None

    created_at: Optional[datetime] = None

    file_upload_data_source: Optional[APIFileUploadDataSource] = None
    """File to upload as data source for knowledge base."""

    item_path: Optional[str] = None

    last_datasource_indexing_job: Optional[APIIndexedDataSource] = None

    last_indexing_job: Optional[APIIndexingJob] = None

    region: Optional[str] = None

    spaces_data_source: Optional[APISpacesDataSource] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

    web_crawler_data_source: Optional[APIWebCrawlerDataSource] = None
