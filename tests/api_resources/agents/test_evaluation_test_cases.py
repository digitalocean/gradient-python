# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents import (
    EvaluationTestCaseListResponse,
    EvaluationTestCaseCreateResponse,
    EvaluationTestCaseUpdateResponse,
    EvaluationTestCaseRetrieveResponse,
    EvaluationTestCaseListEvaluationRunsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationTestCases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.create()
        assert_matches_type(EvaluationTestCaseCreateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.create(
            dataset_uuid="123e4567-e89b-12d3-a456-426614174000",
            description="example string",
            metrics=["example string"],
            name="example name",
            star_metric={
                "metric_uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "example name",
                "success_threshold": 123,
                "success_threshold_pct": 123,
            },
            workspace_uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(EvaluationTestCaseCreateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.agents.evaluation_test_cases.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = response.parse()
        assert_matches_type(EvaluationTestCaseCreateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.agents.evaluation_test_cases.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = response.parse()
            assert_matches_type(EvaluationTestCaseCreateResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.retrieve(
            test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationTestCaseRetrieveResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.retrieve(
            test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            evaluation_test_case_version=0,
        )
        assert_matches_type(EvaluationTestCaseRetrieveResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.agents.evaluation_test_cases.with_raw_response.retrieve(
            test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = response.parse()
        assert_matches_type(EvaluationTestCaseRetrieveResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.agents.evaluation_test_cases.with_streaming_response.retrieve(
            test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = response.parse()
            assert_matches_type(EvaluationTestCaseRetrieveResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_uuid` but received ''"):
            client.agents.evaluation_test_cases.with_raw_response.retrieve(
                test_case_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.update(
            path_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationTestCaseUpdateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.update(
            path_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            dataset_uuid="123e4567-e89b-12d3-a456-426614174000",
            description="example string",
            metrics={"metric_uuids": ["example string"]},
            name="example name",
            star_metric={
                "metric_uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "example name",
                "success_threshold": 123,
                "success_threshold_pct": 123,
            },
            body_test_case_uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(EvaluationTestCaseUpdateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.agents.evaluation_test_cases.with_raw_response.update(
            path_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = response.parse()
        assert_matches_type(EvaluationTestCaseUpdateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.agents.evaluation_test_cases.with_streaming_response.update(
            path_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = response.parse()
            assert_matches_type(EvaluationTestCaseUpdateResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_test_case_uuid` but received ''"):
            client.agents.evaluation_test_cases.with_raw_response.update(
                path_test_case_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.list()
        assert_matches_type(EvaluationTestCaseListResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.agents.evaluation_test_cases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = response.parse()
        assert_matches_type(EvaluationTestCaseListResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.agents.evaluation_test_cases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = response.parse()
            assert_matches_type(EvaluationTestCaseListResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_evaluation_runs(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.list_evaluation_runs(
            evaluation_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationTestCaseListEvaluationRunsResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_evaluation_runs_with_all_params(self, client: Gradient) -> None:
        evaluation_test_case = client.agents.evaluation_test_cases.list_evaluation_runs(
            evaluation_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            evaluation_test_case_version=0,
        )
        assert_matches_type(EvaluationTestCaseListEvaluationRunsResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_evaluation_runs(self, client: Gradient) -> None:
        response = client.agents.evaluation_test_cases.with_raw_response.list_evaluation_runs(
            evaluation_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = response.parse()
        assert_matches_type(EvaluationTestCaseListEvaluationRunsResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_evaluation_runs(self, client: Gradient) -> None:
        with client.agents.evaluation_test_cases.with_streaming_response.list_evaluation_runs(
            evaluation_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = response.parse()
            assert_matches_type(EvaluationTestCaseListEvaluationRunsResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_evaluation_runs(self, client: Gradient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `evaluation_test_case_uuid` but received ''"
        ):
            client.agents.evaluation_test_cases.with_raw_response.list_evaluation_runs(
                evaluation_test_case_uuid="",
            )


class TestAsyncEvaluationTestCases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.create()
        assert_matches_type(EvaluationTestCaseCreateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.create(
            dataset_uuid="123e4567-e89b-12d3-a456-426614174000",
            description="example string",
            metrics=["example string"],
            name="example name",
            star_metric={
                "metric_uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "example name",
                "success_threshold": 123,
                "success_threshold_pct": 123,
            },
            workspace_uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(EvaluationTestCaseCreateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_test_cases.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = await response.parse()
        assert_matches_type(EvaluationTestCaseCreateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_test_cases.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = await response.parse()
            assert_matches_type(EvaluationTestCaseCreateResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.retrieve(
            test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationTestCaseRetrieveResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.retrieve(
            test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            evaluation_test_case_version=0,
        )
        assert_matches_type(EvaluationTestCaseRetrieveResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_test_cases.with_raw_response.retrieve(
            test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = await response.parse()
        assert_matches_type(EvaluationTestCaseRetrieveResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_test_cases.with_streaming_response.retrieve(
            test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = await response.parse()
            assert_matches_type(EvaluationTestCaseRetrieveResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_uuid` but received ''"):
            await async_client.agents.evaluation_test_cases.with_raw_response.retrieve(
                test_case_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.update(
            path_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationTestCaseUpdateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.update(
            path_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            dataset_uuid="123e4567-e89b-12d3-a456-426614174000",
            description="example string",
            metrics={"metric_uuids": ["example string"]},
            name="example name",
            star_metric={
                "metric_uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "example name",
                "success_threshold": 123,
                "success_threshold_pct": 123,
            },
            body_test_case_uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(EvaluationTestCaseUpdateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_test_cases.with_raw_response.update(
            path_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = await response.parse()
        assert_matches_type(EvaluationTestCaseUpdateResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_test_cases.with_streaming_response.update(
            path_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = await response.parse()
            assert_matches_type(EvaluationTestCaseUpdateResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_test_case_uuid` but received ''"):
            await async_client.agents.evaluation_test_cases.with_raw_response.update(
                path_test_case_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.list()
        assert_matches_type(EvaluationTestCaseListResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_test_cases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = await response.parse()
        assert_matches_type(EvaluationTestCaseListResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_test_cases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = await response.parse()
            assert_matches_type(EvaluationTestCaseListResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_evaluation_runs(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.list_evaluation_runs(
            evaluation_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(EvaluationTestCaseListEvaluationRunsResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_evaluation_runs_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_test_case = await async_client.agents.evaluation_test_cases.list_evaluation_runs(
            evaluation_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            evaluation_test_case_version=0,
        )
        assert_matches_type(EvaluationTestCaseListEvaluationRunsResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_evaluation_runs(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_test_cases.with_raw_response.list_evaluation_runs(
            evaluation_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_test_case = await response.parse()
        assert_matches_type(EvaluationTestCaseListEvaluationRunsResponse, evaluation_test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_evaluation_runs(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_test_cases.with_streaming_response.list_evaluation_runs(
            evaluation_test_case_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_test_case = await response.parse()
            assert_matches_type(EvaluationTestCaseListEvaluationRunsResponse, evaluation_test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_evaluation_runs(self, async_client: AsyncGradient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `evaluation_test_case_uuid` but received ''"
        ):
            await async_client.agents.evaluation_test_cases.with_raw_response.list_evaluation_runs(
                evaluation_test_case_uuid="",
            )
