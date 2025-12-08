# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..shared import region, droplet
from ..._models import BaseModel

__all__ = ["FloatingIP", "Droplet", "Region"]

Droplet: TypeAlias = Union[droplet.Droplet, Optional[object]]


class Region(region.Region):
    """The region that the floating IP is reserved to.

    When you query a floating IP, the entire region object will be returned.
    """

    pass


class FloatingIP(BaseModel):
    droplet: Optional[Droplet] = None
    """The Droplet that the floating IP has been assigned to.

    When you query a floating IP, if it is assigned to a Droplet, the entire Droplet
    object will be returned. If it is not assigned, the value will be null.

    Requires `droplet:read` scope.
    """

    ip: Optional[str] = None
    """The public IP address of the floating IP. It also serves as its identifier."""

    locked: Optional[bool] = None
    """
    A boolean value indicating whether or not the floating IP has pending actions
    preventing new ones from being submitted.
    """

    project_id: Optional[str] = None
    """The UUID of the project to which the reserved IP currently belongs.

    Requires `project:read` scope.
    """

    region: Optional[Region] = None
    """The region that the floating IP is reserved to.

    When you query a floating IP, the entire region object will be returned.
    """
