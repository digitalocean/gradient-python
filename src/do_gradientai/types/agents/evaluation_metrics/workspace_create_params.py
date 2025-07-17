# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["WorkspaceCreateParams"]


class WorkspaceCreateParams(TypedDict, total=False):
    agent_uuids: List[str]
    """Ids of the agents(s) to attach to the workspace"""

    description: str
    """Description of the workspace"""

    name: str
    """Name of the workspace"""
