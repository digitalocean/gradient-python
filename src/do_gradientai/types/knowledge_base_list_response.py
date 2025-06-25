# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .agents.api_meta import APIMeta
from .agents.api_links import APILinks
from .api_knowledge_base import APIKnowledgeBase

__all__ = ["KnowledgeBaseListResponse"]


class KnowledgeBaseListResponse(BaseModel):
    knowledge_bases: Optional[List[APIKnowledgeBase]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None
