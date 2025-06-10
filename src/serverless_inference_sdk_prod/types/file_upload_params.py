# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The File object (not file name) to be uploaded."""

    purpose: Required[Literal["assistants", "batch", "fine-tune", "vision", "user_data", "evals"]]
    """The intended purpose of the uploaded file.

    One of: - `assistants`: Used in the Assistants API - `batch`: Used in the Batch
    API - `fine-tune`: Used for fine-tuning - `vision`: Images used for vision
    fine-tuning - `user_data`: Flexible file type for any purpose - `evals`: Used
    for eval data sets
    """
