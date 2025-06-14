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

# IndexingJobs

Types:

```python
from gradientai.types import APIIndexingJob
```

# KnowledgeBases

Types:

```python
from gradientai.types import APIKnowledgeBase
```

## DataSources

Types:

```python
from gradientai.types.knowledge_bases import (
    APIFileUploadDataSource,
    APIKnowledgeBaseDataSource,
    APISpacesDataSource,
    APIWebCrawlerDataSource,
)
```

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
