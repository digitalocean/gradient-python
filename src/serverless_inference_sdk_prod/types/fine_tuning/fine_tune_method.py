# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FineTuneMethod", "Dpo", "DpoHyperparameters", "Supervised", "SupervisedHyperparameters"]


class DpoHyperparameters(BaseModel):
    batch_size: Union[Literal["auto"], int, None] = None
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    beta: Union[Literal["auto"], float, None] = None
    """The beta value for the DPO method.

    A higher beta value will increase the weight of the penalty between the policy
    and reference model.
    """

    learning_rate_multiplier: Union[Literal["auto"], float, None] = None
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int, None] = None
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class Dpo(BaseModel):
    hyperparameters: Optional[DpoHyperparameters] = None
    """The hyperparameters used for the fine-tuning job."""


class SupervisedHyperparameters(BaseModel):
    batch_size: Union[Literal["auto"], int, None] = None
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    learning_rate_multiplier: Union[Literal["auto"], float, None] = None
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int, None] = None
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class Supervised(BaseModel):
    hyperparameters: Optional[SupervisedHyperparameters] = None
    """The hyperparameters used for the fine-tuning job."""


class FineTuneMethod(BaseModel):
    dpo: Optional[Dpo] = None
    """Configuration for the DPO fine-tuning method."""

    supervised: Optional[Supervised] = None
    """Configuration for the supervised fine-tuning method."""

    type: Optional[Literal["supervised", "dpo"]] = None
    """The type of method. Is either `supervised` or `dpo`."""
