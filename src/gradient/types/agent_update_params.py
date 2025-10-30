# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .api_retrieval_method import APIRetrievalMethod

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    agent_log_insights_enabled: bool

    allowed_domains: SequenceNotStr[str]
    """
    Optional list of allowed domains for the chatbot - Must use fully qualified
    domain name (FQDN) such as https://example.com
    """

    anthropic_key_uuid: str
    """Optional anthropic key uuid for use with anthropic models"""

    conversation_logs_enabled: bool
    """Optional update of conversation logs enabled"""

    description: str
    """Agent description"""

    instruction: str
    """Agent instruction.

    Instructions help your agent to perform its job effectively. See
    [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
    for best practices.
    """

    k: int
    """How many results should be considered from an attached knowledge base"""

    max_tokens: int
    """
    Specifies the maximum number of tokens the model can process in a single input
    or output, set as a number between 1 and 512. This determines the length of each
    response.
    """

    model_provider_key_uuid: str
    """Optional Model Provider uuid for use with provider models"""

    model_uuid: str
    """Identifier for the foundation model."""

    name: str
    """Agent name"""

    openai_key_uuid: Annotated[str, PropertyInfo(alias="open_ai_key_uuid")]
    """Optional OpenAI key uuid for use with OpenAI models"""

    project_id: str
    """The id of the DigitalOcean project this agent will belong to"""

    provide_citations: bool

    retrieval_method: APIRetrievalMethod
    """
    - RETRIEVAL_METHOD_UNKNOWN: The retrieval method is unknown
    - RETRIEVAL_METHOD_REWRITE: The retrieval method is rewrite
    - RETRIEVAL_METHOD_STEP_BACK: The retrieval method is step back
    - RETRIEVAL_METHOD_SUB_QUERIES: The retrieval method is sub queries
    - RETRIEVAL_METHOD_NONE: The retrieval method is none
    """

    tags: SequenceNotStr[str]
    """A set of abitrary tags to organize your agent"""

    temperature: float
    """Controls the model’s creativity, specified as a number between 0 and 1.

    Lower values produce more predictable and conservative responses, while higher
    values encourage creativity and variation.
    """

    top_p: float
    """
    Defines the cumulative probability threshold for word selection, specified as a
    number between 0 and 1. Higher values allow for more diverse outputs, while
    lower values ensure focused and coherent responses.
    """

    body_uuid: Annotated[str, PropertyInfo(alias="uuid")]
    """Unique agent id"""
