# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets import (
    FirewallListResponse,
    FirewallCreateResponse,
    FirewallUpdateResponse,
    FirewallRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFirewalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        firewall = client.gpu_droplets.firewalls.create()
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        firewall = client.gpu_droplets.firewalls.create(
            body={
                "droplet_ids": [8043964],
                "inbound_rules": [
                    {
                        "ports": "80",
                        "protocol": "tcp",
                        "sources": {
                            "addresses": ["1.2.3.4", "18.0.0.0/8"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["base-image", "prod"],
                        },
                    },
                    {
                        "ports": "22",
                        "protocol": "tcp",
                        "sources": {
                            "addresses": ["18.0.0.0/8"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["gateway"],
                        },
                    },
                ],
                "name": "firewall",
                "outbound_rules": [
                    {
                        "destinations": {
                            "addresses": ["0.0.0.0/0", "::/0"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["base-image", "prod"],
                        },
                        "ports": "80",
                        "protocol": "tcp",
                    }
                ],
                "tags": ["base-image", "prod"],
            },
        )
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = response.parse()
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = response.parse()
            assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        firewall = client.gpu_droplets.firewalls.retrieve(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        )
        assert_matches_type(FirewallRetrieveResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.with_raw_response.retrieve(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = response.parse()
        assert_matches_type(FirewallRetrieveResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.with_streaming_response.retrieve(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = response.parse()
            assert_matches_type(FirewallRetrieveResponse, firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            client.gpu_droplets.firewalls.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        firewall = client.gpu_droplets.firewalls.update(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            firewall={"name": "frontend-firewall"},
        )
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        firewall = client.gpu_droplets.firewalls.update(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            firewall={
                "droplet_ids": [8043964],
                "inbound_rules": [
                    {
                        "ports": "8080",
                        "protocol": "tcp",
                        "sources": {
                            "addresses": ["1.2.3.4", "18.0.0.0/8"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["base-image", "prod"],
                        },
                    },
                    {
                        "ports": "22",
                        "protocol": "tcp",
                        "sources": {
                            "addresses": ["18.0.0.0/8"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["gateway"],
                        },
                    },
                ],
                "name": "frontend-firewall",
                "outbound_rules": [
                    {
                        "destinations": {
                            "addresses": ["0.0.0.0/0", "::/0"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["base-image", "prod"],
                        },
                        "ports": "8080",
                        "protocol": "tcp",
                    }
                ],
                "tags": ["frontend"],
            },
        )
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.with_raw_response.update(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            firewall={"name": "frontend-firewall"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = response.parse()
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.with_streaming_response.update(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            firewall={"name": "frontend-firewall"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = response.parse()
            assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            client.gpu_droplets.firewalls.with_raw_response.update(
                firewall_id="",
                firewall={"name": "frontend-firewall"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        firewall = client.gpu_droplets.firewalls.list()
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        firewall = client.gpu_droplets.firewalls.list(
            page=1,
            per_page=1,
        )
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = response.parse()
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = response.parse()
            assert_matches_type(FirewallListResponse, firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        firewall = client.gpu_droplets.firewalls.delete(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        )
        assert firewall is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.with_raw_response.delete(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = response.parse()
        assert firewall is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.with_streaming_response.delete(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = response.parse()
            assert firewall is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            client.gpu_droplets.firewalls.with_raw_response.delete(
                "",
            )


class TestAsyncFirewalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        firewall = await async_client.gpu_droplets.firewalls.create()
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        firewall = await async_client.gpu_droplets.firewalls.create(
            body={
                "droplet_ids": [8043964],
                "inbound_rules": [
                    {
                        "ports": "80",
                        "protocol": "tcp",
                        "sources": {
                            "addresses": ["1.2.3.4", "18.0.0.0/8"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["base-image", "prod"],
                        },
                    },
                    {
                        "ports": "22",
                        "protocol": "tcp",
                        "sources": {
                            "addresses": ["18.0.0.0/8"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["gateway"],
                        },
                    },
                ],
                "name": "firewall",
                "outbound_rules": [
                    {
                        "destinations": {
                            "addresses": ["0.0.0.0/0", "::/0"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["base-image", "prod"],
                        },
                        "ports": "80",
                        "protocol": "tcp",
                    }
                ],
                "tags": ["base-image", "prod"],
            },
        )
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = await response.parse()
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = await response.parse()
            assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        firewall = await async_client.gpu_droplets.firewalls.retrieve(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        )
        assert_matches_type(FirewallRetrieveResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.with_raw_response.retrieve(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = await response.parse()
        assert_matches_type(FirewallRetrieveResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.with_streaming_response.retrieve(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = await response.parse()
            assert_matches_type(FirewallRetrieveResponse, firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            await async_client.gpu_droplets.firewalls.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        firewall = await async_client.gpu_droplets.firewalls.update(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            firewall={"name": "frontend-firewall"},
        )
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        firewall = await async_client.gpu_droplets.firewalls.update(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            firewall={
                "droplet_ids": [8043964],
                "inbound_rules": [
                    {
                        "ports": "8080",
                        "protocol": "tcp",
                        "sources": {
                            "addresses": ["1.2.3.4", "18.0.0.0/8"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["base-image", "prod"],
                        },
                    },
                    {
                        "ports": "22",
                        "protocol": "tcp",
                        "sources": {
                            "addresses": ["18.0.0.0/8"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["gateway"],
                        },
                    },
                ],
                "name": "frontend-firewall",
                "outbound_rules": [
                    {
                        "destinations": {
                            "addresses": ["0.0.0.0/0", "::/0"],
                            "droplet_ids": [8043964],
                            "kubernetes_ids": ["41b74c5d-9bd0-5555-5555-a57c495b81a3"],
                            "load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"],
                            "tags": ["base-image", "prod"],
                        },
                        "ports": "8080",
                        "protocol": "tcp",
                    }
                ],
                "tags": ["frontend"],
            },
        )
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.with_raw_response.update(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            firewall={"name": "frontend-firewall"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = await response.parse()
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.with_streaming_response.update(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            firewall={"name": "frontend-firewall"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = await response.parse()
            assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            await async_client.gpu_droplets.firewalls.with_raw_response.update(
                firewall_id="",
                firewall={"name": "frontend-firewall"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        firewall = await async_client.gpu_droplets.firewalls.list()
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        firewall = await async_client.gpu_droplets.firewalls.list(
            page=1,
            per_page=1,
        )
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = await response.parse()
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = await response.parse()
            assert_matches_type(FirewallListResponse, firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        firewall = await async_client.gpu_droplets.firewalls.delete(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        )
        assert firewall is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.with_raw_response.delete(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        firewall = await response.parse()
        assert firewall is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.with_streaming_response.delete(
            "bb4b2611-3d72-467b-8602-280330ecd65c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            firewall = await response.parse()
            assert firewall is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            await async_client.gpu_droplets.firewalls.with_raw_response.delete(
                "",
            )
