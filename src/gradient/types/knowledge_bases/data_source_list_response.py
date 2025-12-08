# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.api_meta import APIMeta
from ..shared.api_links import APILinks
from .api_knowledge_base_data_source import APIKnowledgeBaseDataSource

__all__ = ["DataSourceListResponse"]


class DataSourceListResponse(BaseModel):
    """A list of knowledge base data sources"""

    knowledge_base_data_sources: Optional[List[APIKnowledgeBaseDataSource]] = None
    """The data sources"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""
