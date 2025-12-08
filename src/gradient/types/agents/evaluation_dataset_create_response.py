# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EvaluationDatasetCreateResponse"]


class EvaluationDatasetCreateResponse(BaseModel):
    """Output for creating an agent evaluation dataset"""

    evaluation_dataset_uuid: Optional[str] = None
    """Evaluation dataset uuid."""
