# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .api_knowledge_base_data_source import APIKnowledgeBaseDataSource

__all__ = ["DataSourceCreateResponse"]


class DataSourceCreateResponse(BaseModel):
    """Information about a newly created knowldege base data source"""

    knowledge_base_data_source: Optional[APIKnowledgeBaseDataSource] = None
    """Data Source configuration for Knowledge Bases"""
