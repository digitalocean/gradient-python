# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents import (
    EvaluationDatasetCreateResponse,
    EvaluationDatasetCreateFileUploadPresignedURLsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        evaluation_dataset = client.agents.evaluation_datasets.create()
        assert_matches_type(EvaluationDatasetCreateResponse, evaluation_dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        evaluation_dataset = client.agents.evaluation_datasets.create(
            file_upload_dataset={
                "original_file_name": "example name",
                "size_in_bytes": "12345",
                "stored_object_key": "example string",
            },
            name="example name",
        )
        assert_matches_type(EvaluationDatasetCreateResponse, evaluation_dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.agents.evaluation_datasets.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetCreateResponse, evaluation_dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.agents.evaluation_datasets.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetCreateResponse, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_file_upload_presigned_urls(self, client: Gradient) -> None:
        evaluation_dataset = client.agents.evaluation_datasets.create_file_upload_presigned_urls()
        assert_matches_type(
            EvaluationDatasetCreateFileUploadPresignedURLsResponse, evaluation_dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_file_upload_presigned_urls_with_all_params(self, client: Gradient) -> None:
        evaluation_dataset = client.agents.evaluation_datasets.create_file_upload_presigned_urls(
            files=[
                {
                    "file_name": "example name",
                    "file_size": "file_size",
                }
            ],
        )
        assert_matches_type(
            EvaluationDatasetCreateFileUploadPresignedURLsResponse, evaluation_dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_file_upload_presigned_urls(self, client: Gradient) -> None:
        response = client.agents.evaluation_datasets.with_raw_response.create_file_upload_presigned_urls()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(
            EvaluationDatasetCreateFileUploadPresignedURLsResponse, evaluation_dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_file_upload_presigned_urls(self, client: Gradient) -> None:
        with client.agents.evaluation_datasets.with_streaming_response.create_file_upload_presigned_urls() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(
                EvaluationDatasetCreateFileUploadPresignedURLsResponse, evaluation_dataset, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluationDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        evaluation_dataset = await async_client.agents.evaluation_datasets.create()
        assert_matches_type(EvaluationDatasetCreateResponse, evaluation_dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_dataset = await async_client.agents.evaluation_datasets.create(
            file_upload_dataset={
                "original_file_name": "example name",
                "size_in_bytes": "12345",
                "stored_object_key": "example string",
            },
            name="example name",
        )
        assert_matches_type(EvaluationDatasetCreateResponse, evaluation_dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_datasets.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetCreateResponse, evaluation_dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_datasets.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetCreateResponse, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_file_upload_presigned_urls(self, async_client: AsyncGradient) -> None:
        evaluation_dataset = await async_client.agents.evaluation_datasets.create_file_upload_presigned_urls()
        assert_matches_type(
            EvaluationDatasetCreateFileUploadPresignedURLsResponse, evaluation_dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_file_upload_presigned_urls_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_dataset = await async_client.agents.evaluation_datasets.create_file_upload_presigned_urls(
            files=[
                {
                    "file_name": "example name",
                    "file_size": "file_size",
                }
            ],
        )
        assert_matches_type(
            EvaluationDatasetCreateFileUploadPresignedURLsResponse, evaluation_dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_file_upload_presigned_urls(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_datasets.with_raw_response.create_file_upload_presigned_urls()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(
            EvaluationDatasetCreateFileUploadPresignedURLsResponse, evaluation_dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_file_upload_presigned_urls(self, async_client: AsyncGradient) -> None:
        async with (
            async_client.agents.evaluation_datasets.with_streaming_response.create_file_upload_presigned_urls()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(
                EvaluationDatasetCreateFileUploadPresignedURLsResponse, evaluation_dataset, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
