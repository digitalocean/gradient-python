# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIKeyUpdateParams"]


class APIKeyUpdateParams(TypedDict, total=False):
    body_api_key_uuid: Annotated[str, PropertyInfo(alias="api_key_uuid")]
    """API key ID"""

    name: str
    """Name"""
