# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .computer_tool_call_safety_check import ComputerToolCallSafetyCheck

__all__ = [
    "ComputerToolCall",
    "Action",
    "ActionClick",
    "ActionDoubleClick",
    "ActionDrag",
    "ActionDragPath",
    "ActionKeyPress",
    "ActionMove",
    "ActionScreenshot",
    "ActionScroll",
    "ActionType",
    "ActionWait",
]


class ActionClick(BaseModel):
    button: Literal["left", "right", "wheel", "back", "forward"]
    """Indicates which mouse button was pressed during the click.

    One of `left`, `right`, `wheel`, `back`, or `forward`.
    """

    type: Literal["click"]
    """Specifies the event type.

    For a click action, this property is always set to `click`.
    """

    x: int
    """The x-coordinate where the click occurred."""

    y: int
    """The y-coordinate where the click occurred."""


class ActionDoubleClick(BaseModel):
    type: Literal["double_click"]
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: int
    """The x-coordinate where the double click occurred."""

    y: int
    """The y-coordinate where the double click occurred."""


class ActionDragPath(BaseModel):
    x: int
    """The x-coordinate."""

    y: int
    """The y-coordinate."""


class ActionDrag(BaseModel):
    path: List[ActionDragPath]
    """An array of coordinates representing the path of the drag action.

    Coordinates will appear as an array of objects, eg

    ```
    [

      { x: 100, y: 200 },
      { x: 200, y: 300 }
    ]
    ```
    """

    type: Literal["drag"]
    """Specifies the event type.

    For a drag action, this property is always set to `drag`.
    """


class ActionKeyPress(BaseModel):
    keys: List[str]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Literal["keypress"]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class ActionMove(BaseModel):
    type: Literal["move"]
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: int
    """The x-coordinate to move to."""

    y: int
    """The y-coordinate to move to."""


class ActionScreenshot(BaseModel):
    type: Literal["screenshot"]
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class ActionScroll(BaseModel):
    scroll_x: int
    """The horizontal scroll distance."""

    scroll_y: int
    """The vertical scroll distance."""

    type: Literal["scroll"]
    """Specifies the event type.

    For a scroll action, this property is always set to `scroll`.
    """

    x: int
    """The x-coordinate where the scroll occurred."""

    y: int
    """The y-coordinate where the scroll occurred."""


class ActionType(BaseModel):
    text: str
    """The text to type."""

    type: Literal["type"]
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class ActionWait(BaseModel):
    type: Literal["wait"]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


Action: TypeAlias = Union[
    ActionClick,
    ActionDoubleClick,
    ActionDrag,
    ActionKeyPress,
    ActionMove,
    ActionScreenshot,
    ActionScroll,
    ActionType,
    ActionWait,
]


class ComputerToolCall(BaseModel):
    id: str
    """The unique ID of the computer call."""

    action: Action
    """A click action."""

    call_id: str
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: List[ComputerToolCallSafetyCheck]
    """The pending safety checks for the computer call."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["computer_call"]
    """The type of the computer call. Always `computer_call`."""
