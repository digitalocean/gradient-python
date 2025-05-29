# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .invite import Invite
from ..._models import BaseModel

__all__ = ["InviteListResponse"]


class InviteListResponse(BaseModel):
    data: List[Invite]

    object: Literal["list"]
    """The object type, which is always `list`"""

    first_id: Optional[str] = None
    """The first `invite_id` in the retrieved `list`"""

    has_more: Optional[bool] = None
    """
    The `has_more` property is used for pagination to indicate there are additional
    results.
    """

    last_id: Optional[str] = None
    """The last `invite_id` in the retrieved `list`"""
