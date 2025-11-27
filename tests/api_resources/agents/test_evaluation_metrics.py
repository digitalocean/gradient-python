# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents import (
    EvaluationMetricListResponse,
    EvaluationMetricListRegionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        evaluation_metric = client.agents.evaluation_metrics.list()
        assert_matches_type(EvaluationMetricListResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_metric = response.parse()
        assert_matches_type(EvaluationMetricListResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_metric = response.parse()
            assert_matches_type(EvaluationMetricListResponse, evaluation_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_regions(self, client: Gradient) -> None:
        evaluation_metric = client.agents.evaluation_metrics.list_regions()
        assert_matches_type(EvaluationMetricListRegionsResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_regions_with_all_params(self, client: Gradient) -> None:
        evaluation_metric = client.agents.evaluation_metrics.list_regions(
            serves_batch=True,
            serves_inference=True,
        )
        assert_matches_type(EvaluationMetricListRegionsResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_regions(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.with_raw_response.list_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_metric = response.parse()
        assert_matches_type(EvaluationMetricListRegionsResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_regions(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.with_streaming_response.list_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_metric = response.parse()
            assert_matches_type(EvaluationMetricListRegionsResponse, evaluation_metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluationMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        evaluation_metric = await async_client.agents.evaluation_metrics.list()
        assert_matches_type(EvaluationMetricListResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_metric = await response.parse()
        assert_matches_type(EvaluationMetricListResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_metric = await response.parse()
            assert_matches_type(EvaluationMetricListResponse, evaluation_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_regions(self, async_client: AsyncGradient) -> None:
        evaluation_metric = await async_client.agents.evaluation_metrics.list_regions()
        assert_matches_type(EvaluationMetricListRegionsResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_regions_with_all_params(self, async_client: AsyncGradient) -> None:
        evaluation_metric = await async_client.agents.evaluation_metrics.list_regions(
            serves_batch=True,
            serves_inference=True,
        )
        assert_matches_type(EvaluationMetricListRegionsResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_regions(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.with_raw_response.list_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_metric = await response.parse()
        assert_matches_type(EvaluationMetricListRegionsResponse, evaluation_metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_regions(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.with_streaming_response.list_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_metric = await response.parse()
            assert_matches_type(EvaluationMetricListRegionsResponse, evaluation_metric, path=["response"])

        assert cast(Any, response.is_closed) is True
