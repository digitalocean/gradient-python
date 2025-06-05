# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IndexingJobUpdateCancelParams"]


class IndexingJobUpdateCancelParams(TypedDict, total=False):
    body_uuid: Annotated[str, PropertyInfo(alias="uuid")]
    """A unique identifier for an indexing job."""
