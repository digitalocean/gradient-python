# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .chat.usage import Usage

__all__ = ["CompletionCreateResponse", "Choice", "ChoiceLogprobs"]


class ChoiceLogprobs(BaseModel):
    text_offset: Optional[List[int]] = None

    token_logprobs: Optional[List[float]] = None

    tokens: Optional[List[str]] = None

    top_logprobs: Optional[List[Dict[str, float]]] = None


class Choice(BaseModel):
    finish_reason: Literal["stop", "length", "content_filter"]
    """The reason the model stopped generating tokens.

    This will be `stop` if the model hit a natural stop point or a provided stop
    sequence, `length` if the maximum number of tokens specified in the request was
    reached, or `content_filter` if content was omitted due to a flag from our
    content filters.
    """

    index: int

    logprobs: Optional[ChoiceLogprobs] = None

    text: str


class CompletionCreateResponse(BaseModel):
    id: str
    """A unique identifier for the completion."""

    choices: List[Choice]
    """The list of completion choices the model generated for the input prompt."""

    created: int
    """The Unix timestamp (in seconds) of when the completion was created."""

    model: str
    """The model used for completion."""

    object: Literal["text_completion"]
    """The object type, which is always "text_completion" """

    system_fingerprint: Optional[str] = None
    """This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """

    usage: Optional[Usage] = None
    """Usage statistics for the completion request."""
