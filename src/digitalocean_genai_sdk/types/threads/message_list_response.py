# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .message_object import MessageObject

__all__ = ["MessageListResponse"]


class MessageListResponse(BaseModel):
    data: List[MessageObject]

    first_id: str

    has_more: bool

    last_id: str

    object: str
