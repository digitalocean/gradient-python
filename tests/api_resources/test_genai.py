# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types import GenaiRetrieveRegionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenai:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_regions(self, client: DigitaloceanGenaiSDK) -> None:
        genai = client.genai.retrieve_regions()
        assert_matches_type(GenaiRetrieveRegionsResponse, genai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_regions_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        genai = client.genai.retrieve_regions(
            serves_batch=True,
            serves_inference=True,
        )
        assert_matches_type(GenaiRetrieveRegionsResponse, genai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_regions(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.with_raw_response.retrieve_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        genai = response.parse()
        assert_matches_type(GenaiRetrieveRegionsResponse, genai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_regions(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.with_streaming_response.retrieve_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            genai = response.parse()
            assert_matches_type(GenaiRetrieveRegionsResponse, genai, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenai:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_regions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        genai = await async_client.genai.retrieve_regions()
        assert_matches_type(GenaiRetrieveRegionsResponse, genai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_regions_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        genai = await async_client.genai.retrieve_regions(
            serves_batch=True,
            serves_inference=True,
        )
        assert_matches_type(GenaiRetrieveRegionsResponse, genai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_regions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.with_raw_response.retrieve_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        genai = await response.parse()
        assert_matches_type(GenaiRetrieveRegionsResponse, genai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_regions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.with_streaming_response.retrieve_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            genai = await response.parse()
            assert_matches_type(GenaiRetrieveRegionsResponse, genai, path=["response"])

        assert cast(Any, response.is_closed) is True
