# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConfigUpdateSubjectResponse"]


class ConfigUpdateSubjectResponse(BaseModel):
    compatibility_level: Literal[
        "NONE", "BACKWARD", "BACKWARD_TRANSITIVE", "FORWARD", "FORWARD_TRANSITIVE", "FULL", "FULL_TRANSITIVE"
    ]
    """The compatibility level of the schema registry."""

    subject_name: str
    """The name of the schema subject."""
