# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.kernel import Kernel
from .shared.page_links import PageLinks
from .shared.meta_properties import MetaProperties

__all__ = ["GPUDropletListKernelsResponse"]


class GPUDropletListKernelsResponse(BaseModel):
    meta: MetaProperties
    """Information about the response itself."""

    kernels: Optional[List[Optional[Kernel]]] = None

    links: Optional[PageLinks] = None
