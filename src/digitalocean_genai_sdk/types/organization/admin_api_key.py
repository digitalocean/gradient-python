# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AdminAPIKey", "Owner"]


class Owner(BaseModel):
    id: Optional[str] = None

    created_at: Optional[int] = None

    name: Optional[str] = None

    role: Optional[str] = None

    type: Optional[str] = None


class AdminAPIKey(BaseModel):
    id: Optional[str] = None

    created_at: Optional[int] = None

    name: Optional[str] = None

    object: Optional[str] = None

    owner: Optional[Owner] = None

    redacted_value: Optional[str] = None

    value: Optional[str] = None
