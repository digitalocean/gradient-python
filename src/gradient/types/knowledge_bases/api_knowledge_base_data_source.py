# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .api_spaces_data_source import APISpacesDataSource
from .api_indexed_data_source import APIIndexedDataSource
from .api_file_upload_data_source import APIFileUploadDataSource
from .api_web_crawler_data_source import APIWebCrawlerDataSource

__all__ = [
    "APIKnowledgeBaseDataSource",
    "AwsDataSource",
    "ChunkingOptions",
    "DropboxDataSource",
    "GoogleDriveDataSource",
]


class AwsDataSource(BaseModel):
    """AWS S3 Data Source for Display"""

    bucket_name: Optional[str] = None
    """Spaces bucket name"""

    item_path: Optional[str] = None

    region: Optional[str] = None
    """Region of bucket"""


class ChunkingOptions(BaseModel):
    """Configuration options for the chunking algorithm.

    **Note: This feature requires enabling the knowledgebase enhancements feature preview flag.**
    """

    child_chunk_size: Optional[int] = None
    """Hierarchical options"""

    max_chunk_size: Optional[int] = None
    """Section_Based and Fixed_Length options"""

    parent_chunk_size: Optional[int] = None
    """Hierarchical options"""

    semantic_threshold: Optional[float] = None
    """Semantic options"""


class DropboxDataSource(BaseModel):
    """Dropbox Data Source for Display"""

    folder: Optional[str] = None


class GoogleDriveDataSource(BaseModel):
    """Google Drive Data Source for Display"""

    folder_id: Optional[str] = None

    folder_name: Optional[str] = None
    """Name of the selected folder if available"""


class APIKnowledgeBaseDataSource(BaseModel):
    """Data Source configuration for Knowledge Bases"""

    aws_data_source: Optional[AwsDataSource] = None
    """AWS S3 Data Source for Display"""

    bucket_name: Optional[str] = None
    """Name of storage bucket - Deprecated, moved to data_source_details"""

    chunking_algorithm: Optional[
        Literal[
            "CHUNKING_ALGORITHM_UNKNOWN",
            "CHUNKING_ALGORITHM_SECTION_BASED",
            "CHUNKING_ALGORITHM_HIERARCHICAL",
            "CHUNKING_ALGORITHM_SEMANTIC",
            "CHUNKING_ALGORITHM_FIXED_LENGTH",
        ]
    ] = None
    """The chunking algorithm to use for processing data sources.

    **Note: This feature requires enabling the knowledgebase enhancements feature
    preview flag.**
    """

    chunking_options: Optional[ChunkingOptions] = None
    """Configuration options for the chunking algorithm.

    **Note: This feature requires enabling the knowledgebase enhancements feature
    preview flag.**
    """

    created_at: Optional[datetime] = None
    """Creation date / time"""

    dropbox_data_source: Optional[DropboxDataSource] = None
    """Dropbox Data Source for Display"""

    file_upload_data_source: Optional[APIFileUploadDataSource] = None
    """File to upload as data source for knowledge base."""

    google_drive_data_source: Optional[GoogleDriveDataSource] = None
    """Google Drive Data Source for Display"""

    item_path: Optional[str] = None
    """Path of folder or object in bucket - Deprecated, moved to data_source_details"""

    last_datasource_indexing_job: Optional[APIIndexedDataSource] = None

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
