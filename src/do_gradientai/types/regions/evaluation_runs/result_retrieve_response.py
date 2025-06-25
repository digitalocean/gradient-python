# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .api_prompt import APIPrompt
from .api_evaluation_run import APIEvaluationRun

__all__ = ["ResultRetrieveResponse"]


class ResultRetrieveResponse(BaseModel):
    evaluation_run: Optional[APIEvaluationRun] = None

    prompts: Optional[List[APIPrompt]] = None
    """The prompt level results."""
