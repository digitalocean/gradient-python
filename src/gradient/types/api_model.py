# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .api_agreement import APIAgreement
from .api_model_version import APIModelVersion

__all__ = ["APIModel"]


class APIModel(BaseModel):
    """A machine learning model stored on the GenAI platform"""

    id: Optional[str] = None
    """Human-readable model identifier"""

    agreement: Optional[APIAgreement] = None
    """Agreement Description"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    is_foundational: Optional[bool] = None
    """True if it is a foundational model provided by do"""

    name: Optional[str] = None
    """Display name of the model"""

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

    version: Optional[APIModelVersion] = None
    """Version Information about a Model"""
