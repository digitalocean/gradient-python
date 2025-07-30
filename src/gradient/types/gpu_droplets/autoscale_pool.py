# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .current_utilization import CurrentUtilization
from .autoscale_pool_static_config import AutoscalePoolStaticConfig
from .autoscale_pool_dynamic_config import AutoscalePoolDynamicConfig
from .autoscale_pool_droplet_template import AutoscalePoolDropletTemplate

__all__ = ["AutoscalePool", "Config"]

Config: TypeAlias = Union[AutoscalePoolStaticConfig, AutoscalePoolDynamicConfig]


class AutoscalePool(BaseModel):
    id: str
    """A unique identifier for each autoscale pool instance.

    This is automatically generated upon autoscale pool creation.
    """

    active_resources_count: int
    """The number of active Droplets in the autoscale pool."""

    config: Config
    """
    The scaling configuration for an autoscale pool, which is how the pool scales up
    and down (either by resource utilization or static configuration).
    """

    created_at: datetime
    """
    A time value given in ISO8601 combined date and time format that represents when
    the autoscale pool was created.
    """

    droplet_template: AutoscalePoolDropletTemplate

    name: str
    """The human-readable name set for the autoscale pool."""

    status: Literal["active", "deleting", "error"]
    """The current status of the autoscale pool."""

    updated_at: datetime
    """
    A time value given in ISO8601 combined date and time format that represents when
    the autoscale pool was last updated.
    """

    current_utilization: Optional[CurrentUtilization] = None
