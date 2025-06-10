# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .input_content_param import InputContentParam

__all__ = ["InputMessageParam"]


class InputMessageParam(TypedDict, total=False):
    content: Required[Iterable[InputContentParam]]
    """
    A list of one or many input items to the model, containing different content
    types.
    """

    role: Required[Literal["user", "system", "developer"]]
    """The role of the message input. One of `user`, `system`, or `developer`."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["message"]
    """The type of the message input. Always set to `message`."""
