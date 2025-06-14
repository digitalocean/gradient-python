# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradientai import GradientAI, AsyncGradientAI
from tests.utils import assert_matches_type
from gradientai.types import (
    KnowledgeBaseListResponse,
    KnowledgeBaseCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: GradientAI) -> None:
        knowledge_base = client.knowledge_bases.create()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: GradientAI) -> None:
        knowledge_base = client.knowledge_bases.create(
            database_id="database_id",
            datasources=[
                {
                    "bucket_name": "bucket_name",
                    "bucket_region": "bucket_region",
                    "file_upload_data_source": {
                        "original_file_name": "original_file_name",
                        "size_in_bytes": "size_in_bytes",
                        "stored_object_key": "stored_object_key",
                    },
                    "item_path": "item_path",
                    "spaces_data_source": {
                        "bucket_name": "bucket_name",
                        "item_path": "item_path",
                        "region": "region",
                    },
                    "web_crawler_data_source": {
                        "base_url": "base_url",
                        "crawling_option": "UNKNOWN",
                        "embed_media": True,
                    },
                }
            ],
            embedding_model_uuid="embedding_model_uuid",
            name="name",
            project_id="project_id",
            region="region",
            tags=["string"],
            vpc_uuid="vpc_uuid",
        )
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: GradientAI) -> None:
        response = client.knowledge_bases.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: GradientAI) -> None:
        with client.knowledge_bases.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: GradientAI) -> None:
        knowledge_base = client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: GradientAI) -> None:
        knowledge_base = client.knowledge_bases.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: GradientAI) -> None:
        response = client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: GradientAI) -> None:
        with client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGradientAI) -> None:
        knowledge_base = await async_client.knowledge_bases.create()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradientAI) -> None:
        knowledge_base = await async_client.knowledge_bases.create(
            database_id="database_id",
            datasources=[
                {
                    "bucket_name": "bucket_name",
                    "bucket_region": "bucket_region",
                    "file_upload_data_source": {
                        "original_file_name": "original_file_name",
                        "size_in_bytes": "size_in_bytes",
                        "stored_object_key": "stored_object_key",
                    },
                    "item_path": "item_path",
                    "spaces_data_source": {
                        "bucket_name": "bucket_name",
                        "item_path": "item_path",
                        "region": "region",
                    },
                    "web_crawler_data_source": {
                        "base_url": "base_url",
                        "crawling_option": "UNKNOWN",
                        "embed_media": True,
                    },
                }
            ],
            embedding_model_uuid="embedding_model_uuid",
            name="name",
            project_id="project_id",
            region="region",
            tags=["string"],
            vpc_uuid="vpc_uuid",
        )
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.knowledge_bases.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradientAI) -> None:
        async with async_client.knowledge_bases.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGradientAI) -> None:
        knowledge_base = await async_client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradientAI) -> None:
        knowledge_base = await async_client.knowledge_bases.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradientAI) -> None:
        async with async_client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True
