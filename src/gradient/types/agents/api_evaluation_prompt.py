# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .api_evaluation_metric_result import APIEvaluationMetricResult

__all__ = ["APIEvaluationPrompt", "EvaluationTraceSpan", "EvaluationTraceSpanRetrieverChunk", "PromptChunk"]


class EvaluationTraceSpanRetrieverChunk(BaseModel):
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


class EvaluationTraceSpan(BaseModel):
    """Represents a span within an evaluatioin trace (e.g., LLM call, tool call, etc.)"""

    created_at: Optional[datetime] = None
    """When the span was created"""

    input: Optional[object] = None
    """
    Input data for the span (flexible structure - can be messages array, string,
    etc.)
    """

    name: Optional[str] = None
    """Name/identifier for the span"""

    output: Optional[object] = None
    """Output data from the span (flexible structure - can be message, string, etc.)"""

    retriever_chunks: Optional[List[EvaluationTraceSpanRetrieverChunk]] = None
    """Any retriever span chunks that were included as part of the span."""

    span_level_metric_results: Optional[List[APIEvaluationMetricResult]] = None
    """The span-level metric results."""

    type: Optional[
        Literal["TRACE_SPAN_TYPE_UNKNOWN", "TRACE_SPAN_TYPE_LLM", "TRACE_SPAN_TYPE_RETRIEVER", "TRACE_SPAN_TYPE_TOOL"]
    ] = None
    """Types of spans in a trace"""


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
    evaluation_trace_spans: Optional[List[EvaluationTraceSpan]] = None
    """The evaluated trace spans."""

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

    trace_id: Optional[str] = None
    """The trace id for the prompt."""
