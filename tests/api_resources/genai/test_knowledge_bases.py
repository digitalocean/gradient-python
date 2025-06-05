# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.genai import (
    KnowledgeBaseListResponse,
    KnowledgeBaseCreateResponse,
    KnowledgeBaseDeleteResponse,
    KnowledgeBaseUpdateResponse,
    KnowledgeBaseRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DigitaloceanGenaiSDK) -> None:
        knowledge_base = client.genai.knowledge_bases.create()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        knowledge_base = client.genai.knowledge_bases.create(
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
    def test_raw_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.knowledge_bases.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.knowledge_bases.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        knowledge_base = client.genai.knowledge_bases.retrieve(
            "uuid",
        )
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.knowledge_bases.with_raw_response.retrieve(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.knowledge_bases.with_streaming_response.retrieve(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.genai.knowledge_bases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: DigitaloceanGenaiSDK) -> None:
        knowledge_base = client.genai.knowledge_bases.update(
            path_uuid="uuid",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        knowledge_base = client.genai.knowledge_bases.update(
            path_uuid="uuid",
            database_id="database_id",
            embedding_model_uuid="embedding_model_uuid",
            name="name",
            project_id="project_id",
            tags=["string"],
            body_uuid="uuid",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.knowledge_bases.with_raw_response.update(
            path_uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.knowledge_bases.with_streaming_response.update(
            path_uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            client.genai.knowledge_bases.with_raw_response.update(
                path_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DigitaloceanGenaiSDK) -> None:
        knowledge_base = client.genai.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        knowledge_base = client.genai.knowledge_bases.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DigitaloceanGenaiSDK) -> None:
        knowledge_base = client.genai.knowledge_bases.delete(
            "uuid",
        )
        assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.knowledge_bases.with_raw_response.delete(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.knowledge_bases.with_streaming_response.delete(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.genai.knowledge_bases.with_raw_response.delete(
                "",
            )


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        knowledge_base = await async_client.genai.knowledge_bases.create()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        knowledge_base = await async_client.genai.knowledge_bases.create(
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
    async def test_raw_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.knowledge_bases.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.knowledge_bases.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        knowledge_base = await async_client.genai.knowledge_bases.retrieve(
            "uuid",
        )
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.knowledge_bases.with_raw_response.retrieve(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.knowledge_bases.with_streaming_response.retrieve(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.genai.knowledge_bases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        knowledge_base = await async_client.genai.knowledge_bases.update(
            path_uuid="uuid",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        knowledge_base = await async_client.genai.knowledge_bases.update(
            path_uuid="uuid",
            database_id="database_id",
            embedding_model_uuid="embedding_model_uuid",
            name="name",
            project_id="project_id",
            tags=["string"],
            body_uuid="uuid",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.knowledge_bases.with_raw_response.update(
            path_uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.knowledge_bases.with_streaming_response.update(
            path_uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            await async_client.genai.knowledge_bases.with_raw_response.update(
                path_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        knowledge_base = await async_client.genai.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        knowledge_base = await async_client.genai.knowledge_bases.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        knowledge_base = await async_client.genai.knowledge_bases.delete(
            "uuid",
        )
        assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.knowledge_bases.with_raw_response.delete(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.knowledge_bases.with_streaming_response.delete(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.genai.knowledge_bases.with_raw_response.delete(
                "",
            )
