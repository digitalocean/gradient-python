# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CheckpointRetrieveResponse", "Data", "DataMetrics"]


class DataMetrics(BaseModel):
    full_valid_loss: Optional[float] = None

    full_valid_mean_token_accuracy: Optional[float] = None

    step: Optional[float] = None

    train_loss: Optional[float] = None

    train_mean_token_accuracy: Optional[float] = None

    valid_loss: Optional[float] = None

    valid_mean_token_accuracy: Optional[float] = None


class Data(BaseModel):
    id: str
    """The checkpoint identifier, which can be referenced in the API endpoints."""

    created_at: int
    """The Unix timestamp (in seconds) for when the checkpoint was created."""

    fine_tuned_model_checkpoint: str
    """The name of the fine-tuned checkpoint model that is created."""

    fine_tuning_job_id: str
    """The name of the fine-tuning job that this checkpoint was created from."""

    metrics: DataMetrics
    """Metrics at the step number during the fine-tuning job."""

    object: Literal["fine_tuning.job.checkpoint"]
    """The object type, which is always "fine_tuning.job.checkpoint"."""

    step_number: int
    """The step number that the checkpoint was created at."""


class CheckpointRetrieveResponse(BaseModel):
    data: List[Data]

    has_more: bool

    object: Literal["list"]

    first_id: Optional[str] = None

    last_id: Optional[str] = None
