# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .api_deployment_visibility import APIDeploymentVisibility

__all__ = ["AgentUpdateStatusParams"]


class AgentUpdateStatusParams(TypedDict, total=False):
    body_uuid: Annotated[str, PropertyInfo(alias="uuid")]
    """Unique id"""

    visibility: APIDeploymentVisibility
    """
    - VISIBILITY_UNKNOWN: The status of the deployment is unknown
    - VISIBILITY_DISABLED: The deployment is disabled and will no longer service
      requests
    - VISIBILITY_PLAYGROUND: Deprecated: No longer a valid state
    - VISIBILITY_PUBLIC: The deployment is public and will service requests from the
      public internet
    - VISIBILITY_PRIVATE: The deployment is private and will only service requests
      from other agents, or through API keys
    """
