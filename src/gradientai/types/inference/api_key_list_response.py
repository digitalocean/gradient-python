# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.api_meta import APIMeta
from ..shared.api_links import APILinks
from .api_model_api_key_info import APIModelAPIKeyInfo

__all__ = ["APIKeyListResponse"]


class APIKeyListResponse(BaseModel):
    api_key_infos: Optional[List[APIModelAPIKeyInfo]] = None
    """Api key infos"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""
