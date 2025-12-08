# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VersionUpdateResponse", "AuditHeader"]


class AuditHeader(BaseModel):
    """An alternative way to provide auth information. for internal use only."""

    actor_id: Optional[str] = None

    actor_ip: Optional[str] = None

    actor_uuid: Optional[str] = None

    context_urn: Optional[str] = None

    origin_application: Optional[str] = None

    user_id: Optional[str] = None

    user_uuid: Optional[str] = None


class VersionUpdateResponse(BaseModel):
    audit_header: Optional[AuditHeader] = None
    """An alternative way to provide auth information. for internal use only."""

    version_hash: Optional[str] = None
    """Unique identifier"""
