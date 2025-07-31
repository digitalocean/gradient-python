# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIKeyUpdateParams"]


class APIKeyUpdateParams(TypedDict, total=False):
    path_agent_uuid: Required[Annotated[str, PropertyInfo(alias="agent_uuid")]]

    body_agent_uuid: Annotated[str, PropertyInfo(alias="agent_uuid")]
    """Agent id"""

    body_api_key_uuid: Annotated[str, PropertyInfo(alias="api_key_uuid")]
    """API key ID"""

    name: str
    """Name"""
