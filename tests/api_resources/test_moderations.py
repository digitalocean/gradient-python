# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from serverless_inference_sdk_prod import ServerlessInferenceSDKProd, AsyncServerlessInferenceSDKProd
from serverless_inference_sdk_prod.types import ModerationClassifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify(self, client: ServerlessInferenceSDKProd) -> None:
        moderation = client.moderations.classify(
            input="I want to kill them.",
        )
        assert_matches_type(ModerationClassifyResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        moderation = client.moderations.classify(
            input="I want to kill them.",
            model="omni-moderation-2024-09-26",
        )
        assert_matches_type(ModerationClassifyResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.moderations.with_raw_response.classify(
            input="I want to kill them.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = response.parse()
        assert_matches_type(ModerationClassifyResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify(self, client: ServerlessInferenceSDKProd) -> None:
        with client.moderations.with_streaming_response.classify(
            input="I want to kill them.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = response.parse()
            assert_matches_type(ModerationClassifyResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        moderation = await async_client.moderations.classify(
            input="I want to kill them.",
        )
        assert_matches_type(ModerationClassifyResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        moderation = await async_client.moderations.classify(
            input="I want to kill them.",
            model="omni-moderation-2024-09-26",
        )
        assert_matches_type(ModerationClassifyResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.moderations.with_raw_response.classify(
            input="I want to kill them.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = await response.parse()
        assert_matches_type(ModerationClassifyResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.moderations.with_streaming_response.classify(
            input="I want to kill them.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = await response.parse()
            assert_matches_type(ModerationClassifyResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True
