# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .doagents.api_meta import APIMeta
from .api_knowledge_base import APIKnowledgeBase
from .doagents.api_links import APILinks

__all__ = ["KnowledgeBaseListResponse"]


class KnowledgeBaseListResponse(BaseModel):
    knowledge_bases: Optional[List[APIKnowledgeBase]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None
