# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StepRetrieveParams"]


class StepRetrieveParams(TypedDict, total=False):
    thread_id: Required[str]

    run_id: Required[str]

    include: List[Literal["step_details.tool_calls[*].file_search.results[*].content"]]
    """A list of additional fields to include in the response.

    Currently the only supported value is
    `step_details.tool_calls[*].file_search.results[*].content` to fetch the file
    search result content.

    See the
    [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """
