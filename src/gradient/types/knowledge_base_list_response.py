# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.api_meta import APIMeta
from .shared.api_links import APILinks
from .api_knowledge_base import APIKnowledgeBase

__all__ = ["KnowledgeBaseListResponse"]


class KnowledgeBaseListResponse(BaseModel):
    """List of knowledge bases"""

    knowledge_bases: Optional[List[APIKnowledgeBase]] = None
    """The knowledge bases"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""
