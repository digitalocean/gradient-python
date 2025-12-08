# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DataSourceDeleteResponse"]


class DataSourceDeleteResponse(BaseModel):
    """Information about a newly deleted knowledge base data source"""

    data_source_uuid: Optional[str] = None
    """Data source id"""

    knowledge_base_uuid: Optional[str] = None
    """Knowledge base id"""
