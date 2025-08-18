# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForwardingRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Gradient) -> None:
        forwarding_rule = client.gpu_droplets.load_balancers.forwarding_rules.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )
        assert forwarding_rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.forwarding_rules.with_raw_response.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forwarding_rule = response.parse()
        assert forwarding_rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.forwarding_rules.with_streaming_response.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forwarding_rule = response.parse()
            assert forwarding_rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.forwarding_rules.with_raw_response.add(
                lb_id="",
                forwarding_rules=[
                    {
                        "entry_port": 443,
                        "entry_protocol": "https",
                        "target_port": 80,
                        "target_protocol": "http",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: Gradient) -> None:
        forwarding_rule = client.gpu_droplets.load_balancers.forwarding_rules.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )
        assert forwarding_rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.forwarding_rules.with_raw_response.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forwarding_rule = response.parse()
        assert forwarding_rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.forwarding_rules.with_streaming_response.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forwarding_rule = response.parse()
            assert forwarding_rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.forwarding_rules.with_raw_response.remove(
                lb_id="",
                forwarding_rules=[
                    {
                        "entry_port": 443,
                        "entry_protocol": "https",
                        "target_port": 80,
                        "target_protocol": "http",
                    }
                ],
            )


class TestAsyncForwardingRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncGradient) -> None:
        forwarding_rule = await async_client.gpu_droplets.load_balancers.forwarding_rules.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )
        assert forwarding_rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.forwarding_rules.with_raw_response.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forwarding_rule = await response.parse()
        assert forwarding_rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.forwarding_rules.with_streaming_response.add(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forwarding_rule = await response.parse()
            assert forwarding_rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.forwarding_rules.with_raw_response.add(
                lb_id="",
                forwarding_rules=[
                    {
                        "entry_port": 443,
                        "entry_protocol": "https",
                        "target_port": 80,
                        "target_protocol": "http",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncGradient) -> None:
        forwarding_rule = await async_client.gpu_droplets.load_balancers.forwarding_rules.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )
        assert forwarding_rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.forwarding_rules.with_raw_response.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forwarding_rule = await response.parse()
        assert forwarding_rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.forwarding_rules.with_streaming_response.remove(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forwarding_rule = await response.parse()
            assert forwarding_rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.forwarding_rules.with_raw_response.remove(
                lb_id="",
                forwarding_rules=[
                    {
                        "entry_port": 443,
                        "entry_protocol": "https",
                        "target_port": 80,
                        "target_protocol": "http",
                    }
                ],
            )
