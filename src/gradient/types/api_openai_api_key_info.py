# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_agent_model import APIAgentModel

__all__ = ["APIOpenAIAPIKeyInfo"]


class APIOpenAIAPIKeyInfo(BaseModel):
    """OpenAI API Key Info"""

    created_at: Optional[datetime] = None
    """Key creation date"""

    created_by: Optional[str] = None
    """Created by user id from DO"""

    deleted_at: Optional[datetime] = None
    """Key deleted date"""

    models: Optional[List[APIAgentModel]] = None
    """Models supported by the openAI api key"""

    name: Optional[str] = None
    """Name"""

    updated_at: Optional[datetime] = None
    """Key last updated date"""

    uuid: Optional[str] = None
    """Uuid"""
