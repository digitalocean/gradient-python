# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .computer_tool_call_safety_check_param import ComputerToolCallSafetyCheckParam

__all__ = ["ComputerToolCallOutputParam", "Output"]


class Output(TypedDict, total=False):
    type: Required[Literal["computer_screenshot"]]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """

    file_id: str
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: str
    """The URL of the screenshot image."""


class ComputerToolCallOutputParam(TypedDict, total=False):
    call_id: Required[str]
    """The ID of the computer tool call that produced the output."""

    output: Required[Output]
    """A computer screenshot image used with the computer use tool."""

    type: Required[Literal["computer_call_output"]]
    """The type of the computer tool call output. Always `computer_call_output`."""

    id: str
    """The ID of the computer tool call output."""

    acknowledged_safety_checks: Iterable[ComputerToolCallSafetyCheckParam]
    """
    The safety checks reported by the API that have been acknowledged by the
    developer.
    """

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """
