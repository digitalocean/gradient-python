# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .knowledge_bases.api_indexing_job import APIIndexingJob

__all__ = ["APIKnowledgeBase"]


class APIKnowledgeBase(BaseModel):
    """Knowledgebase Description"""

    added_to_agent_at: Optional[datetime] = None
    """Time when the knowledge base was added to the agent"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    database_id: Optional[str] = None

    embedding_model_uuid: Optional[str] = None

    is_public: Optional[bool] = None
    """Whether the knowledge base is public or not"""

    last_indexing_job: Optional[APIIndexingJob] = None
    """IndexingJob description"""

    name: Optional[str] = None
    """Name of knowledge base"""

    project_id: Optional[str] = None

    region: Optional[str] = None
    """Region code"""

    tags: Optional[List[str]] = None
    """Tags to organize related resources"""

    updated_at: Optional[datetime] = None
    """Last modified"""

    user_id: Optional[str] = None
    """Id of user that created the knowledge base"""

    uuid: Optional[str] = None
    """Unique id for knowledge base"""
