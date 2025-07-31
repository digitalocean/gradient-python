# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    page: int
    """Page number."""

    per_page: int
    """Items per page."""

    public_only: bool
    """Only include models that are publicly available."""

    usecases: List[
        Literal[
            "MODEL_USECASE_UNKNOWN",
            "MODEL_USECASE_AGENT",
            "MODEL_USECASE_FINETUNED",
            "MODEL_USECASE_KNOWLEDGEBASE",
            "MODEL_USECASE_GUARDRAIL",
            "MODEL_USECASE_REASONING",
            "MODEL_USECASE_SERVERLESS",
        ]
    ]
    """Include only models defined for the listed usecases.

    - MODEL_USECASE_UNKNOWN: The use case of the model is unknown
    - MODEL_USECASE_AGENT: The model maybe used in an agent
    - MODEL_USECASE_FINETUNED: The model maybe used for fine tuning
    - MODEL_USECASE_KNOWLEDGEBASE: The model maybe used for knowledge bases
      (embedding models)
    - MODEL_USECASE_GUARDRAIL: The model maybe used for guardrails
    - MODEL_USECASE_REASONING: The model usecase for reasoning
    - MODEL_USECASE_SERVERLESS: The model usecase for serverless inference
    """
