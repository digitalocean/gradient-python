# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["WorkspaceCreateParams"]


class WorkspaceCreateParams(TypedDict, total=False):
    agent_uuids: SequenceNotStr[str]
    """Ids of the agents(s) to attach to the workspace"""

    description: str
    """Description of the workspace"""

    name: str
    """Name of the workspace"""
