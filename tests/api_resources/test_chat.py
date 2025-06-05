# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types import ChatCreateCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_completion(self, client: DigitaloceanGenaiSDK) -> None:
        chat = client.chat.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="llama3-8b-instruct",
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_completion_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        chat = client.chat.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="llama3-8b-instruct",
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=256,
            max_tokens=0,
            metadata={"foo": "string"},
            n=1,
            presence_penalty=-2,
            stop="\n",
            stream=True,
            stream_options={"include_usage": True},
            temperature=1,
            top_logprobs=0,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_completion(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.chat.with_raw_response.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="llama3-8b-instruct",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_completion(self, client: DigitaloceanGenaiSDK) -> None:
        with client.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="llama3-8b-instruct",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        chat = await async_client.chat.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="llama3-8b-instruct",
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        chat = await async_client.chat.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="llama3-8b-instruct",
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=256,
            max_tokens=0,
            metadata={"foo": "string"},
            n=1,
            presence_penalty=-2,
            stop="\n",
            stream=True,
            stream_options={"include_usage": True},
            temperature=1,
            top_logprobs=0,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.chat.with_raw_response.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="llama3-8b-instruct",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="llama3-8b-instruct",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
