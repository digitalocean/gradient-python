# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["WorkspaceListResponse"]


class WorkspaceListResponse(BaseModel):
    workspaces: Optional[List["APIWorkspace"]] = None
    """Workspaces"""


from ...api_workspace import APIWorkspace
