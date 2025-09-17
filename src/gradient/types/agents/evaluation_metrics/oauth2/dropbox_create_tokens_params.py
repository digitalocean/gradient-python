# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DropboxCreateTokensParams"]


class DropboxCreateTokensParams(TypedDict, total=False):
    code: str
    """The oauth2 code from google"""

    redirect_url: str
    """Redirect url"""
