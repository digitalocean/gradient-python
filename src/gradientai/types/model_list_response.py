# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .agents.api_meta import APIMeta
from .agents.api_links import APILinks

__all__ = ["ModelListResponse", "Model", "ModelAgreement", "ModelVersion"]


class ModelAgreement(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    url: Optional[str] = None

    uuid: Optional[str] = None


class ModelVersion(BaseModel):
    major: Optional[int] = None

    minor: Optional[int] = None

    patch: Optional[int] = None


class Model(BaseModel):
    agreement: Optional[ModelAgreement] = None

    created_at: Optional[datetime] = None

    is_foundational: Optional[bool] = None

    name: Optional[str] = None

    parent_uuid: Optional[str] = None

    updated_at: Optional[datetime] = None

    upload_complete: Optional[bool] = None

    url: Optional[str] = None

    uuid: Optional[str] = None

    version: Optional[ModelVersion] = None


class ModelListResponse(BaseModel):
    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None

    models: Optional[List[Model]] = None
