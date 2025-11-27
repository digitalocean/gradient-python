# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["DropboxCreateTokensResponse"]


class DropboxCreateTokensResponse(BaseModel):
    token: Optional[str] = None
    """The access token"""

    refresh_token: Optional[str] = None
    """The refresh token"""
