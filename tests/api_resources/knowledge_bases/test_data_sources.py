# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from do_gradientai import GradientAI, AsyncGradientAI
from do_gradientai.types.knowledge_bases import (
    DataSourceListResponse,
    DataSourceCreateResponse,
    DataSourceDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: GradientAI) -> None:
        data_source = client.knowledge_bases.data_sources.create(
            path_knowledge_base_uuid="knowledge_base_uuid",
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: GradientAI) -> None:
        data_source = client.knowledge_bases.data_sources.create(
            path_knowledge_base_uuid="knowledge_base_uuid",
            aws_data_source={
                "bucket_name": "bucket_name",
                "item_path": "item_path",
                "key_id": "key_id",
                "region": "region",
                "secret_key": "secret_key",
            },
            body_knowledge_base_uuid="knowledge_base_uuid",
            spaces_data_source={
                "bucket_name": "bucket_name",
                "item_path": "item_path",
                "region": "region",
            },
            web_crawler_data_source={
                "base_url": "base_url",
                "crawling_option": "UNKNOWN",
                "embed_media": True,
            },
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: GradientAI) -> None:
        response = client.knowledge_bases.data_sources.with_raw_response.create(
            path_knowledge_base_uuid="knowledge_base_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: GradientAI) -> None:
        with client.knowledge_bases.data_sources.with_streaming_response.create(
            path_knowledge_base_uuid="knowledge_base_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: GradientAI) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_knowledge_base_uuid` but received ''"
        ):
            client.knowledge_bases.data_sources.with_raw_response.create(
                path_knowledge_base_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: GradientAI) -> None:
        data_source = client.knowledge_bases.data_sources.list(
            knowledge_base_uuid="knowledge_base_uuid",
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: GradientAI) -> None:
        data_source = client.knowledge_bases.data_sources.list(
            knowledge_base_uuid="knowledge_base_uuid",
            page=0,
            per_page=0,
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: GradientAI) -> None:
        response = client.knowledge_bases.data_sources.with_raw_response.list(
            knowledge_base_uuid="knowledge_base_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: GradientAI) -> None:
        with client.knowledge_bases.data_sources.with_streaming_response.list(
            knowledge_base_uuid="knowledge_base_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceListResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            client.knowledge_bases.data_sources.with_raw_response.list(
                knowledge_base_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: GradientAI) -> None:
        data_source = client.knowledge_bases.data_sources.delete(
            data_source_uuid="data_source_uuid",
            knowledge_base_uuid="knowledge_base_uuid",
        )
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: GradientAI) -> None:
        response = client.knowledge_bases.data_sources.with_raw_response.delete(
            data_source_uuid="data_source_uuid",
            knowledge_base_uuid="knowledge_base_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: GradientAI) -> None:
        with client.knowledge_bases.data_sources.with_streaming_response.delete(
            data_source_uuid="data_source_uuid",
            knowledge_base_uuid="knowledge_base_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            client.knowledge_bases.data_sources.with_raw_response.delete(
                data_source_uuid="data_source_uuid",
                knowledge_base_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_uuid` but received ''"):
            client.knowledge_bases.data_sources.with_raw_response.delete(
                data_source_uuid="",
                knowledge_base_uuid="knowledge_base_uuid",
            )


class TestAsyncDataSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGradientAI) -> None:
        data_source = await async_client.knowledge_bases.data_sources.create(
            path_knowledge_base_uuid="knowledge_base_uuid",
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradientAI) -> None:
        data_source = await async_client.knowledge_bases.data_sources.create(
            path_knowledge_base_uuid="knowledge_base_uuid",
            aws_data_source={
                "bucket_name": "bucket_name",
                "item_path": "item_path",
                "key_id": "key_id",
                "region": "region",
                "secret_key": "secret_key",
            },
            body_knowledge_base_uuid="knowledge_base_uuid",
            spaces_data_source={
                "bucket_name": "bucket_name",
                "item_path": "item_path",
                "region": "region",
            },
            web_crawler_data_source={
                "base_url": "base_url",
                "crawling_option": "UNKNOWN",
                "embed_media": True,
            },
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.knowledge_bases.data_sources.with_raw_response.create(
            path_knowledge_base_uuid="knowledge_base_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradientAI) -> None:
        async with async_client.knowledge_bases.data_sources.with_streaming_response.create(
            path_knowledge_base_uuid="knowledge_base_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_knowledge_base_uuid` but received ''"
        ):
            await async_client.knowledge_bases.data_sources.with_raw_response.create(
                path_knowledge_base_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGradientAI) -> None:
        data_source = await async_client.knowledge_bases.data_sources.list(
            knowledge_base_uuid="knowledge_base_uuid",
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradientAI) -> None:
        data_source = await async_client.knowledge_bases.data_sources.list(
            knowledge_base_uuid="knowledge_base_uuid",
            page=0,
            per_page=0,
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.knowledge_bases.data_sources.with_raw_response.list(
            knowledge_base_uuid="knowledge_base_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradientAI) -> None:
        async with async_client.knowledge_bases.data_sources.with_streaming_response.list(
            knowledge_base_uuid="knowledge_base_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceListResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            await async_client.knowledge_bases.data_sources.with_raw_response.list(
                knowledge_base_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradientAI) -> None:
        data_source = await async_client.knowledge_bases.data_sources.delete(
            data_source_uuid="data_source_uuid",
            knowledge_base_uuid="knowledge_base_uuid",
        )
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.knowledge_bases.data_sources.with_raw_response.delete(
            data_source_uuid="data_source_uuid",
            knowledge_base_uuid="knowledge_base_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradientAI) -> None:
        async with async_client.knowledge_bases.data_sources.with_streaming_response.delete(
            data_source_uuid="data_source_uuid",
            knowledge_base_uuid="knowledge_base_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            await async_client.knowledge_bases.data_sources.with_raw_response.delete(
                data_source_uuid="data_source_uuid",
                knowledge_base_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_uuid` but received ''"):
            await async_client.knowledge_bases.data_sources.with_raw_response.delete(
                data_source_uuid="",
                knowledge_base_uuid="knowledge_base_uuid",
            )
