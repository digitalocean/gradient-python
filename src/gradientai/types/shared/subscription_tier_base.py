# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SubscriptionTierBase"]


class SubscriptionTierBase(BaseModel):
    allow_storage_overage: Optional[bool] = None
    """
    A boolean indicating whether the subscription tier supports additional storage
    above what is included in the base plan at an additional cost per GiB used.
    """

    included_bandwidth_bytes: Optional[int] = None
    """
    The amount of outbound data transfer included in the subscription tier in bytes.
    """

    included_repositories: Optional[int] = None
    """The number of repositories included in the subscription tier.

    `0` indicates that the subscription tier includes unlimited repositories.
    """

    included_storage_bytes: Optional[int] = None
    """The amount of storage included in the subscription tier in bytes."""

    monthly_price_in_cents: Optional[int] = None
    """The monthly cost of the subscription tier in cents."""

    name: Optional[str] = None
    """The name of the subscription tier."""

    slug: Optional[str] = None
    """The slug identifier of the subscription tier."""

    storage_overage_price_in_cents: Optional[int] = None
    """
    The price paid in cents per GiB for additional storage beyond what is included
    in the subscription plan.
    """
