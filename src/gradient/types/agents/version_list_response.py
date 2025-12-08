# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.api_meta import APIMeta
from ..shared.api_links import APILinks
from ..api_retrieval_method import APIRetrievalMethod

__all__ = [
    "VersionListResponse",
    "AgentVersion",
    "AgentVersionAttachedChildAgent",
    "AgentVersionAttachedFunction",
    "AgentVersionAttachedGuardrail",
    "AgentVersionAttachedKnowledgebase",
]


class AgentVersionAttachedChildAgent(BaseModel):
    agent_name: Optional[str] = None
    """Name of the child agent"""

    child_agent_uuid: Optional[str] = None
    """Child agent unique identifier"""

    if_case: Optional[str] = None
    """If case"""

    is_deleted: Optional[bool] = None
    """Child agent is deleted"""

    route_name: Optional[str] = None
    """Route name"""


class AgentVersionAttachedFunction(BaseModel):
    """Function represents a function configuration for an agent"""

    description: Optional[str] = None
    """Description of the function"""

    faas_name: Optional[str] = None
    """FaaS name of the function"""

    faas_namespace: Optional[str] = None
    """FaaS namespace of the function"""

    is_deleted: Optional[bool] = None
    """Whether the function is deleted"""

    name: Optional[str] = None
    """Name of the function"""


class AgentVersionAttachedGuardrail(BaseModel):
    """Agent Guardrail version"""

    is_deleted: Optional[bool] = None
    """Whether the guardrail is deleted"""

    name: Optional[str] = None
    """Guardrail Name"""

    priority: Optional[int] = None
    """Guardrail Priority"""

    uuid: Optional[str] = None
    """Guardrail UUID"""


class AgentVersionAttachedKnowledgebase(BaseModel):
    is_deleted: Optional[bool] = None
    """Deletet at date / time"""

    name: Optional[str] = None
    """Name of the knowledge base"""

    uuid: Optional[str] = None
    """Unique id of the knowledge base"""


class AgentVersion(BaseModel):
    """Represents an AgentVersion entity"""

    id: Optional[str] = None
    """Unique identifier"""

    agent_uuid: Optional[str] = None
    """Uuid of the agent this version belongs to"""

    attached_child_agents: Optional[List[AgentVersionAttachedChildAgent]] = None
    """List of child agent relationships"""

    attached_functions: Optional[List[AgentVersionAttachedFunction]] = None
    """List of function versions"""

    attached_guardrails: Optional[List[AgentVersionAttachedGuardrail]] = None
    """List of guardrail version"""

    attached_knowledgebases: Optional[List[AgentVersionAttachedKnowledgebase]] = None
    """List of knowledge base agent versions"""

    can_rollback: Optional[bool] = None
    """Whether the version is able to be rolled back to"""

    created_at: Optional[datetime] = None
    """Creation date"""

    created_by_email: Optional[str] = None
    """User who created this version"""

    currently_applied: Optional[bool] = None
    """Whether this is the currently applied configuration"""

    description: Optional[str] = None
    """Description of the agent"""

    instruction: Optional[str] = None
    """Instruction for the agent"""

    k: Optional[int] = None
    """K value for the agent's configuration"""

    max_tokens: Optional[int] = None
    """Max tokens setting for the agent"""

    model: Optional[str] = FieldInfo(alias="model_name", default=None)
    """Name of model associated to the agent version"""

    name: Optional[str] = None
    """Name of the agent"""

    provide_citations: Optional[bool] = None
    """Whether the agent should provide in-response citations"""

    retrieval_method: Optional[APIRetrievalMethod] = None
    """
    - RETRIEVAL_METHOD_UNKNOWN: The retrieval method is unknown
    - RETRIEVAL_METHOD_REWRITE: The retrieval method is rewrite
    - RETRIEVAL_METHOD_STEP_BACK: The retrieval method is step back
    - RETRIEVAL_METHOD_SUB_QUERIES: The retrieval method is sub queries
    - RETRIEVAL_METHOD_NONE: The retrieval method is none
    """

    tags: Optional[List[str]] = None
    """Tags associated with the agent"""

    temperature: Optional[float] = None
    """Temperature setting for the agent"""

    top_p: Optional[float] = None
    """Top_p setting for the agent"""

    trigger_action: Optional[str] = None
    """Action triggering the configuration update"""

    version_hash: Optional[str] = None
    """Version hash"""


class VersionListResponse(BaseModel):
    """List of agent versions"""

    agent_versions: Optional[List[AgentVersion]] = None
    """Agents"""

    links: Optional[APILinks] = None
    """Links to other pages"""

    meta: Optional[APIMeta] = None
    """Meta information about the data set"""
