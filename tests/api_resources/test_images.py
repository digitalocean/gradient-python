# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types import ImageGenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_overload_1(self, client: Gradient) -> None:
        image = client.images.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
        )
        assert_matches_type(ImageGenerateResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_with_all_params_overload_1(self, client: Gradient) -> None:
        image = client.images.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            background="auto",
            model="openai-gpt-image-1",
            moderation="auto",
            n=1,
            output_compression=100,
            output_format="png",
            partial_images=1,
            quality="auto",
            size="auto",
            stream=False,
            user="user-1234",
        )
        assert_matches_type(ImageGenerateResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_overload_1(self, client: Gradient) -> None:
        response = client.images.with_raw_response.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageGenerateResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_overload_1(self, client: Gradient) -> None:
        with client.images.with_streaming_response.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageGenerateResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_overload_2(self, client: Gradient) -> None:
        image_stream = client.images.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            stream=True,
        )
        image_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_with_all_params_overload_2(self, client: Gradient) -> None:
        image_stream = client.images.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            stream=True,
            background="auto",
            model="openai-gpt-image-1",
            moderation="auto",
            n=1,
            output_compression=100,
            output_format="png",
            partial_images=1,
            quality="auto",
            size="auto",
            user="user-1234",
        )
        image_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_overload_2(self, client: Gradient) -> None:
        response = client.images.with_raw_response.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_overload_2(self, client: Gradient) -> None:
        with client.images.with_streaming_response.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncImages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_overload_1(self, async_client: AsyncGradient) -> None:
        image = await async_client.images.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
        )
        assert_matches_type(ImageGenerateResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        image = await async_client.images.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            background="auto",
            model="openai-gpt-image-1",
            moderation="auto",
            n=1,
            output_compression=100,
            output_format="png",
            partial_images=1,
            quality="auto",
            size="auto",
            stream=False,
            user="user-1234",
        )
        assert_matches_type(ImageGenerateResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.images.with_raw_response.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageGenerateResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.images.with_streaming_response.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageGenerateResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_overload_2(self, async_client: AsyncGradient) -> None:
        image_stream = await async_client.images.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            stream=True,
        )
        await image_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        image_stream = await async_client.images.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            stream=True,
            background="auto",
            model="openai-gpt-image-1",
            moderation="auto",
            n=1,
            output_compression=100,
            output_format="png",
            partial_images=1,
            quality="auto",
            size="auto",
            user="user-1234",
        )
        await image_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.images.with_raw_response.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.images.with_streaming_response.generate(
            prompt="A cute baby sea otter floating on its back in calm blue water",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
