# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_model import APIModel
from .shared.api_meta import APIMeta
from .shared.api_links import APILinks

__all__ = ["ModelListResponse"]


class ModelListResponse(BaseModel):
    """A list of models"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""

    models: Optional[List[APIModel]] = None
    """The models"""
