# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .autoscale_pool_static_config_param import AutoscalePoolStaticConfigParam
from .autoscale_pool_dynamic_config_param import AutoscalePoolDynamicConfigParam
from .autoscale_pool_droplet_template_param import AutoscalePoolDropletTemplateParam

__all__ = ["AutoscaleUpdateParams", "Config"]


class AutoscaleUpdateParams(TypedDict, total=False):
    config: Required[Config]
    """
    The scaling configuration for an autoscale pool, which is how the pool scales up
    and down (either by resource utilization or static configuration).
    """

    droplet_template: Required[AutoscalePoolDropletTemplateParam]

    name: Required[str]
    """The human-readable name of the autoscale pool. This field cannot be updated"""


Config: TypeAlias = Union[AutoscalePoolStaticConfigParam, AutoscalePoolDynamicConfigParam]
