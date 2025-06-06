# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIAgentAPIKeyInfo"]


class APIAgentAPIKeyInfo(BaseModel):
    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    deleted_at: Optional[datetime] = None

    name: Optional[str] = None

    secret_key: Optional[str] = None

    uuid: Optional[str] = None
