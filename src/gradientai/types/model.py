# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Model", "Agreement", "Version"]


class Agreement(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    url: Optional[str] = None

    uuid: Optional[str] = None


class Version(BaseModel):
    major: Optional[int] = None

    minor: Optional[int] = None

    patch: Optional[int] = None


class Model(BaseModel):
    agreement: Optional[Agreement] = None

    created_at: Optional[datetime] = None

    is_foundational: Optional[bool] = None

    name: Optional[str] = None

    parent_uuid: Optional[str] = None

    updated_at: Optional[datetime] = None

    upload_complete: Optional[bool] = None

    url: Optional[str] = None

    uuid: Optional[str] = None

    version: Optional[Version] = None
