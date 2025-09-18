# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentRetrieveUsageResponse", "LogInsightsUsage", "LogInsightsUsageMeasurement", "Usage", "UsageMeasurement"]


class LogInsightsUsageMeasurement(BaseModel):
    tokens: Optional[int] = None

    usage_type: Optional[str] = None


class LogInsightsUsage(BaseModel):
    measurements: Optional[List[LogInsightsUsageMeasurement]] = None

    resource_uuid: Optional[str] = None

    start: Optional[datetime] = None

    stop: Optional[datetime] = None


class UsageMeasurement(BaseModel):
    tokens: Optional[int] = None

    usage_type: Optional[str] = None


class Usage(BaseModel):
    measurements: Optional[List[UsageMeasurement]] = None

    resource_uuid: Optional[str] = None

    start: Optional[datetime] = None

    stop: Optional[datetime] = None


class AgentRetrieveUsageResponse(BaseModel):
    log_insights_usage: Optional[LogInsightsUsage] = None
    """Resource Usage Description"""

    usage: Optional[Usage] = None
    """Resource Usage Description"""
