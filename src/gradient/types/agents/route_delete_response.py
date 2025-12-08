# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RouteDeleteResponse"]


class RouteDeleteResponse(BaseModel):
    """Information about a removed linkage"""

    child_agent_uuid: Optional[str] = None
    """Routed agent id"""

    parent_agent_uuid: Optional[str] = None
    """Pagent agent id"""
