# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["DataSourceCreatePresignedURLsParams", "File"]


class DataSourceCreatePresignedURLsParams(TypedDict, total=False):
    files: Iterable[File]
    """A list of files to generate presigned URLs for."""


class File(TypedDict, total=False):
    """A single file’s metadata in the request."""

    file_name: str
    """Local filename"""

    file_size: str
    """The size of the file in bytes."""
