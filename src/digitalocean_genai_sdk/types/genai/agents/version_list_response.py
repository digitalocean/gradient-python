# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .api_meta import APIMeta
from .api_links import APILinks
from ...._models import BaseModel
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

    child_agent_uuid: Optional[str] = None

    if_case: Optional[str] = None

    is_deleted: Optional[bool] = None

    route_name: Optional[str] = None


class AgentVersionAttachedFunction(BaseModel):
    description: Optional[str] = None

    faas_name: Optional[str] = None

    faas_namespace: Optional[str] = None

    is_deleted: Optional[bool] = None

    name: Optional[str] = None


class AgentVersionAttachedGuardrail(BaseModel):
    is_deleted: Optional[bool] = None

    name: Optional[str] = None

    priority: Optional[int] = None

    uuid: Optional[str] = None


class AgentVersionAttachedKnowledgebase(BaseModel):
    is_deleted: Optional[bool] = None

    name: Optional[str] = None

    uuid: Optional[str] = None


class AgentVersion(BaseModel):
    id: Optional[str] = None

    agent_uuid: Optional[str] = None

    attached_child_agents: Optional[List[AgentVersionAttachedChildAgent]] = None

    attached_functions: Optional[List[AgentVersionAttachedFunction]] = None

    attached_guardrails: Optional[List[AgentVersionAttachedGuardrail]] = None

    attached_knowledgebases: Optional[List[AgentVersionAttachedKnowledgebase]] = None

    can_rollback: Optional[bool] = None

    created_at: Optional[datetime] = None

    created_by_email: Optional[str] = None

    currently_applied: Optional[bool] = None

    description: Optional[str] = None

    instruction: Optional[str] = None

    k: Optional[int] = None

    max_tokens: Optional[int] = None

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)

    name: Optional[str] = None

    provide_citations: Optional[bool] = None

    retrieval_method: Optional[APIRetrievalMethod] = None

    tags: Optional[List[str]] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    trigger_action: Optional[str] = None

    version_hash: Optional[str] = None


class VersionListResponse(BaseModel):
    agent_versions: Optional[List[AgentVersion]] = None

    links: Optional[APILinks] = None

    meta: Optional[APIMeta] = None
