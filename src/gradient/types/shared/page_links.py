# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .forward_links import ForwardLinks
from .backward_links import BackwardLinks

__all__ = ["PageLinks", "Pages"]

Pages: TypeAlias = Union[ForwardLinks, BackwardLinks, object]


class PageLinks(BaseModel):
    pages: Optional[Pages] = None
