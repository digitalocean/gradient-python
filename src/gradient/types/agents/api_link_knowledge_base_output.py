# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["APILinkKnowledgeBaseOutput"]


class APILinkKnowledgeBaseOutput(BaseModel):
    """Information about a linked knowledge base"""

    agent: Optional["APIAgent"] = None
    """An Agent"""


from ..api_agent import APIAgent
