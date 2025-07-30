# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SchemaRegistryResource", "AsyncSchemaRegistryResource"]


class SchemaRegistryResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> SchemaRegistryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return SchemaRegistryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaRegistryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return SchemaRegistryResourceWithStreamingResponse(self)


class AsyncSchemaRegistryResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSchemaRegistryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemaRegistryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaRegistryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncSchemaRegistryResourceWithStreamingResponse(self)


class SchemaRegistryResourceWithRawResponse:
    def __init__(self, schema_registry: SchemaRegistryResource) -> None:
        self._schema_registry = schema_registry

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._schema_registry.config)


class AsyncSchemaRegistryResourceWithRawResponse:
    def __init__(self, schema_registry: AsyncSchemaRegistryResource) -> None:
        self._schema_registry = schema_registry

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._schema_registry.config)


class SchemaRegistryResourceWithStreamingResponse:
    def __init__(self, schema_registry: SchemaRegistryResource) -> None:
        self._schema_registry = schema_registry

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._schema_registry.config)


class AsyncSchemaRegistryResourceWithStreamingResponse:
    def __init__(self, schema_registry: AsyncSchemaRegistryResource) -> None:
        self._schema_registry = schema_registry

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._schema_registry.config)
