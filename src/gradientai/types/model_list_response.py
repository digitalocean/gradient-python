# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .model import Model
from .._models import BaseModel
from .agents.api_meta import APIMeta
from .agents.api_links import APILinks

__all__ = ["ModelListResponse"]


class ModelListResponse(BaseModel):
    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None

    models: Optional[List[Model]] = None
