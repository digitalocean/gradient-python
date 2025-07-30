# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from ....shared.api_meta import APIMeta
from ....shared.api_links import APILinks
from ....api_openai_api_key_info import APIOpenAIAPIKeyInfo

__all__ = ["KeyListResponse"]


class KeyListResponse(BaseModel):
    api_key_infos: Optional[List[APIOpenAIAPIKeyInfo]] = None
    """Api key infos"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""
