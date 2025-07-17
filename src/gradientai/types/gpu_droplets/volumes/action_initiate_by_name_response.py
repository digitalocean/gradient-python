# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .volume_action import VolumeAction

__all__ = ["ActionInitiateByNameResponse"]


class ActionInitiateByNameResponse(BaseModel):
    action: Optional[VolumeAction] = None
