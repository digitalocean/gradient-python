# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .project_user import ProjectUser
from .service_account import ServiceAccount

__all__ = ["APIKey", "Owner"]


class Owner(BaseModel):
    service_account: Optional[ServiceAccount] = None
    """Represents an individual service account in a project."""

    type: Optional[Literal["user", "service_account"]] = None
    """`user` or `service_account`"""

    user: Optional[ProjectUser] = None
    """Represents an individual user in a project."""


class APIKey(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints"""

    created_at: int
    """The Unix timestamp (in seconds) of when the API key was created"""

    name: str
    """The name of the API key"""

    object: Literal["organization.project.api_key"]
    """The object type, which is always `organization.project.api_key`"""

    owner: Owner

    redacted_value: str
    """The redacted value of the API key"""
