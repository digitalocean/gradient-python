# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .api_agreement import APIAgreement
from .api_model_version import APIModelVersion

__all__ = ["APIModel"]


class APIModel(BaseModel):
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
