# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    anthropic_key_uuid: str

    description: str

    instruction: str
    """Agent instruction.

    Instructions help your agent to perform its job effectively. See
    [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
    for best practices.
    """

    knowledge_base_uuid: List[str]

    model_uuid: str
    """Identifier for the foundation model."""

    name: str

    openai_key_uuid: Annotated[str, PropertyInfo(alias="open_ai_key_uuid")]

    project_id: str

    region: str

    tags: List[str]
