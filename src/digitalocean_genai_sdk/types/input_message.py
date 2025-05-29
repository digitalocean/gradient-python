# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .input_content import InputContent

__all__ = ["InputMessage"]


class InputMessage(BaseModel):
    content: List[InputContent]
    """
    A list of one or many input items to the model, containing different content
    types.
    """

    role: Literal["user", "system", "developer"]
    """The role of the message input. One of `user`, `system`, or `developer`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always set to `message`."""
