# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "OutputMessageParam",
    "Content",
    "ContentOutputText",
    "ContentOutputTextAnnotation",
    "ContentOutputTextAnnotationFileCitation",
    "ContentOutputTextAnnotationURLCitation",
    "ContentOutputTextAnnotationFilePath",
    "ContentRefusal",
]


class ContentOutputTextAnnotationFileCitation(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file."""

    index: Required[int]
    """The index of the file in the list of files."""

    type: Required[Literal["file_citation"]]
    """The type of the file citation. Always `file_citation`."""


class ContentOutputTextAnnotationURLCitation(TypedDict, total=False):
    end_index: Required[int]
    """The index of the last character of the URL citation in the message."""

    start_index: Required[int]
    """The index of the first character of the URL citation in the message."""

    title: Required[str]
    """The title of the web resource."""

    type: Required[Literal["url_citation"]]
    """The type of the URL citation. Always `url_citation`."""

    url: Required[str]
    """The URL of the web resource."""


class ContentOutputTextAnnotationFilePath(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file."""

    index: Required[int]
    """The index of the file in the list of files."""

    type: Required[Literal["file_path"]]
    """The type of the file path. Always `file_path`."""


ContentOutputTextAnnotation: TypeAlias = Union[
    ContentOutputTextAnnotationFileCitation, ContentOutputTextAnnotationURLCitation, ContentOutputTextAnnotationFilePath
]


class ContentOutputText(TypedDict, total=False):
    annotations: Required[Iterable[ContentOutputTextAnnotation]]
    """The annotations of the text output."""

    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class ContentRefusal(TypedDict, total=False):
    refusal: Required[str]
    """The refusal explanationfrom the model."""

    type: Required[Literal["refusal"]]
    """The type of the refusal. Always `refusal`."""


Content: TypeAlias = Union[ContentOutputText, ContentRefusal]


class OutputMessageParam(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the output message."""

    content: Required[Iterable[Content]]
    """The content of the output message."""

    role: Required[Literal["assistant"]]
    """The role of the output message. Always `assistant`."""

    status: Required[Literal["in_progress", "completed", "incomplete"]]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """

    type: Required[Literal["message"]]
    """The type of the output message. Always `message`."""
