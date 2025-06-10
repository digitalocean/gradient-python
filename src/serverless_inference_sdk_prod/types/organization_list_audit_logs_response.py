# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .audit_log_actor_user import AuditLogActorUser
from .audit_log_event_type import AuditLogEventType

__all__ = [
    "OrganizationListAuditLogsResponse",
    "Data",
    "DataActor",
    "DataActorAPIKey",
    "DataActorAPIKeyServiceAccount",
    "DataActorSession",
    "DataAPIKeyCreated",
    "DataAPIKeyCreatedData",
    "DataAPIKeyDeleted",
    "DataAPIKeyUpdated",
    "DataAPIKeyUpdatedChangesRequested",
    "DataInviteAccepted",
    "DataInviteDeleted",
    "DataInviteSent",
    "DataInviteSentData",
    "DataLoginFailed",
    "DataLogoutFailed",
    "DataOrganizationUpdated",
    "DataOrganizationUpdatedChangesRequested",
    "DataOrganizationUpdatedChangesRequestedSettings",
    "DataProject",
    "DataProjectArchived",
    "DataProjectCreated",
    "DataProjectCreatedData",
    "DataProjectUpdated",
    "DataProjectUpdatedChangesRequested",
    "DataRateLimitDeleted",
    "DataRateLimitUpdated",
    "DataRateLimitUpdatedChangesRequested",
    "DataServiceAccountCreated",
    "DataServiceAccountCreatedData",
    "DataServiceAccountDeleted",
    "DataServiceAccountUpdated",
    "DataServiceAccountUpdatedChangesRequested",
    "DataUserAdded",
    "DataUserAddedData",
    "DataUserDeleted",
    "DataUserUpdated",
    "DataUserUpdatedChangesRequested",
]


class DataActorAPIKeyServiceAccount(BaseModel):
    id: Optional[str] = None
    """The service account id."""


class DataActorAPIKey(BaseModel):
    id: Optional[str] = None
    """The tracking id of the API key."""

    service_account: Optional[DataActorAPIKeyServiceAccount] = None
    """The service account that performed the audit logged action."""

    type: Optional[Literal["user", "service_account"]] = None
    """The type of API key. Can be either `user` or `service_account`."""

    user: Optional[AuditLogActorUser] = None
    """The user who performed the audit logged action."""


class DataActorSession(BaseModel):
    ip_address: Optional[str] = None
    """The IP address from which the action was performed."""

    user: Optional[AuditLogActorUser] = None
    """The user who performed the audit logged action."""


class DataActor(BaseModel):
    api_key: Optional[DataActorAPIKey] = None
    """The API Key used to perform the audit logged action."""

    session: Optional[DataActorSession] = None
    """The session in which the audit logged action was performed."""

    type: Optional[Literal["session", "api_key"]] = None
    """The type of actor. Is either `session` or `api_key`."""


class DataAPIKeyCreatedData(BaseModel):
    scopes: Optional[List[str]] = None
    """A list of scopes allowed for the API key, e.g. `["api.model.request"]`"""


class DataAPIKeyCreated(BaseModel):
    id: Optional[str] = None
    """The tracking ID of the API key."""

    data: Optional[DataAPIKeyCreatedData] = None
    """The payload used to create the API key."""


class DataAPIKeyDeleted(BaseModel):
    id: Optional[str] = None
    """The tracking ID of the API key."""


class DataAPIKeyUpdatedChangesRequested(BaseModel):
    scopes: Optional[List[str]] = None
    """A list of scopes allowed for the API key, e.g. `["api.model.request"]`"""


class DataAPIKeyUpdated(BaseModel):
    id: Optional[str] = None
    """The tracking ID of the API key."""

    changes_requested: Optional[DataAPIKeyUpdatedChangesRequested] = None
    """The payload used to update the API key."""


class DataInviteAccepted(BaseModel):
    id: Optional[str] = None
    """The ID of the invite."""


class DataInviteDeleted(BaseModel):
    id: Optional[str] = None
    """The ID of the invite."""


class DataInviteSentData(BaseModel):
    email: Optional[str] = None
    """The email invited to the organization."""

    role: Optional[str] = None
    """The role the email was invited to be. Is either `owner` or `member`."""


