# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentRetrieveUsageResponse", "LogInsightsUsage", "LogInsightsUsageMeasurement", "Usage", "UsageMeasurement"]


class LogInsightsUsageMeasurement(BaseModel):
    """Usage Measurement Description"""

    tokens: Optional[int] = None

    usage_type: Optional[str] = None


class LogInsightsUsage(BaseModel):
    """Resource Usage Description"""

    measurements: Optional[List[LogInsightsUsageMeasurement]] = None

    resource_uuid: Optional[str] = None

    start: Optional[datetime] = None

    stop: Optional[datetime] = None


class UsageMeasurement(BaseModel):
    """Usage Measurement Description"""

    tokens: Optional[int] = None

    usage_type: Optional[str] = None


class Usage(BaseModel):
    """Resource Usage Description"""

    measurements: Optional[List[UsageMeasurement]] = None

    resource_uuid: Optional[str] = None

    start: Optional[datetime] = None

    stop: Optional[datetime] = None


class AgentRetrieveUsageResponse(BaseModel):
    """Agent usage"""

    log_insights_usage: Optional[LogInsightsUsage] = None
    """Resource Usage Description"""

    usage: Optional[Usage] = None
    """Resource Usage Description"""
