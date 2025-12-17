# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["RetrieveDocumentsResponse", "Result"]


class Result(BaseModel):
    metadata: Dict[str, object]
    """Metadata associated with the document"""

    text_content: str
    """The text content of the document chunk"""


class RetrieveDocumentsResponse(BaseModel):
    results: List[Result]
    """Array of retrieved document chunks"""

    total_results: int
    """Number of results returned"""
