# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ModerationClassifyParams",
    "InputUnionMember2",
    "InputUnionMember2UnionMember0",
    "InputUnionMember2UnionMember0ImageURL",
    "InputUnionMember2UnionMember1",
]


class ModerationClassifyParams(TypedDict, total=False):
    input: Required[Union[str, List[str], Iterable[InputUnionMember2]]]
    """Input (or inputs) to classify.

    Can be a single string, an array of strings, or an array of multi-modal input
    objects similar to other models.
    """

    model: Union[
        str,
        Literal[
            "omni-moderation-latest", "omni-moderation-2024-09-26", "text-moderation-latest", "text-moderation-stable"
        ],
    ]
    """The content moderation model you would like to use.

    Learn more in [the moderation guide](/docs/guides/moderation), and learn about
    available models [here](/docs/models#moderation).
    """


class InputUnionMember2UnionMember0ImageURL(TypedDict, total=False):
    url: Required[str]
    """Either a URL of the image or the base64 encoded image data."""


class InputUnionMember2UnionMember0(TypedDict, total=False):
    image_url: Required[InputUnionMember2UnionMember0ImageURL]
    """Contains either an image URL or a data URL for a base64 encoded image."""

    type: Required[Literal["image_url"]]
    """Always `image_url`."""


class InputUnionMember2UnionMember1(TypedDict, total=False):
    text: Required[str]
    """A string of text to classify."""

    type: Required[Literal["text"]]
    """Always `text`."""


InputUnionMember2: TypeAlias = Union[InputUnionMember2UnionMember0, InputUnionMember2UnionMember1]
