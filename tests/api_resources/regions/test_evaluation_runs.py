# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from do_gradientai import GradientAI, AsyncGradientAI
from do_gradientai.types.regions import (
    EvaluationRunCreateResponse,
    EvaluationRunRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: GradientAI) -> None:
        evaluation_run = client.regions.evaluation_runs.create()
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: GradientAI) -> None:
        evaluation_run = client.regions.evaluation_runs.create(
            agent_uuid="agent_uuid",
            run_name="run_name",
            test_case_uuid="test_case_uuid",
        )
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: GradientAI) -> None:
        response = client.regions.evaluation_runs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = response.parse()
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: GradientAI) -> None:
        with client.regions.evaluation_runs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = response.parse()
            assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: GradientAI) -> None:
        evaluation_run = client.regions.evaluation_runs.retrieve(
            "evaluation_run_uuid",
        )
        assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: GradientAI) -> None:
        response = client.regions.evaluation_runs.with_raw_response.retrieve(
            "evaluation_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = response.parse()
        assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: GradientAI) -> None:
        with client.regions.evaluation_runs.with_streaming_response.retrieve(
            "evaluation_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = response.parse()
            assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            client.regions.evaluation_runs.with_raw_response.retrieve(
                "",
            )


class TestAsyncEvaluationRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGradientAI) -> None:
        evaluation_run = await async_client.regions.evaluation_runs.create()
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradientAI) -> None:
        evaluation_run = await async_client.regions.evaluation_runs.create(
            agent_uuid="agent_uuid",
            run_name="run_name",
            test_case_uuid="test_case_uuid",
        )
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.regions.evaluation_runs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = await response.parse()
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradientAI) -> None:
        async with async_client.regions.evaluation_runs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = await response.parse()
            assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradientAI) -> None:
        evaluation_run = await async_client.regions.evaluation_runs.retrieve(
            "evaluation_run_uuid",
        )
        assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.regions.evaluation_runs.with_raw_response.retrieve(
            "evaluation_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = await response.parse()
        assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradientAI) -> None:
        async with async_client.regions.evaluation_runs.with_streaming_response.retrieve(
            "evaluation_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = await response.parse()
            assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            await async_client.regions.evaluation_runs.with_raw_response.retrieve(
                "",
            )
