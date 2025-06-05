# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ChildAgentDeleteResponse"]


class ChildAgentDeleteResponse(BaseModel):
    child_agent_uuid: Optional[str] = None

    parent_agent_uuid: Optional[str] = None
