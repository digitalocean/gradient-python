# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IndexingJobRetrieveSignedURLResponse"]


class IndexingJobRetrieveSignedURLResponse(BaseModel):
    signed_url: Optional[str] = None
    """The signed url for downloading the indexing job details"""
