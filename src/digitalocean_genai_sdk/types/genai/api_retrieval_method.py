# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["APIRetrievalMethod"]

APIRetrievalMethod: TypeAlias = Literal[
    "RETRIEVAL_METHOD_UNKNOWN",
    "RETRIEVAL_METHOD_REWRITE",
    "RETRIEVAL_METHOD_STEP_BACK",
    "RETRIEVAL_METHOD_SUB_QUERIES",
    "RETRIEVAL_METHOD_NONE",
]
