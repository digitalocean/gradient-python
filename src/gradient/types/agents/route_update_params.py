# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RouteUpdateParams"]


class RouteUpdateParams(TypedDict, total=False):
    path_parent_agent_uuid: Required[Annotated[str, PropertyInfo(alias="parent_agent_uuid")]]

    body_child_agent_uuid: Annotated[str, PropertyInfo(alias="child_agent_uuid")]
    """Routed agent id"""

    if_case: str
    """Describes the case in which the child agent should be used"""

    body_parent_agent_uuid: Annotated[str, PropertyInfo(alias="parent_agent_uuid")]
    """A unique identifier for the parent agent."""

    route_name: str
    """Route name"""

    uuid: str
    """Unique id of linkage"""
