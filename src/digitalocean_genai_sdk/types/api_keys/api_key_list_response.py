# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..agents.api_meta import APIMeta
from ..agents.api_links import APILinks
from .api_model_api_key_info import APIModelAPIKeyInfo

__all__ = ["APIKeyListResponse"]


class APIKeyListResponse(BaseModel):
    api_key_infos: Optional[List[APIModelAPIKeyInfo]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None
