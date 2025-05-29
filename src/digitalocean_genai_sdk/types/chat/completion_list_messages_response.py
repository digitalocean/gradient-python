# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .response_message import ResponseMessage

__all__ = ["CompletionListMessagesResponse", "Data"]


class Data(ResponseMessage):
    id: str
    """The identifier of the chat message."""


class CompletionListMessagesResponse(BaseModel):
    data: List[Data]
    """An array of chat completion message objects."""

    first_id: str
    """The identifier of the first chat message in the data array."""

    has_more: bool
    """Indicates whether there are more chat messages available."""

    last_id: str
    """The identifier of the last chat message in the data array."""

    object: Literal["list"]
    """The type of this object. It is always set to "list"."""
