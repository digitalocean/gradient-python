# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ...shared.api_meta import APIMeta
from ...shared.api_links import APILinks

__all__ = ["ModelListResponse", "Model", "ModelAgreement", "ModelVersion"]


class ModelAgreement(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    url: Optional[str] = None

    uuid: Optional[str] = None


class ModelVersion(BaseModel):
    major: Optional[int] = None
    """Major version number"""

    minor: Optional[int] = None
    """Minor version number"""

    patch: Optional[int] = None
    """Patch version number"""


class Model(BaseModel):
    agreement: Optional[ModelAgreement] = None
    """Agreement Description"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    is_foundational: Optional[bool] = None
    """True if it is a foundational model provided by do"""

    name: Optional[str] = None
    """Name of the model"""

    parent_uuid: Optional[str] = None
    """Unique id of the model, this model is based on"""

    updated_at: Optional[datetime] = None
    """Last modified"""

    upload_complete: Optional[bool] = None
    """Model has been fully uploaded"""

    url: Optional[str] = None
    """Download url"""

    uuid: Optional[str] = None
    """Unique id"""

    version: Optional[ModelVersion] = None
    """Version Information about a Model"""


class ModelListResponse(BaseModel):
    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""

    models: Optional[List[Model]] = None
    """The models"""
