# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .api_evaluation_prompt import APIEvaluationPrompt

__all__ = ["EvaluationRunRetrieveResultsResponse"]


class EvaluationRunRetrieveResultsResponse(BaseModel):
    prompt: Optional[APIEvaluationPrompt] = None
