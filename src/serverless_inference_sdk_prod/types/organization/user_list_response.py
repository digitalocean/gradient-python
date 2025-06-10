# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .user import User
from ..._models import BaseModel

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    data: List[User]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
