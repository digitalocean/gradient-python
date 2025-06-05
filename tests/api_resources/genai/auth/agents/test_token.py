# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.genai.auth.agents import TokenCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DigitaloceanGenaiSDK) -> None:
        token = client.genai.auth.agents.token.create(
            path_agent_uuid="agent_uuid",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        token = client.genai.auth.agents.token.create(
            path_agent_uuid="agent_uuid",
            body_agent_uuid="agent_uuid",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.auth.agents.token.with_raw_response.create(
            path_agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.auth.agents.token.with_streaming_response.create(
            path_agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            client.genai.auth.agents.token.with_raw_response.create(
                path_agent_uuid="",
            )


class TestAsyncToken:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        token = await async_client.genai.auth.agents.token.create(
            path_agent_uuid="agent_uuid",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        token = await async_client.genai.auth.agents.token.create(
            path_agent_uuid="agent_uuid",
            body_agent_uuid="agent_uuid",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.auth.agents.token.with_raw_response.create(
            path_agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.auth.agents.token.with_streaming_response.create(
            path_agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            await async_client.genai.auth.agents.token.with_raw_response.create(
                path_agent_uuid="",
            )
