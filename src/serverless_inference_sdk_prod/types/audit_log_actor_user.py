# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuditLogActorUser"]


class AuditLogActorUser(BaseModel):
    id: Optional[str] = None
    """The user id."""

    email: Optional[str] = None
    """The user email."""
