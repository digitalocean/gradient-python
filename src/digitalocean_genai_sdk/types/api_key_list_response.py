# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_agreement import APIAgreement
from .agents.api_meta import APIMeta
from .agents.api_links import APILinks
from .api_model_version import APIModelVersion

__all__ = ["APIKeyListResponse", "Model"]


class Model(BaseModel):
    agreement: Optional[APIAgreement] = None

    created_at: Optional[datetime] = None

    is_foundational: Optional[bool] = None

    name: Optional[str] = None

    parent_uuid: Optional[str] = None

    updated_at: Optional[datetime] = None

    upload_complete: Optional[bool] = None

    url: Optional[str] = None

    uuid: Optional[str] = None

    version: Optional[APIModelVersion] = None


class APIKeyListResponse(BaseModel):
    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None

    models: Optional[List[Model]] = None
