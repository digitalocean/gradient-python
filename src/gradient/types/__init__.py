# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import (
    agents,
    models,
    api_agent,
    api_workspace,
    agent_create_response,
    agent_delete_response,
    agent_update_response,
    agent_retrieve_response,
    agent_update_status_response,
)
from .. import _compat
from .agents import evaluation_metrics  # type: ignore  # noqa: F401
from .models import providers  # type: ignore  # noqa: F401
from .shared import (
    Size as Size,
    Image as Image,
    Action as Action,
    Kernel as Kernel,
    Region as Region,
    APIMeta as APIMeta,
    Droplet as Droplet,
    GPUInfo as GPUInfo,
    APILinks as APILinks,
    DiskInfo as DiskInfo,
    NetworkV4 as NetworkV4,
    NetworkV6 as NetworkV6,
    PageLinks as PageLinks,
    Snapshots as Snapshots,
    ActionLink as ActionLink,
    VpcPeering as VpcPeering,
    ForwardLinks as ForwardLinks,
    Subscription as Subscription,
    BackwardLinks as BackwardLinks,
    MetaProperties as MetaProperties,
    CompletionUsage as CompletionUsage,
    GarbageCollection as GarbageCollection,
    FirewallRuleTarget as FirewallRuleTarget,
    ChatCompletionChunk as ChatCompletionChunk,
    ImageGenStreamEvent as ImageGenStreamEvent,
    SubscriptionTierBase as SubscriptionTierBase,
    ImageGenCompletedEvent as ImageGenCompletedEvent,
    DropletNextBackupWindow as DropletNextBackupWindow,
    ImageGenPartialImageEvent as ImageGenPartialImageEvent,
    ChatCompletionTokenLogprob as ChatCompletionTokenLogprob,
)
from .api_agent import APIAgent as APIAgent
from .api_model import APIModel as APIModel
from .api_agreement import APIAgreement as APIAgreement
from .api_workspace import APIWorkspace as APIWorkspace
from .nf_list_params import NfListParams as NfListParams
from .api_agent_model import APIAgentModel as APIAgentModel
from .nf_create_params import NfCreateParams as NfCreateParams
from .nf_delete_params import NfDeleteParams as NfDeleteParams
from .nf_list_response import NfListResponse as NfListResponse
from .agent_list_params import AgentListParams as AgentListParams
from .api_model_version import APIModelVersion as APIModelVersion
from .model_list_params import ModelListParams as ModelListParams
from .api_knowledge_base import APIKnowledgeBase as APIKnowledgeBase
from .nf_create_response import NfCreateResponse as NfCreateResponse
from .nf_retrieve_params import NfRetrieveParams as NfRetrieveParams
from .region_list_params import RegionListParams as RegionListParams
from .agent_create_params import AgentCreateParams as AgentCreateParams
from .agent_list_response import AgentListResponse as AgentListResponse
from .agent_update_params import AgentUpdateParams as AgentUpdateParams
from .model_list_response import ModelListResponse as ModelListResponse
from .api_retrieval_method import APIRetrievalMethod as APIRetrievalMethod
from .nf_retrieve_response import NfRetrieveResponse as NfRetrieveResponse
from .region_list_response import RegionListResponse as RegionListResponse
from .agent_create_response import AgentCreateResponse as AgentCreateResponse
from .agent_delete_response import AgentDeleteResponse as AgentDeleteResponse
from .agent_update_response import AgentUpdateResponse as AgentUpdateResponse
from .droplet_backup_policy import DropletBackupPolicy as DropletBackupPolicy
from .image_generate_params import ImageGenerateParams as ImageGenerateParams
from .api_agent_api_key_info import APIAgentAPIKeyInfo as APIAgentAPIKeyInfo
from .agent_retrieve_response import AgentRetrieveResponse as AgentRetrieveResponse
from .api_openai_api_key_info import APIOpenAIAPIKeyInfo as APIOpenAIAPIKeyInfo
from .gpu_droplet_list_params import GPUDropletListParams as GPUDropletListParams
from .image_generate_response import ImageGenerateResponse as ImageGenerateResponse
from .api_deployment_visibility import APIDeploymentVisibility as APIDeploymentVisibility
from .gpu_droplet_create_params import GPUDropletCreateParams as GPUDropletCreateParams
from .gpu_droplet_list_response import GPUDropletListResponse as GPUDropletListResponse
from .nf_initiate_action_params import NfInitiateActionParams as NfInitiateActionParams
from .retrieve_documents_params import RetrieveDocumentsParams as RetrieveDocumentsParams
from .agent_update_status_params import (
    AgentUpdateStatusParams as AgentUpdateStatusParams,
)
from .api_anthropic_api_key_info import APIAnthropicAPIKeyInfo as APIAnthropicAPIKeyInfo
from .knowledge_base_list_params import (
    KnowledgeBaseListParams as KnowledgeBaseListParams,
)
from .agent_retrieve_usage_params import AgentRetrieveUsageParams as AgentRetrieveUsageParams
from .droplet_backup_policy_param import (
    DropletBackupPolicyParam as DropletBackupPolicyParam,
)
from .gpu_droplet_create_response import (
    GPUDropletCreateResponse as GPUDropletCreateResponse,
)
from .nf_initiate_action_response import NfInitiateActionResponse as NfInitiateActionResponse
from .retrieve_documents_response import RetrieveDocumentsResponse as RetrieveDocumentsResponse
from .agent_update_status_response import (
    AgentUpdateStatusResponse as AgentUpdateStatusResponse,
)
from .knowledge_base_create_params import (
    KnowledgeBaseCreateParams as KnowledgeBaseCreateParams,
)
from .knowledge_base_list_response import (
    KnowledgeBaseListResponse as KnowledgeBaseListResponse,
)
from .knowledge_base_update_params import (
    KnowledgeBaseUpdateParams as KnowledgeBaseUpdateParams,
)
from .agent_retrieve_usage_response import AgentRetrieveUsageResponse as AgentRetrieveUsageResponse
from .gpu_droplet_retrieve_response import (
    GPUDropletRetrieveResponse as GPUDropletRetrieveResponse,
)
from .knowledge_base_create_response import (
    KnowledgeBaseCreateResponse as KnowledgeBaseCreateResponse,
)
from .knowledge_base_delete_response import (
    KnowledgeBaseDeleteResponse as KnowledgeBaseDeleteResponse,
)
from .knowledge_base_update_response import (
    KnowledgeBaseUpdateResponse as KnowledgeBaseUpdateResponse,
)
from .gpu_droplet_list_kernels_params import (
    GPUDropletListKernelsParams as GPUDropletListKernelsParams,
)
from .agents.evaluation_metrics.openai import (
    key_list_agents_response,  # type: ignore  # noqa: F401
)
from .gpu_droplet_delete_by_tag_params import (
    GPUDropletDeleteByTagParams as GPUDropletDeleteByTagParams,
)
from .knowledge_base_retrieve_response import (
    KnowledgeBaseRetrieveResponse as KnowledgeBaseRetrieveResponse,
)
from .gpu_droplet_list_firewalls_params import (
    GPUDropletListFirewallsParams as GPUDropletListFirewallsParams,
)
from .gpu_droplet_list_kernels_response import (
    GPUDropletListKernelsResponse as GPUDropletListKernelsResponse,
)
from .gpu_droplet_list_snapshots_params import (
    GPUDropletListSnapshotsParams as GPUDropletListSnapshotsParams,
)
from .agents.evaluation_metrics.anthropic import (
    key_list_response,  # type: ignore  # noqa: F401
)
from .gpu_droplet_list_firewalls_response import (
    GPUDropletListFirewallsResponse as GPUDropletListFirewallsResponse,
)
from .gpu_droplet_list_neighbors_response import (
    GPUDropletListNeighborsResponse as GPUDropletListNeighborsResponse,
)
from .gpu_droplet_list_snapshots_response import (
    GPUDropletListSnapshotsResponse as GPUDropletListSnapshotsResponse,
)
from .agents.evaluation_metrics.workspaces import (
    agent_list_response,  # type: ignore  # noqa: F401
    agent_move_response,  # type: ignore  # noqa: F401
)
from .knowledge_base_list_indexing_jobs_response import (
    KnowledgeBaseListIndexingJobsResponse as KnowledgeBaseListIndexingJobsResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    api_agent.APIAgent.update_forward_refs()  # type: ignore
    api_workspace.APIWorkspace.update_forward_refs()  # type: ignore
    agent_create_response.AgentCreateResponse.update_forward_refs()  # type: ignore
    agent_retrieve_response.AgentRetrieveResponse.update_forward_refs()  # type: ignore
    agent_update_response.AgentUpdateResponse.update_forward_refs()  # type: ignore
    agent_delete_response.AgentDeleteResponse.update_forward_refs()  # type: ignore
    agent_update_status_response.AgentUpdateStatusResponse.update_forward_refs()  # type: ignore
    agents.evaluation_metrics.workspace_create_response.WorkspaceCreateResponse.update_forward_refs()  # type: ignore
    agents.evaluation_metrics.workspace_retrieve_response.WorkspaceRetrieveResponse.update_forward_refs()  # type: ignore
    agents.evaluation_metrics.workspace_update_response.WorkspaceUpdateResponse.update_forward_refs()  # type: ignore
    agents.evaluation_metrics.workspace_list_response.WorkspaceListResponse.update_forward_refs()  # type: ignore
    agents.evaluation_metrics.workspaces.agent_list_response.AgentListResponse.update_forward_refs()  # type: ignore
    agents.evaluation_metrics.workspaces.agent_move_response.AgentMoveResponse.update_forward_refs()  # type: ignore
    agents.evaluation_metrics.anthropic.key_list_agents_response.KeyListAgentsResponse.update_forward_refs()  # type: ignore
    agents.evaluation_metrics.openai.key_list_agents_response.KeyListAgentsResponse.update_forward_refs()  # type: ignore
    agents.function_create_response.FunctionCreateResponse.update_forward_refs()  # type: ignore
    agents.function_update_response.FunctionUpdateResponse.update_forward_refs()  # type: ignore
    agents.function_delete_response.FunctionDeleteResponse.update_forward_refs()  # type: ignore
    agents.api_link_knowledge_base_output.APILinkKnowledgeBaseOutput.update_forward_refs()  # type: ignore
    agents.knowledge_base_detach_response.KnowledgeBaseDetachResponse.update_forward_refs()  # type: ignore
    agents.route_view_response.RouteViewResponse.update_forward_refs()  # type: ignore
    models.providers.anthropic_list_agents_response.AnthropicListAgentsResponse.update_forward_refs()  # type: ignore
    models.providers.openai_retrieve_agents_response.OpenAIRetrieveAgentsResponse.update_forward_refs()  # type: ignore
else:
    api_agent.APIAgent.model_rebuild(_parent_namespace_depth=0)
    api_workspace.APIWorkspace.model_rebuild(_parent_namespace_depth=0)
    agent_create_response.AgentCreateResponse.model_rebuild(_parent_namespace_depth=0)
    agent_retrieve_response.AgentRetrieveResponse.model_rebuild(_parent_namespace_depth=0)
    agent_update_response.AgentUpdateResponse.model_rebuild(_parent_namespace_depth=0)
    agent_delete_response.AgentDeleteResponse.model_rebuild(_parent_namespace_depth=0)
    agent_update_status_response.AgentUpdateStatusResponse.model_rebuild(_parent_namespace_depth=0)
    agents.evaluation_metrics.workspace_create_response.WorkspaceCreateResponse.model_rebuild(_parent_namespace_depth=0)
    agents.evaluation_metrics.workspace_retrieve_response.WorkspaceRetrieveResponse.model_rebuild(
        _parent_namespace_depth=0
    )
    agents.evaluation_metrics.workspace_update_response.WorkspaceUpdateResponse.model_rebuild(_parent_namespace_depth=0)
    agents.evaluation_metrics.workspace_list_response.WorkspaceListResponse.model_rebuild(_parent_namespace_depth=0)
    agents.evaluation_metrics.workspaces.agent_list_response.AgentListResponse.model_rebuild(_parent_namespace_depth=0)
    agents.evaluation_metrics.workspaces.agent_move_response.AgentMoveResponse.model_rebuild(_parent_namespace_depth=0)
    agents.evaluation_metrics.anthropic.key_list_agents_response.KeyListAgentsResponse.model_rebuild(
        _parent_namespace_depth=0
    )
    agents.evaluation_metrics.openai.key_list_agents_response.KeyListAgentsResponse.model_rebuild(
        _parent_namespace_depth=0
    )
    agents.function_create_response.FunctionCreateResponse.model_rebuild(_parent_namespace_depth=0)
    agents.function_update_response.FunctionUpdateResponse.model_rebuild(_parent_namespace_depth=0)
    agents.function_delete_response.FunctionDeleteResponse.model_rebuild(_parent_namespace_depth=0)
    agents.api_link_knowledge_base_output.APILinkKnowledgeBaseOutput.model_rebuild(_parent_namespace_depth=0)
    agents.knowledge_base_detach_response.KnowledgeBaseDetachResponse.model_rebuild(_parent_namespace_depth=0)
    agents.route_view_response.RouteViewResponse.model_rebuild(_parent_namespace_depth=0)
    models.providers.anthropic_list_agents_response.AnthropicListAgentsResponse.model_rebuild(_parent_namespace_depth=0)
    models.providers.openai_retrieve_agents_response.OpenAIRetrieveAgentsResponse.model_rebuild(
        _parent_namespace_depth=0
    )
