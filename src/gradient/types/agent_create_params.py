# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    anthropic_key_uuid: str
    """Optional Anthropic API key ID to use with Anthropic models"""

    description: str
    """A text description of the agent, not used in inference"""

    instruction: str
    """Agent instruction.

    Instructions help your agent to perform its job effectively. See
    [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
    for best practices.
    """

    knowledge_base_uuid: SequenceNotStr[str]
    """Ids of the knowledge base(s) to attach to the agent"""

    model_provider_key_uuid: str

    model_uuid: str
    """Identifier for the foundation model."""

    name: str
    """Agent name"""

    openai_key_uuid: Annotated[str, PropertyInfo(alias="open_ai_key_uuid")]
    """Optional OpenAI API key ID to use with OpenAI models"""

    project_id: str
    """The id of the DigitalOcean project this agent will belong to"""

    region: str
    """The DigitalOcean region to deploy your agent in"""

    tags: SequenceNotStr[str]
    """Agent tag to organize related resources"""

    workspace_uuid: str
    """Identifier for the workspace"""
