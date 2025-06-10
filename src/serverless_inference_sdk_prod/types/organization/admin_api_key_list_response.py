# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .admin_api_key import AdminAPIKey

__all__ = ["AdminAPIKeyListResponse"]


class AdminAPIKeyListResponse(BaseModel):
    data: Optional[List[AdminAPIKey]] = None

    first_id: Optional[str] = None

    has_more: Optional[bool] = None

    last_id: Optional[str] = None

    object: Optional[str] = None
