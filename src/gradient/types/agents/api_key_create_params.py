# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    body_agent_uuid: Annotated[str, PropertyInfo(alias="agent_uuid")]
    """Agent id"""

    name: str
    """A human friendly name to identify the key"""
