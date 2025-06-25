# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradientai import GradientAI, AsyncGradientAI
from tests.utils import assert_matches_type
from gradientai.types.regions.evaluation_runs import ResultRetrieveResponse, ResultRetrievePromptResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: GradientAI) -> None:
        result = client.regions.evaluation_runs.results.retrieve(
            "evaluation_run_uuid",
        )
        assert_matches_type(ResultRetrieveResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: GradientAI) -> None:
        response = client.regions.evaluation_runs.results.with_raw_response.retrieve(
            "evaluation_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ResultRetrieveResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: GradientAI) -> None:
        with client.regions.evaluation_runs.results.with_streaming_response.retrieve(
            "evaluation_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ResultRetrieveResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            client.regions.evaluation_runs.results.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_prompt(self, client: GradientAI) -> None:
        result = client.regions.evaluation_runs.results.retrieve_prompt(
            prompt_id=0,
            evaluation_run_uuid="evaluation_run_uuid",
        )
        assert_matches_type(ResultRetrievePromptResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_prompt(self, client: GradientAI) -> None:
        response = client.regions.evaluation_runs.results.with_raw_response.retrieve_prompt(
            prompt_id=0,
            evaluation_run_uuid="evaluation_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ResultRetrievePromptResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_prompt(self, client: GradientAI) -> None:
        with client.regions.evaluation_runs.results.with_streaming_response.retrieve_prompt(
            prompt_id=0,
            evaluation_run_uuid="evaluation_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ResultRetrievePromptResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_prompt(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            client.regions.evaluation_runs.results.with_raw_response.retrieve_prompt(
                prompt_id=0,
                evaluation_run_uuid="",
            )


class TestAsyncResults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradientAI) -> None:
        result = await async_client.regions.evaluation_runs.results.retrieve(
            "evaluation_run_uuid",
        )
        assert_matches_type(ResultRetrieveResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.regions.evaluation_runs.results.with_raw_response.retrieve(
            "evaluation_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ResultRetrieveResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradientAI) -> None:
        async with async_client.regions.evaluation_runs.results.with_streaming_response.retrieve(
            "evaluation_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ResultRetrieveResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            await async_client.regions.evaluation_runs.results.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_prompt(self, async_client: AsyncGradientAI) -> None:
        result = await async_client.regions.evaluation_runs.results.retrieve_prompt(
            prompt_id=0,
            evaluation_run_uuid="evaluation_run_uuid",
        )
        assert_matches_type(ResultRetrievePromptResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_prompt(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.regions.evaluation_runs.results.with_raw_response.retrieve_prompt(
            prompt_id=0,
            evaluation_run_uuid="evaluation_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ResultRetrievePromptResponse, result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_prompt(self, async_client: AsyncGradientAI) -> None:
        async with async_client.regions.evaluation_runs.results.with_streaming_response.retrieve_prompt(
            prompt_id=0,
            evaluation_run_uuid="evaluation_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ResultRetrievePromptResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_prompt(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_uuid` but received ''"):
            await async_client.regions.evaluation_runs.results.with_raw_response.retrieve_prompt(
                prompt_id=0,
                evaluation_run_uuid="",
            )
