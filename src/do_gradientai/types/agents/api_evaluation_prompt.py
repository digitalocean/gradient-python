# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .api_evaluation_metric_result import APIEvaluationMetricResult

__all__ = ["APIEvaluationPrompt", "PromptChunk"]


class PromptChunk(BaseModel):
    chunk_usage_pct: Optional[float] = None
    """The usage percentage of the chunk."""

    chunk_used: Optional[bool] = None
    """Indicates if the chunk was used in the prompt."""

    index_uuid: Optional[str] = None
    """The index uuid (Knowledge Base) of the chunk."""

    source_name: Optional[str] = None
    """The source name for the chunk, e.g., the file name or document title."""

    text: Optional[str] = None
    """Text content of the chunk."""


class APIEvaluationPrompt(BaseModel):
    ground_truth: Optional[str] = None
    """The ground truth for the prompt."""

    input: Optional[str] = None

    input_tokens: Optional[str] = None
    """The number of input tokens used in the prompt."""

    output: Optional[str] = None

    output_tokens: Optional[str] = None
    """The number of output tokens used in the prompt."""

    prompt_chunks: Optional[List[PromptChunk]] = None
    """The list of prompt chunks."""

    prompt_id: Optional[int] = None
    """Prompt ID"""

    prompt_level_metric_results: Optional[List[APIEvaluationMetricResult]] = None
    """The metric results for the prompt."""
