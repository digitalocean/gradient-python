# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .api_deployment_visibility import APIDeploymentVisibility

__all__ = ["DoagentUpdateStatusParams"]


class DoagentUpdateStatusParams(TypedDict, total=False):
    body_uuid: Annotated[str, PropertyInfo(alias="uuid")]

    visibility: APIDeploymentVisibility
