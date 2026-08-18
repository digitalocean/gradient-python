# Response type for the Responses API (POST /v1/responses). See docs/RESPONSES_API_PR_BREAKDOWN.md.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..shared.completion_usage import CompletionUsage

__all__ = [
    "ResponseCreateResponse",
    "ResponseOutputItem",
    "ResponseOutputMessage",
    "ResponseOutputFunctionCall",
]


class ResponseOutputMessage(BaseModel):
    """Message item in the response output list."""

    type: Literal["message"] = "message"
    role: Literal["assistant"] = "assistant"
    content: Optional[str] = None
    """Text content of the message."""
    output_text: Optional[str] = None
    """Aggregated or final text for this item (when present)."""


class ResponseOutputFunctionCall(BaseModel):
    """Function call item in the response output list."""

    type: Literal["function_call"] = "function_call"
    id: str
    name: str
    arguments: str


# Discriminated union so Pydantic parses each output item by "type".
ResponseOutputItem: TypeAlias = Annotated[
    Union[ResponseOutputMessage, ResponseOutputFunctionCall],
    PropertyInfo(discriminator="type"),
]


class ResponseCreateResponse(BaseModel):
    """
    Response from POST /v1/responses.
    Use the `output_text` property to get aggregated text from message items in `output`.
    """

    id: str
    """Unique identifier for the response."""

    output: List[ResponseOutputItem]
    """List of output items (messages, function calls)."""

    status: str
    """Status of the response (e.g. completed, failed)."""

    error: Optional[str] = None
    """Error message if status indicates failure."""

    model: Optional[str] = None
    """Model used for the response."""

    usage: Optional[CompletionUsage] = None
    """Token usage statistics."""

    @property
    def output_text(self) -> str:
        """
        Aggregate text from all message items in `output`.
        For each item with type "message", uses `output_text` if present, else `content`.
        """
        parts: List[str] = []
        for item in self.output:
            if isinstance(item, ResponseOutputMessage):
                text: Optional[str] = item.output_text if item.output_text is not None else item.content
                if text:
                    parts.append(text)
        return "".join(parts)
