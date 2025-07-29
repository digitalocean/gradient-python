# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigUpdateSubjectParams"]


class ConfigUpdateSubjectParams(TypedDict, total=False):
    database_cluster_uuid: Required[str]

    compatibility_level: Required[
        Literal["NONE", "BACKWARD", "BACKWARD_TRANSITIVE", "FORWARD", "FORWARD_TRANSITIVE", "FULL", "FULL_TRANSITIVE"]
    ]
    """The compatibility level of the schema registry."""
