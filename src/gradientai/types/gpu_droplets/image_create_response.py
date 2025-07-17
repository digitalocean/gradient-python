# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.image import Image

__all__ = ["ImageCreateResponse"]


class ImageCreateResponse(BaseModel):
    image: Optional[Image] = None
