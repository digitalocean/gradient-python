# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .._models import BaseModel

__all__ = ["BillingListInsightsResponse", "DataPoint"]


class DataPoint(BaseModel):
    description: Optional[str] = None
    """Description of the billed resource or service as shown on an invoice item"""

    group_description: Optional[str] = None
    """
    Optional invoice item group name of the billed resource or service, blank when
    not part an invoice item group
    """

    region: Optional[str] = None
    """Region where the usage occurred"""

    sku: Optional[str] = None
    """Unique SKU identifier for the billed resource"""

    start_date: Optional[date] = None
    """Start date of the billing data point in YYYY-MM-DD format"""

    total_amount: Optional[str] = None
    """Total amount for this data point in USD"""

    usage_team_urn: Optional[str] = None
    """URN of the team that incurred the usage"""


class BillingListInsightsResponse(BaseModel):
    current_page: int
    """Current page number"""

    data_points: List[DataPoint]
    """
    Array of billing data points, which are day-over-day changes in billing resource
    usage based on nightly invoice item estimates, for the requested period
    """

    total_items: int
    """Total number of items available across all pages"""

    total_pages: int
    """Total number of pages available"""
