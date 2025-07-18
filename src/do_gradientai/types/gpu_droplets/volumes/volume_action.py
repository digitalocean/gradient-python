# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...shared.action import Action

__all__ = ["VolumeAction"]


class VolumeAction(Action):
    resource_id: Optional[int] = None  # type: ignore

    type: Optional[str] = None  # type: ignore
    """This is the type of action that the object represents.

    For example, this could be "attach_volume" to represent the state of a volume
    attach action.
    """
