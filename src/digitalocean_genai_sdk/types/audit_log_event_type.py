# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AuditLogEventType"]

AuditLogEventType: TypeAlias = Literal[
    "api_key.created",
    "api_key.updated",
    "api_key.deleted",
    "invite.sent",
    "invite.accepted",
    "invite.deleted",
    "login.succeeded",
    "login.failed",
    "logout.succeeded",
    "logout.failed",
    "organization.updated",
    "project.created",
    "project.updated",
    "project.archived",
    "service_account.created",
    "service_account.updated",
    "service_account.deleted",
    "rate_limit.updated",
    "rate_limit.deleted",
    "user.added",
    "user.updated",
    "user.deleted",
]
