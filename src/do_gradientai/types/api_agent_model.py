# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIAgentModel", "Agreement", "Version"]


class Agreement(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    url: Optional[str] = None

    uuid: Optional[str] = None


class Version(BaseModel):
    major: Optional[int] = None
    """Major version number"""

    minor: Optional[int] = None
    """Minor version number"""

    patch: Optional[int] = None
    """Patch version number"""


class APIAgentModel(BaseModel):
    agreement: Optional[Agreement] = None
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

    version: Optional[Version] = None
    """Version Information about a Model"""
