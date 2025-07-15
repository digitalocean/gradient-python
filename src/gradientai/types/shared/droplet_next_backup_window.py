# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DropletNextBackupWindow"]


class DropletNextBackupWindow(BaseModel):
    end: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format specifying the end
    of the Droplet's backup window.
    """

    start: Optional[datetime] = None
    """
    A time value given in ISO8601 combined date and time format specifying the start
    of the Droplet's backup window.
    """
