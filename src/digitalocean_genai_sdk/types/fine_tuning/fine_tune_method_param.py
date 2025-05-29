# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["FineTuneMethodParam", "Dpo", "DpoHyperparameters", "Supervised", "SupervisedHyperparameters"]


class DpoHyperparameters(TypedDict, total=False):
    batch_size: Union[Literal["auto"], int]
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    beta: Union[Literal["auto"], float]
    """The beta value for the DPO method.

    A higher beta value will increase the weight of the penalty between the policy
    and reference model.
    """

    learning_rate_multiplier: Union[Literal["auto"], float]
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int]
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class Dpo(TypedDict, total=False):
    hyperparameters: DpoHyperparameters
    """The hyperparameters used for the fine-tuning job."""


class SupervisedHyperparameters(TypedDict, total=False):
    batch_size: Union[Literal["auto"], int]
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    learning_rate_multiplier: Union[Literal["auto"], float]
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int]
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class Supervised(TypedDict, total=False):
    hyperparameters: SupervisedHyperparameters
    """The hyperparameters used for the fine-tuning job."""


class FineTuneMethodParam(TypedDict, total=False):
    dpo: Dpo
    """Configuration for the DPO fine-tuning method."""

    supervised: Supervised
    """Configuration for the supervised fine-tuning method."""

    type: Literal["supervised", "dpo"]
    """The type of method. Is either `supervised` or `dpo`."""
