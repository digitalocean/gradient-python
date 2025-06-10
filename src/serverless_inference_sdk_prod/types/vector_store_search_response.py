# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreSearchResponse", "Data", "DataContent"]


class DataContent(BaseModel):
    text: str
    """The text content returned from search."""

    type: Literal["text"]
    """The type of content."""


class Data(BaseModel):
    attributes: Optional[Dict[str, Union[str, float, bool]]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    content: List[DataContent]
    """Content chunks from the file."""

    file_id: str
    """The ID of the vector store file."""

    filename: str
    """The name of the vector store file."""

    score: float
    """The similarity score for the result."""


class VectorStoreSearchResponse(BaseModel):
    data: List[Data]
    """The list of search result items."""

    has_more: bool
    """Indicates if there are more results to fetch."""

    next_page: Optional[str] = None
    """The token for the next page, if any."""

    object: Literal["vector_store.search_results.page"]
    """The object type, which is always `vector_store.search_results.page`"""

    search_query: List[str]
