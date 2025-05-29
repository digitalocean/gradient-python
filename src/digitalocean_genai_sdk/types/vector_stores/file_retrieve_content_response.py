# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileRetrieveContentResponse", "Data"]


class Data(BaseModel):
    text: Optional[str] = None
    """The text content"""

    type: Optional[str] = None
    """The content type (currently only `"text"`)"""


class FileRetrieveContentResponse(BaseModel):
    data: List[Data]
    """Parsed content of the file."""

    has_more: bool
    """Indicates if there are more content pages to fetch."""

    next_page: Optional[str] = None
    """The token for the next page, if any."""

    object: Literal["vector_store.file_content.page"]
    """The object type, which is always `vector_store.file_content.page`"""
