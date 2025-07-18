# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..knowledge_bases.api_file_upload_data_source_param import APIFileUploadDataSourceParam

__all__ = ["EvaluationDatasetCreateParams"]


class EvaluationDatasetCreateParams(TypedDict, total=False):
    file_upload_dataset: APIFileUploadDataSourceParam
    """File to upload as data source for knowledge base."""

    name: str
    """The name of the agent evaluation dataset."""
