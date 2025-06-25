# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EvaluationRunCreateResponse"]


class EvaluationRunCreateResponse(BaseModel):
    evaluation_run_uuid: Optional[str] = None
