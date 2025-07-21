# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .api_indexed_data_source import APIIndexedDataSource

__all__ = ["IndexingJobRetrieveDataSourcesResponse"]


class IndexingJobRetrieveDataSourcesResponse(BaseModel):
    indexed_data_sources: Optional[List[APIIndexedDataSource]] = None
