# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._compat import PYDANTIC_V2
from ...._models import BaseModel

__all__ = ["FunctionCreateResponse"]


class FunctionCreateResponse(BaseModel):
    agent: Optional["APIAgent"] = None


from ...shared.api_agent import APIAgent

if PYDANTIC_V2:
    FunctionCreateResponse.model_rebuild()
else:
    FunctionCreateResponse.update_forward_refs()  # type: ignore
