# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["WorkspaceUpdateParams"]


class WorkspaceUpdateParams(TypedDict, total=False):
    description: str
    """The new description of the workspace"""

    name: str
    """The new name of the workspace"""

    body_workspace_uuid: Annotated[str, PropertyInfo(alias="workspace_uuid")]
    """Workspace UUID."""
