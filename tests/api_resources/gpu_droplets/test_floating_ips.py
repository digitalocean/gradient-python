# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets import (
    FloatingIPListResponse,
    FloatingIPCreateResponse,
    FloatingIPRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFloatingIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Gradient) -> None:
        floating_ip = client.gpu_droplets.floating_ips.create(
            droplet_id=2457247,
        )
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.with_raw_response.create(
            droplet_id=2457247,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.with_streaming_response.create(
            droplet_id=2457247,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Gradient) -> None:
        floating_ip = client.gpu_droplets.floating_ips.create(
            region="nyc3",
        )
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gradient) -> None:
        floating_ip = client.gpu_droplets.floating_ips.create(
            region="nyc3",
            project_id="746c6152-2fa2-11ed-92d3-27aaa54e4988",
        )
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.with_raw_response.create(
            region="nyc3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.with_streaming_response.create(
            region="nyc3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        floating_ip = client.gpu_droplets.floating_ips.retrieve(
            "45.55.96.47",
        )
        assert_matches_type(FloatingIPRetrieveResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.with_raw_response.retrieve(
            "45.55.96.47",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(FloatingIPRetrieveResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.with_streaming_response.retrieve(
            "45.55.96.47",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(FloatingIPRetrieveResponse, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            client.gpu_droplets.floating_ips.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        floating_ip = client.gpu_droplets.floating_ips.list()
        assert_matches_type(FloatingIPListResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        floating_ip = client.gpu_droplets.floating_ips.list(
            page=1,
            per_page=1,
        )
        assert_matches_type(FloatingIPListResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert_matches_type(FloatingIPListResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert_matches_type(FloatingIPListResponse, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        floating_ip = client.gpu_droplets.floating_ips.delete(
            "45.55.96.47",
        )
        assert floating_ip is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.with_raw_response.delete(
            "45.55.96.47",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = response.parse()
        assert floating_ip is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.with_streaming_response.delete(
            "45.55.96.47",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = response.parse()
            assert floating_ip is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            client.gpu_droplets.floating_ips.with_raw_response.delete(
                "",
            )


class TestAsyncFloatingIPs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGradient) -> None:
        floating_ip = await async_client.gpu_droplets.floating_ips.create(
            droplet_id=2457247,
        )
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.with_raw_response.create(
            droplet_id=2457247,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.with_streaming_response.create(
            droplet_id=2457247,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGradient) -> None:
        floating_ip = await async_client.gpu_droplets.floating_ips.create(
            region="nyc3",
        )
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        floating_ip = await async_client.gpu_droplets.floating_ips.create(
            region="nyc3",
            project_id="746c6152-2fa2-11ed-92d3-27aaa54e4988",
        )
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.with_raw_response.create(
            region="nyc3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.with_streaming_response.create(
            region="nyc3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(FloatingIPCreateResponse, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        floating_ip = await async_client.gpu_droplets.floating_ips.retrieve(
            "45.55.96.47",
        )
        assert_matches_type(FloatingIPRetrieveResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.with_raw_response.retrieve(
            "45.55.96.47",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(FloatingIPRetrieveResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.with_streaming_response.retrieve(
            "45.55.96.47",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(FloatingIPRetrieveResponse, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            await async_client.gpu_droplets.floating_ips.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        floating_ip = await async_client.gpu_droplets.floating_ips.list()
        assert_matches_type(FloatingIPListResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        floating_ip = await async_client.gpu_droplets.floating_ips.list(
            page=1,
            per_page=1,
        )
        assert_matches_type(FloatingIPListResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert_matches_type(FloatingIPListResponse, floating_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert_matches_type(FloatingIPListResponse, floating_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        floating_ip = await async_client.gpu_droplets.floating_ips.delete(
            "45.55.96.47",
        )
        assert floating_ip is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.with_raw_response.delete(
            "45.55.96.47",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        floating_ip = await response.parse()
        assert floating_ip is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.with_streaming_response.delete(
            "45.55.96.47",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            floating_ip = await response.parse()
            assert floating_ip is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            await async_client.gpu_droplets.floating_ips.with_raw_response.delete(
                "",
            )
