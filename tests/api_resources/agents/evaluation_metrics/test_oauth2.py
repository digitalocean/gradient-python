# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents.evaluation_metrics import Oauth2GenerateURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOauth2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_url(self, client: Gradient) -> None:
        oauth2 = client.agents.evaluation_metrics.oauth2.generate_url()
        assert_matches_type(Oauth2GenerateURLResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_url_with_all_params(self, client: Gradient) -> None:
        oauth2 = client.agents.evaluation_metrics.oauth2.generate_url(
            redirect_url="redirect_url",
            type="type",
        )
        assert_matches_type(Oauth2GenerateURLResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_url(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.oauth2.with_raw_response.generate_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = response.parse()
        assert_matches_type(Oauth2GenerateURLResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_url(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.oauth2.with_streaming_response.generate_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = response.parse()
            assert_matches_type(Oauth2GenerateURLResponse, oauth2, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOauth2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_url(self, async_client: AsyncGradient) -> None:
        oauth2 = await async_client.agents.evaluation_metrics.oauth2.generate_url()
        assert_matches_type(Oauth2GenerateURLResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_url_with_all_params(self, async_client: AsyncGradient) -> None:
        oauth2 = await async_client.agents.evaluation_metrics.oauth2.generate_url(
            redirect_url="redirect_url",
            type="type",
        )
        assert_matches_type(Oauth2GenerateURLResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_url(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.oauth2.with_raw_response.generate_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = await response.parse()
        assert_matches_type(Oauth2GenerateURLResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_url(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.oauth2.with_streaming_response.generate_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = await response.parse()
            assert_matches_type(Oauth2GenerateURLResponse, oauth2, path=["response"])

        assert cast(Any, response.is_closed) is True
