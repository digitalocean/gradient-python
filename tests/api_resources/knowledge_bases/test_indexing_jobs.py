# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest

from gradient import Gradient, AsyncGradient, IndexingJobError, IndexingJobTimeoutError
from tests.utils import assert_matches_type
from gradient.types.knowledge_bases import (
    IndexingJobListResponse,
    IndexingJobCreateResponse,
    IndexingJobRetrieveResponse,
    IndexingJobUpdateCancelResponse,
    IndexingJobRetrieveSignedURLResponse,
    IndexingJobRetrieveDataSourcesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexingJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.create()
        assert_matches_type(IndexingJobCreateResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.create(
            data_source_uuids=["example string"],
            knowledge_base_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(IndexingJobCreateResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.knowledge_bases.indexing_jobs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = response.parse()
        assert_matches_type(IndexingJobCreateResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.knowledge_bases.indexing_jobs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = response.parse()
            assert_matches_type(IndexingJobCreateResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(IndexingJobRetrieveResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.knowledge_bases.indexing_jobs.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = response.parse()
        assert_matches_type(IndexingJobRetrieveResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.knowledge_bases.indexing_jobs.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = response.parse()
            assert_matches_type(IndexingJobRetrieveResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.knowledge_bases.indexing_jobs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.list()
        assert_matches_type(IndexingJobListResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(IndexingJobListResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.knowledge_bases.indexing_jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = response.parse()
        assert_matches_type(IndexingJobListResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.knowledge_bases.indexing_jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = response.parse()
            assert_matches_type(IndexingJobListResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_data_sources(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.retrieve_data_sources(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(IndexingJobRetrieveDataSourcesResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_data_sources(self, client: Gradient) -> None:
        response = client.knowledge_bases.indexing_jobs.with_raw_response.retrieve_data_sources(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = response.parse()
        assert_matches_type(IndexingJobRetrieveDataSourcesResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_data_sources(self, client: Gradient) -> None:
        with client.knowledge_bases.indexing_jobs.with_streaming_response.retrieve_data_sources(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = response.parse()
            assert_matches_type(IndexingJobRetrieveDataSourcesResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_data_sources(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `indexing_job_uuid` but received ''"):
            client.knowledge_bases.indexing_jobs.with_raw_response.retrieve_data_sources(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_signed_url(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.retrieve_signed_url(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(IndexingJobRetrieveSignedURLResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_signed_url(self, client: Gradient) -> None:
        response = client.knowledge_bases.indexing_jobs.with_raw_response.retrieve_signed_url(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = response.parse()
        assert_matches_type(IndexingJobRetrieveSignedURLResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_signed_url(self, client: Gradient) -> None:
        with client.knowledge_bases.indexing_jobs.with_streaming_response.retrieve_signed_url(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = response.parse()
            assert_matches_type(IndexingJobRetrieveSignedURLResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_signed_url(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `indexing_job_uuid` but received ''"):
            client.knowledge_bases.indexing_jobs.with_raw_response.retrieve_signed_url(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_cancel(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.update_cancel(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(IndexingJobUpdateCancelResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_cancel_with_all_params(self, client: Gradient) -> None:
        indexing_job = client.knowledge_bases.indexing_jobs.update_cancel(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(IndexingJobUpdateCancelResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_cancel(self, client: Gradient) -> None:
        response = client.knowledge_bases.indexing_jobs.with_raw_response.update_cancel(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = response.parse()
        assert_matches_type(IndexingJobUpdateCancelResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_cancel(self, client: Gradient) -> None:
        with client.knowledge_bases.indexing_jobs.with_streaming_response.update_cancel(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = response.parse()
            assert_matches_type(IndexingJobUpdateCancelResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_cancel(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            client.knowledge_bases.indexing_jobs.with_raw_response.update_cancel(
                path_uuid="",
            )

    @parametrize
    def test_wait_for_completion_raises_indexing_job_error_on_failed(self, client: Gradient, respx_mock: Any) -> None:
        """Test that IndexingJobError is raised when job phase is FAILED"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_FAILED",
                        "total_items_indexed": "10",
                        "total_items_failed": "5",
                    }
                },
            )
        )

        with pytest.raises(IndexingJobError) as exc_info:
            client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)

        assert exc_info.value.uuid == job_uuid
        assert exc_info.value.phase == "BATCH_JOB_PHASE_FAILED"
        assert "failed" in str(exc_info.value).lower()

    @parametrize
    def test_wait_for_completion_raises_indexing_job_error_on_error(self, client: Gradient, respx_mock: Any) -> None:
        """Test that IndexingJobError is raised when job phase is ERROR"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_ERROR",
                    }
                },
            )
        )

        with pytest.raises(IndexingJobError) as exc_info:
            client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)

        assert exc_info.value.uuid == job_uuid
        assert exc_info.value.phase == "BATCH_JOB_PHASE_ERROR"
        assert "error" in str(exc_info.value).lower()

    @parametrize
    def test_wait_for_completion_raises_indexing_job_error_on_cancelled(
        self, client: Gradient, respx_mock: Any
    ) -> None:
        """Test that IndexingJobError is raised when job phase is CANCELLED"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_CANCELLED",
                    }
                },
            )
        )

        with pytest.raises(IndexingJobError) as exc_info:
            client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)

        assert exc_info.value.uuid == job_uuid
        assert exc_info.value.phase == "BATCH_JOB_PHASE_CANCELLED"
        assert "cancelled" in str(exc_info.value).lower()

    @parametrize
    def test_wait_for_completion_raises_timeout_error(self, client: Gradient, respx_mock: Any) -> None:
        """Test that IndexingJobTimeoutError is raised on timeout"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_RUNNING",
                    }
                },
            )
        )

        with pytest.raises(IndexingJobTimeoutError) as exc_info:
            client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid, poll_interval=0.1, timeout=0.2)

        assert exc_info.value.uuid == job_uuid
        assert exc_info.value.phase == "BATCH_JOB_PHASE_RUNNING"
        assert exc_info.value.timeout == 0.2

    @parametrize
    def test_wait_for_completion_succeeds(self, client: Gradient, respx_mock: Any) -> None:
        """Test that wait_for_completion returns successfully when job succeeds"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_SUCCEEDED",
                        "total_items_indexed": "100",
                        "total_items_failed": "0",
                    }
                },
            )
        )

        result = client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)
        assert_matches_type(IndexingJobRetrieveResponse, result, path=["response"])
        assert result.job is not None
        assert result.job.phase == "BATCH_JOB_PHASE_SUCCEEDED"


class TestAsyncIndexingJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.create()
        assert_matches_type(IndexingJobCreateResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.create(
            data_source_uuids=["example string"],
            knowledge_base_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(IndexingJobCreateResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.indexing_jobs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = await response.parse()
        assert_matches_type(IndexingJobCreateResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.indexing_jobs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = await response.parse()
            assert_matches_type(IndexingJobCreateResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(IndexingJobRetrieveResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.indexing_jobs.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = await response.parse()
        assert_matches_type(IndexingJobRetrieveResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.indexing_jobs.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = await response.parse()
            assert_matches_type(IndexingJobRetrieveResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.knowledge_bases.indexing_jobs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.list()
        assert_matches_type(IndexingJobListResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(IndexingJobListResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.indexing_jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = await response.parse()
        assert_matches_type(IndexingJobListResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.indexing_jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = await response.parse()
            assert_matches_type(IndexingJobListResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_data_sources(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.retrieve_data_sources(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(IndexingJobRetrieveDataSourcesResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_data_sources(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.indexing_jobs.with_raw_response.retrieve_data_sources(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = await response.parse()
        assert_matches_type(IndexingJobRetrieveDataSourcesResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_data_sources(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.indexing_jobs.with_streaming_response.retrieve_data_sources(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = await response.parse()
            assert_matches_type(IndexingJobRetrieveDataSourcesResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_data_sources(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `indexing_job_uuid` but received ''"):
            await async_client.knowledge_bases.indexing_jobs.with_raw_response.retrieve_data_sources(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_signed_url(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.retrieve_signed_url(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(IndexingJobRetrieveSignedURLResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_signed_url(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.indexing_jobs.with_raw_response.retrieve_signed_url(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = await response.parse()
        assert_matches_type(IndexingJobRetrieveSignedURLResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_signed_url(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.indexing_jobs.with_streaming_response.retrieve_signed_url(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = await response.parse()
            assert_matches_type(IndexingJobRetrieveSignedURLResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_signed_url(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `indexing_job_uuid` but received ''"):
            await async_client.knowledge_bases.indexing_jobs.with_raw_response.retrieve_signed_url(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_cancel(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.update_cancel(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(IndexingJobUpdateCancelResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_cancel_with_all_params(self, async_client: AsyncGradient) -> None:
        indexing_job = await async_client.knowledge_bases.indexing_jobs.update_cancel(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(IndexingJobUpdateCancelResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_cancel(self, async_client: AsyncGradient) -> None:
        response = await async_client.knowledge_bases.indexing_jobs.with_raw_response.update_cancel(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indexing_job = await response.parse()
        assert_matches_type(IndexingJobUpdateCancelResponse, indexing_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_cancel(self, async_client: AsyncGradient) -> None:
        async with async_client.knowledge_bases.indexing_jobs.with_streaming_response.update_cancel(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indexing_job = await response.parse()
            assert_matches_type(IndexingJobUpdateCancelResponse, indexing_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_cancel(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            await async_client.knowledge_bases.indexing_jobs.with_raw_response.update_cancel(
                path_uuid="",
            )

    @parametrize
    async def test_wait_for_completion_raises_indexing_job_error_on_failed(
        self, async_client: AsyncGradient, respx_mock: Any
    ) -> None:
        """Test that IndexingJobError is raised when job phase is FAILED"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_FAILED",
                        "total_items_indexed": "10",
                        "total_items_failed": "5",
                    }
                },
            )
        )

        with pytest.raises(IndexingJobError) as exc_info:
            await async_client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)

        assert exc_info.value.uuid == job_uuid
        assert exc_info.value.phase == "BATCH_JOB_PHASE_FAILED"
        assert "failed" in str(exc_info.value).lower()

    @parametrize
    async def test_wait_for_completion_raises_indexing_job_error_on_error(
        self, async_client: AsyncGradient, respx_mock: Any
    ) -> None:
        """Test that IndexingJobError is raised when job phase is ERROR"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_ERROR",
                    }
                },
            )
        )

        with pytest.raises(IndexingJobError) as exc_info:
            await async_client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)

        assert exc_info.value.uuid == job_uuid
        assert exc_info.value.phase == "BATCH_JOB_PHASE_ERROR"
        assert "error" in str(exc_info.value).lower()

    @parametrize
    async def test_wait_for_completion_raises_indexing_job_error_on_cancelled(
        self, async_client: AsyncGradient, respx_mock: Any
    ) -> None:
        """Test that IndexingJobError is raised when job phase is CANCELLED"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_CANCELLED",
                    }
                },
            )
        )

        with pytest.raises(IndexingJobError) as exc_info:
            await async_client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)

        assert exc_info.value.uuid == job_uuid
        assert exc_info.value.phase == "BATCH_JOB_PHASE_CANCELLED"
        assert "cancelled" in str(exc_info.value).lower()

    @parametrize
    async def test_wait_for_completion_raises_timeout_error(self, async_client: AsyncGradient, respx_mock: Any) -> None:
        """Test that IndexingJobTimeoutError is raised on timeout"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_RUNNING",
                    }
                },
            )
        )

        with pytest.raises(IndexingJobTimeoutError) as exc_info:
            await async_client.knowledge_bases.indexing_jobs.wait_for_completion(
                job_uuid, poll_interval=0.1, timeout=0.2
            )

        assert exc_info.value.uuid == job_uuid
        assert exc_info.value.phase == "BATCH_JOB_PHASE_RUNNING"
        assert exc_info.value.timeout == 0.2

    @parametrize
    async def test_wait_for_completion_succeeds(self, async_client: AsyncGradient, respx_mock: Any) -> None:
        """Test that wait_for_completion returns successfully when job succeeds"""
        job_uuid = "test-job-uuid"
        respx_mock.get(f"{base_url}/v2/gen-ai/indexing_jobs/{job_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "job": {
                        "uuid": job_uuid,
                        "phase": "BATCH_JOB_PHASE_SUCCEEDED",
                        "total_items_indexed": "100",
                        "total_items_failed": "0",
                    }
                },
            )
        )

        result = await async_client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)
        assert_matches_type(IndexingJobRetrieveResponse, result, path=["response"])
        assert result.job is not None
        assert result.job.phase == "BATCH_JOB_PHASE_SUCCEEDED"
