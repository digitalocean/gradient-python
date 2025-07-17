# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FunctionUpdateParams"]


class FunctionUpdateParams(TypedDict, total=False):
    path_agent_uuid: Required[Annotated[str, PropertyInfo(alias="agent_uuid")]]

    body_agent_uuid: Annotated[str, PropertyInfo(alias="agent_uuid")]
    """Agent id"""

    description: str
    """Funciton description"""

    faas_name: str
    """The name of the function in the DigitalOcean functions platform"""

    faas_namespace: str
    """The namespace of the function in the DigitalOcean functions platform"""

    function_name: str
    """Function name"""

    body_function_uuid: Annotated[str, PropertyInfo(alias="function_uuid")]
    """Function id"""

    input_schema: object
    """Describe the input schema for the function so the agent may call it"""

    output_schema: object
    """Describe the output schema for the function so the agent handle its response"""
