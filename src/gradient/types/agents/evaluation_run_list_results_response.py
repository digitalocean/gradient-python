# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.api_meta import APIMeta
from ..shared.api_links import APILinks
from .api_evaluation_run import APIEvaluationRun
from .api_evaluation_prompt import APIEvaluationPrompt

__all__ = ["EvaluationRunListResultsResponse"]


class EvaluationRunListResultsResponse(BaseModel):
    """Gets the full results of an evaluation run with all prompts."""

    evaluation_run: Optional[APIEvaluationRun] = None

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""

    prompts: Optional[List[APIEvaluationPrompt]] = None
    """The prompt level results."""
