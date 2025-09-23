# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets.floating_ips import (
    ActionListResponse,
    ActionCreateResponse,
    ActionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Gradient) -> None:
        action = client.gpu_droplets.floating_ips.actions.create(
            floating_ip="45.55.96.47",
            type="assign",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.actions.with_raw_response.create(
            floating_ip="45.55.96.47",
            type="assign",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.actions.with_streaming_response.create(
            floating_ip="45.55.96.47",
            type="assign",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            client.gpu_droplets.floating_ips.actions.with_raw_response.create(
                floating_ip="",
                type="assign",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.floating_ips.actions.create(
            floating_ip="45.55.96.47",
            droplet_id=758604968,
            type="assign",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.actions.with_raw_response.create(
            floating_ip="45.55.96.47",
            droplet_id=758604968,
            type="assign",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.actions.with_streaming_response.create(
            floating_ip="45.55.96.47",
            droplet_id=758604968,
            type="assign",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            client.gpu_droplets.floating_ips.actions.with_raw_response.create(
                floating_ip="",
                droplet_id=758604968,
                type="assign",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        action = client.gpu_droplets.floating_ips.actions.retrieve(
            action_id=36804636,
            floating_ip="45.55.96.47",
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.actions.with_raw_response.retrieve(
            action_id=36804636,
            floating_ip="45.55.96.47",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.actions.with_streaming_response.retrieve(
            action_id=36804636,
            floating_ip="45.55.96.47",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            client.gpu_droplets.floating_ips.actions.with_raw_response.retrieve(
                action_id=36804636,
                floating_ip="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        action = client.gpu_droplets.floating_ips.actions.list(
            "45.55.96.47",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.floating_ips.actions.with_raw_response.list(
            "45.55.96.47",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.floating_ips.actions.with_streaming_response.list(
            "45.55.96.47",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            client.gpu_droplets.floating_ips.actions.with_raw_response.list(
                "",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.floating_ips.actions.create(
            floating_ip="45.55.96.47",
            type="assign",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.actions.with_raw_response.create(
            floating_ip="45.55.96.47",
            type="assign",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.actions.with_streaming_response.create(
            floating_ip="45.55.96.47",
            type="assign",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            await async_client.gpu_droplets.floating_ips.actions.with_raw_response.create(
                floating_ip="",
                type="assign",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.floating_ips.actions.create(
            floating_ip="45.55.96.47",
            droplet_id=758604968,
            type="assign",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.actions.with_raw_response.create(
            floating_ip="45.55.96.47",
            droplet_id=758604968,
            type="assign",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.actions.with_streaming_response.create(
            floating_ip="45.55.96.47",
            droplet_id=758604968,
            type="assign",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            await async_client.gpu_droplets.floating_ips.actions.with_raw_response.create(
                floating_ip="",
                droplet_id=758604968,
                type="assign",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.floating_ips.actions.retrieve(
            action_id=36804636,
            floating_ip="45.55.96.47",
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.actions.with_raw_response.retrieve(
            action_id=36804636,
            floating_ip="45.55.96.47",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.actions.with_streaming_response.retrieve(
            action_id=36804636,
            floating_ip="45.55.96.47",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            await async_client.gpu_droplets.floating_ips.actions.with_raw_response.retrieve(
                action_id=36804636,
                floating_ip="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.floating_ips.actions.list(
            "45.55.96.47",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.floating_ips.actions.with_raw_response.list(
            "45.55.96.47",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.floating_ips.actions.with_streaming_response.list(
            "45.55.96.47",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `floating_ip` but received ''"):
            await async_client.gpu_droplets.floating_ips.actions.with_raw_response.list(
                "",
            )
