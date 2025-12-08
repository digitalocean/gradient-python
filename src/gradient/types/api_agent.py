# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .api_agent_model import APIAgentModel
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
    "LoggingConfig",
    "ModelProviderKey",
    "Template",
    "TemplateGuardrail",
]


class APIKey(BaseModel):
    """Agent API Key"""

    api_key: Optional[str] = None
    """Api key"""


class Chatbot(BaseModel):
    """A Chatbot"""

    allowed_domains: Optional[List[str]] = None

    button_background_color: Optional[str] = None

    logo: Optional[str] = None

    name: Optional[str] = None
    """Name of chatbot"""

    primary_color: Optional[str] = None

    secondary_color: Optional[str] = None

    starting_message: Optional[str] = None


class ChatbotIdentifier(BaseModel):
    """Agent Chatbot Identifier"""

    agent_chatbot_identifier: Optional[str] = None
    """Agent chatbot identifier"""


class Deployment(BaseModel):
    """Description of deployment"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    name: Optional[str] = None
    """Name"""

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
            "STATUS_BUILDING",
        ]
    ] = None

    updated_at: Optional[datetime] = None
    """Last modified"""

    url: Optional[str] = None
    """Access your deployed agent here"""

    uuid: Optional[str] = None
    """Unique id"""

    visibility: Optional[APIDeploymentVisibility] = None
    """
    - VISIBILITY_UNKNOWN: The status of the deployment is unknown
    - VISIBILITY_DISABLED: The deployment is disabled and will no longer service
      requests
    - VISIBILITY_PLAYGROUND: Deprecated: No longer a valid state
    - VISIBILITY_PUBLIC: The deployment is public and will service requests from the
      public internet
    - VISIBILITY_PRIVATE: The deployment is private and will only service requests
      from other agents, or through API keys
    """


class Function(BaseModel):
    """Description missing"""

    api_key: Optional[str] = None
    """Api key"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    created_by: Optional[str] = None
    """Created by user id from DO"""

    description: Optional[str] = None
    """Agent description"""

    faas_name: Optional[str] = None

    faas_namespace: Optional[str] = None

    input_schema: Optional[object] = None

    name: Optional[str] = None
    """Name"""

    output_schema: Optional[object] = None

    updated_at: Optional[datetime] = None
    """Last modified"""

    url: Optional[str] = None
    """Download your agent here"""

    uuid: Optional[str] = None
    """Unique id"""


class Guardrail(BaseModel):
    """A Agent Guardrail"""

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


class LoggingConfig(BaseModel):
    galileo_project_id: Optional[str] = None
    """Galileo project identifier"""

    galileo_project_name: Optional[str] = None
    """Name of the Galileo project"""

    insights_enabled: Optional[bool] = None
    """Whether insights are enabled"""

    insights_enabled_at: Optional[datetime] = None
    """Timestamp when insights were enabled"""

    log_stream_id: Optional[str] = None
    """Identifier for the log stream"""

    log_stream_name: Optional[str] = None
    """Name of the log stream"""


class ModelProviderKey(BaseModel):
    api_key_uuid: Optional[str] = None
    """API key ID"""

    created_at: Optional[datetime] = None
    """Key creation date"""

    created_by: Optional[str] = None
    """Created by user id from DO"""

    deleted_at: Optional[datetime] = None
    """Key deleted date"""

    models: Optional[List[APIAgentModel]] = None
    """Models supported by the openAI api key"""

    name: Optional[str] = None
    """Name of the key"""

    provider: Optional[Literal["MODEL_PROVIDER_DIGITALOCEAN", "MODEL_PROVIDER_ANTHROPIC", "MODEL_PROVIDER_OPENAI"]] = (
        None
    )

    updated_at: Optional[datetime] = None
    """Key last updated date"""


class TemplateGuardrail(BaseModel):
    priority: Optional[int] = None
    """Priority of the guardrail"""

    uuid: Optional[str] = None
    """Uuid of the guardrail"""


