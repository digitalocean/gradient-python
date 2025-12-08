# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RouteAddResponse"]


class RouteAddResponse(BaseModel):
    """Information about a newly linked agent"""

    child_agent_uuid: Optional[str] = None
    """Routed agent id"""

    parent_agent_uuid: Optional[str] = None
    """A unique identifier for the parent agent."""
