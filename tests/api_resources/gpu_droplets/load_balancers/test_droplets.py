# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDroplets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Gradient) -> None:
        droplet = client.gpu_droplets.load_balancers.droplets.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        )
        assert droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.droplets.with_raw_response.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        droplet = response.parse()
        assert droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.droplets.with_streaming_response.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            droplet = response.parse()
            assert droplet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.droplets.with_raw_response.add(
                lb_id="",
                droplet_ids=[3164444, 3164445],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: Gradient) -> None:
        droplet = client.gpu_droplets.load_balancers.droplets.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        )
        assert droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.droplets.with_raw_response.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        droplet = response.parse()
        assert droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.droplets.with_streaming_response.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            droplet = response.parse()
            assert droplet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.droplets.with_raw_response.remove(
                lb_id="",
                droplet_ids=[3164444, 3164445],
            )


class TestAsyncDroplets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncGradient) -> None:
        droplet = await async_client.gpu_droplets.load_balancers.droplets.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        )
        assert droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.droplets.with_raw_response.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        droplet = await response.parse()
        assert droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.droplets.with_streaming_response.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            droplet = await response.parse()
            assert droplet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.droplets.with_raw_response.add(
                lb_id="",
                droplet_ids=[3164444, 3164445],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncGradient) -> None:
        droplet = await async_client.gpu_droplets.load_balancers.droplets.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        )
        assert droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.droplets.with_raw_response.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        droplet = await response.parse()
        assert droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.droplets.with_streaming_response.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            droplet_ids=[3164444, 3164445],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            droplet = await response.parse()
            assert droplet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.droplets.with_raw_response.remove(
                lb_id="",
                droplet_ids=[3164444, 3164445],
            )
