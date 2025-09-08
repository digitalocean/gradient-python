# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["IndexingJobCreateParams"]


class IndexingJobCreateParams(TypedDict, total=False):
    data_source_uuids: SequenceNotStr[str]
    """
    List of data source ids to index, if none are provided, all data sources will be
    indexed
    """

    knowledge_base_uuid: str
    """Knowledge base id"""
