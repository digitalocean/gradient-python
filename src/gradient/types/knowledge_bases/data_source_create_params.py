# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from .aws_data_source_param import AwsDataSourceParam
from .api_spaces_data_source_param import APISpacesDataSourceParam
from .api_web_crawler_data_source_param import APIWebCrawlerDataSourceParam

__all__ = ["DataSourceCreateParams", "ChunkingOptions"]


class DataSourceCreateParams(TypedDict, total=False):
    aws_data_source: AwsDataSourceParam
    """AWS S3 Data Source"""

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

    chunking_options: ChunkingOptions
    """Configuration options for the chunking algorithm.

    **Note: This feature requires enabling the knowledgebase enhancements feature
    preview flag.**
    """

    body_knowledge_base_uuid: Annotated[str, PropertyInfo(alias="knowledge_base_uuid")]
    """Knowledge base id"""

    spaces_data_source: APISpacesDataSourceParam
    """Spaces Bucket Data Source"""

    web_crawler_data_source: APIWebCrawlerDataSourceParam
    """WebCrawlerDataSource"""


class ChunkingOptions(TypedDict, total=False):
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
