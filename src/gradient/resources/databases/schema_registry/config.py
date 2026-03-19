# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.databases.schema_registry import config_update_params, config_update_subject_params
from ....types.databases.schema_registry.config_update_response import ConfigUpdateResponse
from ....types.databases.schema_registry.config_retrieve_response import ConfigRetrieveResponse
from ....types.databases.schema_registry.config_update_subject_response import ConfigUpdateSubjectResponse
from ....types.databases.schema_registry.config_retrieve_subject_response import ConfigRetrieveSubjectResponse

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    def retrieve(
        self,
        database_cluster_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRetrieveResponse:
        """
        To retrieve the Schema Registry configuration for a Kafka cluster, send a GET
        request to `/v2/databases/$DATABASE_ID/schema-registry/config`. The response is
        a JSON object with a `compatibility_level` key, which is set to an object
        containing any database configuration parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not database_cluster_uuid:
            raise ValueError(
                f"Expected a non-empty value for `database_cluster_uuid` but received {database_cluster_uuid!r}"
            )
        return self._get(
            ("https://api.digitalocean.com" if not self._client._base_url_overridden else "")
            + path_template(
                "/v2/databases/{database_cluster_uuid}/schema-registry/config",
                database_cluster_uuid=database_cluster_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveResponse,
        )

    def update(
        self,
        database_cluster_uuid: str,
        *,
        compatibility_level: Literal[
            "NONE", "BACKWARD", "BACKWARD_TRANSITIVE", "FORWARD", "FORWARD_TRANSITIVE", "FULL", "FULL_TRANSITIVE"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateResponse:
        """
        To update the Schema Registry configuration for a Kafka cluster, send a PUT
        request to `/v2/databases/$DATABASE_ID/schema-registry/config`. The response is
        a JSON object with a `compatibility_level` key, which is set to an object
        containing any database configuration parameters.

        Args:
          compatibility_level: The compatibility level of the schema registry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not database_cluster_uuid:
            raise ValueError(
                f"Expected a non-empty value for `database_cluster_uuid` but received {database_cluster_uuid!r}"
            )
        return self._put(
            ("https://api.digitalocean.com" if not self._client._base_url_overridden else "")
            + path_template(
                "/v2/databases/{database_cluster_uuid}/schema-registry/config",
                database_cluster_uuid=database_cluster_uuid,
            ),
            body=maybe_transform({"compatibility_level": compatibility_level}, config_update_params.ConfigUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )

    def retrieve_subject(
        self,
        subject_name: str,
        *,
        database_cluster_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRetrieveSubjectResponse:
        """
        To retrieve the Schema Registry configuration for a Subject of a Kafka cluster,
        send a GET request to
        `/v2/databases/$DATABASE_ID/schema-registry/config/$SUBJECT_NAME`. The response
        is a JSON object with a `compatibility_level` key, which is set to an object
        containing any database configuration parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not database_cluster_uuid:
            raise ValueError(
                f"Expected a non-empty value for `database_cluster_uuid` but received {database_cluster_uuid!r}"
            )
        if not subject_name:
            raise ValueError(f"Expected a non-empty value for `subject_name` but received {subject_name!r}")
        return self._get(
            ("https://api.digitalocean.com" if not self._client._base_url_overridden else "")
            + path_template(
                "/v2/databases/{database_cluster_uuid}/schema-registry/config/{subject_name}",
                database_cluster_uuid=database_cluster_uuid,
                subject_name=subject_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveSubjectResponse,
        )

    def update_subject(
        self,
        subject_name: str,
        *,
        database_cluster_uuid: str,
        compatibility_level: Literal[
            "NONE", "BACKWARD", "BACKWARD_TRANSITIVE", "FORWARD", "FORWARD_TRANSITIVE", "FULL", "FULL_TRANSITIVE"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateSubjectResponse:
        """
        To update the Schema Registry configuration for a Subject of a Kafka cluster,
        send a PUT request to
        `/v2/databases/$DATABASE_ID/schema-registry/config/$SUBJECT_NAME`. The response
        is a JSON object with a `compatibility_level` key, which is set to an object
        containing any database configuration parameters.

        Args:
          compatibility_level: The compatibility level of the schema registry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not database_cluster_uuid:
            raise ValueError(
                f"Expected a non-empty value for `database_cluster_uuid` but received {database_cluster_uuid!r}"
            )
        if not subject_name:
            raise ValueError(f"Expected a non-empty value for `subject_name` but received {subject_name!r}")
        return self._put(
            ("https://api.digitalocean.com" if not self._client._base_url_overridden else "")
            + path_template(
                "/v2/databases/{database_cluster_uuid}/schema-registry/config/{subject_name}",
                database_cluster_uuid=database_cluster_uuid,
                subject_name=subject_name,
            ),
            body=maybe_transform(
                {"compatibility_level": compatibility_level}, config_update_subject_params.ConfigUpdateSubjectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateSubjectResponse,
        )


class AsyncConfigResource(AsyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        database_cluster_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRetrieveResponse:
        """
        To retrieve the Schema Registry configuration for a Kafka cluster, send a GET
        request to `/v2/databases/$DATABASE_ID/schema-registry/config`. The response is
        a JSON object with a `compatibility_level` key, which is set to an object
        containing any database configuration parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not database_cluster_uuid:
            raise ValueError(
                f"Expected a non-empty value for `database_cluster_uuid` but received {database_cluster_uuid!r}"
            )
        return await self._get(
            ("https://api.digitalocean.com" if not self._client._base_url_overridden else "")
            + path_template(
                "/v2/databases/{database_cluster_uuid}/schema-registry/config",
                database_cluster_uuid=database_cluster_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveResponse,
        )

    async def update(
        self,
        database_cluster_uuid: str,
        *,
        compatibility_level: Literal[
            "NONE", "BACKWARD", "BACKWARD_TRANSITIVE", "FORWARD", "FORWARD_TRANSITIVE", "FULL", "FULL_TRANSITIVE"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateResponse:
        """
        To update the Schema Registry configuration for a Kafka cluster, send a PUT
        request to `/v2/databases/$DATABASE_ID/schema-registry/config`. The response is
        a JSON object with a `compatibility_level` key, which is set to an object
        containing any database configuration parameters.

        Args:
          compatibility_level: The compatibility level of the schema registry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not database_cluster_uuid:
            raise ValueError(
                f"Expected a non-empty value for `database_cluster_uuid` but received {database_cluster_uuid!r}"
            )
        return await self._put(
            ("https://api.digitalocean.com" if not self._client._base_url_overridden else "")
            + path_template(
                "/v2/databases/{database_cluster_uuid}/schema-registry/config",
                database_cluster_uuid=database_cluster_uuid,
            ),
            body=await async_maybe_transform(
                {"compatibility_level": compatibility_level}, config_update_params.ConfigUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )

    async def retrieve_subject(
        self,
        subject_name: str,
        *,
        database_cluster_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRetrieveSubjectResponse:
        """
        To retrieve the Schema Registry configuration for a Subject of a Kafka cluster,
        send a GET request to
        `/v2/databases/$DATABASE_ID/schema-registry/config/$SUBJECT_NAME`. The response
        is a JSON object with a `compatibility_level` key, which is set to an object
        containing any database configuration parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not database_cluster_uuid:
            raise ValueError(
                f"Expected a non-empty value for `database_cluster_uuid` but received {database_cluster_uuid!r}"
            )
        if not subject_name:
            raise ValueError(f"Expected a non-empty value for `subject_name` but received {subject_name!r}")
        return await self._get(
            ("https://api.digitalocean.com" if not self._client._base_url_overridden else "")
            + path_template(
                "/v2/databases/{database_cluster_uuid}/schema-registry/config/{subject_name}",
                database_cluster_uuid=database_cluster_uuid,
                subject_name=subject_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveSubjectResponse,
        )

    async def update_subject(
        self,
        subject_name: str,
        *,
        database_cluster_uuid: str,
        compatibility_level: Literal[
            "NONE", "BACKWARD", "BACKWARD_TRANSITIVE", "FORWARD", "FORWARD_TRANSITIVE", "FULL", "FULL_TRANSITIVE"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateSubjectResponse:
        """
        To update the Schema Registry configuration for a Subject of a Kafka cluster,
        send a PUT request to
        `/v2/databases/$DATABASE_ID/schema-registry/config/$SUBJECT_NAME`. The response
        is a JSON object with a `compatibility_level` key, which is set to an object
        containing any database configuration parameters.

        Args:
          compatibility_level: The compatibility level of the schema registry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not database_cluster_uuid:
            raise ValueError(
                f"Expected a non-empty value for `database_cluster_uuid` but received {database_cluster_uuid!r}"
            )
        if not subject_name:
            raise ValueError(f"Expected a non-empty value for `subject_name` but received {subject_name!r}")
        return await self._put(
            ("https://api.digitalocean.com" if not self._client._base_url_overridden else "")
            + path_template(
                "/v2/databases/{database_cluster_uuid}/schema-registry/config/{subject_name}",
                database_cluster_uuid=database_cluster_uuid,
                subject_name=subject_name,
            ),
            body=await async_maybe_transform(
                {"compatibility_level": compatibility_level}, config_update_subject_params.ConfigUpdateSubjectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateSubjectResponse,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.retrieve = to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = to_raw_response_wrapper(
            config.update,
        )
        self.retrieve_subject = to_raw_response_wrapper(
            config.retrieve_subject,
        )
        self.update_subject = to_raw_response_wrapper(
            config.update_subject,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.retrieve = async_to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            config.update,
        )
        self.retrieve_subject = async_to_raw_response_wrapper(
            config.retrieve_subject,
        )
        self.update_subject = async_to_raw_response_wrapper(
            config.update_subject,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.retrieve = to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            config.update,
        )
        self.retrieve_subject = to_streamed_response_wrapper(
            config.retrieve_subject,
        )
        self.update_subject = to_streamed_response_wrapper(
            config.update_subject,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.retrieve = async_to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
        self.retrieve_subject = async_to_streamed_response_wrapper(
            config.retrieve_subject,
        )
        self.update_subject = async_to_streamed_response_wrapper(
            config.update_subject,
        )
