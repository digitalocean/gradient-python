# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FunctionUpdateParams"]


class FunctionUpdateParams(TypedDict, total=False):
    path_agent_uuid: Required[Annotated[str, PropertyInfo(alias="agent_uuid")]]

    body_agent_uuid: Annotated[str, PropertyInfo(alias="agent_uuid")]

    description: str

    faas_name: str

    faas_namespace: str

    function_name: str

    body_function_uuid: Annotated[str, PropertyInfo(alias="function_uuid")]

    input_schema: object

    output_schema: object
