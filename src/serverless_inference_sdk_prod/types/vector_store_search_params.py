# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .compound_filter_param import CompoundFilterParam
from .comparison_filter_param import ComparisonFilterParam

__all__ = ["VectorStoreSearchParams", "Filters", "RankingOptions"]


class VectorStoreSearchParams(TypedDict, total=False):
    query: Required[Union[str, List[str]]]
    """A query string for a search"""

    filters: Filters
    """A filter to apply based on file attributes."""

    max_num_results: int
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: RankingOptions
    """Ranking options for search."""

    rewrite_query: bool
    """Whether to rewrite the natural language query for vector search."""


Filters: TypeAlias = Union[ComparisonFilterParam, CompoundFilterParam]


class RankingOptions(TypedDict, total=False):
    ranker: Literal["auto", "default-2024-11-15"]

    score_threshold: float
