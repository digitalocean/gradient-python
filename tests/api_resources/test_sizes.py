# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradientai import GradientAI, AsyncGradientAI
from tests.utils import assert_matches_type
from gradientai.types import SizeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSizes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: GradientAI) -> None:
        size = client.sizes.list()
        assert_matches_type(SizeListResponse, size, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: GradientAI) -> None:
        size = client.sizes.list(
            page=1,
            per_page=1,
        )
        assert_matches_type(SizeListResponse, size, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: GradientAI) -> None:
        response = client.sizes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        size = response.parse()
        assert_matches_type(SizeListResponse, size, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: GradientAI) -> None:
        with client.sizes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            size = response.parse()
            assert_matches_type(SizeListResponse, size, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSizes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGradientAI) -> None:
        size = await async_client.sizes.list()
        assert_matches_type(SizeListResponse, size, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradientAI) -> None:
        size = await async_client.sizes.list(
            page=1,
            per_page=1,
        )
        assert_matches_type(SizeListResponse, size, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.sizes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        size = await response.parse()
        assert_matches_type(SizeListResponse, size, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradientAI) -> None:
        async with async_client.sizes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            size = await response.parse()
            assert_matches_type(SizeListResponse, size, path=["response"])

        assert cast(Any, response.is_closed) is True
