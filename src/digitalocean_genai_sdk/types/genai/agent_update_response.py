# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["AgentUpdateResponse"]


class AgentUpdateResponse(BaseModel):
    agent: Optional["APIAgent"] = None


from .api_agent import APIAgent

if PYDANTIC_V2:
    AgentUpdateResponse.model_rebuild()
else:
    AgentUpdateResponse.update_forward_refs()  # type: ignore