class DataInviteSent(BaseModel):
    id: Optional[str] = None
    """The ID of the invite."""

    data: Optional[DataInviteSentData] = None
    """The payload used to create the invite."""


class DataLoginFailed(BaseModel):
    error_code: Optional[str] = None
    """The error code of the failure."""

    error_message: Optional[str] = None
    """The error message of the failure."""


class DataLogoutFailed(BaseModel):
    error_code: Optional[str] = None
    """The error code of the failure."""

    error_message: Optional[str] = None
    """The error message of the failure."""


class DataOrganizationUpdatedChangesRequestedSettings(BaseModel):
    threads_ui_visibility: Optional[str] = None
    """
    Visibility of the threads page which shows messages created with the Assistants
    API and Playground. One of `ANY_ROLE`, `OWNERS`, or `NONE`.
    """

    usage_dashboard_visibility: Optional[str] = None
    """
    Visibility of the usage dashboard which shows activity and costs for your
    organization. One of `ANY_ROLE` or `OWNERS`.
    """


class DataOrganizationUpdatedChangesRequested(BaseModel):
    description: Optional[str] = None
    """The organization description."""

    name: Optional[str] = None
    """The organization name."""

    settings: Optional[DataOrganizationUpdatedChangesRequestedSettings] = None

    title: Optional[str] = None
    """The organization title."""


class DataOrganizationUpdated(BaseModel):
    id: Optional[str] = None
    """The organization ID."""

    changes_requested: Optional[DataOrganizationUpdatedChangesRequested] = None
    """The payload used to update the organization settings."""


class DataProject(BaseModel):
    id: Optional[str] = None
    """The project ID."""

    name: Optional[str] = None
    """The project title."""


class DataProjectArchived(BaseModel):
    id: Optional[str] = None
    """The project ID."""


class DataProjectCreatedData(BaseModel):
    name: Optional[str] = None
    """The project name."""

    title: Optional[str] = None
    """The title of the project as seen on the dashboard."""


class DataProjectCreated(BaseModel):
    id: Optional[str] = None
    """The project ID."""

    data: Optional[DataProjectCreatedData] = None
    """The payload used to create the project."""


class DataProjectUpdatedChangesRequested(BaseModel):
    title: Optional[str] = None
    """The title of the project as seen on the dashboard."""


class DataProjectUpdated(BaseModel):
    id: Optional[str] = None
    """The project ID."""

    changes_requested: Optional[DataProjectUpdatedChangesRequested] = None
    """The payload used to update the project."""


class DataRateLimitDeleted(BaseModel):
    id: Optional[str] = None
    """The rate limit ID"""


class DataRateLimitUpdatedChangesRequested(BaseModel):
    batch_1_day_max_input_tokens: Optional[int] = None
    """The maximum batch input tokens per day. Only relevant for certain models."""

    max_audio_megabytes_per_1_minute: Optional[int] = None
    """The maximum audio megabytes per minute. Only relevant for certain models."""

    max_images_per_1_minute: Optional[int] = None
    """The maximum images per minute. Only relevant for certain models."""

    max_requests_per_1_day: Optional[int] = None
    """The maximum requests per day. Only relevant for certain models."""

    max_requests_per_1_minute: Optional[int] = None
    """The maximum requests per minute."""

    max_tokens_per_1_minute: Optional[int] = None
    """The maximum tokens per minute."""


class DataRateLimitUpdated(BaseModel):
    id: Optional[str] = None
    """The rate limit ID"""

    changes_requested: Optional[DataRateLimitUpdatedChangesRequested] = None
    """The payload used to update the rate limits."""


class DataServiceAccountCreatedData(BaseModel):
    role: Optional[str] = None
    """The role of the service account. Is either `owner` or `member`."""


class DataServiceAccountCreated(BaseModel):
    id: Optional[str] = None
    """The service account ID."""

    data: Optional[DataServiceAccountCreatedData] = None
    """The payload used to create the service account."""


class DataServiceAccountDeleted(BaseModel):
    id: Optional[str] = None
    """The service account ID."""


class DataServiceAccountUpdatedChangesRequested(BaseModel):
    role: Optional[str] = None
    """The role of the service account. Is either `owner` or `member`."""


