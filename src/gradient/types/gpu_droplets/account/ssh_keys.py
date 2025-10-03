# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SSHKeys"]


class SSHKeys(BaseModel):
    name: str
    """
    A human-readable display name for this key, used to easily identify the SSH keys
    when they are displayed.
    """

    public_key: str
    """The entire public key string that was uploaded.

    Embedded into the root user's `authorized_keys` file if you include this key
    during Droplet creation.
    """

    id: Optional[int] = None
    """A unique identification number for this key.

    Can be used to embed a specific SSH key into a Droplet.
    """

    fingerprint: Optional[str] = None
    """
    A unique identifier that differentiates this key from other keys using a format
    that SSH recognizes. The fingerprint is created when the key is added to your
    account.
    """
