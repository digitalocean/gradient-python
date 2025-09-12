# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents.evaluation_metrics.oauth2 import DropboxCreateTokensResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDropbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_tokens(self, client: Gradient) -> None:
        dropbox = client.agents.evaluation_metrics.oauth2.dropbox.create_tokens()
        assert_matches_type(DropboxCreateTokensResponse, dropbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_tokens_with_all_params(self, client: Gradient) -> None:
        dropbox = client.agents.evaluation_metrics.oauth2.dropbox.create_tokens(
            code="example string",
            redirect_url="example string",
        )
        assert_matches_type(DropboxCreateTokensResponse, dropbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_tokens(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.oauth2.dropbox.with_raw_response.create_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropbox = response.parse()
        assert_matches_type(DropboxCreateTokensResponse, dropbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_tokens(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.oauth2.dropbox.with_streaming_response.create_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropbox = response.parse()
            assert_matches_type(DropboxCreateTokensResponse, dropbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDropbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_tokens(self, async_client: AsyncGradient) -> None:
        dropbox = await async_client.agents.evaluation_metrics.oauth2.dropbox.create_tokens()
        assert_matches_type(DropboxCreateTokensResponse, dropbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_tokens_with_all_params(self, async_client: AsyncGradient) -> None:
        dropbox = await async_client.agents.evaluation_metrics.oauth2.dropbox.create_tokens(
            code="example string",
            redirect_url="example string",
        )
        assert_matches_type(DropboxCreateTokensResponse, dropbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_tokens(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.oauth2.dropbox.with_raw_response.create_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropbox = await response.parse()
        assert_matches_type(DropboxCreateTokensResponse, dropbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_tokens(self, async_client: AsyncGradient) -> None:
        async with (
            async_client.agents.evaluation_metrics.oauth2.dropbox.with_streaming_response.create_tokens()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropbox = await response.parse()
            assert_matches_type(DropboxCreateTokensResponse, dropbox, path=["response"])

        assert cast(Any, response.is_closed) is True
