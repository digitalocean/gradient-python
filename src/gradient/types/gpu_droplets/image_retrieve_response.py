# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..shared.image import Image

__all__ = ["ImageRetrieveResponse"]


class ImageRetrieveResponse(BaseModel):
    image: Image
