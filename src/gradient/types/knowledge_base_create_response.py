# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_knowledge_base import APIKnowledgeBase

__all__ = ["KnowledgeBaseCreateResponse"]


class KnowledgeBaseCreateResponse(BaseModel):
    """Information about a newly created knowledge base"""

    knowledge_base: Optional[APIKnowledgeBase] = None
    """Knowledgebase Description"""
