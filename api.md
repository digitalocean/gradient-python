# Chat

## Completions

Types:

```python
from digitalocean_genai_sdk.types.chat import (
    CreateModelProperties,
    CreateResponse,
    RequestMessageContentPartText,
    ResponseMessage,
    TokenLogprob,
    Usage,
)
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/digitalocean_genai_sdk/resources/chat/completions.py">create</a>(\*\*<a href="src/digitalocean_genai_sdk/types/chat/completion_create_params.py">params</a>) -> <a href="./src/digitalocean_genai_sdk/types/chat/create_response.py">CreateResponse</a></code>

# Completions

Types:

```python
from digitalocean_genai_sdk.types import ChatCompletionStreamOptions, StopConfiguration
```

# Embeddings

Types:

```python
from digitalocean_genai_sdk.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/digitalocean_genai_sdk/resources/embeddings.py">create</a>(\*\*<a href="src/digitalocean_genai_sdk/types/embedding_create_params.py">params</a>) -> <a href="./src/digitalocean_genai_sdk/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Models

Types:

```python
from digitalocean_genai_sdk.types import Model, ModelListResponse
```

Methods:

- <code title="get /models/{model}">client.models.<a href="./src/digitalocean_genai_sdk/resources/models.py">retrieve</a>(model) -> <a href="./src/digitalocean_genai_sdk/types/model.py">Model</a></code>
- <code title="get /models">client.models.<a href="./src/digitalocean_genai_sdk/resources/models.py">list</a>() -> <a href="./src/digitalocean_genai_sdk/types/model_list_response.py">ModelListResponse</a></code>

# Responses

Types:

```python
from digitalocean_genai_sdk.types import ModelResponseProperties
```
