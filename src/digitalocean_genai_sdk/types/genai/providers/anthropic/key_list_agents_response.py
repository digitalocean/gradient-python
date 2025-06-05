# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ....._compat import PYDANTIC_V2
from ....._models import BaseModel
from ...agents.api_meta import APIMeta
from ...agents.api_links import APILinks

__all__ = ["KeyListAgentsResponse"]


class KeyListAgentsResponse(BaseModel):
    agents: Optional[List["APIAgent"]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None


from ....shared.api_agent import APIAgent

if PYDANTIC_V2:
    KeyListAgentsResponse.model_rebuild()
else:
    KeyListAgentsResponse.update_forward_refs()  # type: ignore
