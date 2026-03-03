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
        """
        DigitalOcean's [managed database service](https://docs.digitalocean.com/products/databases)
        simplifies the creation and management of highly available database clusters. Currently, it
        offers support for [PostgreSQL](http://docs.digitalocean.com/products/databases/postgresql/),
        [Caching](https://docs.digitalocean.com/products/databases/redis/),
        [Valkey](https://docs.digitalocean.com/products/databases/valkey/),
        [MySQL](https://docs.digitalocean.com/products/databases/mysql/),
        [MongoDB](https://docs.digitalocean.com/products/databases/mongodb/), and
        [OpenSearch](https://docs.digitalocean.com/products/databases/opensearch/).

        By sending requests to the `/v2/databases` endpoint, you can list, create, or delete
        database clusters as well as scale the size of a cluster, add or remove read-only replicas,
        and manage other configuration details.

        Database clusters may be deployed in a multi-node, high-availability configuration.
        If your machine type is above the basic nodes, your node plan is above the smallest option,
        or you are running MongoDB, you may additionally include up to two standby nodes in your cluster.

        The size of individual nodes in a database cluster is represented by a human-readable slug,
        which is used in some of the following requests. Each slug denotes the node's identifier,
        CPU count, and amount of RAM, in that order.

        For a list of currently available database slugs and options, use the `/v2/databases/options` endpoint or use the
        `doctl databases options` [command](https://docs.digitalocean.com/reference/doctl/reference/databases/options).
        """
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
        """
        DigitalOcean's [managed database service](https://docs.digitalocean.com/products/databases)
        simplifies the creation and management of highly available database clusters. Currently, it
        offers support for [PostgreSQL](http://docs.digitalocean.com/products/databases/postgresql/),
        [Caching](https://docs.digitalocean.com/products/databases/redis/),
        [Valkey](https://docs.digitalocean.com/products/databases/valkey/),
        [MySQL](https://docs.digitalocean.com/products/databases/mysql/),
        [MongoDB](https://docs.digitalocean.com/products/databases/mongodb/), and
        [OpenSearch](https://docs.digitalocean.com/products/databases/opensearch/).

        By sending requests to the `/v2/databases` endpoint, you can list, create, or delete
        database clusters as well as scale the size of a cluster, add or remove read-only replicas,
        and manage other configuration details.

        Database clusters may be deployed in a multi-node, high-availability configuration.
        If your machine type is above the basic nodes, your node plan is above the smallest option,
        or you are running MongoDB, you may additionally include up to two standby nodes in your cluster.

        The size of individual nodes in a database cluster is represented by a human-readable slug,
        which is used in some of the following requests. Each slug denotes the node's identifier,
        CPU count, and amount of RAM, in that order.

        For a list of currently available database slugs and options, use the `/v2/databases/options` endpoint or use the
        `doctl databases options` [command](https://docs.digitalocean.com/reference/doctl/reference/databases/options).
        """
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
        """
        DigitalOcean's [managed database service](https://docs.digitalocean.com/products/databases)
        simplifies the creation and management of highly available database clusters. Currently, it
        offers support for [PostgreSQL](http://docs.digitalocean.com/products/databases/postgresql/),
        [Caching](https://docs.digitalocean.com/products/databases/redis/),
        [Valkey](https://docs.digitalocean.com/products/databases/valkey/),
        [MySQL](https://docs.digitalocean.com/products/databases/mysql/),
        [MongoDB](https://docs.digitalocean.com/products/databases/mongodb/), and
        [OpenSearch](https://docs.digitalocean.com/products/databases/opensearch/).

        By sending requests to the `/v2/databases` endpoint, you can list, create, or delete
        database clusters as well as scale the size of a cluster, add or remove read-only replicas,
        and manage other configuration details.

        Database clusters may be deployed in a multi-node, high-availability configuration.
        If your machine type is above the basic nodes, your node plan is above the smallest option,
        or you are running MongoDB, you may additionally include up to two standby nodes in your cluster.

        The size of individual nodes in a database cluster is represented by a human-readable slug,
        which is used in some of the following requests. Each slug denotes the node's identifier,
        CPU count, and amount of RAM, in that order.

        For a list of currently available database slugs and options, use the `/v2/databases/options` endpoint or use the
        `doctl databases options` [command](https://docs.digitalocean.com/reference/doctl/reference/databases/options).
        """
        return ConfigResourceWithRawResponse(self._schema_registry.config)


