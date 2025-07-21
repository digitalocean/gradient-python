# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AutoscalePoolStaticConfig"]


class AutoscalePoolStaticConfig(BaseModel):
    target_number_instances: int
    """Fixed number of instances in an autoscale pool."""
