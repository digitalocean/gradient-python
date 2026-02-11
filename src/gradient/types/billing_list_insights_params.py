# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BillingListInsightsParams"]


class BillingListInsightsParams(TypedDict, total=False):
    account_urn: Required[str]

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""
