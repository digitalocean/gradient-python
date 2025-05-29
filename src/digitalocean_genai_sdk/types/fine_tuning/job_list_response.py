# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .fine_tuning_job import FineTuningJob

__all__ = ["JobListResponse"]


class JobListResponse(BaseModel):
    data: List[FineTuningJob]

    has_more: bool

    object: Literal["list"]
