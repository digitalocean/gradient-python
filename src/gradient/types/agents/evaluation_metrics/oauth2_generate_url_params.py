# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Oauth2GenerateURLParams"]


class Oauth2GenerateURLParams(TypedDict, total=False):
    redirect_url: str
    """The redirect url."""

    type: str
    """Type "google" / "dropbox"."""
