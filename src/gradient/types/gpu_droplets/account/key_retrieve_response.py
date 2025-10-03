# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .ssh_keys import SSHKeys
from ...._models import BaseModel

__all__ = ["KeyRetrieveResponse"]


class KeyRetrieveResponse(BaseModel):
    ssh_key: Optional[SSHKeys] = None
