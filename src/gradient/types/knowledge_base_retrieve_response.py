# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .api_knowledge_base import APIKnowledgeBase

__all__ = ["KnowledgeBaseRetrieveResponse"]


class KnowledgeBaseRetrieveResponse(BaseModel):
    """The knowledge base"""

    database_status: Optional[
        Literal[
            "CREATING",
            "ONLINE",
            "POWEROFF",
            "REBUILDING",
            "REBALANCING",
            "DECOMMISSIONED",
            "FORKING",
            "MIGRATING",
            "RESIZING",
            "RESTORING",
            "POWERING_ON",
            "UNHEALTHY",
        ]
    ] = None

    knowledge_base: Optional[APIKnowledgeBase] = None
    """Knowledgebase Description"""
