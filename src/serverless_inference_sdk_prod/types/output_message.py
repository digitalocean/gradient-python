# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "OutputMessage",
    "Content",
    "ContentOutputText",
    "ContentOutputTextAnnotation",
    "ContentOutputTextAnnotationFileCitation",
    "ContentOutputTextAnnotationURLCitation",
    "ContentOutputTextAnnotationFilePath",
    "ContentRefusal",
]


class ContentOutputTextAnnotationFileCitation(BaseModel):
    file_id: str
    """The ID of the file."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_citation"]
    """The type of the file citation. Always `file_citation`."""


class ContentOutputTextAnnotationURLCitation(BaseModel):
    end_index: int
    """The index of the last character of the URL citation in the message."""

    start_index: int
    """The index of the first character of the URL citation in the message."""

    title: str
    """The title of the web resource."""

    type: Literal["url_citation"]
    """The type of the URL citation. Always `url_citation`."""

    url: str
    """The URL of the web resource."""


class ContentOutputTextAnnotationFilePath(BaseModel):
    file_id: str
    """The ID of the file."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_path"]
    """The type of the file path. Always `file_path`."""


ContentOutputTextAnnotation: TypeAlias = Union[
    ContentOutputTextAnnotationFileCitation, ContentOutputTextAnnotationURLCitation, ContentOutputTextAnnotationFilePath
]


class ContentOutputText(BaseModel):
    annotations: List[ContentOutputTextAnnotation]
    """The annotations of the text output."""

    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class ContentRefusal(BaseModel):
    refusal: str
    """The refusal explanationfrom the model."""

    type: Literal["refusal"]
    """The type of the refusal. Always `refusal`."""


Content: TypeAlias = Union[ContentOutputText, ContentRefusal]


class OutputMessage(BaseModel):
    id: str
    """The unique ID of the output message."""

    content: List[Content]
    """The content of the output message."""

    role: Literal["assistant"]
    """The role of the output message. Always `assistant`."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """

    type: Literal["message"]
    """The type of the output message. Always `message`."""
