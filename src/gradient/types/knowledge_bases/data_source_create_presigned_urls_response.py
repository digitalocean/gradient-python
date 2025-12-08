# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DataSourceCreatePresignedURLsResponse", "Upload"]


class Upload(BaseModel):
    """Detailed info about each presigned URL returned to the client."""

    expires_at: Optional[datetime] = None
    """The time the url expires at."""

    object_key: Optional[str] = None
    """The unique object key to store the file as."""

    original_file_name: Optional[str] = None
    """The original file name."""

    presigned_url: Optional[str] = None
    """The actual presigned URL the client can use to upload the file directly."""


class DataSourceCreatePresignedURLsResponse(BaseModel):
    """Response with pre-signed urls to upload files."""

    request_id: Optional[str] = None
    """The ID generated for the request for Presigned URLs."""

    uploads: Optional[List[Upload]] = None
    """A list of generated presigned URLs and object keys, one per file."""
