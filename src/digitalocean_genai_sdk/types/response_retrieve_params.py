# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .includable import Includable

__all__ = ["ResponseRetrieveParams"]


class ResponseRetrieveParams(TypedDict, total=False):
    include: List[Includable]
    """Specify additional output data to include in the response.

    Currently supported values are:

    - `file_search_call.results`: Include the search results of

      the file search tool call.

    - `message.input_image.image_url`: Include image urls from the input message.
    - `computer_call_output.output.image_url`: Include image urls from the computer
      call output.
    """
