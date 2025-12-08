# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .api_agent_model import APIAgentModel
from .shared.api_meta import APIMeta
from .shared.api_links import APILinks
from .api_knowledge_base import APIKnowledgeBase
from .api_retrieval_method import APIRetrievalMethod
from .api_deployment_visibility import APIDeploymentVisibility

__all__ = [
    "AgentListResponse",
    "Agent",
    "AgentChatbot",
    "AgentChatbotIdentifier",
    "AgentDeployment",
    "AgentTemplate",
    "AgentTemplateGuardrail",
]


class AgentChatbot(BaseModel):
    """A Chatbot"""

    allowed_domains: Optional[List[str]] = None

    button_background_color: Optional[str] = None

    logo: Optional[str] = None

    name: Optional[str] = None
    """Name of chatbot"""

    primary_color: Optional[str] = None

    secondary_color: Optional[str] = None

    starting_message: Optional[str] = None


class AgentChatbotIdentifier(BaseModel):
    """Agent Chatbot Identifier"""

    agent_chatbot_identifier: Optional[str] = None
    """Agent chatbot identifier"""


class AgentDeployment(BaseModel):
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


class AgentTemplateGuardrail(BaseModel):
    priority: Optional[int] = None
    """Priority of the guardrail"""

    uuid: Optional[str] = None
    """Uuid of the guardrail"""


class AgentTemplate(BaseModel):
    """Represents an AgentTemplate entity"""

    created_at: Optional[datetime] = None
    """The agent template's creation date"""

    description: Optional[str] = None
    """Deprecated - Use summary instead"""

    guardrails: Optional[List[AgentTemplateGuardrail]] = None
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


class Agent(BaseModel):
    """A GenAI Agent's configuration"""

    chatbot: Optional[AgentChatbot] = None
    """A Chatbot"""

    chatbot_identifiers: Optional[List[AgentChatbotIdentifier]] = None
    """Chatbot identifiers"""

    created_at: Optional[datetime] = None
    """Creation date / time"""

    deployment: Optional[AgentDeployment] = None
    """Description of deployment"""

    description: Optional[str] = None
    """Description of agent"""

    if_case: Optional[str] = None
    """Instructions to the agent on how to use the route"""

    instruction: Optional[str] = None
    """Agent instruction.

    Instructions help your agent to perform its job effectively. See
    [Write Effective Agent Instructions](https://docs.digitalocean.com/products/genai-platform/concepts/best-practices/#agent-instructions)
    for best practices.
    """

    k: Optional[int] = None
    """How many results should be considered from an attached knowledge base"""

    max_tokens: Optional[int] = None
    """
    Specifies the maximum number of tokens the model can process in a single input
    or output, set as a number between 1 and 512. This determines the length of each
    response.
    """

    model: Optional[APIAgentModel] = None
    """Description of a Model"""

    name: Optional[str] = None
    """Agent name"""

    project_id: Optional[str] = None
    """The DigitalOcean project ID associated with the agent"""

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
    """Id of user that created the route"""

    route_name: Optional[str] = None
    """Route name"""

    route_uuid: Optional[str] = None
    """Route uuid"""

    tags: Optional[List[str]] = None
    """A set of abitrary tags to organize your agent"""

    temperature: Optional[float] = None
    """Controls the model’s creativity, specified as a number between 0 and 1.

    Lower values produce more predictable and conservative responses, while higher
    values encourage creativity and variation.
    """

    template: Optional[AgentTemplate] = None
    """Represents an AgentTemplate entity"""

    top_p: Optional[float] = None
    """
    Defines the cumulative probability threshold for word selection, specified as a
    number between 0 and 1. Higher values allow for more diverse outputs, while
    lower values ensure focused and coherent responses.
    """

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


class AgentListResponse(BaseModel):
    """List of Agents"""

    agents: Optional[List[Agent]] = None
    """Agents"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""
