# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_agent_model import APIAgentModel

__all__ = ["APIOpenAIAPIKeyInfo"]


class APIOpenAIAPIKeyInfo(BaseModel):
    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    deleted_at: Optional[datetime] = None

    models: Optional[List[APIAgentModel]] = None

    name: Optional[str] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None
