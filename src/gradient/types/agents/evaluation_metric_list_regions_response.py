# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["EvaluationMetricListRegionsResponse", "Region"]


class Region(BaseModel):
    """Description for a specific Region"""

    inference_url: Optional[str] = None
    """Url for inference server"""

    region: Optional[str] = None
    """Region code"""

    serves_batch: Optional[bool] = None
    """This datacenter is capable of running batch jobs"""

    serves_inference: Optional[bool] = None
    """This datacenter is capable of serving inference"""

    stream_inference_url: Optional[str] = None
    """The url for the inference streaming server"""


class EvaluationMetricListRegionsResponse(BaseModel):
    """Region Codes"""

    regions: Optional[List[Region]] = None
    """Region code"""
