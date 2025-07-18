# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutoscalePoolStaticConfigParam"]


class AutoscalePoolStaticConfigParam(TypedDict, total=False):
    target_number_instances: Required[int]
    """Fixed number of instances in an autoscale pool."""
