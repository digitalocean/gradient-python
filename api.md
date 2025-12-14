# Shared Types

```python
from gradient.types import (
    Action,
    ActionLink,
    APILinks,
    APIMeta,
    BackwardLinks,
    ChatCompletionChunk,
    ChatCompletionTokenLogprob,
    CompletionUsage,
    DiskInfo,
    Droplet,
    DropletNextBackupWindow,
    FirewallRuleTarget,
    ForwardLinks,
    GarbageCollection,
    GPUInfo,
    Image,
    ImageGenCompletedEvent,
    ImageGenPartialImageEvent,
    ImageGenStreamEvent,
    Kernel,
    MetaProperties,
    NetworkV4,
    NetworkV6,
    PageLinks,
    Region,
    Size,
    Snapshots,
    Subscription,
    SubscriptionTierBase,
    VpcPeering,
)
```

# Agents

Types:

```python
from gradient.types import (
    APIAgent,
    APIAgentAPIKeyInfo,
    APIAgentModel,
    APIAnthropicAPIKeyInfo,
    APIDeploymentVisibility,
    APIOpenAIAPIKeyInfo,
    APIRetrievalMethod,
    APIWorkspace,
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentListResponse,
    AgentDeleteResponse,
    AgentRetrieveUsageResponse,
    AgentUpdateStatusResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/agents">client.agents.<a href="./src/gradient/resources/agents/agents.py">create</a>(\*\*<a href="src/gradient/types/agent_create_params.py">params</a>) -> <a href="./src/gradient/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /v2/gen-ai/agents/{uuid}">client.agents.<a href="./src/gradient/resources/agents/agents.py">retrieve</a>(uuid) -> <a href="./src/gradient/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/agents/{uuid}">client.agents.<a href="./src/gradient/resources/agents/agents.py">update</a>(path_uuid, \*\*<a href="src/gradient/types/agent_update_params.py">params</a>) -> <a href="./src/gradient/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /v2/gen-ai/agents">client.agents.<a href="./src/gradient/resources/agents/agents.py">list</a>(\*\*<a href="src/gradient/types/agent_list_params.py">params</a>) -> <a href="./src/gradient/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v2/gen-ai/agents/{uuid}">client.agents.<a href="./src/gradient/resources/agents/agents.py">delete</a>(uuid) -> <a href="./src/gradient/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="get /v2/gen-ai/agents/{uuid}/usage">client.agents.<a href="./src/gradient/resources/agents/agents.py">retrieve_usage</a>(uuid, \*\*<a href="src/gradient/types/agent_retrieve_usage_params.py">params</a>) -> <a href="./src/gradient/types/agent_retrieve_usage_response.py">AgentRetrieveUsageResponse</a></code>
- <code title="put /v2/gen-ai/agents/{uuid}/deployment_visibility">client.agents.<a href="./src/gradient/resources/agents/agents.py">update_status</a>(path_uuid, \*\*<a href="src/gradient/types/agent_update_status_params.py">params</a>) -> <a href="./src/gradient/types/agent_update_status_response.py">AgentUpdateStatusResponse</a></code>

## APIKeys

Types:

```python
from gradient.types.agents import (
    APIKeyCreateResponse,
    APIKeyUpdateResponse,
    APIKeyListResponse,
    APIKeyDeleteResponse,
    APIKeyRegenerateResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/agents/{agent_uuid}/api_keys">client.agents.api_keys.<a href="./src/gradient/resources/agents/api_keys.py">create</a>(path_agent_uuid, \*\*<a href="src/gradient/types/agents/api_key_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="put /v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}">client.agents.api_keys.<a href="./src/gradient/resources/agents/api_keys.py">update</a>(path_api_key_uuid, \*, path_agent_uuid, \*\*<a href="src/gradient/types/agents/api_key_update_params.py">params</a>) -> <a href="./src/gradient/types/agents/api_key_update_response.py">APIKeyUpdateResponse</a></code>
- <code title="get /v2/gen-ai/agents/{agent_uuid}/api_keys">client.agents.api_keys.<a href="./src/gradient/resources/agents/api_keys.py">list</a>(agent_uuid, \*\*<a href="src/gradient/types/agents/api_key_list_params.py">params</a>) -> <a href="./src/gradient/types/agents/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}">client.agents.api_keys.<a href="./src/gradient/resources/agents/api_keys.py">delete</a>(api_key_uuid, \*, agent_uuid) -> <a href="./src/gradient/types/agents/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
- <code title="put /v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate">client.agents.api_keys.<a href="./src/gradient/resources/agents/api_keys.py">regenerate</a>(api_key_uuid, \*, agent_uuid) -> <a href="./src/gradient/types/agents/api_key_regenerate_response.py">APIKeyRegenerateResponse</a></code>

## Chat

### Completions

Types:

```python
from gradient.types.agents.chat import CompletionCreateResponse
```

Methods:

- <code title="post /chat/completions?agent=true">client.agents.chat.completions.<a href="./src/gradient/resources/agents/chat/completions.py">create</a>(\*\*<a href="src/gradient/types/agents/chat/completion_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/chat/completion_create_response.py">CompletionCreateResponse</a></code>

## EvaluationMetrics

Types:

```python
from gradient.types.agents import EvaluationMetricListResponse, EvaluationMetricListRegionsResponse
```

Methods:

- <code title="get /v2/gen-ai/evaluation_metrics">client.agents.evaluation_metrics.<a href="./src/gradient/resources/agents/evaluation_metrics/evaluation_metrics.py">list</a>() -> <a href="./src/gradient/types/agents/evaluation_metric_list_response.py">EvaluationMetricListResponse</a></code>
- <code title="get /v2/gen-ai/regions">client.agents.evaluation_metrics.<a href="./src/gradient/resources/agents/evaluation_metrics/evaluation_metrics.py">list_regions</a>(\*\*<a href="src/gradient/types/agents/evaluation_metric_list_regions_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metric_list_regions_response.py">EvaluationMetricListRegionsResponse</a></code>

### Workspaces

Types:

```python
from gradient.types.agents.evaluation_metrics import (
    WorkspaceCreateResponse,
    WorkspaceRetrieveResponse,
    WorkspaceUpdateResponse,
    WorkspaceListResponse,
    WorkspaceDeleteResponse,
    WorkspaceListEvaluationTestCasesResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/workspaces">client.agents.evaluation_metrics.workspaces.<a href="./src/gradient/resources/agents/evaluation_metrics/workspaces/workspaces.py">create</a>(\*\*<a href="src/gradient/types/agents/evaluation_metrics/workspace_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/workspace_create_response.py">WorkspaceCreateResponse</a></code>
- <code title="get /v2/gen-ai/workspaces/{workspace_uuid}">client.agents.evaluation_metrics.workspaces.<a href="./src/gradient/resources/agents/evaluation_metrics/workspaces/workspaces.py">retrieve</a>(workspace_uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/workspace_retrieve_response.py">WorkspaceRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/workspaces/{workspace_uuid}">client.agents.evaluation_metrics.workspaces.<a href="./src/gradient/resources/agents/evaluation_metrics/workspaces/workspaces.py">update</a>(path_workspace_uuid, \*\*<a href="src/gradient/types/agents/evaluation_metrics/workspace_update_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/workspace_update_response.py">WorkspaceUpdateResponse</a></code>
- <code title="get /v2/gen-ai/workspaces">client.agents.evaluation_metrics.workspaces.<a href="./src/gradient/resources/agents/evaluation_metrics/workspaces/workspaces.py">list</a>() -> <a href="./src/gradient/types/agents/evaluation_metrics/workspace_list_response.py">WorkspaceListResponse</a></code>
- <code title="delete /v2/gen-ai/workspaces/{workspace_uuid}">client.agents.evaluation_metrics.workspaces.<a href="./src/gradient/resources/agents/evaluation_metrics/workspaces/workspaces.py">delete</a>(workspace_uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/workspace_delete_response.py">WorkspaceDeleteResponse</a></code>
- <code title="get /v2/gen-ai/workspaces/{workspace_uuid}/evaluation_test_cases">client.agents.evaluation_metrics.workspaces.<a href="./src/gradient/resources/agents/evaluation_metrics/workspaces/workspaces.py">list_evaluation_test_cases</a>(workspace_uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/workspace_list_evaluation_test_cases_response.py">WorkspaceListEvaluationTestCasesResponse</a></code>

#### Agents

Types:

```python
from gradient.types.agents.evaluation_metrics.workspaces import AgentListResponse, AgentMoveResponse
```

Methods:

- <code title="get /v2/gen-ai/workspaces/{workspace_uuid}/agents">client.agents.evaluation_metrics.workspaces.agents.<a href="./src/gradient/resources/agents/evaluation_metrics/workspaces/agents.py">list</a>(workspace_uuid, \*\*<a href="src/gradient/types/agents/evaluation_metrics/workspaces/agent_list_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/workspaces/agent_list_response.py">AgentListResponse</a></code>
- <code title="put /v2/gen-ai/workspaces/{workspace_uuid}/agents">client.agents.evaluation_metrics.workspaces.agents.<a href="./src/gradient/resources/agents/evaluation_metrics/workspaces/agents.py">move</a>(path_workspace_uuid, \*\*<a href="src/gradient/types/agents/evaluation_metrics/workspaces/agent_move_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/workspaces/agent_move_response.py">AgentMoveResponse</a></code>

### Anthropic

#### Keys

Types:

```python
from gradient.types.agents.evaluation_metrics.anthropic import (
    KeyCreateResponse,
    KeyRetrieveResponse,
    KeyUpdateResponse,
    KeyListResponse,
    KeyDeleteResponse,
    KeyListAgentsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/anthropic/keys">client.agents.evaluation_metrics.anthropic.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/anthropic/keys.py">create</a>(\*\*<a href="src/gradient/types/agents/evaluation_metrics/anthropic/key_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/anthropic/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.agents.evaluation_metrics.anthropic.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/anthropic/keys.py">retrieve</a>(api_key_uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/anthropic/key_retrieve_response.py">KeyRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.agents.evaluation_metrics.anthropic.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/anthropic/keys.py">update</a>(path_api_key_uuid, \*\*<a href="src/gradient/types/agents/evaluation_metrics/anthropic/key_update_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/anthropic/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys">client.agents.evaluation_metrics.anthropic.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/anthropic/keys.py">list</a>(\*\*<a href="src/gradient/types/agents/evaluation_metrics/anthropic/key_list_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/anthropic/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.agents.evaluation_metrics.anthropic.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/anthropic/keys.py">delete</a>(api_key_uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/anthropic/key_delete_response.py">KeyDeleteResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys/{uuid}/agents">client.agents.evaluation_metrics.anthropic.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/anthropic/keys.py">list_agents</a>(uuid, \*\*<a href="src/gradient/types/agents/evaluation_metrics/anthropic/key_list_agents_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/anthropic/key_list_agents_response.py">KeyListAgentsResponse</a></code>

### OpenAI

#### Keys

Types:

```python
from gradient.types.agents.evaluation_metrics.openai import (
    KeyCreateResponse,
    KeyRetrieveResponse,
    KeyUpdateResponse,
    KeyListResponse,
    KeyDeleteResponse,
    KeyListAgentsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/openai/keys">client.agents.evaluation_metrics.openai.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/openai/keys.py">create</a>(\*\*<a href="src/gradient/types/agents/evaluation_metrics/openai/key_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/openai/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys/{api_key_uuid}">client.agents.evaluation_metrics.openai.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/openai/keys.py">retrieve</a>(api_key_uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/openai/key_retrieve_response.py">KeyRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/openai/keys/{api_key_uuid}">client.agents.evaluation_metrics.openai.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/openai/keys.py">update</a>(path_api_key_uuid, \*\*<a href="src/gradient/types/agents/evaluation_metrics/openai/key_update_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/openai/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys">client.agents.evaluation_metrics.openai.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/openai/keys.py">list</a>(\*\*<a href="src/gradient/types/agents/evaluation_metrics/openai/key_list_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/openai/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /v2/gen-ai/openai/keys/{api_key_uuid}">client.agents.evaluation_metrics.openai.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/openai/keys.py">delete</a>(api_key_uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/openai/key_delete_response.py">KeyDeleteResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys/{uuid}/agents">client.agents.evaluation_metrics.openai.keys.<a href="./src/gradient/resources/agents/evaluation_metrics/openai/keys.py">list_agents</a>(uuid, \*\*<a href="src/gradient/types/agents/evaluation_metrics/openai/key_list_agents_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/openai/key_list_agents_response.py">KeyListAgentsResponse</a></code>

### Oauth2

Types:

```python
from gradient.types.agents.evaluation_metrics import Oauth2GenerateURLResponse
```

Methods:

- <code title="get /v2/gen-ai/oauth2/url">client.agents.evaluation_metrics.oauth2.<a href="./src/gradient/resources/agents/evaluation_metrics/oauth2/oauth2.py">generate_url</a>(\*\*<a href="src/gradient/types/agents/evaluation_metrics/oauth2_generate_url_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/oauth2_generate_url_response.py">Oauth2GenerateURLResponse</a></code>

#### Dropbox

Types:

```python
from gradient.types.agents.evaluation_metrics.oauth2 import DropboxCreateTokensResponse
```

Methods:

- <code title="post /v2/gen-ai/oauth2/dropbox/tokens">client.agents.evaluation_metrics.oauth2.dropbox.<a href="./src/gradient/resources/agents/evaluation_metrics/oauth2/dropbox.py">create_tokens</a>(\*\*<a href="src/gradient/types/agents/evaluation_metrics/oauth2/dropbox_create_tokens_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/oauth2/dropbox_create_tokens_response.py">DropboxCreateTokensResponse</a></code>

### ScheduledIndexing

Types:

```python
from gradient.types.agents.evaluation_metrics import (
    ScheduledIndexingCreateResponse,
    ScheduledIndexingRetrieveResponse,
    ScheduledIndexingDeleteResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/scheduled-indexing">client.agents.evaluation_metrics.scheduled_indexing.<a href="./src/gradient/resources/agents/evaluation_metrics/scheduled_indexing.py">create</a>(\*\*<a href="src/gradient/types/agents/evaluation_metrics/scheduled_indexing_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_metrics/scheduled_indexing_create_response.py">ScheduledIndexingCreateResponse</a></code>
- <code title="get /v2/gen-ai/scheduled-indexing/knowledge-base/{knowledge_base_uuid}">client.agents.evaluation_metrics.scheduled_indexing.<a href="./src/gradient/resources/agents/evaluation_metrics/scheduled_indexing.py">retrieve</a>(knowledge_base_uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/scheduled_indexing_retrieve_response.py">ScheduledIndexingRetrieveResponse</a></code>
- <code title="delete /v2/gen-ai/scheduled-indexing/{uuid}">client.agents.evaluation_metrics.scheduled_indexing.<a href="./src/gradient/resources/agents/evaluation_metrics/scheduled_indexing.py">delete</a>(uuid) -> <a href="./src/gradient/types/agents/evaluation_metrics/scheduled_indexing_delete_response.py">ScheduledIndexingDeleteResponse</a></code>

## EvaluationRuns

Types:

```python
from gradient.types.agents import (
    APIEvaluationMetric,
    APIEvaluationMetricResult,
    APIEvaluationPrompt,
    APIEvaluationRun,
    EvaluationRunCreateResponse,
    EvaluationRunRetrieveResponse,
    EvaluationRunListResultsResponse,
    EvaluationRunRetrieveResultsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/evaluation_runs">client.agents.evaluation_runs.<a href="./src/gradient/resources/agents/evaluation_runs.py">create</a>(\*\*<a href="src/gradient/types/agents/evaluation_run_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_run_create_response.py">EvaluationRunCreateResponse</a></code>
- <code title="get /v2/gen-ai/evaluation_runs/{evaluation_run_uuid}">client.agents.evaluation_runs.<a href="./src/gradient/resources/agents/evaluation_runs.py">retrieve</a>(evaluation_run_uuid) -> <a href="./src/gradient/types/agents/evaluation_run_retrieve_response.py">EvaluationRunRetrieveResponse</a></code>
- <code title="get /v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results">client.agents.evaluation_runs.<a href="./src/gradient/resources/agents/evaluation_runs.py">list_results</a>(evaluation_run_uuid, \*\*<a href="src/gradient/types/agents/evaluation_run_list_results_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_run_list_results_response.py">EvaluationRunListResultsResponse</a></code>
- <code title="get /v2/gen-ai/evaluation_runs/{evaluation_run_uuid}/results/{prompt_id}">client.agents.evaluation_runs.<a href="./src/gradient/resources/agents/evaluation_runs.py">retrieve_results</a>(prompt_id, \*, evaluation_run_uuid) -> <a href="./src/gradient/types/agents/evaluation_run_retrieve_results_response.py">EvaluationRunRetrieveResultsResponse</a></code>

## EvaluationTestCases

Types:

```python
from gradient.types.agents import (
    APIEvaluationTestCase,
    APIStarMetric,
    EvaluationTestCaseCreateResponse,
    EvaluationTestCaseRetrieveResponse,
    EvaluationTestCaseUpdateResponse,
    EvaluationTestCaseListResponse,
    EvaluationTestCaseListEvaluationRunsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/evaluation_test_cases">client.agents.evaluation_test_cases.<a href="./src/gradient/resources/agents/evaluation_test_cases.py">create</a>(\*\*<a href="src/gradient/types/agents/evaluation_test_case_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_test_case_create_response.py">EvaluationTestCaseCreateResponse</a></code>
- <code title="get /v2/gen-ai/evaluation_test_cases/{test_case_uuid}">client.agents.evaluation_test_cases.<a href="./src/gradient/resources/agents/evaluation_test_cases.py">retrieve</a>(test_case_uuid, \*\*<a href="src/gradient/types/agents/evaluation_test_case_retrieve_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_test_case_retrieve_response.py">EvaluationTestCaseRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/evaluation_test_cases/{test_case_uuid}">client.agents.evaluation_test_cases.<a href="./src/gradient/resources/agents/evaluation_test_cases.py">update</a>(path_test_case_uuid, \*\*<a href="src/gradient/types/agents/evaluation_test_case_update_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_test_case_update_response.py">EvaluationTestCaseUpdateResponse</a></code>
- <code title="get /v2/gen-ai/evaluation_test_cases">client.agents.evaluation_test_cases.<a href="./src/gradient/resources/agents/evaluation_test_cases.py">list</a>() -> <a href="./src/gradient/types/agents/evaluation_test_case_list_response.py">EvaluationTestCaseListResponse</a></code>
- <code title="get /v2/gen-ai/evaluation_test_cases/{evaluation_test_case_uuid}/evaluation_runs">client.agents.evaluation_test_cases.<a href="./src/gradient/resources/agents/evaluation_test_cases.py">list_evaluation_runs</a>(evaluation_test_case_uuid, \*\*<a href="src/gradient/types/agents/evaluation_test_case_list_evaluation_runs_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_test_case_list_evaluation_runs_response.py">EvaluationTestCaseListEvaluationRunsResponse</a></code>

## EvaluationDatasets

Types:

```python
from gradient.types.agents import (
    EvaluationDatasetCreateResponse,
    EvaluationDatasetCreateFileUploadPresignedURLsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/evaluation_datasets">client.agents.evaluation_datasets.<a href="./src/gradient/resources/agents/evaluation_datasets.py">create</a>(\*\*<a href="src/gradient/types/agents/evaluation_dataset_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_dataset_create_response.py">EvaluationDatasetCreateResponse</a></code>
- <code title="post /v2/gen-ai/evaluation_datasets/file_upload_presigned_urls">client.agents.evaluation_datasets.<a href="./src/gradient/resources/agents/evaluation_datasets.py">create_file_upload_presigned_urls</a>(\*\*<a href="src/gradient/types/agents/evaluation_dataset_create_file_upload_presigned_urls_params.py">params</a>) -> <a href="./src/gradient/types/agents/evaluation_dataset_create_file_upload_presigned_urls_response.py">EvaluationDatasetCreateFileUploadPresignedURLsResponse</a></code>

## Functions

Types:

```python
from gradient.types.agents import (
    FunctionCreateResponse,
    FunctionUpdateResponse,
    FunctionDeleteResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/agents/{agent_uuid}/functions">client.agents.functions.<a href="./src/gradient/resources/agents/functions.py">create</a>(path_agent_uuid, \*\*<a href="src/gradient/types/agents/function_create_params.py">params</a>) -> <a href="./src/gradient/types/agents/function_create_response.py">FunctionCreateResponse</a></code>
- <code title="put /v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}">client.agents.functions.<a href="./src/gradient/resources/agents/functions.py">update</a>(path_function_uuid, \*, path_agent_uuid, \*\*<a href="src/gradient/types/agents/function_update_params.py">params</a>) -> <a href="./src/gradient/types/agents/function_update_response.py">FunctionUpdateResponse</a></code>
- <code title="delete /v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}">client.agents.functions.<a href="./src/gradient/resources/agents/functions.py">delete</a>(function_uuid, \*, agent_uuid) -> <a href="./src/gradient/types/agents/function_delete_response.py">FunctionDeleteResponse</a></code>

## Versions

Types:

```python
from gradient.types.agents import VersionUpdateResponse, VersionListResponse
```

Methods:

- <code title="put /v2/gen-ai/agents/{uuid}/versions">client.agents.versions.<a href="./src/gradient/resources/agents/versions.py">update</a>(path_uuid, \*\*<a href="src/gradient/types/agents/version_update_params.py">params</a>) -> <a href="./src/gradient/types/agents/version_update_response.py">VersionUpdateResponse</a></code>
- <code title="get /v2/gen-ai/agents/{uuid}/versions">client.agents.versions.<a href="./src/gradient/resources/agents/versions.py">list</a>(uuid, \*\*<a href="src/gradient/types/agents/version_list_params.py">params</a>) -> <a href="./src/gradient/types/agents/version_list_response.py">VersionListResponse</a></code>

## KnowledgeBases

Types:

```python
from gradient.types.agents import APILinkKnowledgeBaseOutput, KnowledgeBaseDetachResponse
```

Methods:

- <code title="post /v2/gen-ai/agents/{agent_uuid}/knowledge_bases">client.agents.knowledge_bases.<a href="./src/gradient/resources/agents/knowledge_bases.py">attach</a>(agent_uuid) -> <a href="./src/gradient/types/agents/api_link_knowledge_base_output.py">APILinkKnowledgeBaseOutput</a></code>
- <code title="post /v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}">client.agents.knowledge_bases.<a href="./src/gradient/resources/agents/knowledge_bases.py">attach_single</a>(knowledge_base_uuid, \*, agent_uuid) -> <a href="./src/gradient/types/agents/api_link_knowledge_base_output.py">APILinkKnowledgeBaseOutput</a></code>
- <code title="delete /v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}">client.agents.knowledge_bases.<a href="./src/gradient/resources/agents/knowledge_bases.py">detach</a>(knowledge_base_uuid, \*, agent_uuid) -> <a href="./src/gradient/types/agents/knowledge_base_detach_response.py">KnowledgeBaseDetachResponse</a></code>

## Routes

Types:

```python
from gradient.types.agents import (
    RouteUpdateResponse,
    RouteDeleteResponse,
    RouteAddResponse,
    RouteViewResponse,
)
```

Methods:

- <code title="put /v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}">client.agents.routes.<a href="./src/gradient/resources/agents/routes.py">update</a>(path_child_agent_uuid, \*, path_parent_agent_uuid, \*\*<a href="src/gradient/types/agents/route_update_params.py">params</a>) -> <a href="./src/gradient/types/agents/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="delete /v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}">client.agents.routes.<a href="./src/gradient/resources/agents/routes.py">delete</a>(child_agent_uuid, \*, parent_agent_uuid) -> <a href="./src/gradient/types/agents/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="post /v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}">client.agents.routes.<a href="./src/gradient/resources/agents/routes.py">add</a>(path_child_agent_uuid, \*, path_parent_agent_uuid, \*\*<a href="src/gradient/types/agents/route_add_params.py">params</a>) -> <a href="./src/gradient/types/agents/route_add_response.py">RouteAddResponse</a></code>
- <code title="get /v2/gen-ai/agents/{uuid}/child_agents">client.agents.routes.<a href="./src/gradient/resources/agents/routes.py">view</a>(uuid) -> <a href="./src/gradient/types/agents/route_view_response.py">RouteViewResponse</a></code>

# Chat

## Completions

Types:

```python
from gradient.types.chat import CompletionCreateResponse
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/gradient/resources/chat/completions.py">create</a>(\*\*<a href="src/gradient/types/chat/completion_create_params.py">params</a>) -> <a href="./src/gradient/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

# Images

Types:

```python
from gradient.types import ImageGenerateResponse
```

Methods:

- <code title="post /images/generations">client.images.<a href="./src/gradient/resources/images.py">generate</a>(\*\*<a href="src/gradient/types/image_generate_params.py">params</a>) -> <a href="./src/gradient/types/image_generate_response.py">ImageGenerateResponse</a></code>

# GPUDroplets

Types:

```python
from gradient.types import (
    DropletBackupPolicy,
    GPUDropletCreateResponse,
    GPUDropletRetrieveResponse,
    GPUDropletListResponse,
    GPUDropletListFirewallsResponse,
    GPUDropletListKernelsResponse,
    GPUDropletListNeighborsResponse,
    GPUDropletListSnapshotsResponse,
)
```

Methods:

- <code title="post /v2/droplets">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">create</a>(\*\*<a href="src/gradient/types/gpu_droplet_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplet_create_response.py">GPUDropletCreateResponse</a></code>
- <code title="get /v2/droplets/{droplet_id}">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">retrieve</a>(droplet_id) -> <a href="./src/gradient/types/gpu_droplet_retrieve_response.py">GPUDropletRetrieveResponse</a></code>
- <code title="get /v2/droplets">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplet_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplet_list_response.py">GPUDropletListResponse</a></code>
- <code title="delete /v2/droplets/{droplet_id}">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">delete</a>(droplet_id) -> None</code>
- <code title="delete /v2/droplets">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">delete_by_tag</a>(\*\*<a href="src/gradient/types/gpu_droplet_delete_by_tag_params.py">params</a>) -> None</code>
- <code title="get /v2/droplets/{droplet_id}/firewalls">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">list_firewalls</a>(droplet_id, \*\*<a href="src/gradient/types/gpu_droplet_list_firewalls_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplet_list_firewalls_response.py">GPUDropletListFirewallsResponse</a></code>
- <code title="get /v2/droplets/{droplet_id}/kernels">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">list_kernels</a>(droplet_id, \*\*<a href="src/gradient/types/gpu_droplet_list_kernels_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplet_list_kernels_response.py">GPUDropletListKernelsResponse</a></code>
- <code title="get /v2/droplets/{droplet_id}/neighbors">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">list_neighbors</a>(droplet_id) -> <a href="./src/gradient/types/gpu_droplet_list_neighbors_response.py">GPUDropletListNeighborsResponse</a></code>
- <code title="get /v2/droplets/{droplet_id}/snapshots">client.gpu_droplets.<a href="./src/gradient/resources/gpu_droplets/gpu_droplets.py">list_snapshots</a>(droplet_id, \*\*<a href="src/gradient/types/gpu_droplet_list_snapshots_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplet_list_snapshots_response.py">GPUDropletListSnapshotsResponse</a></code>

## Backups

Types:

```python
from gradient.types.gpu_droplets import (
    BackupListResponse,
    BackupListPoliciesResponse,
    BackupListSupportedPoliciesResponse,
    BackupRetrievePolicyResponse,
)
```

Methods:

- <code title="get /v2/droplets/{droplet_id}/backups">client.gpu_droplets.backups.<a href="./src/gradient/resources/gpu_droplets/backups.py">list</a>(droplet_id, \*\*<a href="src/gradient/types/gpu_droplets/backup_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/backup_list_response.py">BackupListResponse</a></code>
- <code title="get /v2/droplets/backups/policies">client.gpu_droplets.backups.<a href="./src/gradient/resources/gpu_droplets/backups.py">list_policies</a>(\*\*<a href="src/gradient/types/gpu_droplets/backup_list_policies_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/backup_list_policies_response.py">BackupListPoliciesResponse</a></code>
- <code title="get /v2/droplets/backups/supported_policies">client.gpu_droplets.backups.<a href="./src/gradient/resources/gpu_droplets/backups.py">list_supported_policies</a>() -> <a href="./src/gradient/types/gpu_droplets/backup_list_supported_policies_response.py">BackupListSupportedPoliciesResponse</a></code>
- <code title="get /v2/droplets/{droplet_id}/backups/policy">client.gpu_droplets.backups.<a href="./src/gradient/resources/gpu_droplets/backups.py">retrieve_policy</a>(droplet_id) -> <a href="./src/gradient/types/gpu_droplets/backup_retrieve_policy_response.py">BackupRetrievePolicyResponse</a></code>

## Actions

Types:

```python
from gradient.types.gpu_droplets import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionBulkInitiateResponse,
    ActionInitiateResponse,
)
```

Methods:

- <code title="get /v2/droplets/{droplet_id}/actions/{action_id}">client.gpu_droplets.actions.<a href="./src/gradient/resources/gpu_droplets/actions.py">retrieve</a>(action_id, \*, droplet_id) -> <a href="./src/gradient/types/gpu_droplets/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /v2/droplets/{droplet_id}/actions">client.gpu_droplets.actions.<a href="./src/gradient/resources/gpu_droplets/actions.py">list</a>(droplet_id, \*\*<a href="src/gradient/types/gpu_droplets/action_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/action_list_response.py">ActionListResponse</a></code>
- <code title="post /v2/droplets/actions">client.gpu_droplets.actions.<a href="./src/gradient/resources/gpu_droplets/actions.py">bulk_initiate</a>(\*\*<a href="src/gradient/types/gpu_droplets/action_bulk_initiate_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/action_bulk_initiate_response.py">ActionBulkInitiateResponse</a></code>
- <code title="post /v2/droplets/{droplet_id}/actions">client.gpu_droplets.actions.<a href="./src/gradient/resources/gpu_droplets/actions.py">initiate</a>(droplet_id, \*\*<a href="src/gradient/types/gpu_droplets/action_initiate_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/action_initiate_response.py">ActionInitiateResponse</a></code>

## DestroyWithAssociatedResources

Types:

```python
from gradient.types.gpu_droplets import (
    AssociatedResource,
    DestroyedAssociatedResource,
    DestroyWithAssociatedResourceListResponse,
    DestroyWithAssociatedResourceCheckStatusResponse,
)
```

Methods:

- <code title="get /v2/droplets/{droplet_id}/destroy_with_associated_resources">client.gpu_droplets.destroy_with_associated_resources.<a href="./src/gradient/resources/gpu_droplets/destroy_with_associated_resources.py">list</a>(droplet_id) -> <a href="./src/gradient/types/gpu_droplets/destroy_with_associated_resource_list_response.py">DestroyWithAssociatedResourceListResponse</a></code>
- <code title="get /v2/droplets/{droplet_id}/destroy_with_associated_resources/status">client.gpu_droplets.destroy_with_associated_resources.<a href="./src/gradient/resources/gpu_droplets/destroy_with_associated_resources.py">check_status</a>(droplet_id) -> <a href="./src/gradient/types/gpu_droplets/destroy_with_associated_resource_check_status_response.py">DestroyWithAssociatedResourceCheckStatusResponse</a></code>
- <code title="delete /v2/droplets/{droplet_id}/destroy_with_associated_resources/dangerous">client.gpu_droplets.destroy_with_associated_resources.<a href="./src/gradient/resources/gpu_droplets/destroy_with_associated_resources.py">delete_dangerous</a>(droplet_id) -> None</code>
- <code title="delete /v2/droplets/{droplet_id}/destroy_with_associated_resources/selective">client.gpu_droplets.destroy_with_associated_resources.<a href="./src/gradient/resources/gpu_droplets/destroy_with_associated_resources.py">delete_selective</a>(droplet_id, \*\*<a href="src/gradient/types/gpu_droplets/destroy_with_associated_resource_delete_selective_params.py">params</a>) -> None</code>
- <code title="post /v2/droplets/{droplet_id}/destroy_with_associated_resources/retry">client.gpu_droplets.destroy_with_associated_resources.<a href="./src/gradient/resources/gpu_droplets/destroy_with_associated_resources.py">retry</a>(droplet_id) -> None</code>

## Autoscale

Types:

```python
from gradient.types.gpu_droplets import (
    AutoscalePool,
    AutoscalePoolDropletTemplate,
    AutoscalePoolDynamicConfig,
    AutoscalePoolStaticConfig,
    CurrentUtilization,
    AutoscaleCreateResponse,
    AutoscaleRetrieveResponse,
    AutoscaleUpdateResponse,
    AutoscaleListResponse,
    AutoscaleListHistoryResponse,
    AutoscaleListMembersResponse,
)
```

Methods:

- <code title="post /v2/droplets/autoscale">client.gpu_droplets.autoscale.<a href="./src/gradient/resources/gpu_droplets/autoscale.py">create</a>(\*\*<a href="src/gradient/types/gpu_droplets/autoscale_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/autoscale_create_response.py">AutoscaleCreateResponse</a></code>
- <code title="get /v2/droplets/autoscale/{autoscale_pool_id}">client.gpu_droplets.autoscale.<a href="./src/gradient/resources/gpu_droplets/autoscale.py">retrieve</a>(autoscale_pool_id) -> <a href="./src/gradient/types/gpu_droplets/autoscale_retrieve_response.py">AutoscaleRetrieveResponse</a></code>
- <code title="put /v2/droplets/autoscale/{autoscale_pool_id}">client.gpu_droplets.autoscale.<a href="./src/gradient/resources/gpu_droplets/autoscale.py">update</a>(autoscale_pool_id, \*\*<a href="src/gradient/types/gpu_droplets/autoscale_update_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/autoscale_update_response.py">AutoscaleUpdateResponse</a></code>
- <code title="get /v2/droplets/autoscale">client.gpu_droplets.autoscale.<a href="./src/gradient/resources/gpu_droplets/autoscale.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/autoscale_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/autoscale_list_response.py">AutoscaleListResponse</a></code>
- <code title="delete /v2/droplets/autoscale/{autoscale_pool_id}">client.gpu_droplets.autoscale.<a href="./src/gradient/resources/gpu_droplets/autoscale.py">delete</a>(autoscale_pool_id) -> None</code>
- <code title="delete /v2/droplets/autoscale/{autoscale_pool_id}/dangerous">client.gpu_droplets.autoscale.<a href="./src/gradient/resources/gpu_droplets/autoscale.py">delete_dangerous</a>(autoscale_pool_id) -> None</code>
- <code title="get /v2/droplets/autoscale/{autoscale_pool_id}/history">client.gpu_droplets.autoscale.<a href="./src/gradient/resources/gpu_droplets/autoscale.py">list_history</a>(autoscale_pool_id, \*\*<a href="src/gradient/types/gpu_droplets/autoscale_list_history_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/autoscale_list_history_response.py">AutoscaleListHistoryResponse</a></code>
- <code title="get /v2/droplets/autoscale/{autoscale_pool_id}/members">client.gpu_droplets.autoscale.<a href="./src/gradient/resources/gpu_droplets/autoscale.py">list_members</a>(autoscale_pool_id, \*\*<a href="src/gradient/types/gpu_droplets/autoscale_list_members_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/autoscale_list_members_response.py">AutoscaleListMembersResponse</a></code>

## Firewalls

Types:

```python
from gradient.types.gpu_droplets import (
    Firewall,
    FirewallCreateResponse,
    FirewallRetrieveResponse,
    FirewallUpdateResponse,
    FirewallListResponse,
)
```

Methods:

- <code title="post /v2/firewalls">client.gpu_droplets.firewalls.<a href="./src/gradient/resources/gpu_droplets/firewalls/firewalls.py">create</a>(\*\*<a href="src/gradient/types/gpu_droplets/firewall_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/firewall_create_response.py">FirewallCreateResponse</a></code>
- <code title="get /v2/firewalls/{firewall_id}">client.gpu_droplets.firewalls.<a href="./src/gradient/resources/gpu_droplets/firewalls/firewalls.py">retrieve</a>(firewall_id) -> <a href="./src/gradient/types/gpu_droplets/firewall_retrieve_response.py">FirewallRetrieveResponse</a></code>
- <code title="put /v2/firewalls/{firewall_id}">client.gpu_droplets.firewalls.<a href="./src/gradient/resources/gpu_droplets/firewalls/firewalls.py">update</a>(firewall_id, \*\*<a href="src/gradient/types/gpu_droplets/firewall_update_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/firewall_update_response.py">FirewallUpdateResponse</a></code>
- <code title="get /v2/firewalls">client.gpu_droplets.firewalls.<a href="./src/gradient/resources/gpu_droplets/firewalls/firewalls.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/firewall_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/firewall_list_response.py">FirewallListResponse</a></code>
- <code title="delete /v2/firewalls/{firewall_id}">client.gpu_droplets.firewalls.<a href="./src/gradient/resources/gpu_droplets/firewalls/firewalls.py">delete</a>(firewall_id) -> None</code>

### Droplets

Methods:

- <code title="post /v2/firewalls/{firewall_id}/droplets">client.gpu_droplets.firewalls.droplets.<a href="./src/gradient/resources/gpu_droplets/firewalls/droplets.py">add</a>(firewall_id, \*\*<a href="src/gradient/types/gpu_droplets/firewalls/droplet_add_params.py">params</a>) -> None</code>
- <code title="delete /v2/firewalls/{firewall_id}/droplets">client.gpu_droplets.firewalls.droplets.<a href="./src/gradient/resources/gpu_droplets/firewalls/droplets.py">remove</a>(firewall_id, \*\*<a href="src/gradient/types/gpu_droplets/firewalls/droplet_remove_params.py">params</a>) -> None</code>

### Tags

Methods:

- <code title="post /v2/firewalls/{firewall_id}/tags">client.gpu_droplets.firewalls.tags.<a href="./src/gradient/resources/gpu_droplets/firewalls/tags.py">add</a>(firewall_id, \*\*<a href="src/gradient/types/gpu_droplets/firewalls/tag_add_params.py">params</a>) -> None</code>
- <code title="delete /v2/firewalls/{firewall_id}/tags">client.gpu_droplets.firewalls.tags.<a href="./src/gradient/resources/gpu_droplets/firewalls/tags.py">remove</a>(firewall_id, \*\*<a href="src/gradient/types/gpu_droplets/firewalls/tag_remove_params.py">params</a>) -> None</code>

### Rules

Methods:

- <code title="post /v2/firewalls/{firewall_id}/rules">client.gpu_droplets.firewalls.rules.<a href="./src/gradient/resources/gpu_droplets/firewalls/rules.py">add</a>(firewall_id, \*\*<a href="src/gradient/types/gpu_droplets/firewalls/rule_add_params.py">params</a>) -> None</code>
- <code title="delete /v2/firewalls/{firewall_id}/rules">client.gpu_droplets.firewalls.rules.<a href="./src/gradient/resources/gpu_droplets/firewalls/rules.py">remove</a>(firewall_id, \*\*<a href="src/gradient/types/gpu_droplets/firewalls/rule_remove_params.py">params</a>) -> None</code>

## FloatingIPs

Types:

```python
from gradient.types.gpu_droplets import (
    FloatingIP,
    FloatingIPCreateResponse,
    FloatingIPRetrieveResponse,
    FloatingIPListResponse,
)
```

Methods:

- <code title="post /v2/floating_ips">client.gpu_droplets.floating_ips.<a href="./src/gradient/resources/gpu_droplets/floating_ips/floating_ips.py">create</a>(\*\*<a href="src/gradient/types/gpu_droplets/floating_ip_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/floating_ip_create_response.py">FloatingIPCreateResponse</a></code>
- <code title="get /v2/floating_ips/{floating_ip}">client.gpu_droplets.floating_ips.<a href="./src/gradient/resources/gpu_droplets/floating_ips/floating_ips.py">retrieve</a>(floating_ip) -> <a href="./src/gradient/types/gpu_droplets/floating_ip_retrieve_response.py">FloatingIPRetrieveResponse</a></code>
- <code title="get /v2/floating_ips">client.gpu_droplets.floating_ips.<a href="./src/gradient/resources/gpu_droplets/floating_ips/floating_ips.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/floating_ip_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/floating_ip_list_response.py">FloatingIPListResponse</a></code>
- <code title="delete /v2/floating_ips/{floating_ip}">client.gpu_droplets.floating_ips.<a href="./src/gradient/resources/gpu_droplets/floating_ips/floating_ips.py">delete</a>(floating_ip) -> None</code>

### Actions

Types:

```python
from gradient.types.gpu_droplets.floating_ips import (
    ActionCreateResponse,
    ActionRetrieveResponse,
    ActionListResponse,
)
```

Methods:

- <code title="post /v2/floating_ips/{floating_ip}/actions">client.gpu_droplets.floating_ips.actions.<a href="./src/gradient/resources/gpu_droplets/floating_ips/actions.py">create</a>(floating_ip, \*\*<a href="src/gradient/types/gpu_droplets/floating_ips/action_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/floating_ips/action_create_response.py">ActionCreateResponse</a></code>
- <code title="get /v2/floating_ips/{floating_ip}/actions/{action_id}">client.gpu_droplets.floating_ips.actions.<a href="./src/gradient/resources/gpu_droplets/floating_ips/actions.py">retrieve</a>(action_id, \*, floating_ip) -> <a href="./src/gradient/types/gpu_droplets/floating_ips/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /v2/floating_ips/{floating_ip}/actions">client.gpu_droplets.floating_ips.actions.<a href="./src/gradient/resources/gpu_droplets/floating_ips/actions.py">list</a>(floating_ip) -> <a href="./src/gradient/types/gpu_droplets/floating_ips/action_list_response.py">ActionListResponse</a></code>

## Images

Types:

```python
from gradient.types.gpu_droplets import (
    ImageCreateResponse,
    ImageRetrieveResponse,
    ImageUpdateResponse,
    ImageListResponse,
)
```

Methods:

- <code title="post /v2/images">client.gpu_droplets.images.<a href="./src/gradient/resources/gpu_droplets/images/images.py">create</a>(\*\*<a href="src/gradient/types/gpu_droplets/image_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/image_create_response.py">ImageCreateResponse</a></code>
- <code title="get /v2/images/{image_id}">client.gpu_droplets.images.<a href="./src/gradient/resources/gpu_droplets/images/images.py">retrieve</a>(image_id) -> <a href="./src/gradient/types/gpu_droplets/image_retrieve_response.py">ImageRetrieveResponse</a></code>
- <code title="put /v2/images/{image_id}">client.gpu_droplets.images.<a href="./src/gradient/resources/gpu_droplets/images/images.py">update</a>(image_id, \*\*<a href="src/gradient/types/gpu_droplets/image_update_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/image_update_response.py">ImageUpdateResponse</a></code>
- <code title="get /v2/images">client.gpu_droplets.images.<a href="./src/gradient/resources/gpu_droplets/images/images.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/image_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/image_list_response.py">ImageListResponse</a></code>
- <code title="delete /v2/images/{image_id}">client.gpu_droplets.images.<a href="./src/gradient/resources/gpu_droplets/images/images.py">delete</a>(image_id) -> None</code>

### Actions

Types:

```python
from gradient.types.gpu_droplets.images import ActionListResponse
```

Methods:

- <code title="post /v2/images/{image_id}/actions">client.gpu_droplets.images.actions.<a href="./src/gradient/resources/gpu_droplets/images/actions.py">create</a>(image_id, \*\*<a href="src/gradient/types/gpu_droplets/images/action_create_params.py">params</a>) -> <a href="./src/gradient/types/shared/action.py">Action</a></code>
- <code title="get /v2/images/{image_id}/actions/{action_id}">client.gpu_droplets.images.actions.<a href="./src/gradient/resources/gpu_droplets/images/actions.py">retrieve</a>(action_id, \*, image_id) -> <a href="./src/gradient/types/shared/action.py">Action</a></code>
- <code title="get /v2/images/{image_id}/actions">client.gpu_droplets.images.actions.<a href="./src/gradient/resources/gpu_droplets/images/actions.py">list</a>(image_id) -> <a href="./src/gradient/types/gpu_droplets/images/action_list_response.py">ActionListResponse</a></code>

## LoadBalancers

Types:

```python
from gradient.types.gpu_droplets import (
    Domains,
    ForwardingRule,
    GlbSettings,
    HealthCheck,
    LbFirewall,
    LoadBalancer,
    StickySessions,
    LoadBalancerCreateResponse,
    LoadBalancerRetrieveResponse,
    LoadBalancerUpdateResponse,
    LoadBalancerListResponse,
)
```

Methods:

- <code title="post /v2/load_balancers">client.gpu_droplets.load_balancers.<a href="./src/gradient/resources/gpu_droplets/load_balancers/load_balancers.py">create</a>(\*\*<a href="src/gradient/types/gpu_droplets/load_balancer_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/load_balancer_create_response.py">LoadBalancerCreateResponse</a></code>
- <code title="get /v2/load_balancers/{lb_id}">client.gpu_droplets.load_balancers.<a href="./src/gradient/resources/gpu_droplets/load_balancers/load_balancers.py">retrieve</a>(lb_id) -> <a href="./src/gradient/types/gpu_droplets/load_balancer_retrieve_response.py">LoadBalancerRetrieveResponse</a></code>
- <code title="put /v2/load_balancers/{lb_id}">client.gpu_droplets.load_balancers.<a href="./src/gradient/resources/gpu_droplets/load_balancers/load_balancers.py">update</a>(lb_id, \*\*<a href="src/gradient/types/gpu_droplets/load_balancer_update_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/load_balancer_update_response.py">LoadBalancerUpdateResponse</a></code>
- <code title="get /v2/load_balancers">client.gpu_droplets.load_balancers.<a href="./src/gradient/resources/gpu_droplets/load_balancers/load_balancers.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/load_balancer_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/load_balancer_list_response.py">LoadBalancerListResponse</a></code>
- <code title="delete /v2/load_balancers/{lb_id}">client.gpu_droplets.load_balancers.<a href="./src/gradient/resources/gpu_droplets/load_balancers/load_balancers.py">delete</a>(lb_id) -> None</code>
- <code title="delete /v2/load_balancers/{lb_id}/cache">client.gpu_droplets.load_balancers.<a href="./src/gradient/resources/gpu_droplets/load_balancers/load_balancers.py">delete_cache</a>(lb_id) -> None</code>

### Droplets

Methods:

- <code title="post /v2/load_balancers/{lb_id}/droplets">client.gpu_droplets.load_balancers.droplets.<a href="./src/gradient/resources/gpu_droplets/load_balancers/droplets.py">add</a>(lb_id, \*\*<a href="src/gradient/types/gpu_droplets/load_balancers/droplet_add_params.py">params</a>) -> None</code>
- <code title="delete /v2/load_balancers/{lb_id}/droplets">client.gpu_droplets.load_balancers.droplets.<a href="./src/gradient/resources/gpu_droplets/load_balancers/droplets.py">remove</a>(lb_id, \*\*<a href="src/gradient/types/gpu_droplets/load_balancers/droplet_remove_params.py">params</a>) -> None</code>

### ForwardingRules

Methods:

- <code title="post /v2/load_balancers/{lb_id}/forwarding_rules">client.gpu_droplets.load_balancers.forwarding_rules.<a href="./src/gradient/resources/gpu_droplets/load_balancers/forwarding_rules.py">add</a>(lb_id, \*\*<a href="src/gradient/types/gpu_droplets/load_balancers/forwarding_rule_add_params.py">params</a>) -> None</code>
- <code title="delete /v2/load_balancers/{lb_id}/forwarding_rules">client.gpu_droplets.load_balancers.forwarding_rules.<a href="./src/gradient/resources/gpu_droplets/load_balancers/forwarding_rules.py">remove</a>(lb_id, \*\*<a href="src/gradient/types/gpu_droplets/load_balancers/forwarding_rule_remove_params.py">params</a>) -> None</code>

## Sizes

Types:

```python
from gradient.types.gpu_droplets import SizeListResponse
```

Methods:

- <code title="get /v2/sizes">client.gpu_droplets.sizes.<a href="./src/gradient/resources/gpu_droplets/sizes.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/size_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/size_list_response.py">SizeListResponse</a></code>

## Snapshots

Types:

```python
from gradient.types.gpu_droplets import SnapshotRetrieveResponse, SnapshotListResponse
```

Methods:

- <code title="get /v2/snapshots/{snapshot_id}">client.gpu_droplets.snapshots.<a href="./src/gradient/resources/gpu_droplets/snapshots.py">retrieve</a>(snapshot_id) -> <a href="./src/gradient/types/gpu_droplets/snapshot_retrieve_response.py">SnapshotRetrieveResponse</a></code>
- <code title="get /v2/snapshots">client.gpu_droplets.snapshots.<a href="./src/gradient/resources/gpu_droplets/snapshots.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/snapshot_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/snapshot_list_response.py">SnapshotListResponse</a></code>
- <code title="delete /v2/snapshots/{snapshot_id}">client.gpu_droplets.snapshots.<a href="./src/gradient/resources/gpu_droplets/snapshots.py">delete</a>(snapshot_id) -> None</code>

## Volumes

Types:

```python
from gradient.types.gpu_droplets import (
    VolumeCreateResponse,
    VolumeRetrieveResponse,
    VolumeListResponse,
)
```

Methods:

- <code title="post /v2/volumes">client.gpu_droplets.volumes.<a href="./src/gradient/resources/gpu_droplets/volumes/volumes.py">create</a>(\*\*<a href="src/gradient/types/gpu_droplets/volume_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/volume_create_response.py">VolumeCreateResponse</a></code>
- <code title="get /v2/volumes/{volume_id}">client.gpu_droplets.volumes.<a href="./src/gradient/resources/gpu_droplets/volumes/volumes.py">retrieve</a>(volume_id) -> <a href="./src/gradient/types/gpu_droplets/volume_retrieve_response.py">VolumeRetrieveResponse</a></code>
- <code title="get /v2/volumes">client.gpu_droplets.volumes.<a href="./src/gradient/resources/gpu_droplets/volumes/volumes.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/volume_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/volume_list_response.py">VolumeListResponse</a></code>
- <code title="delete /v2/volumes/{volume_id}">client.gpu_droplets.volumes.<a href="./src/gradient/resources/gpu_droplets/volumes/volumes.py">delete</a>(volume_id) -> None</code>
- <code title="delete /v2/volumes">client.gpu_droplets.volumes.<a href="./src/gradient/resources/gpu_droplets/volumes/volumes.py">delete_by_name</a>(\*\*<a href="src/gradient/types/gpu_droplets/volume_delete_by_name_params.py">params</a>) -> None</code>

### Actions

Types:

```python
from gradient.types.gpu_droplets.volumes import (
    VolumeAction,
    ActionRetrieveResponse,
    ActionListResponse,
    ActionInitiateByIDResponse,
    ActionInitiateByNameResponse,
)
```

Methods:

- <code title="get /v2/volumes/{volume_id}/actions/{action_id}">client.gpu_droplets.volumes.actions.<a href="./src/gradient/resources/gpu_droplets/volumes/actions.py">retrieve</a>(action_id, \*, volume_id, \*\*<a href="src/gradient/types/gpu_droplets/volumes/action_retrieve_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/volumes/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /v2/volumes/{volume_id}/actions">client.gpu_droplets.volumes.actions.<a href="./src/gradient/resources/gpu_droplets/volumes/actions.py">list</a>(volume_id, \*\*<a href="src/gradient/types/gpu_droplets/volumes/action_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/volumes/action_list_response.py">ActionListResponse</a></code>
- <code title="post /v2/volumes/{volume_id}/actions">client.gpu_droplets.volumes.actions.<a href="./src/gradient/resources/gpu_droplets/volumes/actions.py">initiate_by_id</a>(volume_id, \*\*<a href="src/gradient/types/gpu_droplets/volumes/action_initiate_by_id_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/volumes/action_initiate_by_id_response.py">ActionInitiateByIDResponse</a></code>
- <code title="post /v2/volumes/actions">client.gpu_droplets.volumes.actions.<a href="./src/gradient/resources/gpu_droplets/volumes/actions.py">initiate_by_name</a>(\*\*<a href="src/gradient/types/gpu_droplets/volumes/action_initiate_by_name_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/volumes/action_initiate_by_name_response.py">ActionInitiateByNameResponse</a></code>

### Snapshots

Types:

```python
from gradient.types.gpu_droplets.volumes import (
    SnapshotCreateResponse,
    SnapshotRetrieveResponse,
    SnapshotListResponse,
)
```

Methods:

- <code title="post /v2/volumes/{volume_id}/snapshots">client.gpu_droplets.volumes.snapshots.<a href="./src/gradient/resources/gpu_droplets/volumes/snapshots.py">create</a>(volume_id, \*\*<a href="src/gradient/types/gpu_droplets/volumes/snapshot_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/volumes/snapshot_create_response.py">SnapshotCreateResponse</a></code>
- <code title="get /v2/volumes/snapshots/{snapshot_id}">client.gpu_droplets.volumes.snapshots.<a href="./src/gradient/resources/gpu_droplets/volumes/snapshots.py">retrieve</a>(snapshot_id) -> <a href="./src/gradient/types/gpu_droplets/volumes/snapshot_retrieve_response.py">SnapshotRetrieveResponse</a></code>
- <code title="get /v2/volumes/{volume_id}/snapshots">client.gpu_droplets.volumes.snapshots.<a href="./src/gradient/resources/gpu_droplets/volumes/snapshots.py">list</a>(volume_id, \*\*<a href="src/gradient/types/gpu_droplets/volumes/snapshot_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/volumes/snapshot_list_response.py">SnapshotListResponse</a></code>
- <code title="delete /v2/volumes/snapshots/{snapshot_id}">client.gpu_droplets.volumes.snapshots.<a href="./src/gradient/resources/gpu_droplets/volumes/snapshots.py">delete</a>(snapshot_id) -> None</code>

## Account

### Keys

Types:

```python
from gradient.types.gpu_droplets.account import (
    SSHKeys,
    KeyCreateResponse,
    KeyRetrieveResponse,
    KeyUpdateResponse,
    KeyListResponse,
)
```

Methods:

- <code title="post /v2/account/keys">client.gpu_droplets.account.keys.<a href="./src/gradient/resources/gpu_droplets/account/keys.py">create</a>(\*\*<a href="src/gradient/types/gpu_droplets/account/key_create_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/account/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /v2/account/keys/{ssh_key_identifier}">client.gpu_droplets.account.keys.<a href="./src/gradient/resources/gpu_droplets/account/keys.py">retrieve</a>(ssh_key_identifier) -> <a href="./src/gradient/types/gpu_droplets/account/key_retrieve_response.py">KeyRetrieveResponse</a></code>
- <code title="put /v2/account/keys/{ssh_key_identifier}">client.gpu_droplets.account.keys.<a href="./src/gradient/resources/gpu_droplets/account/keys.py">update</a>(ssh_key_identifier, \*\*<a href="src/gradient/types/gpu_droplets/account/key_update_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/account/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="get /v2/account/keys">client.gpu_droplets.account.keys.<a href="./src/gradient/resources/gpu_droplets/account/keys.py">list</a>(\*\*<a href="src/gradient/types/gpu_droplets/account/key_list_params.py">params</a>) -> <a href="./src/gradient/types/gpu_droplets/account/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /v2/account/keys/{ssh_key_identifier}">client.gpu_droplets.account.keys.<a href="./src/gradient/resources/gpu_droplets/account/keys.py">delete</a>(ssh_key_identifier) -> None</code>

# Inference

## APIKeys

Types:

```python
from gradient.types.inference import (
    APIModelAPIKeyInfo,
    APIKeyCreateResponse,
    APIKeyUpdateResponse,
    APIKeyListResponse,
    APIKeyDeleteResponse,
    APIKeyUpdateRegenerateResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/models/api_keys">client.inference.api_keys.<a href="./src/gradient/resources/inference/api_keys.py">create</a>(\*\*<a href="src/gradient/types/inference/api_key_create_params.py">params</a>) -> <a href="./src/gradient/types/inference/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="put /v2/gen-ai/models/api_keys/{api_key_uuid}">client.inference.api_keys.<a href="./src/gradient/resources/inference/api_keys.py">update</a>(path_api_key_uuid, \*\*<a href="src/gradient/types/inference/api_key_update_params.py">params</a>) -> <a href="./src/gradient/types/inference/api_key_update_response.py">APIKeyUpdateResponse</a></code>
- <code title="get /v2/gen-ai/models/api_keys">client.inference.api_keys.<a href="./src/gradient/resources/inference/api_keys.py">list</a>(\*\*<a href="src/gradient/types/inference/api_key_list_params.py">params</a>) -> <a href="./src/gradient/types/inference/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v2/gen-ai/models/api_keys/{api_key_uuid}">client.inference.api_keys.<a href="./src/gradient/resources/inference/api_keys.py">delete</a>(api_key_uuid) -> <a href="./src/gradient/types/inference/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
- <code title="put /v2/gen-ai/models/api_keys/{api_key_uuid}/regenerate">client.inference.api_keys.<a href="./src/gradient/resources/inference/api_keys.py">update_regenerate</a>(api_key_uuid) -> <a href="./src/gradient/types/inference/api_key_update_regenerate_response.py">APIKeyUpdateRegenerateResponse</a></code>

# KnowledgeBases

Types:

```python
from gradient.types import (
    APIKnowledgeBase,
    KnowledgeBaseCreateResponse,
    KnowledgeBaseRetrieveResponse,
    KnowledgeBaseUpdateResponse,
    KnowledgeBaseListResponse,
    KnowledgeBaseDeleteResponse,
    KnowledgeBaseListIndexingJobsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/knowledge_bases">client.knowledge_bases.<a href="./src/gradient/resources/knowledge_bases/knowledge_bases.py">create</a>(\*\*<a href="src/gradient/types/knowledge_base_create_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_base_create_response.py">KnowledgeBaseCreateResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases/{uuid}">client.knowledge_bases.<a href="./src/gradient/resources/knowledge_bases/knowledge_bases.py">retrieve</a>(uuid) -> <a href="./src/gradient/types/knowledge_base_retrieve_response.py">KnowledgeBaseRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/knowledge_bases/{uuid}">client.knowledge_bases.<a href="./src/gradient/resources/knowledge_bases/knowledge_bases.py">update</a>(path_uuid, \*\*<a href="src/gradient/types/knowledge_base_update_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_base_update_response.py">KnowledgeBaseUpdateResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases">client.knowledge_bases.<a href="./src/gradient/resources/knowledge_bases/knowledge_bases.py">list</a>(\*\*<a href="src/gradient/types/knowledge_base_list_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_base_list_response.py">KnowledgeBaseListResponse</a></code>
- <code title="delete /v2/gen-ai/knowledge_bases/{uuid}">client.knowledge_bases.<a href="./src/gradient/resources/knowledge_bases/knowledge_bases.py">delete</a>(uuid) -> <a href="./src/gradient/types/knowledge_base_delete_response.py">KnowledgeBaseDeleteResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/indexing_jobs">client.knowledge_bases.<a href="./src/gradient/resources/knowledge_bases/knowledge_bases.py">list_indexing_jobs</a>(knowledge_base_uuid) -> <a href="./src/gradient/types/knowledge_base_list_indexing_jobs_response.py">KnowledgeBaseListIndexingJobsResponse</a></code>

## DataSources

Types:

```python
from gradient.types.knowledge_bases import (
    APIFileUploadDataSource,
    APIKnowledgeBaseDataSource,
    APISpacesDataSource,
    APIWebCrawlerDataSource,
    AwsDataSource,
    DataSourceCreateResponse,
    DataSourceListResponse,
    DataSourceDeleteResponse,
    DataSourceCreatePresignedURLsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources">client.knowledge_bases.data_sources.<a href="./src/gradient/resources/knowledge_bases/data_sources.py">create</a>(path_knowledge_base_uuid, \*\*<a href="src/gradient/types/knowledge_bases/data_source_create_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_bases/data_source_create_response.py">DataSourceCreateResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources">client.knowledge_bases.data_sources.<a href="./src/gradient/resources/knowledge_bases/data_sources.py">list</a>(knowledge_base_uuid, \*\*<a href="src/gradient/types/knowledge_bases/data_source_list_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_bases/data_source_list_response.py">DataSourceListResponse</a></code>
- <code title="delete /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}">client.knowledge_bases.data_sources.<a href="./src/gradient/resources/knowledge_bases/data_sources.py">delete</a>(data_source_uuid, \*, knowledge_base_uuid) -> <a href="./src/gradient/types/knowledge_bases/data_source_delete_response.py">DataSourceDeleteResponse</a></code>
- <code title="post /v2/gen-ai/knowledge_bases/data_sources/file_upload_presigned_urls">client.knowledge_bases.data_sources.<a href="./src/gradient/resources/knowledge_bases/data_sources.py">create_presigned_urls</a>(\*\*<a href="src/gradient/types/knowledge_bases/data_source_create_presigned_urls_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_bases/data_source_create_presigned_urls_response.py">DataSourceCreatePresignedURLsResponse</a></code>

## IndexingJobs

Types:

```python
from gradient.types.knowledge_bases import (
    APIIndexedDataSource,
    APIIndexingJob,
    IndexingJobCreateResponse,
    IndexingJobRetrieveResponse,
    IndexingJobListResponse,
    IndexingJobRetrieveDataSourcesResponse,
    IndexingJobRetrieveSignedURLResponse,
    IndexingJobUpdateCancelResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/indexing_jobs">client.knowledge_bases.indexing_jobs.<a href="./src/gradient/resources/knowledge_bases/indexing_jobs.py">create</a>(\*\*<a href="src/gradient/types/knowledge_bases/indexing_job_create_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_bases/indexing_job_create_response.py">IndexingJobCreateResponse</a></code>
- <code title="get /v2/gen-ai/indexing_jobs/{uuid}">client.knowledge_bases.indexing_jobs.<a href="./src/gradient/resources/knowledge_bases/indexing_jobs.py">retrieve</a>(uuid) -> <a href="./src/gradient/types/knowledge_bases/indexing_job_retrieve_response.py">IndexingJobRetrieveResponse</a></code>
- <code title="get /v2/gen-ai/indexing_jobs">client.knowledge_bases.indexing_jobs.<a href="./src/gradient/resources/knowledge_bases/indexing_jobs.py">list</a>(\*\*<a href="src/gradient/types/knowledge_bases/indexing_job_list_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_bases/indexing_job_list_response.py">IndexingJobListResponse</a></code>
- <code title="get /v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources">client.knowledge_bases.indexing_jobs.<a href="./src/gradient/resources/knowledge_bases/indexing_jobs.py">retrieve_data_sources</a>(indexing_job_uuid) -> <a href="./src/gradient/types/knowledge_bases/indexing_job_retrieve_data_sources_response.py">IndexingJobRetrieveDataSourcesResponse</a></code>
- <code title="get /v2/gen-ai/indexing_jobs/{indexing_job_uuid}/details_signed_url">client.knowledge_bases.indexing_jobs.<a href="./src/gradient/resources/knowledge_bases/indexing_jobs.py">retrieve_signed_url</a>(indexing_job_uuid) -> <a href="./src/gradient/types/knowledge_bases/indexing_job_retrieve_signed_url_response.py">IndexingJobRetrieveSignedURLResponse</a></code>
- <code title="put /v2/gen-ai/indexing_jobs/{uuid}/cancel">client.knowledge_bases.indexing_jobs.<a href="./src/gradient/resources/knowledge_bases/indexing_jobs.py">update_cancel</a>(path_uuid, \*\*<a href="src/gradient/types/knowledge_bases/indexing_job_update_cancel_params.py">params</a>) -> <a href="./src/gradient/types/knowledge_bases/indexing_job_update_cancel_response.py">IndexingJobUpdateCancelResponse</a></code>

# Models

Types:

```python
from gradient.types import APIAgreement, APIModel, APIModelVersion, ModelListResponse
```

Methods:

- <code title="get /v2/gen-ai/models">client.models.<a href="./src/gradient/resources/models/models.py">list</a>(\*\*<a href="src/gradient/types/model_list_params.py">params</a>) -> <a href="./src/gradient/types/model_list_response.py">ModelListResponse</a></code>

## Providers

### Anthropic

Types:

```python
from gradient.types.models.providers import (
    AnthropicCreateResponse,
    AnthropicRetrieveResponse,
    AnthropicUpdateResponse,
    AnthropicListResponse,
    AnthropicDeleteResponse,
    AnthropicListAgentsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/anthropic/keys">client.models.providers.anthropic.<a href="./src/gradient/resources/models/providers/anthropic.py">create</a>(\*\*<a href="src/gradient/types/models/providers/anthropic_create_params.py">params</a>) -> <a href="./src/gradient/types/models/providers/anthropic_create_response.py">AnthropicCreateResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.models.providers.anthropic.<a href="./src/gradient/resources/models/providers/anthropic.py">retrieve</a>(api_key_uuid) -> <a href="./src/gradient/types/models/providers/anthropic_retrieve_response.py">AnthropicRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.models.providers.anthropic.<a href="./src/gradient/resources/models/providers/anthropic.py">update</a>(path_api_key_uuid, \*\*<a href="src/gradient/types/models/providers/anthropic_update_params.py">params</a>) -> <a href="./src/gradient/types/models/providers/anthropic_update_response.py">AnthropicUpdateResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys">client.models.providers.anthropic.<a href="./src/gradient/resources/models/providers/anthropic.py">list</a>(\*\*<a href="src/gradient/types/models/providers/anthropic_list_params.py">params</a>) -> <a href="./src/gradient/types/models/providers/anthropic_list_response.py">AnthropicListResponse</a></code>
- <code title="delete /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.models.providers.anthropic.<a href="./src/gradient/resources/models/providers/anthropic.py">delete</a>(api_key_uuid) -> <a href="./src/gradient/types/models/providers/anthropic_delete_response.py">AnthropicDeleteResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys/{uuid}/agents">client.models.providers.anthropic.<a href="./src/gradient/resources/models/providers/anthropic.py">list_agents</a>(uuid, \*\*<a href="src/gradient/types/models/providers/anthropic_list_agents_params.py">params</a>) -> <a href="./src/gradient/types/models/providers/anthropic_list_agents_response.py">AnthropicListAgentsResponse</a></code>

### OpenAI

Types:

```python
from gradient.types.models.providers import (
    OpenAICreateResponse,
    OpenAIRetrieveResponse,
    OpenAIUpdateResponse,
    OpenAIListResponse,
    OpenAIDeleteResponse,
    OpenAIRetrieveAgentsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/openai/keys">client.models.providers.openai.<a href="./src/gradient/resources/models/providers/openai.py">create</a>(\*\*<a href="src/gradient/types/models/providers/openai_create_params.py">params</a>) -> <a href="./src/gradient/types/models/providers/openai_create_response.py">OpenAICreateResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys/{api_key_uuid}">client.models.providers.openai.<a href="./src/gradient/resources/models/providers/openai.py">retrieve</a>(api_key_uuid) -> <a href="./src/gradient/types/models/providers/openai_retrieve_response.py">OpenAIRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/openai/keys/{api_key_uuid}">client.models.providers.openai.<a href="./src/gradient/resources/models/providers/openai.py">update</a>(path_api_key_uuid, \*\*<a href="src/gradient/types/models/providers/openai_update_params.py">params</a>) -> <a href="./src/gradient/types/models/providers/openai_update_response.py">OpenAIUpdateResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys">client.models.providers.openai.<a href="./src/gradient/resources/models/providers/openai.py">list</a>(\*\*<a href="src/gradient/types/models/providers/openai_list_params.py">params</a>) -> <a href="./src/gradient/types/models/providers/openai_list_response.py">OpenAIListResponse</a></code>
- <code title="delete /v2/gen-ai/openai/keys/{api_key_uuid}">client.models.providers.openai.<a href="./src/gradient/resources/models/providers/openai.py">delete</a>(api_key_uuid) -> <a href="./src/gradient/types/models/providers/openai_delete_response.py">OpenAIDeleteResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys/{uuid}/agents">client.models.providers.openai.<a href="./src/gradient/resources/models/providers/openai.py">retrieve_agents</a>(uuid, \*\*<a href="src/gradient/types/models/providers/openai_retrieve_agents_params.py">params</a>) -> <a href="./src/gradient/types/models/providers/openai_retrieve_agents_response.py">OpenAIRetrieveAgentsResponse</a></code>

# Regions

Types:

```python
from gradient.types import RegionListResponse
```

Methods:

- <code title="get /v2/regions">client.regions.<a href="./src/gradient/resources/regions.py">list</a>(\*\*<a href="src/gradient/types/region_list_params.py">params</a>) -> <a href="./src/gradient/types/region_list_response.py">RegionListResponse</a></code>

# Databases

## SchemaRegistry

### Config

Types:

```python
from gradient.types.databases.schema_registry import (
    ConfigRetrieveResponse,
    ConfigUpdateResponse,
    ConfigRetrieveSubjectResponse,
    ConfigUpdateSubjectResponse,
)
```

Methods:

- <code title="get /v2/databases/{database_cluster_uuid}/schema-registry/config">client.databases.schema_registry.config.<a href="./src/gradient/resources/databases/schema_registry/config.py">retrieve</a>(database_cluster_uuid) -> <a href="./src/gradient/types/databases/schema_registry/config_retrieve_response.py">ConfigRetrieveResponse</a></code>
- <code title="put /v2/databases/{database_cluster_uuid}/schema-registry/config">client.databases.schema_registry.config.<a href="./src/gradient/resources/databases/schema_registry/config.py">update</a>(database_cluster_uuid, \*\*<a href="src/gradient/types/databases/schema_registry/config_update_params.py">params</a>) -> <a href="./src/gradient/types/databases/schema_registry/config_update_response.py">ConfigUpdateResponse</a></code>
- <code title="get /v2/databases/{database_cluster_uuid}/schema-registry/config/{subject_name}">client.databases.schema_registry.config.<a href="./src/gradient/resources/databases/schema_registry/config.py">retrieve_subject</a>(subject_name, \*, database_cluster_uuid) -> <a href="./src/gradient/types/databases/schema_registry/config_retrieve_subject_response.py">ConfigRetrieveSubjectResponse</a></code>
- <code title="put /v2/databases/{database_cluster_uuid}/schema-registry/config/{subject_name}">client.databases.schema_registry.config.<a href="./src/gradient/resources/databases/schema_registry/config.py">update_subject</a>(subject_name, \*, database_cluster_uuid, \*\*<a href="src/gradient/types/databases/schema_registry/config_update_subject_params.py">params</a>) -> <a href="./src/gradient/types/databases/schema_registry/config_update_subject_response.py">ConfigUpdateSubjectResponse</a></code>

# Nfs

Types:

```python
from gradient.types import (
    NfCreateResponse,
    NfRetrieveResponse,
    NfListResponse,
    NfInitiateActionResponse,
)
```

Methods:

- <code title="post /v2/nfs">client.nfs.<a href="./src/gradient/resources/nfs/nfs.py">create</a>(\*\*<a href="src/gradient/types/nf_create_params.py">params</a>) -> <a href="./src/gradient/types/nf_create_response.py">NfCreateResponse</a></code>
- <code title="get /v2/nfs/{nfs_id}">client.nfs.<a href="./src/gradient/resources/nfs/nfs.py">retrieve</a>(nfs_id, \*\*<a href="src/gradient/types/nf_retrieve_params.py">params</a>) -> <a href="./src/gradient/types/nf_retrieve_response.py">NfRetrieveResponse</a></code>
- <code title="get /v2/nfs">client.nfs.<a href="./src/gradient/resources/nfs/nfs.py">list</a>(\*\*<a href="src/gradient/types/nf_list_params.py">params</a>) -> <a href="./src/gradient/types/nf_list_response.py">NfListResponse</a></code>
- <code title="delete /v2/nfs/{nfs_id}">client.nfs.<a href="./src/gradient/resources/nfs/nfs.py">delete</a>(nfs_id, \*\*<a href="src/gradient/types/nf_delete_params.py">params</a>) -> None</code>
- <code title="post /v2/nfs/{nfs_id}/actions">client.nfs.<a href="./src/gradient/resources/nfs/nfs.py">initiate_action</a>(nfs_id, \*\*<a href="src/gradient/types/nf_initiate_action_params.py">params</a>) -> <a href="./src/gradient/types/nf_initiate_action_response.py">NfInitiateActionResponse</a></code>

## Snapshots

Types:

```python
from gradient.types.nfs import SnapshotRetrieveResponse, SnapshotListResponse
```

Methods:

- <code title="get /v2/nfs/snapshots/{nfs_snapshot_id}">client.nfs.snapshots.<a href="./src/gradient/resources/nfs/snapshots.py">retrieve</a>(nfs_snapshot_id, \*\*<a href="src/gradient/types/nfs/snapshot_retrieve_params.py">params</a>) -> <a href="./src/gradient/types/nfs/snapshot_retrieve_response.py">SnapshotRetrieveResponse</a></code>
- <code title="get /v2/nfs/snapshots">client.nfs.snapshots.<a href="./src/gradient/resources/nfs/snapshots.py">list</a>(\*\*<a href="src/gradient/types/nfs/snapshot_list_params.py">params</a>) -> <a href="./src/gradient/types/nfs/snapshot_list_response.py">SnapshotListResponse</a></code>
- <code title="delete /v2/nfs/snapshots/{nfs_snapshot_id}">client.nfs.snapshots.<a href="./src/gradient/resources/nfs/snapshots.py">delete</a>(nfs_snapshot_id, \*\*<a href="src/gradient/types/nfs/snapshot_delete_params.py">params</a>) -> None</code>

# Retrieve

Types:

```python
from gradient.types import RetrieveDocumentsResponse
```

Methods:

- <code title="post /{knowledgeBaseId}/retrieve">client.retrieve.<a href="./src/gradient/resources/retrieve.py">documents</a>(knowledge_base_id, \*\*<a href="src/gradient/types/retrieve_documents_params.py">params</a>) -> <a href="./src/gradient/types/retrieve_documents_response.py">RetrieveDocumentsResponse</a></code>
