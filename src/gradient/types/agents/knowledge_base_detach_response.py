# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["KnowledgeBaseDetachResponse"]


class KnowledgeBaseDetachResponse(BaseModel):
    """Informatinon about a unlinked knowledge base"""

    agent: Optional["APIAgent"] = None
    """An Agent"""


from ..api_agent import APIAgent
