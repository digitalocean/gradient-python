# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types import (
    KnowledgeBaseListResponse,
    KnowledgeBaseCreateResponse,
    KnowledgeBaseDeleteResponse,
    KnowledgeBaseUpdateResponse,
    KnowledgeBaseRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.create()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.create(
            database_id='"12345678-1234-1234-1234-123456789012"',
            datasources=[
                {
                    "aws_data_source": {
                        "bucket_name": "example name",
                        "item_path": "example string",
                        "key_id": "123e4567-e89b-12d3-a456-426614174000",
                        "region": "example string",
                        "secret_key": "example string",
                    },
                    "bucket_name": "example name",
                    "bucket_region": "example string",
                    "dropbox_data_source": {
                        "folder": "example string",
                        "refresh_token": "example string",
                    },
                    "file_upload_data_source": {
                        "original_file_name": "example name",
                        "size_in_bytes": "12345",
                        "stored_object_key": "example string",
                    },
                    "item_path": "example string",
                    "spaces_data_source": {
                        "bucket_name": "example name",
                        "item_path": "example string",
                        "region": "example string",
                    },
                    "web_crawler_data_source": {
                        "base_url": "example string",
                        "crawling_option": "UNKNOWN",
                        "embed_media": True,
                    },
                }
            ],
            embedding_model_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"My Knowledge Base"',
            project_id='"12345678-1234-1234-1234-123456789012"',
            region='"tor1"',
            tags=["example string"],
            vpc_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.knowledge_bases.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.knowledge_bases.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.knowledge_bases.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.knowledge_bases.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.knowledge_bases.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_wait_until_database_online(self, client: Gradient, respx_mock: Any) -> None:
        """Test successful wait_until_database_online when database becomes ONLINE."""
        kb_uuid = "test-kb-id"

        call_count = [0]

        def get_response(_: httpx.Request) -> httpx.Response:
            call_count[0] += 1
            if call_count[0] == 1:
                return httpx.Response(200, json={"database_status": "CREATING"})
            else:
                return httpx.Response(200, json={"database_status": "ONLINE"})

        respx_mock.get(f"/v2/gen-ai/knowledge_bases/{kb_uuid}").mock(side_effect=get_response)

        kb = client.knowledge_bases.wait_until_database_online(kb_uuid, poll_interval=0.1, timeout=10.0)
        assert_matches_type(KnowledgeBaseRetrieveResponse, kb, path=["response"])
        assert kb.database_status == "ONLINE"

    @parametrize
    def test_wait_until_database_online_timeout(self, client: Gradient, respx_mock: Any) -> None:
        """Test that wait_until_database_online raises timeout error."""
        from gradient._exceptions import KnowledgeBaseDatabaseTimeoutError

        kb_uuid = "test-kb-id"

        respx_mock.get(f"/v2/gen-ai/knowledge_bases/{kb_uuid}").mock(
            return_value=httpx.Response(200, json={"database_status": "CREATING"})
        )

        with pytest.raises(KnowledgeBaseDatabaseTimeoutError) as exc_info:
            client.knowledge_bases.wait_until_database_online(kb_uuid, poll_interval=0.1, timeout=0.5)

        assert "did not reach ONLINE within" in str(exc_info.value)
        assert exc_info.value.knowledge_base_id == kb_uuid

    @parametrize
    def test_wait_until_database_online_failed(self, client: Gradient, respx_mock: Any) -> None:
        """Test that wait_until_database_online raises error on failure status."""
        from gradient._exceptions import KnowledgeBaseDatabaseError

        kb_uuid = "test-kb-id"

        respx_mock.get(f"/v2/gen-ai/knowledge_bases/{kb_uuid}").mock(
            return_value=httpx.Response(200, json={"database_status": "UNHEALTHY"})
        )

        with pytest.raises(KnowledgeBaseDatabaseError) as exc_info:
            client.knowledge_bases.wait_until_database_online(kb_uuid, poll_interval=0.1, timeout=10.0)

        assert "failed with status: UNHEALTHY" in str(exc_info.value)

    @parametrize
    def test_wait_until_database_online_empty_uuid(self, client: Gradient) -> None:
        """Test that wait_until_database_online validates empty uuid."""
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid`"):
            client.knowledge_bases.wait_until_database_online("")

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            database_id='"12345678-1234-1234-1234-123456789012"',
            embedding_model_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"My Knowledge Base"',
            project_id='"12345678-1234-1234-1234-123456789012"',
            tags=["example string"],
            body_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.knowledge_bases.with_raw_response.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.knowledge_bases.with_streaming_response.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            client.knowledge_bases.with_raw_response.update(
                path_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.knowledge_bases.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.knowledge_bases.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.knowledge_bases.with_raw_response.delete(
                "",
            )


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.create()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.create(
            database_id='"12345678-1234-1234-1234-123456789012"',
            datasources=[
                {
                    "aws_data_source": {
                        "bucket_name": "example name",
                        "item_path": "example string",
                        "key_id": "123e4567-e89b-12d3-a456-426614174000",
                        "region": "example string",
                        "secret_key": "example string",
                    },
                    "bucket_name": "example name",
                    "bucket_region": "example string",
                    "dropbox_data_source": {
                        "folder": "example string",
                        "refresh_token": "example string",
                    },
                    "file_upload_data_source": {
                        "original_file_name": "example name",
                        "size_in_bytes": "12345",
                        "stored_object_key": "example string",
                    },
                    "item_path": "example string",
                    "spaces_data_source": {
                        "bucket_name": "example name",
                        "item_path": "example string",
                        "region": "example string",
                    },
                    "web_crawler_data_source": {
                        "base_url": "example string",
                        "crawling_option": "UNKNOWN",
                        "embed_media": True,
                    },
                }
            ],
            embedding_model_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"My Knowledge Base"',
            project_id='"12345678-1234-1234-1234-123456789012"',
            region='"tor1"',
            tags=["example string"],
            vpc_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseCreateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.knowledge_bases.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_wait_until_database_online(self, async_client: AsyncGradient, respx_mock: Any) -> None:
        """Async: Test successful wait_until_database_online when database becomes ONLINE."""
        kb_uuid = "test-kb-id"

        call_count = [0]

        def get_response(_: httpx.Request) -> httpx.Response:
            call_count[0] += 1
            if call_count[0] == 1:
                return httpx.Response(200, json={"database_status": "CREATING"})
            else:
                return httpx.Response(200, json={"database_status": "ONLINE"})

        respx_mock.get(f"/v2/gen-ai/knowledge_bases/{kb_uuid}").mock(side_effect=get_response)

        kb = await async_client.knowledge_bases.wait_until_database_online(kb_uuid, poll_interval=0.1, timeout=10.0)
        assert_matches_type(KnowledgeBaseRetrieveResponse, kb, path=["response"])
        assert kb.database_status == "ONLINE"

    @parametrize
    async def test_wait_until_database_online_timeout(self, async_client: AsyncGradient, respx_mock: Any) -> None:
        """Async: Test that wait_until_database_online raises timeout error."""
        from gradient._exceptions import KnowledgeBaseDatabaseTimeoutError

        kb_uuid = "test-kb-id"

        respx_mock.get(f"/v2/gen-ai/knowledge_bases/{kb_uuid}").mock(
            return_value=httpx.Response(200, json={"database_status": "CREATING"})
        )

        with pytest.raises(KnowledgeBaseDatabaseTimeoutError) as exc_info:
            await async_client.knowledge_bases.wait_until_database_online(kb_uuid, poll_interval=0.1, timeout=0.5)

        assert "did not reach ONLINE within" in str(exc_info.value)
        assert exc_info.value.knowledge_base_id == kb_uuid

    @parametrize
    async def test_wait_until_database_online_failed(self, async_client: AsyncGradient, respx_mock: Any) -> None:
        """Async: Test that wait_until_database_online raises error on failure status."""
        from gradient._exceptions import KnowledgeBaseDatabaseError

        kb_uuid = "test-kb-id"

        respx_mock.get(f"/v2/gen-ai/knowledge_bases/{kb_uuid}").mock(
            return_value=httpx.Response(200, json={"database_status": "UNHEALTHY"})
        )

        with pytest.raises(KnowledgeBaseDatabaseError) as exc_info:
            await async_client.knowledge_bases.wait_until_database_online(kb_uuid, poll_interval=0.1, timeout=10.0)

        assert "failed with status: UNHEALTHY" in str(exc_info.value)

    @parametrize
    async def test_wait_until_database_online_empty_uuid(self, async_client: AsyncGradient) -> None:
        """Async: Test that wait_until_database_online validates empty uuid."""
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid`"):
            await async_client.knowledge_bases.wait_until_database_online("")

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            database_id='"12345678-1234-1234-1234-123456789012"',
            embedding_model_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"My Knowledge Base"',
            project_id='"12345678-1234-1234-1234-123456789012"',
            tags=["example string"],
            body_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            await async_client.knowledge_bases.with_raw_response.update(
                path_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseDeleteResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.knowledge_bases.with_raw_response.delete(
                "",
            )
