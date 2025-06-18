# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import TypedDict

from .knowledge_bases.api_spaces_data_source_param import APISpacesDataSourceParam
from .knowledge_bases.api_file_upload_data_source_param import APIFileUploadDataSourceParam
from .knowledge_bases.api_web_crawler_data_source_param import APIWebCrawlerDataSourceParam

__all__ = ["KnowledgeBaseCreateParams", "Datasource", "DatasourceAwsDataSource"]


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

    tags: List[str]
    """Tags to organize your knowledge base."""

    vpc_uuid: str


class DatasourceAwsDataSource(TypedDict, total=False):
    bucket_name: str

    item_path: str

    key_id: str

    region: str

    secret_key: str


class Datasource(TypedDict, total=False):
    aws_data_source: DatasourceAwsDataSource

    bucket_name: str

    bucket_region: str

    file_upload_data_source: APIFileUploadDataSourceParam
    """File to upload as data source for knowledge base."""

    item_path: str

    spaces_data_source: APISpacesDataSourceParam

    web_crawler_data_source: APIWebCrawlerDataSourceParam