class AsyncSchemaRegistryResourceWithRawResponse:
    def __init__(self, schema_registry: AsyncSchemaRegistryResource) -> None:
        self._schema_registry = schema_registry

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        """
        DigitalOcean's [managed database service](https://docs.digitalocean.com/products/databases)
        simplifies the creation and management of highly available database clusters. Currently, it
        offers support for [PostgreSQL](http://docs.digitalocean.com/products/databases/postgresql/),
        [Caching](https://docs.digitalocean.com/products/databases/redis/),
        [Valkey](https://docs.digitalocean.com/products/databases/valkey/),
        [MySQL](https://docs.digitalocean.com/products/databases/mysql/),
        [MongoDB](https://docs.digitalocean.com/products/databases/mongodb/), and
        [OpenSearch](https://docs.digitalocean.com/products/databases/opensearch/).

        By sending requests to the `/v2/databases` endpoint, you can list, create, or delete
        database clusters as well as scale the size of a cluster, add or remove read-only replicas,
        and manage other configuration details.

        Database clusters may be deployed in a multi-node, high-availability configuration.
        If your machine type is above the basic nodes, your node plan is above the smallest option,
        or you are running MongoDB, you may additionally include up to two standby nodes in your cluster.

        The size of individual nodes in a database cluster is represented by a human-readable slug,
        which is used in some of the following requests. Each slug denotes the node's identifier,
        CPU count, and amount of RAM, in that order.

        For a list of currently available database slugs and options, use the `/v2/databases/options` endpoint or use the
        `doctl databases options` [command](https://docs.digitalocean.com/reference/doctl/reference/databases/options).
        """
        return AsyncConfigResourceWithRawResponse(self._schema_registry.config)


class SchemaRegistryResourceWithStreamingResponse:
    def __init__(self, schema_registry: SchemaRegistryResource) -> None:
        self._schema_registry = schema_registry

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        """
        DigitalOcean's [managed database service](https://docs.digitalocean.com/products/databases)
        simplifies the creation and management of highly available database clusters. Currently, it
        offers support for [PostgreSQL](http://docs.digitalocean.com/products/databases/postgresql/),
        [Caching](https://docs.digitalocean.com/products/databases/redis/),
        [Valkey](https://docs.digitalocean.com/products/databases/valkey/),
        [MySQL](https://docs.digitalocean.com/products/databases/mysql/),
        [MongoDB](https://docs.digitalocean.com/products/databases/mongodb/), and
        [OpenSearch](https://docs.digitalocean.com/products/databases/opensearch/).

        By sending requests to the `/v2/databases` endpoint, you can list, create, or delete
        database clusters as well as scale the size of a cluster, add or remove read-only replicas,
        and manage other configuration details.

        Database clusters may be deployed in a multi-node, high-availability configuration.
        If your machine type is above the basic nodes, your node plan is above the smallest option,
        or you are running MongoDB, you may additionally include up to two standby nodes in your cluster.

        The size of individual nodes in a database cluster is represented by a human-readable slug,
        which is used in some of the following requests. Each slug denotes the node's identifier,
        CPU count, and amount of RAM, in that order.

        For a list of currently available database slugs and options, use the `/v2/databases/options` endpoint or use the
        `doctl databases options` [command](https://docs.digitalocean.com/reference/doctl/reference/databases/options).
        """
        return ConfigResourceWithStreamingResponse(self._schema_registry.config)


class AsyncSchemaRegistryResourceWithStreamingResponse:
    def __init__(self, schema_registry: AsyncSchemaRegistryResource) -> None:
        self._schema_registry = schema_registry

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        DigitalOcean's [managed database service](https://docs.digitalocean.com/products/databases)
        simplifies the creation and management of highly available database clusters. Currently, it
        offers support for [PostgreSQL](http://docs.digitalocean.com/products/databases/postgresql/),
        [Caching](https://docs.digitalocean.com/products/databases/redis/),
        [Valkey](https://docs.digitalocean.com/products/databases/valkey/),
        [MySQL](https://docs.digitalocean.com/products/databases/mysql/),
        [MongoDB](https://docs.digitalocean.com/products/databases/mongodb/), and
        [OpenSearch](https://docs.digitalocean.com/products/databases/opensearch/).

        By sending requests to the `/v2/databases` endpoint, you can list, create, or delete
        database clusters as well as scale the size of a cluster, add or remove read-only replicas,
        and manage other configuration details.

        Database clusters may be deployed in a multi-node, high-availability configuration.
        If your machine type is above the basic nodes, your node plan is above the smallest option,
        or you are running MongoDB, you may additionally include up to two standby nodes in your cluster.

        The size of individual nodes in a database cluster is represented by a human-readable slug,
        which is used in some of the following requests. Each slug denotes the node's identifier,
        CPU count, and amount of RAM, in that order.

        For a list of currently available database slugs and options, use the `/v2/databases/options` endpoint or use the
        `doctl databases options` [command](https://docs.digitalocean.com/reference/doctl/reference/databases/options).
        """
        return AsyncConfigResourceWithStreamingResponse(self._schema_registry.config)
