# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from ..auto_chunking_strategy_request_param import AutoChunkingStrategyRequestParam
from ..static_chunking_strategy_request_param import StaticChunkingStrategyRequestParam

__all__ = ["ChunkingStrategyRequestParam"]

ChunkingStrategyRequestParam: TypeAlias = Union[AutoChunkingStrategyRequestParam, StaticChunkingStrategyRequestParam]
