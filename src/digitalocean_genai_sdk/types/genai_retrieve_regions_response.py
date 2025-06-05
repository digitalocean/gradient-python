# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["GenaiRetrieveRegionsResponse", "Region"]


class Region(BaseModel):
    inference_url: Optional[str] = None

    region: Optional[str] = None

    serves_batch: Optional[bool] = None

    serves_inference: Optional[bool] = None

    stream_inference_url: Optional[str] = None


class GenaiRetrieveRegionsResponse(BaseModel):
    regions: Optional[List[Region]] = None
