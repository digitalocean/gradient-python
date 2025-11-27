# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .ssh_keys import SSHKeys
from ...._models import BaseModel
from ...shared.page_links import PageLinks
from ...shared.meta_properties import MetaProperties

__all__ = ["KeyListResponse"]


class KeyListResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    links: Optional[PageLinks] = None

    ssh_keys: Optional[List[SSHKeys]] = None
