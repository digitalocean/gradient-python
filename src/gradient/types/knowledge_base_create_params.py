# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .knowledge_bases.aws_data_source_param import AwsDataSourceParam
from .knowledge_bases.api_spaces_data_source_param import APISpacesDataSourceParam
from .knowledge_bases.api_file_upload_data_source_param import APIFileUploadDataSourceParam
from .knowledge_bases.api_web_crawler_data_source_param import APIWebCrawlerDataSourceParam

__all__ = [
    "KnowledgeBaseCreateParams",
    "Datasource",
    "DatasourceChunkingOptions",
    "DatasourceDropboxDataSource",
    "DatasourceGoogleDriveDataSource",
]


class KnowledgeBaseCreateParams(TypedDict, total=False):
    database_id: str
    """
    Identifier of the DigitalOcean OpenSearch database this knowledge base will use,
    optional. If not provided, we create a new database for the knowledge base in
    the same region as the knowledge base.
    """

    datasources: Iterable[Datasource]
    """The data sources to use for this knowledge base.

    See
    [Organize Data Sources](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#spaces-buckets)
    for more information on data sources best practices.
    """

    embedding_model_uuid: str
    """
    Identifier for the
    [embedding model](https://docs.digitalocean.com/products/genai-platform/details/models/#embedding-models).
    """

    name: str
    """Name of the knowledge base."""

    project_id: str
    """Identifier of the DigitalOcean project this knowledge base will belong to."""

    region: str
    """The datacenter region to deploy the knowledge base in."""

    tags: SequenceNotStr[str]
    """Tags to organize your knowledge base."""

    vpc_uuid: str
    """The VPC to deploy the knowledge base database in"""


class DatasourceChunkingOptions(TypedDict, total=False):
    """Configuration options for the chunking algorithm.

    **Note: This feature requires enabling the knowledgebase enhancements feature preview flag.**
    """

    child_chunk_size: int
    """Hierarchical options"""

    max_chunk_size: int
    """Section_Based and Fixed_Length options"""

    parent_chunk_size: int
    """Hierarchical options"""

    semantic_threshold: float
    """Semantic options"""


class DatasourceDropboxDataSource(TypedDict, total=False):
    """Dropbox Data Source"""

    folder: str

    refresh_token: str
    """Refresh token.

    you can obrain a refresh token by following the oauth2 flow. see
    /v2/gen-ai/oauth2/dropbox/tokens for reference.
    """


class DatasourceGoogleDriveDataSource(TypedDict, total=False):
    """Google Drive Data Source"""

    folder_id: str

    refresh_token: str
    """Refresh token.

    you can obrain a refresh token by following the oauth2 flow. see
    /v2/gen-ai/oauth2/google/tokens for reference.
    """


class Datasource(TypedDict, total=False):
    aws_data_source: AwsDataSourceParam
    """AWS S3 Data Source"""

    bucket_name: str
    """Deprecated, moved to data_source_details"""

    bucket_region: str
    """Deprecated, moved to data_source_details"""

    chunking_algorithm: Literal[
        "CHUNKING_ALGORITHM_UNKNOWN",
        "CHUNKING_ALGORITHM_SECTION_BASED",
        "CHUNKING_ALGORITHM_HIERARCHICAL",
        "CHUNKING_ALGORITHM_SEMANTIC",
        "CHUNKING_ALGORITHM_FIXED_LENGTH",
    ]
    """The chunking algorithm to use for processing data sources.

    **Note: This feature requires enabling the knowledgebase enhancements feature
    preview flag.**
    """

    chunking_options: DatasourceChunkingOptions
    """Configuration options for the chunking algorithm.

    **Note: This feature requires enabling the knowledgebase enhancements feature
    preview flag.**
    """

    dropbox_data_source: DatasourceDropboxDataSource
    """Dropbox Data Source"""

    file_upload_data_source: APIFileUploadDataSourceParam
    """File to upload as data source for knowledge base."""

    google_drive_data_source: DatasourceGoogleDriveDataSource
    """Google Drive Data Source"""

    item_path: str

    spaces_data_source: APISpacesDataSourceParam
    """Spaces Bucket Data Source"""

    web_crawler_data_source: APIWebCrawlerDataSourceParam
    """WebCrawlerDataSource"""
