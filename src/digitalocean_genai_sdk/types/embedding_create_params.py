# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["EmbeddingCreateParams"]


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Union[str, List[str]]]
    """Input text to embed, encoded as a string or array of tokens.

    To embed multiple inputs in a single request, pass an array of strings.
    """

    model: Required[str]
    """ID of the model to use.

    You can use the List models API to see all of your available models.
    """

    user: str
    """
    A unique identifier representing your end-user, which can help DigitalOcean to
    monitor and detect abuse.
    """
