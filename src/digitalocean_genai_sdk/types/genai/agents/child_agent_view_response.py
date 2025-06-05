# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._compat import PYDANTIC_V2
from ...._models import BaseModel

__all__ = ["ChildAgentViewResponse"]


class ChildAgentViewResponse(BaseModel):
    children: Optional[List["APIAgent"]] = None


from ..api_agent import APIAgent

if PYDANTIC_V2:
    ChildAgentViewResponse.model_rebuild()
else:
    ChildAgentViewResponse.update_forward_refs()  # type: ignore
