# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_model import APIModel
from .doagents.api_meta import APIMeta
from .doagents.api_links import APILinks

__all__ = ["ModelListResponse"]


class ModelListResponse(BaseModel):
    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None

    models: Optional[List[APIModel]] = None
