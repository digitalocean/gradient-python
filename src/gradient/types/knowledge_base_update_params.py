# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["KnowledgeBaseUpdateParams"]


class KnowledgeBaseUpdateParams(TypedDict, total=False):
    database_id: str
    """The id of the DigitalOcean database this knowledge base will use, optiona."""

    embedding_model_uuid: str
    """Identifier for the foundation model."""

    name: str
    """Knowledge base name"""

    project_id: str
    """The id of the DigitalOcean project this knowledge base will belong to"""

    tags: SequenceNotStr[str]
    """Tags to organize your knowledge base."""

    body_uuid: Annotated[str, PropertyInfo(alias="uuid")]
    """Knowledge base id"""
