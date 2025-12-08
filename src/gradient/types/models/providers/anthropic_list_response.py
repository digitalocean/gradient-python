# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.api_meta import APIMeta
from ...shared.api_links import APILinks
from ...api_anthropic_api_key_info import APIAnthropicAPIKeyInfo

__all__ = ["AnthropicListResponse"]


class AnthropicListResponse(BaseModel):
    """
    ListAnthropicAPIKeysOutput is used to return the list of Anthropic API keys for a specific agent.
    """

    api_key_infos: Optional[List[APIAnthropicAPIKeyInfo]] = None
    """Api key infos"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""
