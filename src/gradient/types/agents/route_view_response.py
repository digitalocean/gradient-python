# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RouteViewResponse"]


class RouteViewResponse(BaseModel):
    """Child list for an agent"""

    children: Optional[List["APIAgent"]] = None
    """Child agents"""


from ..api_agent import APIAgent
