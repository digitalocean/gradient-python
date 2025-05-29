# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .run_step_object import RunStepObject

__all__ = ["StepListResponse"]


class StepListResponse(BaseModel):
    data: List[RunStepObject]

    first_id: str

    has_more: bool

    last_id: str

    object: str
