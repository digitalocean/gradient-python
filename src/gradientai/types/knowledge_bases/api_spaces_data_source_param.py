# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["APISpacesDataSourceParam"]


class APISpacesDataSourceParam(TypedDict, total=False):
    bucket_name: str

    item_path: str

    region: str
