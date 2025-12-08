# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.api_meta import APIMeta
from .api_indexing_job import APIIndexingJob
from ..shared.api_links import APILinks

__all__ = ["IndexingJobListResponse"]


class IndexingJobListResponse(BaseModel):
    """Indexing jobs"""

    jobs: Optional[List[APIIndexingJob]] = None
    """The indexing jobs"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""
