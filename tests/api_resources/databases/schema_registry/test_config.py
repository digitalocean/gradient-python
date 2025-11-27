# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.databases.schema_registry import (
    ConfigUpdateResponse,
    ConfigRetrieveResponse,
    ConfigUpdateSubjectResponse,
    ConfigRetrieveSubjectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        config = client.databases.schema_registry.config.retrieve(
            "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        )
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.databases.schema_registry.config.with_raw_response.retrieve(
            "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.databases.schema_registry.config.with_streaming_response.retrieve(
            "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_cluster_uuid` but received ''"):
            client.databases.schema_registry.config.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        config = client.databases.schema_registry.config.update(
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.databases.schema_registry.config.with_raw_response.update(
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.databases.schema_registry.config.with_streaming_response.update(
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_cluster_uuid` but received ''"):
            client.databases.schema_registry.config.with_raw_response.update(
                database_cluster_uuid="",
                compatibility_level="BACKWARD",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_subject(self, client: Gradient) -> None:
        config = client.databases.schema_registry.config.retrieve_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        )
        assert_matches_type(ConfigRetrieveSubjectResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_subject(self, client: Gradient) -> None:
        response = client.databases.schema_registry.config.with_raw_response.retrieve_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigRetrieveSubjectResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_subject(self, client: Gradient) -> None:
        with client.databases.schema_registry.config.with_streaming_response.retrieve_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigRetrieveSubjectResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_subject(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_cluster_uuid` but received ''"):
            client.databases.schema_registry.config.with_raw_response.retrieve_subject(
                subject_name="customer-schema",
                database_cluster_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subject_name` but received ''"):
            client.databases.schema_registry.config.with_raw_response.retrieve_subject(
                subject_name="",
                database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_subject(self, client: Gradient) -> None:
        config = client.databases.schema_registry.config.update_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        )
        assert_matches_type(ConfigUpdateSubjectResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_subject(self, client: Gradient) -> None:
        response = client.databases.schema_registry.config.with_raw_response.update_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigUpdateSubjectResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_subject(self, client: Gradient) -> None:
        with client.databases.schema_registry.config.with_streaming_response.update_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigUpdateSubjectResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_subject(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_cluster_uuid` but received ''"):
            client.databases.schema_registry.config.with_raw_response.update_subject(
                subject_name="customer-schema",
                database_cluster_uuid="",
                compatibility_level="BACKWARD",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subject_name` but received ''"):
            client.databases.schema_registry.config.with_raw_response.update_subject(
                subject_name="",
                database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
                compatibility_level="BACKWARD",
            )


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        config = await async_client.databases.schema_registry.config.retrieve(
            "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        )
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.databases.schema_registry.config.with_raw_response.retrieve(
            "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.databases.schema_registry.config.with_streaming_response.retrieve(
            "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_cluster_uuid` but received ''"):
            await async_client.databases.schema_registry.config.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        config = await async_client.databases.schema_registry.config.update(
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.databases.schema_registry.config.with_raw_response.update(
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.databases.schema_registry.config.with_streaming_response.update(
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_cluster_uuid` but received ''"):
            await async_client.databases.schema_registry.config.with_raw_response.update(
                database_cluster_uuid="",
                compatibility_level="BACKWARD",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_subject(self, async_client: AsyncGradient) -> None:
        config = await async_client.databases.schema_registry.config.retrieve_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        )
        assert_matches_type(ConfigRetrieveSubjectResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_subject(self, async_client: AsyncGradient) -> None:
        response = await async_client.databases.schema_registry.config.with_raw_response.retrieve_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigRetrieveSubjectResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_subject(self, async_client: AsyncGradient) -> None:
        async with async_client.databases.schema_registry.config.with_streaming_response.retrieve_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigRetrieveSubjectResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_subject(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_cluster_uuid` but received ''"):
            await async_client.databases.schema_registry.config.with_raw_response.retrieve_subject(
                subject_name="customer-schema",
                database_cluster_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subject_name` but received ''"):
            await async_client.databases.schema_registry.config.with_raw_response.retrieve_subject(
                subject_name="",
                database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_subject(self, async_client: AsyncGradient) -> None:
        config = await async_client.databases.schema_registry.config.update_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        )
        assert_matches_type(ConfigUpdateSubjectResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_subject(self, async_client: AsyncGradient) -> None:
        response = await async_client.databases.schema_registry.config.with_raw_response.update_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigUpdateSubjectResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_subject(self, async_client: AsyncGradient) -> None:
        async with async_client.databases.schema_registry.config.with_streaming_response.update_subject(
            subject_name="customer-schema",
            database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
            compatibility_level="BACKWARD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigUpdateSubjectResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_subject(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_cluster_uuid` but received ''"):
            await async_client.databases.schema_registry.config.with_raw_response.update_subject(
                subject_name="customer-schema",
                database_cluster_uuid="",
                compatibility_level="BACKWARD",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subject_name` but received ''"):
            await async_client.databases.schema_registry.config.with_raw_response.update_subject(
                subject_name="",
                database_cluster_uuid="9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
                compatibility_level="BACKWARD",
            )
