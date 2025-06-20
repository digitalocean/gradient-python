# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..doagents.api_meta import APIMeta
from ..doagents.api_links import APILinks
from .api_knowledge_base_data_source import APIKnowledgeBaseDataSource

__all__ = ["DataSourceListResponse"]


class DataSourceListResponse(BaseModel):
    knowledge_base_data_sources: Optional[List[APIKnowledgeBaseDataSource]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None
