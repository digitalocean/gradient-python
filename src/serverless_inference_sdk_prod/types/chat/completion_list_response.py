# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .create_response import CreateResponse

__all__ = ["CompletionListResponse"]


class CompletionListResponse(BaseModel):
    data: List[CreateResponse]
    """An array of chat completion objects."""

    first_id: str
    """The identifier of the first chat completion in the data array."""

    has_more: bool
    """Indicates whether there are more Chat Completions available."""

    last_id: str
    """The identifier of the last chat completion in the data array."""

    object: Literal["list"]
    """The type of this object. It is always set to "list"."""
