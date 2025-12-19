# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["RetrieveDocumentsParams", "Filters", "FiltersMust", "FiltersMustNot", "FiltersShould"]


class RetrieveDocumentsParams(TypedDict, total=False):
    num_results: Required[int]
    """Number of results to return"""

    query: Required[str]
    """The search query text"""

    alpha: float
    """Weight for hybrid search (0-1):

    - 0 = pure keyword search (BM25)
    - 1 = pure vector search (default)
    - 0.5 = balanced hybrid search
    """

    filters: Filters
    """Metadata filters to apply to the search"""


class FiltersMust(TypedDict, total=False):
    field: Required[str]
    """Metadata field name"""

    operator: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte", "in", "not_in", "contains"]]
    """Comparison operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str]]]
    """Value to compare against (type depends on field)"""


class FiltersMustNot(TypedDict, total=False):
    field: Required[str]
    """Metadata field name"""

    operator: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte", "in", "not_in", "contains"]]
    """Comparison operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str]]]
    """Value to compare against (type depends on field)"""


class FiltersShould(TypedDict, total=False):
    field: Required[str]
    """Metadata field name"""

    operator: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte", "in", "not_in", "contains"]]
    """Comparison operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str]]]
    """Value to compare against (type depends on field)"""


class Filters(TypedDict, total=False):
    """Metadata filters to apply to the search"""

    must: Iterable[FiltersMust]
    """All conditions must match (AND)"""

    must_not: Iterable[FiltersMustNot]
    """No conditions should match (NOT)"""

    should: Iterable[FiltersShould]
    """At least one condition must match (OR)"""

