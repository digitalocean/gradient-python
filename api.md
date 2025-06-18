# Agents

Types:

```python
from gradientai.types import (
    APIAgent,
    APIAgentAPIKeyInfo,
    APIAnthropicAPIKeyInfo,
    APIDeploymentVisibility,
    APIModel,
    APIOpenAIAPIKeyInfo,
    APIRetrievalMethod,
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentListResponse,
    AgentDeleteResponse,
    AgentUpdateStatusResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/agents">client.agents.<a href="./src/gradientai/resources/agents/agents.py">create</a>(\*\*<a href="src/gradientai/types/agent_create_params.py">params</a>) -> <a href="./src/gradientai/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /v2/gen-ai/agents/{uuid}">client.agents.<a href="./src/gradientai/resources/agents/agents.py">retrieve</a>(uuid) -> <a href="./src/gradientai/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/agents/{uuid}">client.agents.<a href="./src/gradientai/resources/agents/agents.py">update</a>(path_uuid, \*\*<a href="src/gradientai/types/agent_update_params.py">params</a>) -> <a href="./src/gradientai/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /v2/gen-ai/agents">client.agents.<a href="./src/gradientai/resources/agents/agents.py">list</a>(\*\*<a href="src/gradientai/types/agent_list_params.py">params</a>) -> <a href="./src/gradientai/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v2/gen-ai/agents/{uuid}">client.agents.<a href="./src/gradientai/resources/agents/agents.py">delete</a>(uuid) -> <a href="./src/gradientai/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="put /v2/gen-ai/agents/{uuid}/deployment_visibility">client.agents.<a href="./src/gradientai/resources/agents/agents.py">update_status</a>(path_uuid, \*\*<a href="src/gradientai/types/agent_update_status_params.py">params</a>) -> <a href="./src/gradientai/types/agent_update_status_response.py">AgentUpdateStatusResponse</a></code>

## APIKeys

Types:

```python
from gradientai.types.agents import (
    APIKeyCreateResponse,
    APIKeyUpdateResponse,
    APIKeyListResponse,
    APIKeyDeleteResponse,
    APIKeyRegenerateResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/agents/{agent_uuid}/api_keys">client.agents.api_keys.<a href="./src/gradientai/resources/agents/api_keys.py">create</a>(path_agent_uuid, \*\*<a href="src/gradientai/types/agents/api_key_create_params.py">params</a>) -> <a href="./src/gradientai/types/agents/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="put /v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}">client.agents.api_keys.<a href="./src/gradientai/resources/agents/api_keys.py">update</a>(path_api_key_uuid, \*, path_agent_uuid, \*\*<a href="src/gradientai/types/agents/api_key_update_params.py">params</a>) -> <a href="./src/gradientai/types/agents/api_key_update_response.py">APIKeyUpdateResponse</a></code>
- <code title="get /v2/gen-ai/agents/{agent_uuid}/api_keys">client.agents.api_keys.<a href="./src/gradientai/resources/agents/api_keys.py">list</a>(agent_uuid, \*\*<a href="src/gradientai/types/agents/api_key_list_params.py">params</a>) -> <a href="./src/gradientai/types/agents/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}">client.agents.api_keys.<a href="./src/gradientai/resources/agents/api_keys.py">delete</a>(api_key_uuid, \*, agent_uuid) -> <a href="./src/gradientai/types/agents/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
- <code title="put /v2/gen-ai/agents/{agent_uuid}/api_keys/{api_key_uuid}/regenerate">client.agents.api_keys.<a href="./src/gradientai/resources/agents/api_keys.py">regenerate</a>(api_key_uuid, \*, agent_uuid) -> <a href="./src/gradientai/types/agents/api_key_regenerate_response.py">APIKeyRegenerateResponse</a></code>

## Functions

Types:

```python
from gradientai.types.agents import (
    FunctionCreateResponse,
    FunctionUpdateResponse,
    FunctionDeleteResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/agents/{agent_uuid}/functions">client.agents.functions.<a href="./src/gradientai/resources/agents/functions.py">create</a>(path_agent_uuid, \*\*<a href="src/gradientai/types/agents/function_create_params.py">params</a>) -> <a href="./src/gradientai/types/agents/function_create_response.py">FunctionCreateResponse</a></code>
- <code title="put /v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}">client.agents.functions.<a href="./src/gradientai/resources/agents/functions.py">update</a>(path_function_uuid, \*, path_agent_uuid, \*\*<a href="src/gradientai/types/agents/function_update_params.py">params</a>) -> <a href="./src/gradientai/types/agents/function_update_response.py">FunctionUpdateResponse</a></code>
- <code title="delete /v2/gen-ai/agents/{agent_uuid}/functions/{function_uuid}">client.agents.functions.<a href="./src/gradientai/resources/agents/functions.py">delete</a>(function_uuid, \*, agent_uuid) -> <a href="./src/gradientai/types/agents/function_delete_response.py">FunctionDeleteResponse</a></code>

## Versions

Types:

```python
from gradientai.types.agents import APILinks, APIMeta, VersionUpdateResponse, VersionListResponse
```

Methods:

- <code title="put /v2/gen-ai/agents/{uuid}/versions">client.agents.versions.<a href="./src/gradientai/resources/agents/versions.py">update</a>(path_uuid, \*\*<a href="src/gradientai/types/agents/version_update_params.py">params</a>) -> <a href="./src/gradientai/types/agents/version_update_response.py">VersionUpdateResponse</a></code>
- <code title="get /v2/gen-ai/agents/{uuid}/versions">client.agents.versions.<a href="./src/gradientai/resources/agents/versions.py">list</a>(uuid, \*\*<a href="src/gradientai/types/agents/version_list_params.py">params</a>) -> <a href="./src/gradientai/types/agents/version_list_response.py">VersionListResponse</a></code>

## KnowledgeBases

Types:

```python
from gradientai.types.agents import APILinkKnowledgeBaseOutput, KnowledgeBaseDetachResponse
```

Methods:

- <code title="post /v2/gen-ai/agents/{agent_uuid}/knowledge_bases">client.agents.knowledge_bases.<a href="./src/gradientai/resources/agents/knowledge_bases.py">attach</a>(agent_uuid) -> <a href="./src/gradientai/types/agents/api_link_knowledge_base_output.py">APILinkKnowledgeBaseOutput</a></code>
- <code title="post /v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}">client.agents.knowledge_bases.<a href="./src/gradientai/resources/agents/knowledge_bases.py">attach_single</a>(knowledge_base_uuid, \*, agent_uuid) -> <a href="./src/gradientai/types/agents/api_link_knowledge_base_output.py">APILinkKnowledgeBaseOutput</a></code>
- <code title="delete /v2/gen-ai/agents/{agent_uuid}/knowledge_bases/{knowledge_base_uuid}">client.agents.knowledge_bases.<a href="./src/gradientai/resources/agents/knowledge_bases.py">detach</a>(knowledge_base_uuid, \*, agent_uuid) -> <a href="./src/gradientai/types/agents/knowledge_base_detach_response.py">KnowledgeBaseDetachResponse</a></code>

## ChildAgents

Types:

```python
from gradientai.types.agents import (
    ChildAgentUpdateResponse,
    ChildAgentDeleteResponse,
    ChildAgentAddResponse,
    ChildAgentViewResponse,
)
```

Methods:

- <code title="put /v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}">client.agents.child_agents.<a href="./src/gradientai/resources/agents/child_agents.py">update</a>(path_child_agent_uuid, \*, path_parent_agent_uuid, \*\*<a href="src/gradientai/types/agents/child_agent_update_params.py">params</a>) -> <a href="./src/gradientai/types/agents/child_agent_update_response.py">ChildAgentUpdateResponse</a></code>
- <code title="delete /v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}">client.agents.child_agents.<a href="./src/gradientai/resources/agents/child_agents.py">delete</a>(child_agent_uuid, \*, parent_agent_uuid) -> <a href="./src/gradientai/types/agents/child_agent_delete_response.py">ChildAgentDeleteResponse</a></code>
- <code title="post /v2/gen-ai/agents/{parent_agent_uuid}/child_agents/{child_agent_uuid}">client.agents.child_agents.<a href="./src/gradientai/resources/agents/child_agents.py">add</a>(path_child_agent_uuid, \*, path_parent_agent_uuid, \*\*<a href="src/gradientai/types/agents/child_agent_add_params.py">params</a>) -> <a href="./src/gradientai/types/agents/child_agent_add_response.py">ChildAgentAddResponse</a></code>
- <code title="get /v2/gen-ai/agents/{uuid}/child_agents">client.agents.child_agents.<a href="./src/gradientai/resources/agents/child_agents.py">view</a>(uuid) -> <a href="./src/gradientai/types/agents/child_agent_view_response.py">ChildAgentViewResponse</a></code>

# Providers

## Anthropic

### Keys

Types:

```python
from gradientai.types.providers.anthropic import (
    KeyCreateResponse,
    KeyRetrieveResponse,
    KeyUpdateResponse,
    KeyListResponse,
    KeyDeleteResponse,
    KeyListAgentsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/anthropic/keys">client.providers.anthropic.keys.<a href="./src/gradientai/resources/providers/anthropic/keys.py">create</a>(\*\*<a href="src/gradientai/types/providers/anthropic/key_create_params.py">params</a>) -> <a href="./src/gradientai/types/providers/anthropic/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.providers.anthropic.keys.<a href="./src/gradientai/resources/providers/anthropic/keys.py">retrieve</a>(api_key_uuid) -> <a href="./src/gradientai/types/providers/anthropic/key_retrieve_response.py">KeyRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.providers.anthropic.keys.<a href="./src/gradientai/resources/providers/anthropic/keys.py">update</a>(path_api_key_uuid, \*\*<a href="src/gradientai/types/providers/anthropic/key_update_params.py">params</a>) -> <a href="./src/gradientai/types/providers/anthropic/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys">client.providers.anthropic.keys.<a href="./src/gradientai/resources/providers/anthropic/keys.py">list</a>(\*\*<a href="src/gradientai/types/providers/anthropic/key_list_params.py">params</a>) -> <a href="./src/gradientai/types/providers/anthropic/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /v2/gen-ai/anthropic/keys/{api_key_uuid}">client.providers.anthropic.keys.<a href="./src/gradientai/resources/providers/anthropic/keys.py">delete</a>(api_key_uuid) -> <a href="./src/gradientai/types/providers/anthropic/key_delete_response.py">KeyDeleteResponse</a></code>
- <code title="get /v2/gen-ai/anthropic/keys/{uuid}/agents">client.providers.anthropic.keys.<a href="./src/gradientai/resources/providers/anthropic/keys.py">list_agents</a>(uuid, \*\*<a href="src/gradientai/types/providers/anthropic/key_list_agents_params.py">params</a>) -> <a href="./src/gradientai/types/providers/anthropic/key_list_agents_response.py">KeyListAgentsResponse</a></code>

## OpenAI

### Keys

Types:

```python
from gradientai.types.providers.openai import (
    KeyCreateResponse,
    KeyRetrieveResponse,
    KeyUpdateResponse,
    KeyListResponse,
    KeyDeleteResponse,
    KeyRetrieveAgentsResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/openai/keys">client.providers.openai.keys.<a href="./src/gradientai/resources/providers/openai/keys.py">create</a>(\*\*<a href="src/gradientai/types/providers/openai/key_create_params.py">params</a>) -> <a href="./src/gradientai/types/providers/openai/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys/{api_key_uuid}">client.providers.openai.keys.<a href="./src/gradientai/resources/providers/openai/keys.py">retrieve</a>(api_key_uuid) -> <a href="./src/gradientai/types/providers/openai/key_retrieve_response.py">KeyRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/openai/keys/{api_key_uuid}">client.providers.openai.keys.<a href="./src/gradientai/resources/providers/openai/keys.py">update</a>(path_api_key_uuid, \*\*<a href="src/gradientai/types/providers/openai/key_update_params.py">params</a>) -> <a href="./src/gradientai/types/providers/openai/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys">client.providers.openai.keys.<a href="./src/gradientai/resources/providers/openai/keys.py">list</a>(\*\*<a href="src/gradientai/types/providers/openai/key_list_params.py">params</a>) -> <a href="./src/gradientai/types/providers/openai/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /v2/gen-ai/openai/keys/{api_key_uuid}">client.providers.openai.keys.<a href="./src/gradientai/resources/providers/openai/keys.py">delete</a>(api_key_uuid) -> <a href="./src/gradientai/types/providers/openai/key_delete_response.py">KeyDeleteResponse</a></code>
- <code title="get /v2/gen-ai/openai/keys/{uuid}/agents">client.providers.openai.keys.<a href="./src/gradientai/resources/providers/openai/keys.py">retrieve_agents</a>(uuid, \*\*<a href="src/gradientai/types/providers/openai/key_retrieve_agents_params.py">params</a>) -> <a href="./src/gradientai/types/providers/openai/key_retrieve_agents_response.py">KeyRetrieveAgentsResponse</a></code>

# Regions

Types:

```python
from gradientai.types import RegionListResponse
```

Methods:

- <code title="get /v2/gen-ai/regions">client.regions.<a href="./src/gradientai/resources/regions.py">list</a>(\*\*<a href="src/gradientai/types/region_list_params.py">params</a>) -> <a href="./src/gradientai/types/region_list_response.py">RegionListResponse</a></code>

# IndexingJobs

Types:

```python
from gradientai.types import (
    APIIndexingJob,
    IndexingJobCreateResponse,
    IndexingJobRetrieveResponse,
    IndexingJobListResponse,
    IndexingJobRetrieveDataSourcesResponse,
    IndexingJobUpdateCancelResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/indexing_jobs">client.indexing_jobs.<a href="./src/gradientai/resources/indexing_jobs.py">create</a>(\*\*<a href="src/gradientai/types/indexing_job_create_params.py">params</a>) -> <a href="./src/gradientai/types/indexing_job_create_response.py">IndexingJobCreateResponse</a></code>
- <code title="get /v2/gen-ai/indexing_jobs/{uuid}">client.indexing_jobs.<a href="./src/gradientai/resources/indexing_jobs.py">retrieve</a>(uuid) -> <a href="./src/gradientai/types/indexing_job_retrieve_response.py">IndexingJobRetrieveResponse</a></code>
- <code title="get /v2/gen-ai/indexing_jobs">client.indexing_jobs.<a href="./src/gradientai/resources/indexing_jobs.py">list</a>(\*\*<a href="src/gradientai/types/indexing_job_list_params.py">params</a>) -> <a href="./src/gradientai/types/indexing_job_list_response.py">IndexingJobListResponse</a></code>
- <code title="get /v2/gen-ai/indexing_jobs/{indexing_job_uuid}/data_sources">client.indexing_jobs.<a href="./src/gradientai/resources/indexing_jobs.py">retrieve_data_sources</a>(indexing_job_uuid) -> <a href="./src/gradientai/types/indexing_job_retrieve_data_sources_response.py">IndexingJobRetrieveDataSourcesResponse</a></code>
- <code title="put /v2/gen-ai/indexing_jobs/{uuid}/cancel">client.indexing_jobs.<a href="./src/gradientai/resources/indexing_jobs.py">update_cancel</a>(path_uuid, \*\*<a href="src/gradientai/types/indexing_job_update_cancel_params.py">params</a>) -> <a href="./src/gradientai/types/indexing_job_update_cancel_response.py">IndexingJobUpdateCancelResponse</a></code>

# KnowledgeBases

Types:

```python
from gradientai.types import (
    APIKnowledgeBase,
    KnowledgeBaseCreateResponse,
    KnowledgeBaseRetrieveResponse,
    KnowledgeBaseUpdateResponse,
    KnowledgeBaseListResponse,
    KnowledgeBaseDeleteResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/knowledge_bases">client.knowledge_bases.<a href="./src/gradientai/resources/knowledge_bases/knowledge_bases.py">create</a>(\*\*<a href="src/gradientai/types/knowledge_base_create_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_base_create_response.py">KnowledgeBaseCreateResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases/{uuid}">client.knowledge_bases.<a href="./src/gradientai/resources/knowledge_bases/knowledge_bases.py">retrieve</a>(uuid) -> <a href="./src/gradientai/types/knowledge_base_retrieve_response.py">KnowledgeBaseRetrieveResponse</a></code>
- <code title="put /v2/gen-ai/knowledge_bases/{uuid}">client.knowledge_bases.<a href="./src/gradientai/resources/knowledge_bases/knowledge_bases.py">update</a>(path_uuid, \*\*<a href="src/gradientai/types/knowledge_base_update_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_base_update_response.py">KnowledgeBaseUpdateResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases">client.knowledge_bases.<a href="./src/gradientai/resources/knowledge_bases/knowledge_bases.py">list</a>(\*\*<a href="src/gradientai/types/knowledge_base_list_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_base_list_response.py">KnowledgeBaseListResponse</a></code>
- <code title="delete /v2/gen-ai/knowledge_bases/{uuid}">client.knowledge_bases.<a href="./src/gradientai/resources/knowledge_bases/knowledge_bases.py">delete</a>(uuid) -> <a href="./src/gradientai/types/knowledge_base_delete_response.py">KnowledgeBaseDeleteResponse</a></code>

## DataSources

Types:

```python
from gradientai.types.knowledge_bases import (
    APIFileUploadDataSource,
    APIKnowledgeBaseDataSource,
    APISpacesDataSource,
    APIWebCrawlerDataSource,
    DataSourceCreateResponse,
    DataSourceListResponse,
    DataSourceDeleteResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources">client.knowledge_bases.data_sources.<a href="./src/gradientai/resources/knowledge_bases/data_sources.py">create</a>(path_knowledge_base_uuid, \*\*<a href="src/gradientai/types/knowledge_bases/data_source_create_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_bases/data_source_create_response.py">DataSourceCreateResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources">client.knowledge_bases.data_sources.<a href="./src/gradientai/resources/knowledge_bases/data_sources.py">list</a>(knowledge_base_uuid, \*\*<a href="src/gradientai/types/knowledge_bases/data_source_list_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_bases/data_source_list_response.py">DataSourceListResponse</a></code>
- <code title="delete /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources/{data_source_uuid}">client.knowledge_bases.data_sources.<a href="./src/gradientai/resources/knowledge_bases/data_sources.py">delete</a>(data_source_uuid, \*, knowledge_base_uuid) -> <a href="./src/gradientai/types/knowledge_bases/data_source_delete_response.py">DataSourceDeleteResponse</a></code>

# APIKeys

Types:

```python
from gradientai.types import (
    APIModelAPIKeyInfo,
    APIKeyCreateResponse,
    APIKeyUpdateResponse,
    APIKeyListResponse,
    APIKeyDeleteResponse,
    APIKeyUpdateRegenerateResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/models/api_keys">client.api_keys.<a href="./src/gradientai/resources/api_keys.py">create</a>(\*\*<a href="src/gradientai/types/api_key_create_params.py">params</a>) -> <a href="./src/gradientai/types/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="put /v2/gen-ai/models/api_keys/{api_key_uuid}">client.api_keys.<a href="./src/gradientai/resources/api_keys.py">update</a>(path_api_key_uuid, \*\*<a href="src/gradientai/types/api_key_update_params.py">params</a>) -> <a href="./src/gradientai/types/api_key_update_response.py">APIKeyUpdateResponse</a></code>
- <code title="get /v2/gen-ai/models/api_keys">client.api_keys.<a href="./src/gradientai/resources/api_keys.py">list</a>(\*\*<a href="src/gradientai/types/api_key_list_params.py">params</a>) -> <a href="./src/gradientai/types/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v2/gen-ai/models/api_keys/{api_key_uuid}">client.api_keys.<a href="./src/gradientai/resources/api_keys.py">delete</a>(api_key_uuid) -> <a href="./src/gradientai/types/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
- <code title="put /v2/gen-ai/models/api_keys/{api_key_uuid}/regenerate">client.api_keys.<a href="./src/gradientai/resources/api_keys.py">update_regenerate</a>(api_key_uuid) -> <a href="./src/gradientai/types/api_key_update_regenerate_response.py">APIKeyUpdateRegenerateResponse</a></code>

# Chat

## Completions

Types:

```python
from gradientai.types.chat import CompletionCreateResponse
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/gradientai/resources/chat/completions.py">create</a>(\*\*<a href="src/gradientai/types/chat/completion_create_params.py">params</a>) -> <a href="./src/gradientai/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

# Models

Types:

```python
from gradientai.types import Model, ModelListResponse
```

Methods:

- <code title="get /v2/gen-ai/models">client.models.<a href="./src/gradientai/resources/models.py">list</a>(\*\*<a href="src/gradientai/types/model_list_params.py">params</a>) -> <a href="./src/gradientai/types/model_list_response.py">ModelListResponse</a></code>
