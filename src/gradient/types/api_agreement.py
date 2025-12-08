# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["APIAgreement"]


class APIAgreement(BaseModel):
    """Agreement Description"""

    description: Optional[str] = None

    name: Optional[str] = None

    url: Optional[str] = None

    uuid: Optional[str] = None
