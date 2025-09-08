# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["AgentMoveParams"]


class AgentMoveParams(TypedDict, total=False):
    agent_uuids: SequenceNotStr[str]
    """Agent uuids"""

    body_workspace_uuid: Annotated[str, PropertyInfo(alias="workspace_uuid")]
    """Workspace uuid to move agents to"""
