# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel

__all__ = ["WorkspaceUpdateResponse"]


class WorkspaceUpdateResponse(BaseModel):
    workspace: Optional["APIWorkspace"] = None


from ...api_workspace import APIWorkspace
