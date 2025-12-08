# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["DropboxCreateTokensResponse"]


class DropboxCreateTokensResponse(BaseModel):
    """The dropbox oauth2 token and refresh token"""

    token: Optional[str] = None
    """The access token"""

    refresh_token: Optional[str] = None
    """The refresh token"""
