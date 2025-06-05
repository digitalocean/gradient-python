# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ChildAgentUpdateResponse"]


class ChildAgentUpdateResponse(BaseModel):
    child_agent_uuid: Optional[str] = None

    parent_agent_uuid: Optional[str] = None
    """A unique identifier for the parent agent."""

    rollback: Optional[bool] = None

    uuid: Optional[str] = None
