# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AwsDataSourceParam"]


class AwsDataSourceParam(TypedDict, total=False):
    bucket_name: str

    item_path: str

    key_id: str

    region: str

    secret_key: str
