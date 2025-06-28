# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from ...shared.api_meta import APIMeta
from ...shared.api_links import APILinks

__all__ = ["AnthropicListAgentsResponse"]


class AnthropicListAgentsResponse(BaseModel):
    agents: Optional[List["APIAgent"]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None


from ...api_agent import APIAgent
