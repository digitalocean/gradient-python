# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import chat, agents, models, regions, databases, inference, gpu_droplets, knowledge_bases
    from .resources.regions import RegionsResource, AsyncRegionsResource
    from .resources.chat.chat import ChatResource, AsyncChatResource
    from .resources.gpu_droplets import (
        GPUDropletsResource,
        AsyncGPUDropletsResource,
    )
    from .resources.agents.agents import AgentsResource, AsyncAgentsResource
    from .resources.models.models import ModelsResource, AsyncModelsResource
    from .resources.databases.databases import DatabasesResource, AsyncDatabasesResource
    from .resources.inference.inference import InferenceResource, AsyncInferenceResource
    from .resources.gpu_droplets.snapshots import (
        SnapshotsResource,
    )
    from .resources.gpu_droplets.images.images import (
        ImagesResource,
    )
    from .resources.gpu_droplets.account.account import (
        AccountResource,
    )
    from .resources.gpu_droplets.volumes.volumes import (
        VolumesResource,
    )
    from .resources.knowledge_bases.knowledge_bases import (
        KnowledgeBasesResource,
        AsyncKnowledgeBasesResource,
    )
    from .resources.gpu_droplets.firewalls.firewalls import (
        FirewallsResource,
    )
    from .resources.gpu_droplets.floating_ips.floating_ips import (
        FloatingIPsResource,
    )
    from .resources.gpu_droplets.load_balancers.load_balancers import (
        LoadBalancersResource,
    )

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "GradientAI",
    "AsyncGradientAI",
    "Client",
    "AsyncClient",
]


