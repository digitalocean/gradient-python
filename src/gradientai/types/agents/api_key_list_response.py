# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.api_meta import APIMeta
from ..shared.api_links import APILinks
from ..api_agent_api_key_info import APIAgentAPIKeyInfo

__all__ = ["APIKeyListResponse"]


class APIKeyListResponse(BaseModel):
    api_key_infos: Optional[List[APIAgentAPIKeyInfo]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None
