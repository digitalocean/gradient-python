# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .autoscale_pool import AutoscalePool

__all__ = ["AutoscaleCreateResponse"]


class AutoscaleCreateResponse(BaseModel):
    autoscale_pool: Optional[AutoscalePool] = None
