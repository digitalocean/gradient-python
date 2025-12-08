# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .api_agreement import APIAgreement
from .api_model_version import APIModelVersion

__all__ = ["APIAgentModel"]


class APIAgentModel(BaseModel):
    """Description of a Model"""

    agreement: Optional[APIAgreement] = None
    """Agreement Description"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    inference_name: Optional[str] = None
    """Internally used name"""

    inference_version: Optional[str] = None
    """Internally used version"""

    is_foundational: Optional[bool] = None
    """True if it is a foundational model provided by do"""

    metadata: Optional[object] = None
    """Additional meta data"""

    name: Optional[str] = None
    """Name of the model"""

    parent_uuid: Optional[str] = None
    """Unique id of the model, this model is based on"""

    provider: Optional[Literal["MODEL_PROVIDER_DIGITALOCEAN", "MODEL_PROVIDER_ANTHROPIC", "MODEL_PROVIDER_OPENAI"]] = (
        None
    )

    updated_at: Optional[datetime] = None
    """Last modified"""

    upload_complete: Optional[bool] = None
    """Model has been fully uploaded"""

    url: Optional[str] = None
    """Download url"""

    usecases: Optional[
        List[
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
    ] = None
    """Usecases of the model"""

    uuid: Optional[str] = None
    """Unique id"""

    version: Optional[APIModelVersion] = None
    """Version Information about a Model"""
