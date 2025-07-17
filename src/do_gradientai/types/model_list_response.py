# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ModelListResponse", "Data"]


class Data(BaseModel):
    id: str
    """The model identifier, which can be referenced in the API endpoints."""

    created: int
    """The Unix timestamp (in seconds) when the model was created."""

    object: Literal["model"]
    """The object type, which is always "model"."""

    owned_by: str
    """The organization that owns the model."""


class ModelListResponse(BaseModel):
    data: List[Data]

    object: Literal["list"]
