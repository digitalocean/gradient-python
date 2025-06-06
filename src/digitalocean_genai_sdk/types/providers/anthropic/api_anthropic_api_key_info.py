# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["APIAnthropicAPIKeyInfo"]


class APIAnthropicAPIKeyInfo(BaseModel):
    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    deleted_at: Optional[datetime] = None

    name: Optional[str] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None
