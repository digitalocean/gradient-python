# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.action import Action

__all__ = ["ActionInitiateResponse"]


class ActionInitiateResponse(BaseModel):
    action: Optional[Action] = None
