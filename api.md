# Assistants

Types:

```python
from serverless_inference_sdk_prod.types import (
    APIResponseFormatOption,
    AssistantObject,
    AssistantSupportedModels,
    AssistantToolsCode,
    AssistantToolsFileSearch,
    AssistantToolsFunction,
    FileSearchRanker,
    FunctionObject,
    ReasoningEffort,
    AssistantListResponse,
    AssistantDeleteResponse,
)
```

Methods:

- <code title="post /assistants">client.assistants.<a href="./src/serverless_inference_sdk_prod/resources/assistants.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/assistant_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/assistant_object.py">AssistantObject</a></code>
- <code title="get /assistants/{assistant_id}">client.assistants.<a href="./src/serverless_inference_sdk_prod/resources/assistants.py">retrieve</a>(assistant_id) -> <a href="./src/serverless_inference_sdk_prod/types/assistant_object.py">AssistantObject</a></code>
- <code title="post /assistants/{assistant_id}">client.assistants.<a href="./src/serverless_inference_sdk_prod/resources/assistants.py">update</a>(assistant_id, \*\*<a href="src/serverless_inference_sdk_prod/types/assistant_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/assistant_object.py">AssistantObject</a></code>
- <code title="get /assistants">client.assistants.<a href="./src/serverless_inference_sdk_prod/resources/assistants.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/assistant_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/assistant_list_response.py">AssistantListResponse</a></code>
- <code title="delete /assistants/{assistant_id}">client.assistants.<a href="./src/serverless_inference_sdk_prod/resources/assistants.py">delete</a>(assistant_id) -> <a href="./src/serverless_inference_sdk_prod/types/assistant_delete_response.py">AssistantDeleteResponse</a></code>

# Audio

Types:

```python
from serverless_inference_sdk_prod.types import (
    TranscriptionSegment,
    VoiceIDsShared,
    AudioTranscribeAudioResponse,
    AudioTranslateAudioResponse,
)
```

Methods:

- <code title="post /audio/speech">client.audio.<a href="./src/serverless_inference_sdk_prod/resources/audio.py">generate_speech</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/audio_generate_speech_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /audio/transcriptions">client.audio.<a href="./src/serverless_inference_sdk_prod/resources/audio.py">transcribe_audio</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/audio_transcribe_audio_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/audio_transcribe_audio_response.py">AudioTranscribeAudioResponse</a></code>
- <code title="post /audio/translations">client.audio.<a href="./src/serverless_inference_sdk_prod/resources/audio.py">translate_audio</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/audio_translate_audio_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/audio_translate_audio_response.py">AudioTranslateAudioResponse</a></code>

# Batches

Types:

```python
from serverless_inference_sdk_prod.types import Batch, BatchListResponse
```

Methods:

- <code title="post /batches">client.batches.<a href="./src/serverless_inference_sdk_prod/resources/batches.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/batch_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/batch.py">Batch</a></code>
- <code title="get /batches/{batch_id}">client.batches.<a href="./src/serverless_inference_sdk_prod/resources/batches.py">retrieve</a>(batch_id) -> <a href="./src/serverless_inference_sdk_prod/types/batch.py">Batch</a></code>
- <code title="get /batches">client.batches.<a href="./src/serverless_inference_sdk_prod/resources/batches.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/batch_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/batch_list_response.py">BatchListResponse</a></code>
- <code title="post /batches/{batch_id}/cancel">client.batches.<a href="./src/serverless_inference_sdk_prod/resources/batches.py">cancel</a>(batch_id) -> <a href="./src/serverless_inference_sdk_prod/types/batch.py">Batch</a></code>

# Chat

## Completions

Types:

```python
from serverless_inference_sdk_prod.types.chat import (
    CreateModelProperties,
    CreateResponse,
    MessageToolCall,
    ModelIDsShared,
    RequestMessageContentPartText,
    ResponseFormatJsonObject,
    ResponseFormatJsonSchema,
    ResponseFormatText,
    ResponseMessage,
    TokenLogprob,
    Usage,
    WebSearchContextSize,
    WebSearchLocation,
    CompletionListResponse,
    CompletionDeleteResponse,
    CompletionRetrieveMessagesResponse,
)
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/serverless_inference_sdk_prod/resources/chat/completions.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/chat/completion_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/chat/create_response.py">CreateResponse</a></code>
- <code title="get /chat/completions/{completion_id}">client.chat.completions.<a href="./src/serverless_inference_sdk_prod/resources/chat/completions.py">retrieve</a>(completion_id) -> <a href="./src/serverless_inference_sdk_prod/types/chat/create_response.py">CreateResponse</a></code>
- <code title="post /chat/completions/{completion_id}">client.chat.completions.<a href="./src/serverless_inference_sdk_prod/resources/chat/completions.py">update</a>(completion_id, \*\*<a href="src/serverless_inference_sdk_prod/types/chat/completion_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/chat/create_response.py">CreateResponse</a></code>
- <code title="get /chat/completions">client.chat.completions.<a href="./src/serverless_inference_sdk_prod/resources/chat/completions.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/chat/completion_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/chat/completion_list_response.py">CompletionListResponse</a></code>
- <code title="delete /chat/completions/{completion_id}">client.chat.completions.<a href="./src/serverless_inference_sdk_prod/resources/chat/completions.py">delete</a>(completion_id) -> <a href="./src/serverless_inference_sdk_prod/types/chat/completion_delete_response.py">CompletionDeleteResponse</a></code>
- <code title="get /chat/completions/{completion_id}/messages">client.chat.completions.<a href="./src/serverless_inference_sdk_prod/resources/chat/completions.py">retrieve_messages</a>(completion_id, \*\*<a href="src/serverless_inference_sdk_prod/types/chat/completion_retrieve_messages_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/chat/completion_retrieve_messages_response.py">CompletionRetrieveMessagesResponse</a></code>

# Completions

Types:

```python
from serverless_inference_sdk_prod.types import (
    ChatCompletionStreamOptions,
    StopConfiguration,
    CompletionCreateResponse,
)
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/serverless_inference_sdk_prod/resources/completions.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/completion_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/completion_create_response.py">CompletionCreateResponse</a></code>

# Embeddings

Types:

```python
from serverless_inference_sdk_prod.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/serverless_inference_sdk_prod/resources/embeddings.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/embedding_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Files

Types:

```python
from serverless_inference_sdk_prod.types import (
    OpenAIFile,
    FileListResponse,
    FileDeleteResponse,
    FileRetrieveContentResponse,
)
```

Methods:

- <code title="get /files/{file_id}">client.files.<a href="./src/serverless_inference_sdk_prod/resources/files.py">retrieve</a>(file_id) -> <a href="./src/serverless_inference_sdk_prod/types/openai_file.py">OpenAIFile</a></code>
- <code title="get /files">client.files.<a href="./src/serverless_inference_sdk_prod/resources/files.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/file_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/serverless_inference_sdk_prod/resources/files.py">delete</a>(file_id) -> <a href="./src/serverless_inference_sdk_prod/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/serverless_inference_sdk_prod/resources/files.py">retrieve_content</a>(file_id) -> str</code>
- <code title="post /files">client.files.<a href="./src/serverless_inference_sdk_prod/resources/files.py">upload</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/file_upload_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/openai_file.py">OpenAIFile</a></code>

# FineTuning

## Checkpoints

### Permissions

Types:

```python
from serverless_inference_sdk_prod.types.fine_tuning.checkpoints import (
    ListFineTuningCheckpointPermission,
    PermissionDeleteResponse,
)
```

Methods:

- <code title="post /fine_tuning/checkpoints/{permission_id}/permissions">client.fine_tuning.checkpoints.permissions.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/checkpoints/permissions.py">create</a>(permission_id, \*\*<a href="src/serverless_inference_sdk_prod/types/fine_tuning/checkpoints/permission_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/checkpoints/list_fine_tuning_checkpoint_permission.py">ListFineTuningCheckpointPermission</a></code>
- <code title="get /fine_tuning/checkpoints/{permission_id}/permissions">client.fine_tuning.checkpoints.permissions.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/checkpoints/permissions.py">retrieve</a>(permission_id, \*\*<a href="src/serverless_inference_sdk_prod/types/fine_tuning/checkpoints/permission_retrieve_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/checkpoints/list_fine_tuning_checkpoint_permission.py">ListFineTuningCheckpointPermission</a></code>
- <code title="delete /fine_tuning/checkpoints/{permission_id}/permissions">client.fine_tuning.checkpoints.permissions.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/checkpoints/permissions.py">delete</a>(permission_id) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/checkpoints/permission_delete_response.py">PermissionDeleteResponse</a></code>

## Jobs

Types:

```python
from serverless_inference_sdk_prod.types.fine_tuning import (
    FineTuneMethod,
    FineTuningJob,
    JobListResponse,
)
```

Methods:

- <code title="post /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/jobs/jobs.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/fine_tuning/job_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}">client.fine_tuning.jobs.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/jobs/jobs.py">retrieve</a>(fine_tuning_job_id) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/jobs/jobs.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/fine_tuning/job_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/job_list_response.py">JobListResponse</a></code>
- <code title="post /fine_tuning/jobs/{fine_tuning_job_id}/cancel">client.fine_tuning.jobs.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/jobs/jobs.py">cancel</a>(fine_tuning_job_id) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>

### Checkpoints

Types:

```python
from serverless_inference_sdk_prod.types.fine_tuning.jobs import CheckpointRetrieveResponse
```

Methods:

- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints">client.fine_tuning.jobs.checkpoints.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/jobs/checkpoints.py">retrieve</a>(fine_tuning_job_id, \*\*<a href="src/serverless_inference_sdk_prod/types/fine_tuning/jobs/checkpoint_retrieve_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/jobs/checkpoint_retrieve_response.py">CheckpointRetrieveResponse</a></code>

### Events

Types:

```python
from serverless_inference_sdk_prod.types.fine_tuning.jobs import EventRetrieveResponse
```

Methods:

- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/events">client.fine_tuning.jobs.events.<a href="./src/serverless_inference_sdk_prod/resources/fine_tuning/jobs/events.py">retrieve</a>(fine_tuning_job_id, \*\*<a href="src/serverless_inference_sdk_prod/types/fine_tuning/jobs/event_retrieve_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/fine_tuning/jobs/event_retrieve_response.py">EventRetrieveResponse</a></code>

# Images

Types:

```python
from serverless_inference_sdk_prod.types import ImagesResponse
```

Methods:

- <code title="post /images/edits">client.images.<a href="./src/serverless_inference_sdk_prod/resources/images.py">create_edit</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/image_create_edit_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/images_response.py">ImagesResponse</a></code>
- <code title="post /images/generations">client.images.<a href="./src/serverless_inference_sdk_prod/resources/images.py">create_generation</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/image_create_generation_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/images_response.py">ImagesResponse</a></code>
- <code title="post /images/variations">client.images.<a href="./src/serverless_inference_sdk_prod/resources/images.py">create_variation</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/image_create_variation_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/images_response.py">ImagesResponse</a></code>

# Models

Types:

```python
from serverless_inference_sdk_prod.types import Model, ModelListResponse, ModelDeleteResponse
```

Methods:

- <code title="get /models/{model}">client.models.<a href="./src/serverless_inference_sdk_prod/resources/models.py">retrieve</a>(model) -> <a href="./src/serverless_inference_sdk_prod/types/model.py">Model</a></code>
- <code title="get /models">client.models.<a href="./src/serverless_inference_sdk_prod/resources/models.py">list</a>() -> <a href="./src/serverless_inference_sdk_prod/types/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /models/{model}">client.models.<a href="./src/serverless_inference_sdk_prod/resources/models.py">delete</a>(model) -> <a href="./src/serverless_inference_sdk_prod/types/model_delete_response.py">ModelDeleteResponse</a></code>

# Moderations

Types:

```python
from serverless_inference_sdk_prod.types import ModerationClassifyResponse
```

Methods:

- <code title="post /moderations">client.moderations.<a href="./src/serverless_inference_sdk_prod/resources/moderations.py">classify</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/moderation_classify_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/moderation_classify_response.py">ModerationClassifyResponse</a></code>

# Organization

Types:

```python
from serverless_inference_sdk_prod.types import (
    AuditLogActorUser,
    AuditLogEventType,
    UsageResponse,
    OrganizationListAuditLogsResponse,
)
```

Methods:

- <code title="get /organization/costs">client.organization.<a href="./src/serverless_inference_sdk_prod/resources/organization/organization.py">get_costs</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization_get_costs_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>
- <code title="get /organization/audit_logs">client.organization.<a href="./src/serverless_inference_sdk_prod/resources/organization/organization.py">list_audit_logs</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization_list_audit_logs_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization_list_audit_logs_response.py">OrganizationListAuditLogsResponse</a></code>

## AdminAPIKeys

Types:

```python
from serverless_inference_sdk_prod.types.organization import (
    AdminAPIKey,
    AdminAPIKeyListResponse,
    AdminAPIKeyDeleteResponse,
)
```

Methods:

- <code title="post /organization/admin_api_keys">client.organization.admin_api_keys.<a href="./src/serverless_inference_sdk_prod/resources/organization/admin_api_keys.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/admin_api_key_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/admin_api_key.py">AdminAPIKey</a></code>
- <code title="get /organization/admin_api_keys/{key_id}">client.organization.admin_api_keys.<a href="./src/serverless_inference_sdk_prod/resources/organization/admin_api_keys.py">retrieve</a>(key_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/admin_api_key.py">AdminAPIKey</a></code>
- <code title="get /organization/admin_api_keys">client.organization.admin_api_keys.<a href="./src/serverless_inference_sdk_prod/resources/organization/admin_api_keys.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/admin_api_key_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/admin_api_key_list_response.py">AdminAPIKeyListResponse</a></code>
- <code title="delete /organization/admin_api_keys/{key_id}">client.organization.admin_api_keys.<a href="./src/serverless_inference_sdk_prod/resources/organization/admin_api_keys.py">delete</a>(key_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/admin_api_key_delete_response.py">AdminAPIKeyDeleteResponse</a></code>

## Invites

Types:

```python
from serverless_inference_sdk_prod.types.organization import (
    Invite,
    InviteListResponse,
    InviteDeleteResponse,
)
```

Methods:

- <code title="post /organization/invites">client.organization.invites.<a href="./src/serverless_inference_sdk_prod/resources/organization/invites.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/invite_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/invite.py">Invite</a></code>
- <code title="get /organization/invites/{invite_id}">client.organization.invites.<a href="./src/serverless_inference_sdk_prod/resources/organization/invites.py">retrieve</a>(invite_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/invite.py">Invite</a></code>
- <code title="get /organization/invites">client.organization.invites.<a href="./src/serverless_inference_sdk_prod/resources/organization/invites.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/invite_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/invite_list_response.py">InviteListResponse</a></code>
- <code title="delete /organization/invites/{invite_id}">client.organization.invites.<a href="./src/serverless_inference_sdk_prod/resources/organization/invites.py">delete</a>(invite_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/invite_delete_response.py">InviteDeleteResponse</a></code>

## Projects

Types:

```python
from serverless_inference_sdk_prod.types.organization import Project, ProjectListResponse
```

Methods:

- <code title="post /organization/projects">client.organization.projects.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/projects.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/project_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/project.py">Project</a></code>
- <code title="get /organization/projects/{project_id}">client.organization.projects.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/project.py">Project</a></code>
- <code title="post /organization/projects/{project_id}">client.organization.projects.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/projects.py">update</a>(project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/project_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/project.py">Project</a></code>
- <code title="get /organization/projects">client.organization.projects.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/projects.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/project_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/project_list_response.py">ProjectListResponse</a></code>
- <code title="post /organization/projects/{project_id}/archive">client.organization.projects.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/projects.py">archive</a>(project_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/project.py">Project</a></code>

### APIKeys

Types:

```python
from serverless_inference_sdk_prod.types.organization.projects import (
    ProjectAPIKey,
    APIKeyListResponse,
    APIKeyDeleteResponse,
)
```

Methods:

- <code title="get /organization/projects/{project_id}/api_keys/{key_id}">client.organization.projects.api_keys.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/api_keys.py">retrieve</a>(key_id, \*, project_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/project_api_key.py">ProjectAPIKey</a></code>
- <code title="get /organization/projects/{project_id}/api_keys">client.organization.projects.api_keys.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/api_keys.py">list</a>(project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/projects/api_key_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /organization/projects/{project_id}/api_keys/{key_id}">client.organization.projects.api_keys.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/api_keys.py">delete</a>(key_id, \*, project_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/api_key_delete_response.py">APIKeyDeleteResponse</a></code>

### RateLimits

Types:

```python
from serverless_inference_sdk_prod.types.organization.projects import (
    ProjectRateLimit,
    RateLimitListResponse,
)
```

Methods:

- <code title="post /organization/projects/{project_id}/rate_limits/{rate_limit_id}">client.organization.projects.rate_limits.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/rate_limits.py">update</a>(rate_limit_id, \*, project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/projects/rate_limit_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/project_rate_limit.py">ProjectRateLimit</a></code>
- <code title="get /organization/projects/{project_id}/rate_limits">client.organization.projects.rate_limits.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/rate_limits.py">list</a>(project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/projects/rate_limit_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/rate_limit_list_response.py">RateLimitListResponse</a></code>

### ServiceAccounts

Types:

```python
from serverless_inference_sdk_prod.types.organization.projects import (
    ProjectServiceAccount,
    ServiceAccountCreateResponse,
    ServiceAccountListResponse,
    ServiceAccountDeleteResponse,
)
```

Methods:

- <code title="post /organization/projects/{project_id}/service_accounts">client.organization.projects.service_accounts.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/service_accounts.py">create</a>(project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/projects/service_account_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/service_account_create_response.py">ServiceAccountCreateResponse</a></code>
- <code title="get /organization/projects/{project_id}/service_accounts/{service_account_id}">client.organization.projects.service_accounts.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/service_accounts.py">retrieve</a>(service_account_id, \*, project_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/project_service_account.py">ProjectServiceAccount</a></code>
- <code title="get /organization/projects/{project_id}/service_accounts">client.organization.projects.service_accounts.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/service_accounts.py">list</a>(project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/projects/service_account_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/service_account_list_response.py">ServiceAccountListResponse</a></code>
- <code title="delete /organization/projects/{project_id}/service_accounts/{service_account_id}">client.organization.projects.service_accounts.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/service_accounts.py">delete</a>(service_account_id, \*, project_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/service_account_delete_response.py">ServiceAccountDeleteResponse</a></code>

### Users

Types:

```python
from serverless_inference_sdk_prod.types.organization.projects import (
    ProjectUser,
    UserListResponse,
    UserDeleteResponse,
)
```

Methods:

- <code title="get /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/users.py">retrieve</a>(user_id, \*, project_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/project_user.py">ProjectUser</a></code>
- <code title="post /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/users.py">update</a>(user_id, \*, project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/projects/user_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/project_user.py">ProjectUser</a></code>
- <code title="get /organization/projects/{project_id}/users">client.organization.projects.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/users.py">list</a>(project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/projects/user_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/user_list_response.py">UserListResponse</a></code>
- <code title="delete /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/users.py">delete</a>(user_id, \*, project_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="post /organization/projects/{project_id}/users">client.organization.projects.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/projects/users.py">add</a>(project_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/projects/user_add_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/projects/project_user.py">ProjectUser</a></code>

## Usage

Methods:

- <code title="get /organization/usage/audio_speeches">client.organization.usage.<a href="./src/serverless_inference_sdk_prod/resources/organization/usage.py">audio_speeches</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/usage_audio_speeches_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>
- <code title="get /organization/usage/audio_transcriptions">client.organization.usage.<a href="./src/serverless_inference_sdk_prod/resources/organization/usage.py">audio_transcriptions</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/usage_audio_transcriptions_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>
- <code title="get /organization/usage/code_interpreter_sessions">client.organization.usage.<a href="./src/serverless_inference_sdk_prod/resources/organization/usage.py">code_interpreter_sessions</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/usage_code_interpreter_sessions_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>
- <code title="get /organization/usage/completions">client.organization.usage.<a href="./src/serverless_inference_sdk_prod/resources/organization/usage.py">completions</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/usage_completions_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>
- <code title="get /organization/usage/embeddings">client.organization.usage.<a href="./src/serverless_inference_sdk_prod/resources/organization/usage.py">embeddings</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/usage_embeddings_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>
- <code title="get /organization/usage/images">client.organization.usage.<a href="./src/serverless_inference_sdk_prod/resources/organization/usage.py">images</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/usage_images_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>
- <code title="get /organization/usage/moderations">client.organization.usage.<a href="./src/serverless_inference_sdk_prod/resources/organization/usage.py">moderations</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/usage_moderations_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>
- <code title="get /organization/usage/vector_stores">client.organization.usage.<a href="./src/serverless_inference_sdk_prod/resources/organization/usage.py">vector_stores</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/usage_vector_stores_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/usage_response.py">UsageResponse</a></code>

## Users

Types:

```python
from serverless_inference_sdk_prod.types.organization import (
    User,
    UserListResponse,
    UserDeleteResponse,
)
```

Methods:

- <code title="get /organization/users/{user_id}">client.organization.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/users.py">retrieve</a>(user_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/user.py">User</a></code>
- <code title="post /organization/users/{user_id}">client.organization.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/users.py">update</a>(user_id, \*\*<a href="src/serverless_inference_sdk_prod/types/organization/user_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/user.py">User</a></code>
- <code title="get /organization/users">client.organization.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/users.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/organization/user_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/organization/user_list_response.py">UserListResponse</a></code>
- <code title="delete /organization/users/{user_id}">client.organization.users.<a href="./src/serverless_inference_sdk_prod/resources/organization/users.py">delete</a>(user_id) -> <a href="./src/serverless_inference_sdk_prod/types/organization/user_delete_response.py">UserDeleteResponse</a></code>

# Realtime

Types:

```python
from serverless_inference_sdk_prod.types import (
    RealtimeCreateSessionResponse,
    RealtimeCreateTranscriptionSessionResponse,
)
```

Methods:

- <code title="post /realtime/sessions">client.realtime.<a href="./src/serverless_inference_sdk_prod/resources/realtime.py">create_session</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/realtime_create_session_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/realtime_create_session_response.py">RealtimeCreateSessionResponse</a></code>
- <code title="post /realtime/transcription_sessions">client.realtime.<a href="./src/serverless_inference_sdk_prod/resources/realtime.py">create_transcription_session</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/realtime_create_transcription_session_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/realtime_create_transcription_session_response.py">RealtimeCreateTranscriptionSessionResponse</a></code>

# Responses

Types:

```python
from serverless_inference_sdk_prod.types import (
    ComputerToolCall,
    ComputerToolCallOutput,
    ComputerToolCallSafetyCheck,
    FileSearchToolCall,
    FunctionToolCall,
    FunctionToolCallOutput,
    Includable,
    InputContent,
    InputMessage,
    ModelResponseProperties,
    OutputMessage,
    ReasoningItem,
    Response,
    ResponseProperties,
    WebSearchToolCall,
    ResponseListInputItemsResponse,
)
```

Methods:

- <code title="post /responses">client.responses.<a href="./src/serverless_inference_sdk_prod/resources/responses.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/response_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/response.py">Response</a></code>
- <code title="get /responses/{response_id}">client.responses.<a href="./src/serverless_inference_sdk_prod/resources/responses.py">retrieve</a>(response_id, \*\*<a href="src/serverless_inference_sdk_prod/types/response_retrieve_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/response.py">Response</a></code>
- <code title="delete /responses/{response_id}">client.responses.<a href="./src/serverless_inference_sdk_prod/resources/responses.py">delete</a>(response_id) -> None</code>
- <code title="get /responses/{response_id}/input_items">client.responses.<a href="./src/serverless_inference_sdk_prod/resources/responses.py">list_input_items</a>(response_id, \*\*<a href="src/serverless_inference_sdk_prod/types/response_list_input_items_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/response_list_input_items_response.py">ResponseListInputItemsResponse</a></code>

# Threads

Types:

```python
from serverless_inference_sdk_prod.types import (
    CreateThreadRequest,
    ThreadObject,
    ThreadDeleteResponse,
)
```

Methods:

- <code title="post /threads">client.threads.<a href="./src/serverless_inference_sdk_prod/resources/threads/threads.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/thread_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/thread_object.py">ThreadObject</a></code>
- <code title="get /threads/{thread_id}">client.threads.<a href="./src/serverless_inference_sdk_prod/resources/threads/threads.py">retrieve</a>(thread_id) -> <a href="./src/serverless_inference_sdk_prod/types/thread_object.py">ThreadObject</a></code>
- <code title="post /threads/{thread_id}">client.threads.<a href="./src/serverless_inference_sdk_prod/resources/threads/threads.py">update</a>(thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/thread_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/thread_object.py">ThreadObject</a></code>
- <code title="delete /threads/{thread_id}">client.threads.<a href="./src/serverless_inference_sdk_prod/resources/threads/threads.py">delete</a>(thread_id) -> <a href="./src/serverless_inference_sdk_prod/types/thread_delete_response.py">ThreadDeleteResponse</a></code>

## Runs

Types:

```python
from serverless_inference_sdk_prod.types.threads import (
    AssistantsAPIToolChoiceOption,
    RunObject,
    TruncationObject,
    RunListResponse,
)
```

Methods:

- <code title="post /threads/runs">client.threads.runs.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/runs.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/threads/run_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/run_object.py">RunObject</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}">client.threads.runs.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/runs.py">retrieve</a>(run_id, \*, thread_id) -> <a href="./src/serverless_inference_sdk_prod/types/threads/run_object.py">RunObject</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}">client.threads.runs.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/runs.py">update</a>(run_id, \*, thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/run_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/run_object.py">RunObject</a></code>
- <code title="get /threads/{thread_id}/runs">client.threads.runs.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/runs.py">list</a>(thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/run_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/run_list_response.py">RunListResponse</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/cancel">client.threads.runs.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/runs.py">cancel</a>(run_id, \*, thread_id) -> <a href="./src/serverless_inference_sdk_prod/types/threads/run_object.py">RunObject</a></code>
- <code title="post /threads/{thread_id}/runs">client.threads.runs.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/runs.py">create_run</a>(thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/run_create_run_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/run_object.py">RunObject</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/submit_tool_outputs">client.threads.runs.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/runs.py">submit_tool_outputs</a>(run_id, \*, thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/run_submit_tool_outputs_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/run_object.py">RunObject</a></code>

### Steps

Types:

```python
from serverless_inference_sdk_prod.types.threads.runs import RunStepObject, StepListResponse
```

Methods:

- <code title="get /threads/{thread_id}/runs/{run_id}/steps/{step_id}">client.threads.runs.steps.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/steps.py">retrieve</a>(step_id, \*, thread_id, run_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/runs/step_retrieve_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/runs/run_step_object.py">RunStepObject</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}/steps">client.threads.runs.steps.<a href="./src/serverless_inference_sdk_prod/resources/threads/runs/steps.py">list</a>(run_id, \*, thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/runs/step_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/runs/step_list_response.py">StepListResponse</a></code>

## Messages

Types:

```python
from serverless_inference_sdk_prod.types.threads import (
    AssistantToolsFileSearchTypeOnly,
    CreateMessageRequest,
    MessageContentImageFileObject,
    MessageContentImageURLObject,
    MessageObject,
    MessageListResponse,
    MessageDeleteResponse,
)
```

Methods:

- <code title="post /threads/{thread_id}/messages">client.threads.messages.<a href="./src/serverless_inference_sdk_prod/resources/threads/messages.py">create</a>(thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/message_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/message_object.py">MessageObject</a></code>
- <code title="get /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/serverless_inference_sdk_prod/resources/threads/messages.py">retrieve</a>(message_id, \*, thread_id) -> <a href="./src/serverless_inference_sdk_prod/types/threads/message_object.py">MessageObject</a></code>
- <code title="post /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/serverless_inference_sdk_prod/resources/threads/messages.py">update</a>(message_id, \*, thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/message_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/message_object.py">MessageObject</a></code>
- <code title="get /threads/{thread_id}/messages">client.threads.messages.<a href="./src/serverless_inference_sdk_prod/resources/threads/messages.py">list</a>(thread_id, \*\*<a href="src/serverless_inference_sdk_prod/types/threads/message_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/threads/message_list_response.py">MessageListResponse</a></code>
- <code title="delete /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/serverless_inference_sdk_prod/resources/threads/messages.py">delete</a>(message_id, \*, thread_id) -> <a href="./src/serverless_inference_sdk_prod/types/threads/message_delete_response.py">MessageDeleteResponse</a></code>

# Uploads

Types:

```python
from serverless_inference_sdk_prod.types import Upload, UploadAddPartResponse
```

Methods:

- <code title="post /uploads">client.uploads.<a href="./src/serverless_inference_sdk_prod/resources/uploads.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/upload_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/upload.py">Upload</a></code>
- <code title="post /uploads/{upload_id}/parts">client.uploads.<a href="./src/serverless_inference_sdk_prod/resources/uploads.py">add_part</a>(upload_id, \*\*<a href="src/serverless_inference_sdk_prod/types/upload_add_part_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/upload_add_part_response.py">UploadAddPartResponse</a></code>
- <code title="post /uploads/{upload_id}/cancel">client.uploads.<a href="./src/serverless_inference_sdk_prod/resources/uploads.py">cancel</a>(upload_id) -> <a href="./src/serverless_inference_sdk_prod/types/upload.py">Upload</a></code>
- <code title="post /uploads/{upload_id}/complete">client.uploads.<a href="./src/serverless_inference_sdk_prod/resources/uploads.py">complete</a>(upload_id, \*\*<a href="src/serverless_inference_sdk_prod/types/upload_complete_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/upload.py">Upload</a></code>

# VectorStores

Types:

```python
from serverless_inference_sdk_prod.types import (
    AutoChunkingStrategyRequestParam,
    ComparisonFilter,
    CompoundFilter,
    StaticChunkingStrategy,
    StaticChunkingStrategyRequestParam,
    VectorStoreExpirationAfter,
    VectorStoreObject,
    VectorStoreListResponse,
    VectorStoreDeleteResponse,
    VectorStoreSearchResponse,
)
```

Methods:

- <code title="post /vector_stores">client.vector_stores.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/vector_store_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="get /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/serverless_inference_sdk_prod/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="post /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/serverless_inference_sdk_prod/types/vector_store_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="get /vector_stores">client.vector_stores.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/serverless_inference_sdk_prod/types/vector_store_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="delete /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/serverless_inference_sdk_prod/types/vector_store_delete_response.py">VectorStoreDeleteResponse</a></code>
- <code title="post /vector_stores/{vector_store_id}/search">client.vector_stores.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/vector_stores.py">search</a>(vector_store_id, \*\*<a href="src/serverless_inference_sdk_prod/types/vector_store_search_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_store_search_response.py">VectorStoreSearchResponse</a></code>

## FileBatches

Types:

```python
from serverless_inference_sdk_prod.types.vector_stores import (
    ChunkingStrategyRequestParam,
    ListVectorStoreFilesResponse,
    VectorStoreFileBatchObject,
)
```

Methods:

- <code title="post /vector_stores/{vector_store_id}/file_batches">client.vector_stores.file_batches.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/file_batches.py">create</a>(vector_store_id, \*\*<a href="src/serverless_inference_sdk_prod/types/vector_stores/file_batch_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/vector_store_file_batch_object.py">VectorStoreFileBatchObject</a></code>
- <code title="get /vector_stores/{vector_store_id}/file_batches/{batch_id}">client.vector_stores.file_batches.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/file_batches.py">retrieve</a>(batch_id, \*, vector_store_id) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/vector_store_file_batch_object.py">VectorStoreFileBatchObject</a></code>
- <code title="post /vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel">client.vector_stores.file_batches.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/file_batches.py">cancel</a>(batch_id, \*, vector_store_id) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/vector_store_file_batch_object.py">VectorStoreFileBatchObject</a></code>
- <code title="get /vector_stores/{vector_store_id}/file_batches/{batch_id}/files">client.vector_stores.file_batches.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/file_batches.py">list_files</a>(batch_id, \*, vector_store_id, \*\*<a href="src/serverless_inference_sdk_prod/types/vector_stores/file_batch_list_files_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/list_vector_store_files_response.py">ListVectorStoreFilesResponse</a></code>

## Files

Types:

```python
from serverless_inference_sdk_prod.types.vector_stores import (
    VectorStoreFileObject,
    FileDeleteResponse,
    FileRetrieveContentResponse,
)
```

Methods:

- <code title="post /vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/serverless_inference_sdk_prod/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/vector_store_file_object.py">VectorStoreFileObject</a></code>
- <code title="get /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/vector_store_file_object.py">VectorStoreFileObject</a></code>
- <code title="post /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/files.py">update</a>(file_id, \*, vector_store_id, \*\*<a href="src/serverless_inference_sdk_prod/types/vector_stores/file_update_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/vector_store_file_object.py">VectorStoreFileObject</a></code>
- <code title="get /vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/serverless_inference_sdk_prod/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/list_vector_store_files_response.py">ListVectorStoreFilesResponse</a></code>
- <code title="delete /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /vector_stores/{vector_store_id}/files/{file_id}/content">client.vector_stores.files.<a href="./src/serverless_inference_sdk_prod/resources/vector_stores/files.py">retrieve_content</a>(file_id, \*, vector_store_id) -> <a href="./src/serverless_inference_sdk_prod/types/vector_stores/file_retrieve_content_response.py">FileRetrieveContentResponse</a></code>