class DataServiceAccountUpdated(BaseModel):
    id: Optional[str] = None
    """The service account ID."""

    changes_requested: Optional[DataServiceAccountUpdatedChangesRequested] = None
    """The payload used to updated the service account."""


class DataUserAddedData(BaseModel):
    role: Optional[str] = None
    """The role of the user. Is either `owner` or `member`."""


class DataUserAdded(BaseModel):
    id: Optional[str] = None
    """The user ID."""

    data: Optional[DataUserAddedData] = None
    """The payload used to add the user to the project."""


class DataUserDeleted(BaseModel):
    id: Optional[str] = None
    """The user ID."""


class DataUserUpdatedChangesRequested(BaseModel):
    role: Optional[str] = None
    """The role of the user. Is either `owner` or `member`."""


class DataUserUpdated(BaseModel):
    id: Optional[str] = None
    """The project ID."""

    changes_requested: Optional[DataUserUpdatedChangesRequested] = None
    """The payload used to update the user."""


class Data(BaseModel):
    id: str
    """The ID of this log."""

    actor: DataActor
    """The actor who performed the audit logged action."""

    effective_at: int
    """The Unix timestamp (in seconds) of the event."""

    type: AuditLogEventType
    """The event type."""

    api_key_created: Optional[DataAPIKeyCreated] = FieldInfo(alias="api_key.created", default=None)
    """The details for events with this `type`."""

    api_key_deleted: Optional[DataAPIKeyDeleted] = FieldInfo(alias="api_key.deleted", default=None)
    """The details for events with this `type`."""

    api_key_updated: Optional[DataAPIKeyUpdated] = FieldInfo(alias="api_key.updated", default=None)
    """The details for events with this `type`."""

    invite_accepted: Optional[DataInviteAccepted] = FieldInfo(alias="invite.accepted", default=None)
    """The details for events with this `type`."""

    invite_deleted: Optional[DataInviteDeleted] = FieldInfo(alias="invite.deleted", default=None)
    """The details for events with this `type`."""

    invite_sent: Optional[DataInviteSent] = FieldInfo(alias="invite.sent", default=None)
    """The details for events with this `type`."""

    login_failed: Optional[DataLoginFailed] = FieldInfo(alias="login.failed", default=None)
    """The details for events with this `type`."""

    logout_failed: Optional[DataLogoutFailed] = FieldInfo(alias="logout.failed", default=None)
    """The details for events with this `type`."""

    organization_updated: Optional[DataOrganizationUpdated] = FieldInfo(alias="organization.updated", default=None)
    """The details for events with this `type`."""

    project: Optional[DataProject] = None
    """The project that the action was scoped to.

    Absent for actions not scoped to projects.
    """

    project_archived: Optional[DataProjectArchived] = FieldInfo(alias="project.archived", default=None)
    """The details for events with this `type`."""

    project_created: Optional[DataProjectCreated] = FieldInfo(alias="project.created", default=None)
    """The details for events with this `type`."""

    project_updated: Optional[DataProjectUpdated] = FieldInfo(alias="project.updated", default=None)
    """The details for events with this `type`."""

    rate_limit_deleted: Optional[DataRateLimitDeleted] = FieldInfo(alias="rate_limit.deleted", default=None)
    """The details for events with this `type`."""

    rate_limit_updated: Optional[DataRateLimitUpdated] = FieldInfo(alias="rate_limit.updated", default=None)
    """The details for events with this `type`."""

    service_account_created: Optional[DataServiceAccountCreated] = FieldInfo(
        alias="service_account.created", default=None
    )
    """The details for events with this `type`."""

    service_account_deleted: Optional[DataServiceAccountDeleted] = FieldInfo(
        alias="service_account.deleted", default=None
    )
    """The details for events with this `type`."""

    service_account_updated: Optional[DataServiceAccountUpdated] = FieldInfo(
        alias="service_account.updated", default=None
    )
    """The details for events with this `type`."""

    user_added: Optional[DataUserAdded] = FieldInfo(alias="user.added", default=None)
    """The details for events with this `type`."""

    user_deleted: Optional[DataUserDeleted] = FieldInfo(alias="user.deleted", default=None)
    """The details for events with this `type`."""

    user_updated: Optional[DataUserUpdated] = FieldInfo(alias="user.updated", default=None)
    """The details for events with this `type`."""


class OrganizationListAuditLogsResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
