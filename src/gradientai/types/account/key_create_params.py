# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    A human-readable display name for this key, used to easily identify the SSH keys
    when they are displayed.
    """

    public_key: Required[str]
    """The entire public key string that was uploaded.

    Embedded into the root user's `authorized_keys` file if you include this key
    during Droplet creation.
    """
