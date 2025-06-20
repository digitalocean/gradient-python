# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_indexing_job import APIIndexingJob
from .doagents.api_meta import APIMeta
from .doagents.api_links import APILinks

__all__ = ["IndexingJobListResponse"]


class IndexingJobListResponse(BaseModel):
    jobs: Optional[List[APIIndexingJob]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None
