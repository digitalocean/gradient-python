# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["EvaluationRunCreateResponse"]


class EvaluationRunCreateResponse(BaseModel):
    evaluation_run_uuids: Optional[List[str]] = None
