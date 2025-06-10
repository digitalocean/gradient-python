# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .project_user import ProjectUser

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    data: List[ProjectUser]

    first_id: str

    has_more: bool

    last_id: str

    object: str
