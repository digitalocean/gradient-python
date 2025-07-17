# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse", "Account", "AccountTeam"]


class AccountTeam(BaseModel):
    name: Optional[str] = None
    """The name for the current team."""

    uuid: Optional[str] = None
    """The unique universal identifier for the current team."""


class Account(BaseModel):
    droplet_limit: int
    """The total number of Droplets current user or team may have active at one time.

    Requires `droplet:read` scope.
    """

    email: str
    """The email address used by the current user to register for DigitalOcean."""

    email_verified: bool
    """If true, the user has verified their account via email. False otherwise."""

    floating_ip_limit: int
    """The total number of Floating IPs the current user or team may have.

    Requires `reserved_ip:read` scope.
    """

    status: Literal["active", "warning", "locked"]
    """This value is one of "active", "warning" or "locked"."""

    status_message: str
    """A human-readable message giving more details about the status of the account."""

    uuid: str
    """The unique universal identifier for the current user."""

    name: Optional[str] = None
    """The display name for the current user."""

    team: Optional[AccountTeam] = None
    """When authorized in a team context, includes information about the current team."""


class AccountRetrieveResponse(BaseModel):
    account: Optional[Account] = None