class Template(BaseModel):
    """Represents an AgentTemplate entity"""

    created_at: Optional[datetime] = None
    """The agent template's creation date"""

    description: Optional[str] = None
    """Deprecated - Use summary instead"""

    guardrails: Optional[List[TemplateGuardrail]] = None
    """List of guardrails associated with the agent template"""

    instruction: Optional[str] = None
    """Instructions for the agent template"""

    k: Optional[int] = None
    """The 'k' value for the agent template"""

    knowledge_bases: Optional[List[APIKnowledgeBase]] = None
    """List of knowledge bases associated with the agent template"""

    long_description: Optional[str] = None
    """The long description of the agent template"""

    max_tokens: Optional[int] = None
    """The max_tokens setting for the agent template"""

    model: Optional[APIAgentModel] = None
    """Description of a Model"""

    name: Optional[str] = None
    """Name of the agent template"""

    short_description: Optional[str] = None
    """The short description of the agent template"""

    summary: Optional[str] = None
    """The summary of the agent template"""

    tags: Optional[List[str]] = None
    """List of tags associated with the agent template"""

    temperature: Optional[float] = None
    """The temperature setting for the agent template"""

    template_type: Optional[Literal["AGENT_TEMPLATE_TYPE_STANDARD", "AGENT_TEMPLATE_TYPE_ONE_CLICK"]] = None
    """
    - AGENT_TEMPLATE_TYPE_STANDARD: The standard agent template
    - AGENT_TEMPLATE_TYPE_ONE_CLICK: The one click agent template
    """

    top_p: Optional[float] = None
    """The top_p setting for the agent template"""

    updated_at: Optional[datetime] = None
    """The agent template's last updated date"""

    uuid: Optional[str] = None
    """Unique id"""


class APIAgent(BaseModel):
    """An Agent"""

    anthropic_api_key: Optional[APIAnthropicAPIKeyInfo] = None
    """Anthropic API Key Info"""

    api_key_infos: Optional[List[APIAgentAPIKeyInfo]] = None
    """Api key infos"""

    api_keys: Optional[List[APIKey]] = None
    """Api keys"""

    chatbot: Optional[Chatbot] = None
    """A Chatbot"""

    chatbot_identifiers: Optional[List[ChatbotIdentifier]] = None
    """Chatbot identifiers"""

    child_agents: Optional[List["APIAgent"]] = None
    """Child agents"""

    conversation_logs_enabled: Optional[bool] = None
    """Whether conversation logs are enabled for the agent"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    deployment: Optional[Deployment] = None
    """Description of deployment"""

    description: Optional[str] = None
    """Description of agent"""

    functions: Optional[List[Function]] = None

    guardrails: Optional[List[Guardrail]] = None
    """The guardrails the agent is attached to"""

    if_case: Optional[str] = None

    instruction: Optional[str] = None
    """Agent instruction.

    Instructions help your agent to perform its job effectively. See
    [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
    for best practices.
    """

    k: Optional[int] = None

    knowledge_bases: Optional[List[APIKnowledgeBase]] = None
    """Knowledge bases"""

    logging_config: Optional[LoggingConfig] = None

    max_tokens: Optional[int] = None

    model: Optional[APIAgentModel] = None
    """Description of a Model"""

    api_model_provider_key: Optional[ModelProviderKey] = FieldInfo(alias="model_provider_key", default=None)

    name: Optional[str] = None
    """Agent name"""

    openai_api_key: Optional[APIOpenAIAPIKeyInfo] = None
    """OpenAI API Key Info"""

    parent_agents: Optional[List["APIAgent"]] = None
    """Parent agents"""

    project_id: Optional[str] = None

    provide_citations: Optional[bool] = None
    """Whether the agent should provide in-response citations"""

    region: Optional[str] = None
    """Region code"""

    retrieval_method: Optional[APIRetrievalMethod] = None
    """
    - RETRIEVAL_METHOD_UNKNOWN: The retrieval method is unknown
    - RETRIEVAL_METHOD_REWRITE: The retrieval method is rewrite
    - RETRIEVAL_METHOD_STEP_BACK: The retrieval method is step back
    - RETRIEVAL_METHOD_SUB_QUERIES: The retrieval method is sub queries
    - RETRIEVAL_METHOD_NONE: The retrieval method is none
    """

    route_created_at: Optional[datetime] = None
    """Creation of route date / time"""

    route_created_by: Optional[str] = None

    route_name: Optional[str] = None
    """Route name"""

    route_uuid: Optional[str] = None

    tags: Optional[List[str]] = None
    """Agent tag to organize related resources"""

    temperature: Optional[float] = None

    template: Optional[Template] = None
    """Represents an AgentTemplate entity"""

    top_p: Optional[float] = None

    updated_at: Optional[datetime] = None
    """Last modified"""

    url: Optional[str] = None
    """Access your agent under this url"""

    user_id: Optional[str] = None
    """Id of user that created the agent"""

    uuid: Optional[str] = None
    """Unique agent id"""

    version_hash: Optional[str] = None
    """The latest version of the agent"""

    vpc_egress_ips: Optional[List[str]] = None
    """VPC Egress IPs"""

    vpc_uuid: Optional[str] = None

    workspace: Optional["APIWorkspace"] = None


from .api_workspace import APIWorkspace
