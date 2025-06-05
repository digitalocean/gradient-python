# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FunctionCreateParams"]


class FunctionCreateParams(TypedDict, total=False):
    body_agent_uuid: Annotated[str, PropertyInfo(alias="agent_uuid")]

    description: str

    faas_name: str

    faas_namespace: str

    function_name: str

    input_schema: object

    output_schema: object
