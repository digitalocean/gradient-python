# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AwsDataSourceParam"]


class AwsDataSourceParam(TypedDict, total=False):
    """AWS S3 Data Source"""

    bucket_name: str
    """Spaces bucket name"""

    item_path: str

    key_id: str
    """The AWS Key ID"""

    region: str
    """Region of bucket"""

    secret_key: str
    """The AWS Secret Key"""
