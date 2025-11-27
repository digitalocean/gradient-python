# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets import (
    LoadBalancerListResponse,
    LoadBalancerCreateResponse,
    LoadBalancerUpdateResponse,
    LoadBalancerRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoadBalancers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.create(
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.create(
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "tls_passthrough": False,
                }
            ],
            algorithm="round_robin",
            disable_lets_encrypt_dns_records=True,
            domains=[
                {
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "is_managed": True,
                    "name": "example.com",
                }
            ],
            droplet_ids=[3164444, 3164445],
            enable_backend_keepalive=True,
            enable_proxy_protocol=True,
            firewall={
                "allow": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
                "deny": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
            },
            glb_settings={
                "cdn": {"is_enabled": True},
                "failover_threshold": 50,
                "region_priorities": {
                    "nyc1": 1,
                    "fra1": 2,
                    "sgp1": 3,
                },
                "target_port": 80,
                "target_protocol": "http",
            },
            health_check={
                "check_interval_seconds": 10,
                "healthy_threshold": 3,
                "path": "/",
                "port": 80,
                "protocol": "http",
                "response_timeout_seconds": 5,
                "unhealthy_threshold": 5,
            },
            http_idle_timeout_seconds=90,
            name="example-lb-01",
            network="EXTERNAL",
            network_stack="IPV4",
            project_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            redirect_http_to_https=True,
            region="nyc3",
            size="lb-small",
            size_unit=3,
            sticky_sessions={
                "cookie_name": "DO-LB",
                "cookie_ttl_seconds": 300,
                "type": "cookies",
            },
            target_load_balancer_ids=["7dbf91fe-cbdb-48dc-8290-c3a181554905", "996fa239-fac3-42a2-b9a1-9fa822268b7a"],
            tls_cipher_policy="STRONG",
            type="REGIONAL",
            vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.with_raw_response.create(
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
        load_balancer = response.parse()
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.with_streaming_response.create(
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

            load_balancer = response.parse()
            assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.create(
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.create(
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "tls_passthrough": False,
                }
            ],
            algorithm="round_robin",
            disable_lets_encrypt_dns_records=True,
            domains=[
                {
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "is_managed": True,
                    "name": "example.com",
                }
            ],
            enable_backend_keepalive=True,
            enable_proxy_protocol=True,
            firewall={
                "allow": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
                "deny": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
            },
            glb_settings={
                "cdn": {"is_enabled": True},
                "failover_threshold": 50,
                "region_priorities": {
                    "nyc1": 1,
                    "fra1": 2,
                    "sgp1": 3,
                },
                "target_port": 80,
                "target_protocol": "http",
            },
            health_check={
                "check_interval_seconds": 10,
                "healthy_threshold": 3,
                "path": "/",
                "port": 80,
                "protocol": "http",
                "response_timeout_seconds": 5,
                "unhealthy_threshold": 5,
            },
            http_idle_timeout_seconds=90,
            name="example-lb-01",
            network="EXTERNAL",
            network_stack="IPV4",
            project_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            redirect_http_to_https=True,
            region="nyc3",
            size="lb-small",
            size_unit=3,
            sticky_sessions={
                "cookie_name": "DO-LB",
                "cookie_ttl_seconds": 300,
                "type": "cookies",
            },
            tag="prod:web",
            target_load_balancer_ids=["7dbf91fe-cbdb-48dc-8290-c3a181554905", "996fa239-fac3-42a2-b9a1-9fa822268b7a"],
            tls_cipher_policy="STRONG",
            type="REGIONAL",
            vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.with_raw_response.create(
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
        load_balancer = response.parse()
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.with_streaming_response.create(
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

            load_balancer = response.parse()
            assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.retrieve(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )
        assert_matches_type(LoadBalancerRetrieveResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.with_raw_response.retrieve(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancerRetrieveResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.with_streaming_response.retrieve(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancerRetrieveResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.update(
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
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.update(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "tls_passthrough": False,
                }
            ],
            algorithm="round_robin",
            disable_lets_encrypt_dns_records=True,
            domains=[
                {
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "is_managed": True,
                    "name": "example.com",
                }
            ],
            droplet_ids=[3164444, 3164445],
            enable_backend_keepalive=True,
            enable_proxy_protocol=True,
            firewall={
                "allow": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
                "deny": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
            },
            glb_settings={
                "cdn": {"is_enabled": True},
                "failover_threshold": 50,
                "region_priorities": {
                    "nyc1": 1,
                    "fra1": 2,
                    "sgp1": 3,
                },
                "target_port": 80,
                "target_protocol": "http",
            },
            health_check={
                "check_interval_seconds": 10,
                "healthy_threshold": 3,
                "path": "/",
                "port": 80,
                "protocol": "http",
                "response_timeout_seconds": 5,
                "unhealthy_threshold": 5,
            },
            http_idle_timeout_seconds=90,
            name="example-lb-01",
            network="EXTERNAL",
            network_stack="IPV4",
            project_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            redirect_http_to_https=True,
            region="nyc3",
            size="lb-small",
            size_unit=3,
            sticky_sessions={
                "cookie_name": "DO-LB",
                "cookie_ttl_seconds": 300,
                "type": "cookies",
            },
            target_load_balancer_ids=["7dbf91fe-cbdb-48dc-8290-c3a181554905", "996fa239-fac3-42a2-b9a1-9fa822268b7a"],
            tls_cipher_policy="STRONG",
            type="REGIONAL",
            vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        )
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.with_raw_response.update(
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
        load_balancer = response.parse()
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.with_streaming_response.update(
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

            load_balancer = response.parse()
            assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.with_raw_response.update(
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
    def test_method_update_overload_2(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.update(
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
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.update(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "tls_passthrough": False,
                }
            ],
            algorithm="round_robin",
            disable_lets_encrypt_dns_records=True,
            domains=[
                {
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "is_managed": True,
                    "name": "example.com",
                }
            ],
            enable_backend_keepalive=True,
            enable_proxy_protocol=True,
            firewall={
                "allow": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
                "deny": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
            },
            glb_settings={
                "cdn": {"is_enabled": True},
                "failover_threshold": 50,
                "region_priorities": {
                    "nyc1": 1,
                    "fra1": 2,
                    "sgp1": 3,
                },
                "target_port": 80,
                "target_protocol": "http",
            },
            health_check={
                "check_interval_seconds": 10,
                "healthy_threshold": 3,
                "path": "/",
                "port": 80,
                "protocol": "http",
                "response_timeout_seconds": 5,
                "unhealthy_threshold": 5,
            },
            http_idle_timeout_seconds=90,
            name="example-lb-01",
            network="EXTERNAL",
            network_stack="IPV4",
            project_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            redirect_http_to_https=True,
            region="nyc3",
            size="lb-small",
            size_unit=3,
            sticky_sessions={
                "cookie_name": "DO-LB",
                "cookie_ttl_seconds": 300,
                "type": "cookies",
            },
            tag="prod:web",
            target_load_balancer_ids=["7dbf91fe-cbdb-48dc-8290-c3a181554905", "996fa239-fac3-42a2-b9a1-9fa822268b7a"],
            tls_cipher_policy="STRONG",
            type="REGIONAL",
            vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        )
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.with_raw_response.update(
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
        load_balancer = response.parse()
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.with_streaming_response.update(
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

            load_balancer = response.parse()
            assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.with_raw_response.update(
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
    def test_method_list(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.list()
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.list(
            page=1,
            per_page=1,
        )
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.delete(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )
        assert load_balancer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.with_raw_response.delete(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert load_balancer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.with_streaming_response.delete(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert load_balancer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_cache(self, client: Gradient) -> None:
        load_balancer = client.gpu_droplets.load_balancers.delete_cache(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )
        assert load_balancer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_cache(self, client: Gradient) -> None:
        response = client.gpu_droplets.load_balancers.with_raw_response.delete_cache(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert load_balancer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_cache(self, client: Gradient) -> None:
        with client.gpu_droplets.load_balancers.with_streaming_response.delete_cache(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert load_balancer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_cache(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            client.gpu_droplets.load_balancers.with_raw_response.delete_cache(
                "",
            )


class TestAsyncLoadBalancers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.create(
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.create(
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "tls_passthrough": False,
                }
            ],
            algorithm="round_robin",
            disable_lets_encrypt_dns_records=True,
            domains=[
                {
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "is_managed": True,
                    "name": "example.com",
                }
            ],
            droplet_ids=[3164444, 3164445],
            enable_backend_keepalive=True,
            enable_proxy_protocol=True,
            firewall={
                "allow": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
                "deny": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
            },
            glb_settings={
                "cdn": {"is_enabled": True},
                "failover_threshold": 50,
                "region_priorities": {
                    "nyc1": 1,
                    "fra1": 2,
                    "sgp1": 3,
                },
                "target_port": 80,
                "target_protocol": "http",
            },
            health_check={
                "check_interval_seconds": 10,
                "healthy_threshold": 3,
                "path": "/",
                "port": 80,
                "protocol": "http",
                "response_timeout_seconds": 5,
                "unhealthy_threshold": 5,
            },
            http_idle_timeout_seconds=90,
            name="example-lb-01",
            network="EXTERNAL",
            network_stack="IPV4",
            project_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            redirect_http_to_https=True,
            region="nyc3",
            size="lb-small",
            size_unit=3,
            sticky_sessions={
                "cookie_name": "DO-LB",
                "cookie_ttl_seconds": 300,
                "type": "cookies",
            },
            target_load_balancer_ids=["7dbf91fe-cbdb-48dc-8290-c3a181554905", "996fa239-fac3-42a2-b9a1-9fa822268b7a"],
            tls_cipher_policy="STRONG",
            type="REGIONAL",
            vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.with_raw_response.create(
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
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.with_streaming_response.create(
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

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.create(
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                }
            ],
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.create(
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "tls_passthrough": False,
                }
            ],
            algorithm="round_robin",
            disable_lets_encrypt_dns_records=True,
            domains=[
                {
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "is_managed": True,
                    "name": "example.com",
                }
            ],
            enable_backend_keepalive=True,
            enable_proxy_protocol=True,
            firewall={
                "allow": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
                "deny": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
            },
            glb_settings={
                "cdn": {"is_enabled": True},
                "failover_threshold": 50,
                "region_priorities": {
                    "nyc1": 1,
                    "fra1": 2,
                    "sgp1": 3,
                },
                "target_port": 80,
                "target_protocol": "http",
            },
            health_check={
                "check_interval_seconds": 10,
                "healthy_threshold": 3,
                "path": "/",
                "port": 80,
                "protocol": "http",
                "response_timeout_seconds": 5,
                "unhealthy_threshold": 5,
            },
            http_idle_timeout_seconds=90,
            name="example-lb-01",
            network="EXTERNAL",
            network_stack="IPV4",
            project_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            redirect_http_to_https=True,
            region="nyc3",
            size="lb-small",
            size_unit=3,
            sticky_sessions={
                "cookie_name": "DO-LB",
                "cookie_ttl_seconds": 300,
                "type": "cookies",
            },
            tag="prod:web",
            target_load_balancer_ids=["7dbf91fe-cbdb-48dc-8290-c3a181554905", "996fa239-fac3-42a2-b9a1-9fa822268b7a"],
            tls_cipher_policy="STRONG",
            type="REGIONAL",
            vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.with_raw_response.create(
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
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.with_streaming_response.create(
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

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.retrieve(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )
        assert_matches_type(LoadBalancerRetrieveResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.with_raw_response.retrieve(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancerRetrieveResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.with_streaming_response.retrieve(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancerRetrieveResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.update(
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
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.update(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "tls_passthrough": False,
                }
            ],
            algorithm="round_robin",
            disable_lets_encrypt_dns_records=True,
            domains=[
                {
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "is_managed": True,
                    "name": "example.com",
                }
            ],
            droplet_ids=[3164444, 3164445],
            enable_backend_keepalive=True,
            enable_proxy_protocol=True,
            firewall={
                "allow": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
                "deny": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
            },
            glb_settings={
                "cdn": {"is_enabled": True},
                "failover_threshold": 50,
                "region_priorities": {
                    "nyc1": 1,
                    "fra1": 2,
                    "sgp1": 3,
                },
                "target_port": 80,
                "target_protocol": "http",
            },
            health_check={
                "check_interval_seconds": 10,
                "healthy_threshold": 3,
                "path": "/",
                "port": 80,
                "protocol": "http",
                "response_timeout_seconds": 5,
                "unhealthy_threshold": 5,
            },
            http_idle_timeout_seconds=90,
            name="example-lb-01",
            network="EXTERNAL",
            network_stack="IPV4",
            project_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            redirect_http_to_https=True,
            region="nyc3",
            size="lb-small",
            size_unit=3,
            sticky_sessions={
                "cookie_name": "DO-LB",
                "cookie_ttl_seconds": 300,
                "type": "cookies",
            },
            target_load_balancer_ids=["7dbf91fe-cbdb-48dc-8290-c3a181554905", "996fa239-fac3-42a2-b9a1-9fa822268b7a"],
            tls_cipher_policy="STRONG",
            type="REGIONAL",
            vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        )
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.with_raw_response.update(
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
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.with_streaming_response.update(
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

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.with_raw_response.update(
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
    async def test_method_update_overload_2(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.update(
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
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.update(
            lb_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            forwarding_rules=[
                {
                    "entry_port": 443,
                    "entry_protocol": "https",
                    "target_port": 80,
                    "target_protocol": "http",
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "tls_passthrough": False,
                }
            ],
            algorithm="round_robin",
            disable_lets_encrypt_dns_records=True,
            domains=[
                {
                    "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
                    "is_managed": True,
                    "name": "example.com",
                }
            ],
            enable_backend_keepalive=True,
            enable_proxy_protocol=True,
            firewall={
                "allow": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
                "deny": ["ip:1.2.3.4", "cidr:2.3.0.0/16"],
            },
            glb_settings={
                "cdn": {"is_enabled": True},
                "failover_threshold": 50,
                "region_priorities": {
                    "nyc1": 1,
                    "fra1": 2,
                    "sgp1": 3,
                },
                "target_port": 80,
                "target_protocol": "http",
            },
            health_check={
                "check_interval_seconds": 10,
                "healthy_threshold": 3,
                "path": "/",
                "port": 80,
                "protocol": "http",
                "response_timeout_seconds": 5,
                "unhealthy_threshold": 5,
            },
            http_idle_timeout_seconds=90,
            name="example-lb-01",
            network="EXTERNAL",
            network_stack="IPV4",
            project_id="4de7ac8b-495b-4884-9a69-1050c6793cd6",
            redirect_http_to_https=True,
            region="nyc3",
            size="lb-small",
            size_unit=3,
            sticky_sessions={
                "cookie_name": "DO-LB",
                "cookie_ttl_seconds": 300,
                "type": "cookies",
            },
            tag="prod:web",
            target_load_balancer_ids=["7dbf91fe-cbdb-48dc-8290-c3a181554905", "996fa239-fac3-42a2-b9a1-9fa822268b7a"],
            tls_cipher_policy="STRONG",
            type="REGIONAL",
            vpc_uuid="c33931f2-a26a-4e61-b85c-4e95a2ec431b",
        )
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.with_raw_response.update(
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
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.with_streaming_response.update(
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

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.with_raw_response.update(
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
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.list()
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.list(
            page=1,
            per_page=1,
        )
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.delete(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )
        assert load_balancer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.with_raw_response.delete(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert load_balancer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.with_streaming_response.delete(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert load_balancer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_cache(self, async_client: AsyncGradient) -> None:
        load_balancer = await async_client.gpu_droplets.load_balancers.delete_cache(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )
        assert load_balancer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_cache(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.load_balancers.with_raw_response.delete_cache(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert load_balancer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_cache(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.load_balancers.with_streaming_response.delete_cache(
            "4de7ac8b-495b-4884-9a69-1050c6793cd6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert load_balancer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_cache(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lb_id` but received ''"):
            await async_client.gpu_droplets.load_balancers.with_raw_response.delete_cache(
                "",
            )
