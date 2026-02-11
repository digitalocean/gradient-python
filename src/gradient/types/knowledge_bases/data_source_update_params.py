# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DataSourceUpdateParams", "ChunkingOptions"]


class DataSourceUpdateParams(TypedDict, total=False):
    path_knowledge_base_uuid: Required[Annotated[str, PropertyInfo(alias="knowledge_base_uuid")]]

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

    body_data_source_uuid: Annotated[str, PropertyInfo(alias="data_source_uuid")]
    """Data Source ID (Path Parameter)"""

    body_knowledge_base_uuid: Annotated[str, PropertyInfo(alias="knowledge_base_uuid")]
    """Knowledge Base ID (Path Parameter)"""


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
