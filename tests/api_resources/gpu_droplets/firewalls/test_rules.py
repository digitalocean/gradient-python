# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Gradient) -> None:
        rule = client.gpu_droplets.firewalls.rules.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Gradient) -> None:
        rule = client.gpu_droplets.firewalls.rules.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            inbound_rules=[
                {
                    "ports": "3306",
                    "protocol": "tcp",
                    "sources": {
                        "addresses": ["1.2.3.4", "18.0.0.0/8"],
                        "droplet_ids": [49696269],
                        "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                        "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                        "tags": ["base-image", "prod"],
                    },
                }
            ],
            outbound_rules=[
                {
                    "destinations": {
                        "addresses": ["1.2.3.4", "18.0.0.0/8"],
                        "droplet_ids": [49696269],
                        "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                        "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                        "tags": ["base-image", "prod"],
                    },
                    "ports": "3306",
                    "protocol": "tcp",
                }
            ],
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.rules.with_raw_response.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.rules.with_streaming_response.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            client.gpu_droplets.firewalls.rules.with_raw_response.add(
                firewall_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: Gradient) -> None:
        rule = client.gpu_droplets.firewalls.rules.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_with_all_params(self, client: Gradient) -> None:
        rule = client.gpu_droplets.firewalls.rules.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            inbound_rules=[
                {
                    "ports": "3306",
                    "protocol": "tcp",
                    "sources": {
                        "addresses": ["1.2.3.4", "18.0.0.0/8"],
                        "droplet_ids": [49696269],
                        "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                        "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                        "tags": ["base-image", "prod"],
                    },
                }
            ],
            outbound_rules=[
                {
                    "destinations": {
                        "addresses": ["1.2.3.4", "18.0.0.0/8"],
                        "droplet_ids": [49696269],
                        "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                        "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                        "tags": ["base-image", "prod"],
                    },
                    "ports": "3306",
                    "protocol": "tcp",
                }
            ],
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.rules.with_raw_response.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.rules.with_streaming_response.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            client.gpu_droplets.firewalls.rules.with_raw_response.remove(
                firewall_id="",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncGradient) -> None:
        rule = await async_client.gpu_droplets.firewalls.rules.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncGradient) -> None:
        rule = await async_client.gpu_droplets.firewalls.rules.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            inbound_rules=[
                {
                    "ports": "3306",
                    "protocol": "tcp",
                    "sources": {
                        "addresses": ["1.2.3.4", "18.0.0.0/8"],
                        "droplet_ids": [49696269],
                        "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                        "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                        "tags": ["base-image", "prod"],
                    },
                }
            ],
            outbound_rules=[
                {
                    "destinations": {
                        "addresses": ["1.2.3.4", "18.0.0.0/8"],
                        "droplet_ids": [49696269],
                        "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                        "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                        "tags": ["base-image", "prod"],
                    },
                    "ports": "3306",
                    "protocol": "tcp",
                }
            ],
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.rules.with_raw_response.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.rules.with_streaming_response.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            await async_client.gpu_droplets.firewalls.rules.with_raw_response.add(
                firewall_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncGradient) -> None:
        rule = await async_client.gpu_droplets.firewalls.rules.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncGradient) -> None:
        rule = await async_client.gpu_droplets.firewalls.rules.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            inbound_rules=[
                {
                    "ports": "3306",
                    "protocol": "tcp",
                    "sources": {
                        "addresses": ["1.2.3.4", "18.0.0.0/8"],
                        "droplet_ids": [49696269],
                        "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                        "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                        "tags": ["base-image", "prod"],
                    },
                }
            ],
            outbound_rules=[
                {
                    "destinations": {
                        "addresses": ["1.2.3.4", "18.0.0.0/8"],
                        "droplet_ids": [49696269],
                        "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                        "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                        "tags": ["base-image", "prod"],
                    },
                    "ports": "3306",
                    "protocol": "tcp",
                }
            ],
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.rules.with_raw_response.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.rules.with_streaming_response.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            await async_client.gpu_droplets.firewalls.rules.with_raw_response.remove(
                firewall_id="",
            )
