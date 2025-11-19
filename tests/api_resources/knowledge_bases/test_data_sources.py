# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.knowledge_bases import (
    DataSourceListResponse,
    DataSourceCreateResponse,
    DataSourceDeleteResponse,
    DataSourceCreatePresignedURLsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        data_source = client.knowledge_bases.data_sources.create(
            path_knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        data_source = client.knowledge_bases.data_sources.create(
            path_knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            aws_data_source={
                "bucket_name": "example name",
                "item_path": "example string",
                "key_id": "123e4567-e89b-12d3-a456-426614174000",
                "region": "example string",
                "secret_key": "example string",
            },
            body_knowledge_base_uuid='"12345678-1234-1234-1234-123456789012"',
            spaces_data_source={
                "bucket_name": "example name",
                "item_path": "example string",
                "region": "example string",
            },
            web_crawler_data_source={
                "base_url": "example string",
                "crawling_option": "UNKNOWN",
                "embed_media": True,
                "exclude_tags": ["example string"],
            },
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.knowledge_bases.data_sources.with_raw_response.create(
            path_knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.knowledge_bases.data_sources.with_streaming_response.create(
            path_knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Gradient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_knowledge_base_uuid` but received ''"
        ):
            client.knowledge_bases.data_sources.with_raw_response.create(
                path_knowledge_base_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        data_source = client.knowledge_bases.data_sources.list(
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        data_source = client.knowledge_bases.data_sources.list(
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            page=0,
            per_page=0,
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.knowledge_bases.data_sources.with_raw_response.list(
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.knowledge_bases.data_sources.with_streaming_response.list(
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceListResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            client.knowledge_bases.data_sources.with_raw_response.list(
                knowledge_base_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        data_source = client.knowledge_bases.data_sources.delete(
            data_source_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.knowledge_bases.data_sources.with_raw_response.delete(
            data_source_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.knowledge_bases.data_sources.with_streaming_response.delete(
            data_source_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            client.knowledge_bases.data_sources.with_raw_response.delete(
                data_source_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                knowledge_base_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_uuid` but received ''"):
            client.knowledge_bases.data_sources.with_raw_response.delete(
                data_source_uuid="",
                knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_presigned_urls(self, client: Gradient) -> None:
        data_source = client.knowledge_bases.data_sources.create_presigned_urls()
        assert_matches_type(DataSourceCreatePresignedURLsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_presigned_urls_with_all_params(self, client: Gradient) -> None:
        data_source = client.knowledge_bases.data_sources.create_presigned_urls(
            files=[
                {
                    "file_name": "example name",
                    "file_size": "file_size",
                }
            ],
        )
        assert_matches_type(DataSourceCreatePresignedURLsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_presigned_urls(self, client: Gradient) -> None:
        response = client.knowledge_bases.data_sources.with_raw_response.create_presigned_urls()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceCreatePresignedURLsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_presigned_urls(self, client: Gradient) -> None:
        with client.knowledge_bases.data_sources.with_streaming_response.create_presigned_urls() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceCreatePresignedURLsResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        data_source = await async_client.knowledge_bases.data_sources.create(
            path_knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        data_source = await async_client.knowledge_bases.data_sources.create(
            path_knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            aws_data_source={
                "bucket_name": "example name",
                "item_path": "example string",
                "key_id": "123e4567-e89b-12d3-a456-426614174000",
                "region": "example string",
                "secret_key": "example string",
            },
            body_knowledge_base_uuid='"12345678-1234-1234-1234-123456789012"',
            spaces_data_source={
                "bucket_name": "example name",
                "item_path": "example string",
                "region": "example string",
            },
            web_crawler_data_source={
                "base_url": "example string",
                "crawling_option": "UNKNOWN",
                "embed_media": True,
                "exclude_tags": ["example string"],
            },
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.data_sources.with_raw_response.create(
            path_knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.data_sources.with_streaming_response.create(
            path_knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncGradient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_knowledge_base_uuid` but received ''"
        ):
            await async_client.knowledge_bases.data_sources.with_raw_response.create(
                path_knowledge_base_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        data_source = await async_client.knowledge_bases.data_sources.list(
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        data_source = await async_client.knowledge_bases.data_sources.list(
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            page=0,
            per_page=0,
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.data_sources.with_raw_response.list(
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.data_sources.with_streaming_response.list(
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceListResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            await async_client.knowledge_bases.data_sources.with_raw_response.list(
                knowledge_base_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        data_source = await async_client.knowledge_bases.data_sources.delete(
            data_source_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.data_sources.with_raw_response.delete(
            data_source_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.data_sources.with_streaming_response.delete(
            data_source_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            await async_client.knowledge_bases.data_sources.with_raw_response.delete(
                data_source_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                knowledge_base_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_uuid` but received ''"):
            await async_client.knowledge_bases.data_sources.with_raw_response.delete(
                data_source_uuid="",
                knowledge_base_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_presigned_urls(self, async_client: AsyncGradient) -> None:
        data_source = await async_client.knowledge_bases.data_sources.create_presigned_urls()
        assert_matches_type(DataSourceCreatePresignedURLsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_presigned_urls_with_all_params(self, async_client: AsyncGradient) -> None:
        data_source = await async_client.knowledge_bases.data_sources.create_presigned_urls(
            files=[
                {
                    "file_name": "example name",
                    "file_size": "file_size",
                }
            ],
        )
        assert_matches_type(DataSourceCreatePresignedURLsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_presigned_urls(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.data_sources.with_raw_response.create_presigned_urls()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceCreatePresignedURLsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_presigned_urls(self, async_client: AsyncGradient) -> None:
        async with (
            async_client.knowledge_bases.data_sources.with_streaming_response.create_presigned_urls()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceCreatePresignedURLsResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True
