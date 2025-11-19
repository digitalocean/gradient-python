# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types import (
    KnowledgeBaseListResponse,
    KnowledgeBaseCreateResponse,
    KnowledgeBaseDeleteResponse,
    KnowledgeBaseUpdateResponse,
    KnowledgeBaseRetrieveResponse,
    KnowledgeBaseListIndexingJobsResponse,
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
                    "google_drive_data_source": {
                        "folder_id": "123e4567-e89b-12d3-a456-426614174000",
                        "refresh_token": "example string",
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
                        "exclude_tags": ["example string"],
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

    @parametrize
    def test_method_wait_for_database_success(self, client: Gradient) -> None:
        """Test wait_for_database with successful database status transition."""
        from unittest.mock import Mock

        call_count = [0]

        def mock_retrieve(uuid: str, **kwargs: object) -> Mock:  # noqa: ARG001
            call_count[0] += 1
            response = Mock()
            # Simulate CREATING -> ONLINE transition
            response.database_status = "CREATING" if call_count[0] == 1 else "ONLINE"
            return response

        client.knowledge_bases.retrieve = mock_retrieve  # type: ignore[method-assign]

        result = client.knowledge_bases.wait_for_database(
            "test-uuid",
            timeout=10.0,
            poll_interval=0.1,
        )

        assert result.database_status == "ONLINE"
        assert call_count[0] == 2

    @parametrize
    def test_method_wait_for_database_failed_state(self, client: Gradient) -> None:
        """Test wait_for_database with failed database status."""
        from unittest.mock import Mock

        from gradient.resources.knowledge_bases import KnowledgeBaseDatabaseError

        def mock_retrieve(uuid: str, **kwargs: object) -> Mock:  # noqa: ARG001
            response = Mock()
            response.database_status = "UNHEALTHY"
            return response

        client.knowledge_bases.retrieve = mock_retrieve  # type: ignore[method-assign]

        with pytest.raises(KnowledgeBaseDatabaseError, match="UNHEALTHY"):
            client.knowledge_bases.wait_for_database(
                "test-uuid",
                timeout=10.0,
                poll_interval=0.1,
            )

    @parametrize
    def test_method_wait_for_database_timeout(self, client: Gradient) -> None:
        """Test wait_for_database with timeout."""
        from unittest.mock import Mock

        from gradient.resources.knowledge_bases import KnowledgeBaseTimeoutError

        def mock_retrieve(uuid: str, **kwargs: object) -> Mock:  # noqa: ARG001
            response = Mock()
            response.database_status = "CREATING"
            return response

        client.knowledge_bases.retrieve = mock_retrieve  # type: ignore[method-assign]

        with pytest.raises(KnowledgeBaseTimeoutError):
            client.knowledge_bases.wait_for_database(
                "test-uuid",
                timeout=0.3,
                poll_interval=0.1,
            )

    @parametrize
    def test_method_wait_for_database_decommissioned(self, client: Gradient) -> None:
        """Test wait_for_database with DECOMMISSIONED status."""
        from unittest.mock import Mock

        from gradient.resources.knowledge_bases import KnowledgeBaseDatabaseError

        def mock_retrieve(uuid: str, **kwargs: object) -> Mock:  # noqa: ARG001
            response = Mock()
            response.database_status = "DECOMMISSIONED"
            return response

        client.knowledge_bases.retrieve = mock_retrieve  # type: ignore[method-assign]

        with pytest.raises(KnowledgeBaseDatabaseError, match="DECOMMISSIONED"):
            client.knowledge_bases.wait_for_database(
                "test-uuid",
                timeout=10.0,
                poll_interval=0.1,
            )

    @parametrize
    def test_path_params_wait_for_database(self, client: Gradient) -> None:
        """Test wait_for_database validates uuid parameter."""
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.knowledge_bases.wait_for_database(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_indexing_jobs(self, client: Gradient) -> None:
        knowledge_base = client.knowledge_bases.list_indexing_jobs(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KnowledgeBaseListIndexingJobsResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_indexing_jobs(self, client: Gradient) -> None:
        response = client.knowledge_bases.with_raw_response.list_indexing_jobs(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseListIndexingJobsResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_indexing_jobs(self, client: Gradient) -> None:
        with client.knowledge_bases.with_streaming_response.list_indexing_jobs(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseListIndexingJobsResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_indexing_jobs(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            client.knowledge_bases.with_raw_response.list_indexing_jobs(
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
                    "google_drive_data_source": {
                        "folder_id": "123e4567-e89b-12d3-a456-426614174000",
                        "refresh_token": "example string",
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
                        "exclude_tags": ["example string"],
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

    @parametrize
    async def test_method_wait_for_database_success(self, async_client: AsyncGradient) -> None:
        """Test async wait_for_database with successful database status transition."""
        from unittest.mock import Mock

        call_count = [0]

        async def mock_retrieve(uuid: str, **kwargs: object) -> Mock:  # noqa: ARG001
            call_count[0] += 1
            response = Mock()
            # Simulate CREATING -> ONLINE transition
            response.database_status = "CREATING" if call_count[0] == 1 else "ONLINE"
            return response

        async_client.knowledge_bases.retrieve = mock_retrieve  # type: ignore[method-assign]

        result = await async_client.knowledge_bases.wait_for_database(
            "test-uuid",
            timeout=10.0,
            poll_interval=0.1,
        )

        assert result.database_status == "ONLINE"
        assert call_count[0] == 2

    @parametrize
    async def test_method_wait_for_database_failed_state(self, async_client: AsyncGradient) -> None:
        """Test async wait_for_database with failed database status."""
        from unittest.mock import Mock

        from gradient.resources.knowledge_bases import KnowledgeBaseDatabaseError

        async def mock_retrieve(uuid: str, **kwargs: object) -> Mock:  # noqa: ARG001
            response = Mock()
            response.database_status = "UNHEALTHY"
            return response

        async_client.knowledge_bases.retrieve = mock_retrieve  # type: ignore[method-assign]

        with pytest.raises(KnowledgeBaseDatabaseError, match="UNHEALTHY"):
            await async_client.knowledge_bases.wait_for_database(
                "test-uuid",
                timeout=10.0,
                poll_interval=0.1,
            )

    @parametrize
    async def test_method_wait_for_database_timeout(self, async_client: AsyncGradient) -> None:
        """Test async wait_for_database with timeout."""
        from unittest.mock import Mock

        from gradient.resources.knowledge_bases import KnowledgeBaseTimeoutError

        async def mock_retrieve(uuid: str, **kwargs: object) -> Mock:  # noqa: ARG001
            response = Mock()
            response.database_status = "CREATING"
            return response

        async_client.knowledge_bases.retrieve = mock_retrieve  # type: ignore[method-assign]

        with pytest.raises(KnowledgeBaseTimeoutError):
            await async_client.knowledge_bases.wait_for_database(
                "test-uuid",
                timeout=0.3,
                poll_interval=0.1,
            )

    @parametrize
    async def test_method_wait_for_database_decommissioned(self, async_client: AsyncGradient) -> None:
        """Test async wait_for_database with DECOMMISSIONED status."""
        from unittest.mock import Mock

        from gradient.resources.knowledge_bases import KnowledgeBaseDatabaseError

        async def mock_retrieve(uuid: str, **kwargs: object) -> Mock:  # noqa: ARG001
            response = Mock()
            response.database_status = "DECOMMISSIONED"
            return response

        async_client.knowledge_bases.retrieve = mock_retrieve  # type: ignore[method-assign]

        with pytest.raises(KnowledgeBaseDatabaseError, match="DECOMMISSIONED"):
            await async_client.knowledge_bases.wait_for_database(
                "test-uuid",
                timeout=10.0,
                poll_interval=0.1,
            )

    @parametrize
    async def test_path_params_wait_for_database(self, async_client: AsyncGradient) -> None:
        """Test async wait_for_database validates uuid parameter."""
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.knowledge_bases.wait_for_database(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_indexing_jobs(self, async_client: AsyncGradient) -> None:
        knowledge_base = await async_client.knowledge_bases.list_indexing_jobs(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KnowledgeBaseListIndexingJobsResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_indexing_jobs(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.list_indexing_jobs(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseListIndexingJobsResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_indexing_jobs(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.list_indexing_jobs(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseListIndexingJobsResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_indexing_jobs(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            await async_client.knowledge_bases.with_raw_response.list_indexing_jobs(
                "",
            )
