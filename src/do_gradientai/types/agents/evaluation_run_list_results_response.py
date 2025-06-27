# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .api_evaluation_run import APIEvaluationRun
from .api_evaluation_prompt import APIEvaluationPrompt

__all__ = ["EvaluationRunListResultsResponse"]


class EvaluationRunListResultsResponse(BaseModel):
    evaluation_run: Optional[APIEvaluationRun] = None

    prompts: Optional[List[APIEvaluationPrompt]] = None
    """The prompt level results."""
