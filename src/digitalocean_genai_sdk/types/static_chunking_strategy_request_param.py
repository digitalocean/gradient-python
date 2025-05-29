# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .static_chunking_strategy_param import StaticChunkingStrategyParam

__all__ = ["StaticChunkingStrategyRequestParam"]


class StaticChunkingStrategyRequestParam(TypedDict, total=False):
    static: Required[StaticChunkingStrategyParam]

    type: Required[Literal["static"]]
    """Always `static`."""
