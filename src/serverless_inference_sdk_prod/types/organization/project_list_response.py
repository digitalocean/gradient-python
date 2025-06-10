# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .project import Project
from ..._models import BaseModel

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    data: List[Project]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
