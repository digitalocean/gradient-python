# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["APIAnthropicAPIKeyInfo"]


class APIAnthropicAPIKeyInfo(BaseModel):
    """Anthropic API Key Info"""

    created_at: Optional[datetime] = None
    """Key creation date"""

    created_by: Optional[str] = None
    """Created by user id from DO"""

    deleted_at: Optional[datetime] = None
    """Key deleted date"""

    name: Optional[str] = None
    """Name"""

    updated_at: Optional[datetime] = None
    """Key last updated date"""

    uuid: Optional[str] = None
    """Uuid"""
