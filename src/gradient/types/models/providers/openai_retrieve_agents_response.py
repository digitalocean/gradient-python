# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from ...shared.api_meta import APIMeta
from ...shared.api_links import APILinks

__all__ = ["OpenAIRetrieveAgentsResponse"]


class OpenAIRetrieveAgentsResponse(BaseModel):
    """List of Agents that are linked to a specific OpenAI Key"""

    agents: Optional[List["APIAgent"]] = None

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""


from ...api_agent import APIAgent
