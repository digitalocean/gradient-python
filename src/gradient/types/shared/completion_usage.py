# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CompletionUsage", "CacheCreation"]


class CacheCreation(BaseModel):
    """Breakdown of prompt tokens written to cache."""

    ephemeral_1h_input_tokens: int
    """Number of prompt tokens written to 1h cache."""

    ephemeral_5m_input_tokens: int
    """Number of prompt tokens written to 5m cache."""


class CompletionUsage(BaseModel):
    """Usage statistics for the completion request."""

    cache_created_input_tokens: int
    """Number of prompt tokens written to cache."""

    cache_creation: CacheCreation
    """Breakdown of prompt tokens written to cache."""

    cache_read_input_tokens: int
    """Number of prompt tokens read from cache."""

    completion_tokens: int
    """Number of tokens in the generated completion."""

    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total number of tokens used in the request (prompt + completion)."""
