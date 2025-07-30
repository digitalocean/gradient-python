# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["FloatingIPCreateParams", "AssignToDroplet", "ReserveToRegion"]


class AssignToDroplet(TypedDict, total=False):
    droplet_id: Required[int]
    """The ID of the Droplet that the floating IP will be assigned to."""


class ReserveToRegion(TypedDict, total=False):
    region: Required[str]
    """The slug identifier for the region the floating IP will be reserved to."""

    project_id: str
    """The UUID of the project to which the floating IP will be assigned."""


FloatingIPCreateParams: TypeAlias = Union[AssignToDroplet, ReserveToRegion]
