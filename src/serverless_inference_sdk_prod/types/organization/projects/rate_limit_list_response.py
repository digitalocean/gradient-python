# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel
from .project_rate_limit import ProjectRateLimit

__all__ = ["RateLimitListResponse"]


class RateLimitListResponse(BaseModel):
    data: List[ProjectRateLimit]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
