# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.action import Action

__all__ = ["ActionBulkInitiateResponse"]


class ActionBulkInitiateResponse(BaseModel):
    actions: Optional[List[Action]] = None
