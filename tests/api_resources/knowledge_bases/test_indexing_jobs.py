# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
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
