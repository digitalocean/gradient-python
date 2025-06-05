# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_retrieval_method import APIRetrievalMethod

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    anthropic_key_uuid: str

    description: str

    instruction: str
    """Agent instruction.

    Instructions help your agent to perform its job effectively. See
    [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
    for best practices.
    """

    k: int

    max_tokens: int
    """
    Specifies the maximum number of tokens the model can process in a single input
    or output, set as a number between 1 and 512. This determines the length of each
    response.
    """

    model_uuid: str
    """Identifier for the foundation model."""

    name: str

    openai_key_uuid: Annotated[str, PropertyInfo(alias="open_ai_key_uuid")]

    project_id: str

    provide_citations: bool

    retrieval_method: APIRetrievalMethod

    tags: List[str]

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
