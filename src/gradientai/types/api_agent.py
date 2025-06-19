# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .api_knowledge_base import APIKnowledgeBase
from .api_retrieval_method import APIRetrievalMethod
from .api_agent_api_key_info import APIAgentAPIKeyInfo
from .api_openai_api_key_info import APIOpenAIAPIKeyInfo
from .api_deployment_visibility import APIDeploymentVisibility
from .api_anthropic_api_key_info import APIAnthropicAPIKeyInfo

__all__ = [
    "APIAgent",
    "APIKey",
    "Chatbot",
    "ChatbotIdentifier",
    "Deployment",
    "Function",
    "Guardrail",
    "Model",
    "ModelAgreement",
    "ModelVersion",
    "Template",
    "TemplateGuardrail",
    "TemplateModel",
    "TemplateModelAgreement",
    "TemplateModelVersion",
]


class APIKey(BaseModel):
    api_key: Optional[str] = None


class Chatbot(BaseModel):
    button_background_color: Optional[str] = None

    logo: Optional[str] = None

    name: Optional[str] = None

    primary_color: Optional[str] = None

    secondary_color: Optional[str] = None

    starting_message: Optional[str] = None


class ChatbotIdentifier(BaseModel):
    agent_chatbot_identifier: Optional[str] = None


class Deployment(BaseModel):
    created_at: Optional[datetime] = None

    name: Optional[str] = None

    status: Optional[
        Literal[
            "STATUS_UNKNOWN",
            "STATUS_WAITING_FOR_DEPLOYMENT",
            "STATUS_DEPLOYING",
            "STATUS_RUNNING",
            "STATUS_FAILED",
            "STATUS_WAITING_FOR_UNDEPLOYMENT",
            "STATUS_UNDEPLOYING",
            "STATUS_UNDEPLOYMENT_FAILED",
            "STATUS_DELETED",
        ]
    ] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None

    uuid: Optional[str] = None

    visibility: Optional[APIDeploymentVisibility] = None


class Function(BaseModel):
    api_key: Optional[str] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    faas_name: Optional[str] = None

    faas_namespace: Optional[str] = None

    input_schema: Optional[object] = None

    name: Optional[str] = None

    output_schema: Optional[object] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None

    uuid: Optional[str] = None


class Guardrail(BaseModel):
    agent_uuid: Optional[str] = None

    created_at: Optional[datetime] = None

    default_response: Optional[str] = None

    description: Optional[str] = None

    guardrail_uuid: Optional[str] = None

    is_attached: Optional[bool] = None

    is_default: Optional[bool] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    priority: Optional[int] = None

    type: Optional[
        Literal[
            "GUARDRAIL_TYPE_UNKNOWN",
            "GUARDRAIL_TYPE_JAILBREAK",
            "GUARDRAIL_TYPE_SENSITIVE_DATA",
            "GUARDRAIL_TYPE_CONTENT_MODERATION",
        ]
    ] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class ModelAgreement(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    url: Optional[str] = None

    uuid: Optional[str] = None


class ModelVersion(BaseModel):
    major: Optional[int] = None

    minor: Optional[int] = None

    patch: Optional[int] = None


class Model(BaseModel):
    agreement: Optional[ModelAgreement] = None

    created_at: Optional[datetime] = None

    inference_name: Optional[str] = None

    inference_version: Optional[str] = None

    is_foundational: Optional[bool] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    parent_uuid: Optional[str] = None

    provider: Optional[Literal["MODEL_PROVIDER_DIGITALOCEAN", "MODEL_PROVIDER_ANTHROPIC", "MODEL_PROVIDER_OPENAI"]] = (
        None
    )

    updated_at: Optional[datetime] = None

    upload_complete: Optional[bool] = None

    url: Optional[str] = None

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

    uuid: Optional[str] = None

    version: Optional[ModelVersion] = None


class TemplateGuardrail(BaseModel):
    priority: Optional[int] = None

    uuid: Optional[str] = None


class TemplateModelAgreement(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    url: Optional[str] = None

    uuid: Optional[str] = None


class TemplateModelVersion(BaseModel):
    major: Optional[int] = None

    minor: Optional[int] = None

    patch: Optional[int] = None


class TemplateModel(BaseModel):
    agreement: Optional[TemplateModelAgreement] = None

    created_at: Optional[datetime] = None

    inference_name: Optional[str] = None

    inference_version: Optional[str] = None

    is_foundational: Optional[bool] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    parent_uuid: Optional[str] = None

    provider: Optional[Literal["MODEL_PROVIDER_DIGITALOCEAN", "MODEL_PROVIDER_ANTHROPIC", "MODEL_PROVIDER_OPENAI"]] = (
        None
    )

    updated_at: Optional[datetime] = None

    upload_complete: Optional[bool] = None

    url: Optional[str] = None

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

    uuid: Optional[str] = None

    version: Optional[TemplateModelVersion] = None


class Template(BaseModel):
    created_at: Optional[datetime] = None

    description: Optional[str] = None

    guardrails: Optional[List[TemplateGuardrail]] = None

    instruction: Optional[str] = None

    k: Optional[int] = None

    knowledge_bases: Optional[List[APIKnowledgeBase]] = None

    long_description: Optional[str] = None

    max_tokens: Optional[int] = None

    model: Optional[TemplateModel] = None

    name: Optional[str] = None

    short_description: Optional[str] = None

    summary: Optional[str] = None

    tags: Optional[List[str]] = None

    temperature: Optional[float] = None

    template_type: Optional[Literal["AGENT_TEMPLATE_TYPE_STANDARD", "AGENT_TEMPLATE_TYPE_ONE_CLICK"]] = None

    top_p: Optional[float] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None


class APIAgent(BaseModel):
    anthropic_api_key: Optional[APIAnthropicAPIKeyInfo] = None

    api_key_infos: Optional[List[APIAgentAPIKeyInfo]] = None

    api_keys: Optional[List[APIKey]] = None

    chatbot: Optional[Chatbot] = None

    chatbot_identifiers: Optional[List[ChatbotIdentifier]] = None

    child_agents: Optional[List["APIAgent"]] = None

    created_at: Optional[datetime] = None

    deployment: Optional[Deployment] = None

    description: Optional[str] = None

    functions: Optional[List[Function]] = None

    guardrails: Optional[List[Guardrail]] = None

    if_case: Optional[str] = None

    instruction: Optional[str] = None
    """Agent instruction.

    Instructions help your agent to perform its job effectively. See
    [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
    for best practices.
    """

    k: Optional[int] = None

    knowledge_bases: Optional[List[APIKnowledgeBase]] = None

    max_tokens: Optional[int] = None

    model: Optional[Model] = None

    name: Optional[str] = None

    openai_api_key: Optional[APIOpenAIAPIKeyInfo] = None

    parent_agents: Optional[List["APIAgent"]] = None

    project_id: Optional[str] = None

    provide_citations: Optional[bool] = None

    region: Optional[str] = None

    retrieval_method: Optional[APIRetrievalMethod] = None

    route_created_at: Optional[datetime] = None

    route_created_by: Optional[str] = None

    route_name: Optional[str] = None

    route_uuid: Optional[str] = None

    tags: Optional[List[str]] = None

    temperature: Optional[float] = None

    template: Optional[Template] = None

    top_p: Optional[float] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None

    user_id: Optional[str] = None

    uuid: Optional[str] = None

    workspace: Optional[object] = None
