# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .api_indexing_job import APIIndexingJob

__all__ = ["IndexingJobCreateResponse"]


class IndexingJobCreateResponse(BaseModel):
    """StartKnowledgeBaseIndexingJobOutput description"""

    job: Optional[APIIndexingJob] = None
    """IndexingJob description"""