class GradientAI(SyncAPIClient):
    # client options
    api_key: str | None
    inference_key: str | None
    agent_key: str | None
    _agent_endpoint: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        inference_key: str | None = None,
        agent_key: str | None = None,
        agent_endpoint: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous GradientAI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `GRADIENTAI_API_KEY`
        - `inference_key` from `GRADIENTAI_INFERENCE_KEY`
        - `agent_key` from `GRADIENTAI_AGENT_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("GRADIENTAI_API_KEY")
        self.api_key = api_key

        if inference_key is None:
            inference_key = os.environ.get("GRADIENTAI_INFERENCE_KEY")
        self.inference_key = inference_key

        if agent_key is None:
            agent_key = os.environ.get("GRADIENTAI_AGENT_KEY")
        self.agent_key = agent_key

        self._agent_endpoint = agent_endpoint

        if base_url is None:
            base_url = os.environ.get("GRADIENT_AI_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.digitalocean.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

    @cached_property
    def agent_endpoint(self) -> str:
        """
        Returns the agent endpoint URL.
        """
        if self._agent_endpoint is None:
            raise ValueError(
                "Agent endpoint is not set. Please provide an agent endpoint when initializing the client."
            )
        if self._agent_endpoint.startswith("https://"):
            return self._agent_endpoint
        return "https://" + self._agent_endpoint

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def gpu_droplets(self) -> GPUDropletsResource:
        from .resources.gpu_droplets import GPUDropletsResource

        return GPUDropletsResource(self)

    @cached_property
    def inference(self) -> InferenceResource:
        from .resources.inference import InferenceResource

        return InferenceResource(self)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResource:
        from .resources.knowledge_bases import KnowledgeBasesResource

        return KnowledgeBasesResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def regions(self) -> RegionsResource:
        from .resources.regions import RegionsResource

        return RegionsResource(self)

    @cached_property
    def databases(self) -> DatabasesResource:
        from .resources.databases import DatabasesResource

        return DatabasesResource(self)

    @cached_property
    def databases(self) -> DatabasesResource:
        from .resources.databases import DatabasesResource

        return DatabasesResource(self)

    @cached_property
    def firewalls(self) -> FirewallsResource:
        from .resources.gpu_droplets.firewalls import FirewallsResource

        return FirewallsResource(self)

    @cached_property
    def floating_ips(self) -> FloatingIPsResource:
        from .resources.gpu_droplets.floating_ips import FloatingIPsResource

        return FloatingIPsResource(self)

    @cached_property
    def images(self) -> ImagesResource:
        from .resources.gpu_droplets.images import ImagesResource

        return ImagesResource(self)

    @cached_property
    def load_balancers(self) -> LoadBalancersResource:
        from .resources.gpu_droplets.load_balancers import LoadBalancersResource

        return LoadBalancersResource(self)

    @cached_property
    def snapshots(self) -> SnapshotsResource:
        from .resources.gpu_droplets.snapshots import SnapshotsResource

        return SnapshotsResource(self)

    @cached_property
    def volumes(self) -> VolumesResource:
        from .resources.gpu_droplets.volumes import VolumesResource

        return VolumesResource(self)

    @cached_property
    def account(self) -> AccountResource:
        from .resources.gpu_droplets.account import AccountResource

        return AccountResource(self)

    @cached_property
    def with_raw_response(self) -> GradientAIWithRawResponse:
        return GradientAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GradientAIWithStreamedResponse:
        return GradientAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if (self.api_key or self.agent_key or self.inference_key) and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected api_key, agent_key, or inference_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        inference_key: str | None = None,
        agent_key: str | None = None,
        agent_endpoint: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            api_key=api_key or self.api_key,
            inference_key=inference_key or self.inference_key,
            agent_key=agent_key or self.agent_key,
            agent_endpoint=agent_endpoint or self._agent_endpoint,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGradientAI(AsyncAPIClient):
    # client options
    api_key: str | None
    inference_key: str | None
    agent_key: str | None
    _agent_endpoint: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        inference_key: str | None = None,
        agent_key: str | None = None,
        agent_endpoint: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGradientAI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `GRADIENTAI_API_KEY`
        - `inference_key` from `GRADIENTAI_INFERENCE_KEY`
        - `agent_key` from `GRADIENTAI_AGENT_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("GRADIENTAI_API_KEY")
        self.api_key = api_key

        if inference_key is None:
            inference_key = os.environ.get("GRADIENTAI_INFERENCE_KEY")
        self.inference_key = inference_key

        if agent_key is None:
            agent_key = os.environ.get("GRADIENTAI_AGENT_KEY")
        self.agent_key = agent_key

        self._agent_endpoint = agent_endpoint

        if base_url is None:
            base_url = os.environ.get("GRADIENT_AI_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.digitalocean.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

    @cached_property
    def agent_endpoint(self) -> str:
        """
        Returns the agent endpoint URL.
        """
        if self._agent_endpoint is None:
            raise ValueError(
                "Agent endpoint is not set. Please provide an agent endpoint when initializing the client."
            )
        if self._agent_endpoint.startswith("https://"):
            return self._agent_endpoint
        return "https://" + self._agent_endpoint

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def gpu_droplets(self) -> AsyncGPUDropletsResource:
        from .resources.gpu_droplets import AsyncGPUDropletsResource

        return AsyncGPUDropletsResource(self)

    @cached_property
    def inference(self) -> AsyncInferenceResource:
        from .resources.inference import AsyncInferenceResource

        return AsyncInferenceResource(self)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResource:
        from .resources.knowledge_bases import AsyncKnowledgeBasesResource

        return AsyncKnowledgeBasesResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        from .resources.regions import AsyncRegionsResource

        return AsyncRegionsResource(self)

    @cached_property
    def databases(self) -> AsyncDatabasesResource:
        from .resources.databases import AsyncDatabasesResource

        return AsyncDatabasesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncGradientAIWithRawResponse:
        return AsyncGradientAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGradientAIWithStreamedResponse:
        return AsyncGradientAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if (self.api_key or self.agent_key or self.inference_key) and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected api_key, agent_key, or inference_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        inference_key: str | None = None,
        agent_key: str | None = None,
        agent_endpoint: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            api_key=api_key or self.api_key,
            inference_key=inference_key or self.inference_key,
            agent_key=agent_key or self.agent_key,
            agent_endpoint=agent_endpoint or self._agent_endpoint,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GradientAIWithRawResponse:
    _client: GradientAI

    def __init__(self, client: GradientAI) -> None:
        self._client = client

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def gpu_droplets(self) -> gpu_droplets.GPUDropletsResourceWithRawResponse:
        from .resources.gpu_droplets import GPUDropletsResourceWithRawResponse

        return GPUDropletsResourceWithRawResponse(self._client.gpu_droplets)

    @cached_property
    def inference(self) -> inference.InferenceResourceWithRawResponse:
        from .resources.inference import InferenceResourceWithRawResponse

        return InferenceResourceWithRawResponse(self._client.inference)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.KnowledgeBasesResourceWithRawResponse:
        from .resources.knowledge_bases import KnowledgeBasesResourceWithRawResponse

        return KnowledgeBasesResourceWithRawResponse(self._client.knowledge_bases)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def regions(self) -> regions.RegionsResourceWithRawResponse:
        from .resources.regions import RegionsResourceWithRawResponse

        return RegionsResourceWithRawResponse(self._client.regions)

    @cached_property
    def databases(self) -> databases.DatabasesResourceWithRawResponse:
        from .resources.databases import DatabasesResourceWithRawResponse

        return DatabasesResourceWithRawResponse(self._client.databases)


class AsyncGradientAIWithRawResponse:
    _client: AsyncGradientAI

    def __init__(self, client: AsyncGradientAI) -> None:
        self._client = client

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def gpu_droplets(self) -> gpu_droplets.AsyncGPUDropletsResourceWithRawResponse:
        from .resources.gpu_droplets import AsyncGPUDropletsResourceWithRawResponse

        return AsyncGPUDropletsResourceWithRawResponse(self._client.gpu_droplets)

    @cached_property
    def inference(self) -> inference.AsyncInferenceResourceWithRawResponse:
        from .resources.inference import AsyncInferenceResourceWithRawResponse

        return AsyncInferenceResourceWithRawResponse(self._client.inference)

    @cached_property
    def knowledge_bases(
        self,
    ) -> knowledge_bases.AsyncKnowledgeBasesResourceWithRawResponse:
        from .resources.knowledge_bases import (
            AsyncKnowledgeBasesResourceWithRawResponse,
        )

        return AsyncKnowledgeBasesResourceWithRawResponse(self._client.knowledge_bases)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def regions(self) -> regions.AsyncRegionsResourceWithRawResponse:
        from .resources.regions import AsyncRegionsResourceWithRawResponse

        return AsyncRegionsResourceWithRawResponse(self._client.regions)

    @cached_property
    def databases(self) -> databases.AsyncDatabasesResourceWithRawResponse:
        from .resources.databases import AsyncDatabasesResourceWithRawResponse

        return AsyncDatabasesResourceWithRawResponse(self._client.databases)


class GradientAIWithStreamedResponse:
    _client: GradientAI

    def __init__(self, client: GradientAI) -> None:
        self._client = client

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def gpu_droplets(self) -> gpu_droplets.GPUDropletsResourceWithStreamingResponse:
        from .resources.gpu_droplets import GPUDropletsResourceWithStreamingResponse

        return GPUDropletsResourceWithStreamingResponse(self._client.gpu_droplets)

    @cached_property
    def inference(self) -> inference.InferenceResourceWithStreamingResponse:
        from .resources.inference import InferenceResourceWithStreamingResponse

        return InferenceResourceWithStreamingResponse(self._client.inference)

    @cached_property
    def knowledge_bases(
        self,
    ) -> knowledge_bases.KnowledgeBasesResourceWithStreamingResponse:
        from .resources.knowledge_bases import (
            KnowledgeBasesResourceWithStreamingResponse,
        )

        return KnowledgeBasesResourceWithStreamingResponse(self._client.knowledge_bases)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def regions(self) -> regions.RegionsResourceWithStreamingResponse:
        from .resources.regions import RegionsResourceWithStreamingResponse

        return RegionsResourceWithStreamingResponse(self._client.regions)

    @cached_property
    def databases(self) -> databases.DatabasesResourceWithStreamingResponse:
        from .resources.databases import DatabasesResourceWithStreamingResponse

        return DatabasesResourceWithStreamingResponse(self._client.databases)

    @cached_property
    def databases(self) -> databases.DatabasesResourceWithStreamingResponse:
        from .resources.databases import DatabasesResourceWithStreamingResponse

        return DatabasesResourceWithStreamingResponse(self._client.databases)


class AsyncGradientAIWithStreamedResponse:
    _client: AsyncGradientAI

    def __init__(self, client: AsyncGradientAI) -> None:
        self._client = client

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def gpu_droplets(
        self,
    ) -> gpu_droplets.AsyncGPUDropletsResourceWithStreamingResponse:
        from .resources.gpu_droplets import (
            AsyncGPUDropletsResourceWithStreamingResponse,
        )

        return AsyncGPUDropletsResourceWithStreamingResponse(self._client.gpu_droplets)

    @cached_property
    def inference(self) -> inference.AsyncInferenceResourceWithStreamingResponse:
        from .resources.inference import AsyncInferenceResourceWithStreamingResponse

        return AsyncInferenceResourceWithStreamingResponse(self._client.inference)

    @cached_property
    def knowledge_bases(
        self,
    ) -> knowledge_bases.AsyncKnowledgeBasesResourceWithStreamingResponse:
        from .resources.knowledge_bases import (
            AsyncKnowledgeBasesResourceWithStreamingResponse,
        )

        return AsyncKnowledgeBasesResourceWithStreamingResponse(self._client.knowledge_bases)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def regions(self) -> regions.AsyncRegionsResourceWithStreamingResponse:
        from .resources.regions import AsyncRegionsResourceWithStreamingResponse

        return AsyncRegionsResourceWithStreamingResponse(self._client.regions)

    @cached_property
    def databases(self) -> databases.AsyncDatabasesResourceWithStreamingResponse:
        from .resources.databases import AsyncDatabasesResourceWithStreamingResponse

        return AsyncDatabasesResourceWithStreamingResponse(self._client.databases)


Client = GradientAI

AsyncClient = AsyncGradientAI
