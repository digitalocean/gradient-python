# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents import (
    EvaluationRunCreateResponse,
    EvaluationRunRetrieveResponse,
    EvaluationRunListResultsResponse,
    EvaluationRunRetrieveResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        evaluation_run = client.agents.evaluation_runs.create()
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        evaluation_run = client.agents.evaluation_runs.create(
            agent_uuids=["example string"],
            run_name="Evaluation Run Name",
            test_case_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.agents.evaluation_runs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = response.parse()
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.agents.evaluation_runs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = response.parse()
            assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        evaluation_run = client.agents.evaluation_runs.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.agents.evaluation_runs.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = response.parse()
        assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.agents.evaluation_runs.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = response.parse()
            assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            client.agents.evaluation_runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_results(self, client: Gradient) -> None:
        evaluation_run = client.agents.evaluation_runs.list_results(
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationRunListResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_results_with_all_params(self, client: Gradient) -> None:
        evaluation_run = client.agents.evaluation_runs.list_results(
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            page=0,
            per_page=0,
        )
        assert_matches_type(EvaluationRunListResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_results(self, client: Gradient) -> None:
        response = client.agents.evaluation_runs.with_raw_response.list_results(
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = response.parse()
        assert_matches_type(EvaluationRunListResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_results(self, client: Gradient) -> None:
        with client.agents.evaluation_runs.with_streaming_response.list_results(
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = response.parse()
            assert_matches_type(EvaluationRunListResultsResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_results(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            client.agents.evaluation_runs.with_raw_response.list_results(
                evaluation_run_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_results(self, client: Gradient) -> None:
        evaluation_run = client.agents.evaluation_runs.retrieve_results(
            prompt_id=1,
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationRunRetrieveResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_results(self, client: Gradient) -> None:
        response = client.agents.evaluation_runs.with_raw_response.retrieve_results(
            prompt_id=1,
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = response.parse()
        assert_matches_type(EvaluationRunRetrieveResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_results(self, client: Gradient) -> None:
        with client.agents.evaluation_runs.with_streaming_response.retrieve_results(
            prompt_id=1,
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = response.parse()
            assert_matches_type(EvaluationRunRetrieveResultsResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_results(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            client.agents.evaluation_runs.with_raw_response.retrieve_results(
                prompt_id=1,
                evaluation_run_uuid="",
            )


class TestAsyncEvaluationRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        evaluation_run = await async_client.agents.evaluation_runs.create()
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_run = await async_client.agents.evaluation_runs.create(
            agent_uuids=["example string"],
            run_name="Evaluation Run Name",
            test_case_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_runs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = await response.parse()
        assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_runs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = await response.parse()
            assert_matches_type(EvaluationRunCreateResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        evaluation_run = await async_client.agents.evaluation_runs.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_runs.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = await response.parse()
        assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_runs.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = await response.parse()
            assert_matches_type(EvaluationRunRetrieveResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            await async_client.agents.evaluation_runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_results(self, async_client: AsyncGradient) -> None:
        evaluation_run = await async_client.agents.evaluation_runs.list_results(
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationRunListResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_results_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_run = await async_client.agents.evaluation_runs.list_results(
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            page=0,
            per_page=0,
        )
        assert_matches_type(EvaluationRunListResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_results(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_runs.with_raw_response.list_results(
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = await response.parse()
        assert_matches_type(EvaluationRunListResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_results(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_runs.with_streaming_response.list_results(
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = await response.parse()
            assert_matches_type(EvaluationRunListResultsResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_results(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            await async_client.agents.evaluation_runs.with_raw_response.list_results(
                evaluation_run_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_results(self, async_client: AsyncGradient) -> None:
        evaluation_run = await async_client.agents.evaluation_runs.retrieve_results(
            prompt_id=1,
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationRunRetrieveResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_results(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_runs.with_raw_response.retrieve_results(
            prompt_id=1,
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_run = await response.parse()
        assert_matches_type(EvaluationRunRetrieveResultsResponse, evaluation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_results(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_runs.with_streaming_response.retrieve_results(
            prompt_id=1,
            evaluation_run_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_run = await response.parse()
            assert_matches_type(EvaluationRunRetrieveResultsResponse, evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_results(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            await async_client.agents.evaluation_runs.with_raw_response.retrieve_results(
                prompt_id=1,
                evaluation_run_uuid="",
            )
