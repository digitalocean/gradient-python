# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...shared import action
from ...._models import BaseModel

__all__ = ["ActionRetrieveResponse", "Action"]


class Action(action.Action):
    project_id: Optional[str] = None
    """The UUID of the project to which the reserved IP currently belongs."""


class ActionRetrieveResponse(BaseModel):
    action: Optional[Action] = None
