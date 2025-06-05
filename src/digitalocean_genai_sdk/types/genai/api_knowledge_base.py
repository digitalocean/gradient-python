# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .api_indexing_job import APIIndexingJob

__all__ = ["APIKnowledgeBase"]


class APIKnowledgeBase(BaseModel):
    added_to_agent_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    database_id: Optional[str] = None

    embedding_model_uuid: Optional[str] = None

    is_public: Optional[bool] = None

    last_indexing_job: Optional[APIIndexingJob] = None

    name: Optional[str] = None

    project_id: Optional[str] = None

    region: Optional[str] = None

    tags: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None

    uuid: Optional[str] = None
