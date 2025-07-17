# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ActionCreateParams", "FloatingIPActionUnassign", "FloatingIPActionAssign"]


class FloatingIPActionUnassign(TypedDict, total=False):
    type: Required[Literal["assign", "unassign"]]
    """The type of action to initiate for the floating IP."""


class FloatingIPActionAssign(TypedDict, total=False):
    droplet_id: Required[int]
    """The ID of the Droplet that the floating IP will be assigned to."""

    type: Required[Literal["assign", "unassign"]]
    """The type of action to initiate for the floating IP."""


ActionCreateParams: TypeAlias = Union[FloatingIPActionUnassign, FloatingIPActionAssign]
