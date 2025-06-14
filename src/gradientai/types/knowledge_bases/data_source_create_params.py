# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_spaces_data_source_param import APISpacesDataSourceParam
from .api_web_crawler_data_source_param import APIWebCrawlerDataSourceParam

__all__ = ["DataSourceCreateParams", "AwsDataSource"]


class DataSourceCreateParams(TypedDict, total=False):
    aws_data_source: AwsDataSource

    body_knowledge_base_uuid: Annotated[str, PropertyInfo(alias="knowledge_base_uuid")]

    spaces_data_source: APISpacesDataSourceParam

    web_crawler_data_source: APIWebCrawlerDataSourceParam


class AwsDataSource(TypedDict, total=False):
    bucket_name: str

    item_path: str

    key_id: str

    region: str

    secret_key: str
