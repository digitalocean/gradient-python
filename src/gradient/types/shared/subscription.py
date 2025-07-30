# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .subscription_tier_base import SubscriptionTierBase

__all__ = ["Subscription"]


class Subscription(BaseModel):
    created_at: Optional[datetime] = None
    """The time at which the subscription was created."""

    tier: Optional[SubscriptionTierBase] = None

    updated_at: Optional[datetime] = None
    """The time at which the subscription was last updated."""
