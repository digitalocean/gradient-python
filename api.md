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
    AgentListResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/agents">client.agents.<a href="./src/gradientai/resources/agents/agents.py">create</a>(\*\*<a href="src/gradientai/types/agent_create_params.py">params</a>) -> <a href="./src/gradientai/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /v2/gen-ai/agents">client.agents.<a href="./src/gradientai/resources/agents/agents.py">list</a>(\*\*<a href="src/gradientai/types/agent_list_params.py">params</a>) -> <a href="./src/gradientai/types/agent_list_response.py">AgentListResponse</a></code>

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
from gradientai.types.agents import APILinkKnowledgeBaseOutput
```

Methods:

- <code title="post /v2/gen-ai/agents/{agent_uuid}/knowledge_bases">client.agents.knowledge_bases.<a href="./src/gradientai/resources/agents/knowledge_bases.py">attach</a>(agent_uuid) -> <a href="./src/gradientai/types/agents/api_link_knowledge_base_output.py">APILinkKnowledgeBaseOutput</a></code>

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
    KnowledgeBaseListResponse,
)
```

Methods:

- <code title="post /v2/gen-ai/knowledge_bases">client.knowledge_bases.<a href="./src/gradientai/resources/knowledge_bases/knowledge_bases.py">create</a>(\*\*<a href="src/gradientai/types/knowledge_base_create_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_base_create_response.py">KnowledgeBaseCreateResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases">client.knowledge_bases.<a href="./src/gradientai/resources/knowledge_bases/knowledge_bases.py">list</a>(\*\*<a href="src/gradientai/types/knowledge_base_list_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_base_list_response.py">KnowledgeBaseListResponse</a></code>

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
)
```

Methods:

- <code title="post /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources">client.knowledge_bases.data_sources.<a href="./src/gradientai/resources/knowledge_bases/data_sources.py">create</a>(path_knowledge_base_uuid, \*\*<a href="src/gradientai/types/knowledge_bases/data_source_create_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_bases/data_source_create_response.py">DataSourceCreateResponse</a></code>
- <code title="get /v2/gen-ai/knowledge_bases/{knowledge_base_uuid}/data_sources">client.knowledge_bases.data_sources.<a href="./src/gradientai/resources/knowledge_bases/data_sources.py">list</a>(knowledge_base_uuid, \*\*<a href="src/gradientai/types/knowledge_bases/data_source_list_params.py">params</a>) -> <a href="./src/gradientai/types/knowledge_bases/data_source_list_response.py">DataSourceListResponse</a></code>

# APIKeys

Types:

```python
from gradientai.types import APIAgreement, APIModelVersion
```

## APIKeys

Types:

```python
from gradientai.types.api_keys import APIModelAPIKeyInfo
```

# Chat

Types:

```python
from gradientai.types import (
    ChatCompletionRequestMessageContentPartText,
    ChatCompletionTokenLogprob,
    ChatCreateCompletionResponse,
)
```

Methods:

- <code title="post /chat/completions">client.chat.<a href="./src/gradientai/resources/chat.py">create_completion</a>(\*\*<a href="src/gradientai/types/chat_create_completion_params.py">params</a>) -> <a href="./src/gradientai/types/chat_create_completion_response.py">ChatCreateCompletionResponse</a></code>

# Embeddings

Types:

```python
from gradientai.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/gradientai/resources/embeddings.py">create</a>(\*\*<a href="src/gradientai/types/embedding_create_params.py">params</a>) -> <a href="./src/gradientai/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Models

Types:

```python
from gradientai.types import Model, ModelListResponse
```

Methods:

- <code title="get /models/{model}">client.models.<a href="./src/gradientai/resources/models.py">retrieve</a>(model) -> <a href="./src/gradientai/types/model.py">Model</a></code>
- <code title="get /models">client.models.<a href="./src/gradientai/resources/models.py">list</a>() -> <a href="./src/gradientai/types/model_list_response.py">ModelListResponse</a></code>
