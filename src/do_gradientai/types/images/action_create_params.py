# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ActionCreateParams", "ImageActionBase", "ImageActionTransfer"]


class ImageActionBase(TypedDict, total=False):
    type: Required[Literal["convert", "transfer"]]
    """The action to be taken on the image. Can be either `convert` or `transfer`."""


class ImageActionTransfer(TypedDict, total=False):
    region: Required[
        Literal[
            "ams1",
            "ams2",
            "ams3",
            "blr1",
            "fra1",
            "lon1",
            "nyc1",
            "nyc2",
            "nyc3",
            "sfo1",
            "sfo2",
            "sfo3",
            "sgp1",
            "tor1",
            "syd1",
        ]
    ]
    """
    The slug identifier for the region where the resource will initially be
    available.
    """

    type: Required[Literal["convert", "transfer"]]
    """The action to be taken on the image. Can be either `convert` or `transfer`."""


ActionCreateParams: TypeAlias = Union[ImageActionBase, ImageActionTransfer]
