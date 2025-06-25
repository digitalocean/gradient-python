# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .aws_data_source_param import AwsDataSourceParam
from .api_spaces_data_source_param import APISpacesDataSourceParam
from .api_web_crawler_data_source_param import APIWebCrawlerDataSourceParam

__all__ = ["DataSourceCreateParams"]


class DataSourceCreateParams(TypedDict, total=False):
    aws_data_source: AwsDataSourceParam

    body_knowledge_base_uuid: Annotated[str, PropertyInfo(alias="knowledge_base_uuid")]

    spaces_data_source: APISpacesDataSourceParam

    web_crawler_data_source: APIWebCrawlerDataSourceParam
