# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .computer_tool_call_safety_check import ComputerToolCallSafetyCheck

__all__ = ["ComputerToolCallOutput", "Output"]


class Output(BaseModel):
    type: Literal["computer_screenshot"]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """

    file_id: Optional[str] = None
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: Optional[str] = None
    """The URL of the screenshot image."""


class ComputerToolCallOutput(BaseModel):
    call_id: str
    """The ID of the computer tool call that produced the output."""

    output: Output
    """A computer screenshot image used with the computer use tool."""

    type: Literal["computer_call_output"]
    """The type of the computer tool call output. Always `computer_call_output`."""

    id: Optional[str] = None
    """The ID of the computer tool call output."""

    acknowledged_safety_checks: Optional[List[ComputerToolCallSafetyCheck]] = None
    """
    The safety checks reported by the API that have been acknowledged by the
    developer.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """
