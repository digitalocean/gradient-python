# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.shared import CreateResponseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Gradient) -> None:
        response = client.responses.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
        )
        assert_matches_type(CreateResponseResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gradient) -> None:
        response = client.responses.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            instructions="You are a helpful assistant.",
            max_output_tokens=1024,
            max_tokens=1024,
            metadata={"foo": "string"},
            modalities=["text"],
            parallel_tool_calls=True,
            stop="\n",
            stream=False,
            stream_options={"include_usage": True},
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "description": "description",
                    "name": "name",
                    "parameters": {"foo": "bar"},
                }
            ],
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(CreateResponseResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Gradient) -> None:
        http_response = client.responses.with_raw_response.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(CreateResponseResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gradient) -> None:
        with client.responses.with_streaming_response.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(CreateResponseResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Gradient) -> None:
        response_stream = client.responses.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            stream=True,
        )
        response_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gradient) -> None:
        response_stream = client.responses.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            stream=True,
            instructions="You are a helpful assistant.",
            max_output_tokens=1024,
            max_tokens=1024,
            metadata={"foo": "string"},
            modalities=["text"],
            parallel_tool_calls=True,
            stop="\n",
            stream_options={"include_usage": True},
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "description": "description",
                    "name": "name",
                    "parameters": {"foo": "bar"},
                }
            ],
            top_p=1,
            user="user-1234",
        )
        response_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Gradient) -> None:
        response = client.responses.with_raw_response.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gradient) -> None:
        with client.responses.with_streaming_response.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.responses.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
        )
        assert_matches_type(CreateResponseResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.responses.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            instructions="You are a helpful assistant.",
            max_output_tokens=1024,
            max_tokens=1024,
            metadata={"foo": "string"},
            modalities=["text"],
            parallel_tool_calls=True,
            stop="\n",
            stream=False,
            stream_options={"include_usage": True},
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "description": "description",
                    "name": "name",
                    "parameters": {"foo": "bar"},
                }
            ],
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(CreateResponseResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        http_response = await async_client.responses.with_raw_response.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(CreateResponseResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(CreateResponseResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGradient) -> None:
        response_stream = await async_client.responses.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            stream=True,
        )
        await response_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        response_stream = await async_client.responses.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            stream=True,
            instructions="You are a helpful assistant.",
            max_output_tokens=1024,
            max_tokens=1024,
            metadata={"foo": "string"},
            modalities=["text"],
            parallel_tool_calls=True,
            stop="\n",
            stream_options={"include_usage": True},
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "description": "description",
                    "name": "name",
                    "parameters": {"foo": "bar"},
                }
            ],
            top_p=1,
            user="user-1234",
        )
        await response_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.responses.with_raw_response.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="Tell me a three-sentence bedtime story about a unicorn.",
            model="llama3-8b-instruct",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
