# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types import (
    GPUDropletListResponse,
    GPUDropletCreateResponse,
    GPUDropletRetrieveResponse,
    GPUDropletListKernelsResponse,
    GPUDropletListFirewallsResponse,
    GPUDropletListNeighborsResponse,
    GPUDropletListSnapshotsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGPUDroplets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.create(
            image="ubuntu-20-04-x64",
            name="example.com",
            size="s-1vcpu-1gb",
        )
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.create(
            image="ubuntu-20-04-x64",
            name="example.com",
            size="s-1vcpu-1gb",
            backup_policy={
                "hour": 0,
                "plan": "daily",
                "weekday": "SUN",
            },
            backups=True,
            ipv6=True,
            monitoring=True,
            private_networking=True,
            region="nyc3",
            ssh_keys=[289794, "3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            tags=["env:prod", "web"],
            user_data="#cloud-config\nruncmd:\n  - touch /test.txt\n",
            volumes=["12e97116-7280-11ed-b3d0-0a58ac146812"],
            vpc_uuid="760e09ef-dc84-11e8-981e-3cfdfeaae000",
            with_droplet_agent=True,
        )
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.create(
            image="ubuntu-20-04-x64",
            name="example.com",
            size="s-1vcpu-1gb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.create(
            image="ubuntu-20-04-x64",
            name="example.com",
            size="s-1vcpu-1gb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.create(
            image="ubuntu-20-04-x64",
            names=["sub-01.example.com", "sub-02.example.com"],
            size="s-1vcpu-1gb",
        )
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.create(
            image="ubuntu-20-04-x64",
            names=["sub-01.example.com", "sub-02.example.com"],
            size="s-1vcpu-1gb",
            backup_policy={
                "hour": 0,
                "plan": "daily",
                "weekday": "SUN",
            },
            backups=True,
            ipv6=True,
            monitoring=True,
            private_networking=True,
            region="nyc3",
            ssh_keys=[289794, "3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            tags=["env:prod", "web"],
            user_data="#cloud-config\nruncmd:\n  - touch /test.txt\n",
            volumes=["12e97116-7280-11ed-b3d0-0a58ac146812"],
            vpc_uuid="760e09ef-dc84-11e8-981e-3cfdfeaae000",
            with_droplet_agent=True,
        )
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.create(
            image="ubuntu-20-04-x64",
            names=["sub-01.example.com", "sub-02.example.com"],
            size="s-1vcpu-1gb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.create(
            image="ubuntu-20-04-x64",
            names=["sub-01.example.com", "sub-02.example.com"],
            size="s-1vcpu-1gb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.retrieve(
            3164444,
        )
        assert_matches_type(GPUDropletRetrieveResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.retrieve(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert_matches_type(GPUDropletRetrieveResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.retrieve(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert_matches_type(GPUDropletRetrieveResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list()
        assert_matches_type(GPUDropletListResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list(
            name="name",
            page=1,
            per_page=1,
            tag_name="tag_name",
            type="droplets",
        )
        assert_matches_type(GPUDropletListResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert_matches_type(GPUDropletListResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert_matches_type(GPUDropletListResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.delete(
            3164444,
        )
        assert gpu_droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.delete(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert gpu_droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.delete(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert gpu_droplet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_by_tag(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.delete_by_tag(
            tag_name="tag_name",
        )
        assert gpu_droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_by_tag(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.delete_by_tag(
            tag_name="tag_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert gpu_droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_tag(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.delete_by_tag(
            tag_name="tag_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert gpu_droplet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_firewalls(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list_firewalls(
            droplet_id=3164444,
        )
        assert_matches_type(GPUDropletListFirewallsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_firewalls_with_all_params(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list_firewalls(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(GPUDropletListFirewallsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_firewalls(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.list_firewalls(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert_matches_type(GPUDropletListFirewallsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_firewalls(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.list_firewalls(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert_matches_type(GPUDropletListFirewallsResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_kernels(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list_kernels(
            droplet_id=3164444,
        )
        assert_matches_type(GPUDropletListKernelsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_kernels_with_all_params(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list_kernels(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(GPUDropletListKernelsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_kernels(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.list_kernels(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert_matches_type(GPUDropletListKernelsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_kernels(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.list_kernels(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert_matches_type(GPUDropletListKernelsResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_neighbors(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list_neighbors(
            3164444,
        )
        assert_matches_type(GPUDropletListNeighborsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_neighbors(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.list_neighbors(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert_matches_type(GPUDropletListNeighborsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_neighbors(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.list_neighbors(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert_matches_type(GPUDropletListNeighborsResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_snapshots(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list_snapshots(
            droplet_id=3164444,
        )
        assert_matches_type(GPUDropletListSnapshotsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_snapshots_with_all_params(self, client: Gradient) -> None:
        gpu_droplet = client.gpu_droplets.list_snapshots(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(GPUDropletListSnapshotsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_snapshots(self, client: Gradient) -> None:
        response = client.gpu_droplets.with_raw_response.list_snapshots(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = response.parse()
        assert_matches_type(GPUDropletListSnapshotsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_snapshots(self, client: Gradient) -> None:
        with client.gpu_droplets.with_streaming_response.list_snapshots(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = response.parse()
            assert_matches_type(GPUDropletListSnapshotsResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGPUDroplets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.create(
            image="ubuntu-20-04-x64",
            name="example.com",
            size="s-1vcpu-1gb",
        )
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.create(
            image="ubuntu-20-04-x64",
            name="example.com",
            size="s-1vcpu-1gb",
            backup_policy={
                "hour": 0,
                "plan": "daily",
                "weekday": "SUN",
            },
            backups=True,
            ipv6=True,
            monitoring=True,
            private_networking=True,
            region="nyc3",
            ssh_keys=[289794, "3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            tags=["env:prod", "web"],
            user_data="#cloud-config\nruncmd:\n  - touch /test.txt\n",
            volumes=["12e97116-7280-11ed-b3d0-0a58ac146812"],
            vpc_uuid="760e09ef-dc84-11e8-981e-3cfdfeaae000",
            with_droplet_agent=True,
        )
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.create(
            image="ubuntu-20-04-x64",
            name="example.com",
            size="s-1vcpu-1gb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.create(
            image="ubuntu-20-04-x64",
            name="example.com",
            size="s-1vcpu-1gb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.create(
            image="ubuntu-20-04-x64",
            names=["sub-01.example.com", "sub-02.example.com"],
            size="s-1vcpu-1gb",
        )
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.create(
            image="ubuntu-20-04-x64",
            names=["sub-01.example.com", "sub-02.example.com"],
            size="s-1vcpu-1gb",
            backup_policy={
                "hour": 0,
                "plan": "daily",
                "weekday": "SUN",
            },
            backups=True,
            ipv6=True,
            monitoring=True,
            private_networking=True,
            region="nyc3",
            ssh_keys=[289794, "3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            tags=["env:prod", "web"],
            user_data="#cloud-config\nruncmd:\n  - touch /test.txt\n",
            volumes=["12e97116-7280-11ed-b3d0-0a58ac146812"],
            vpc_uuid="760e09ef-dc84-11e8-981e-3cfdfeaae000",
            with_droplet_agent=True,
        )
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.create(
            image="ubuntu-20-04-x64",
            names=["sub-01.example.com", "sub-02.example.com"],
            size="s-1vcpu-1gb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.create(
            image="ubuntu-20-04-x64",
            names=["sub-01.example.com", "sub-02.example.com"],
            size="s-1vcpu-1gb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert_matches_type(GPUDropletCreateResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.retrieve(
            3164444,
        )
        assert_matches_type(GPUDropletRetrieveResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.retrieve(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert_matches_type(GPUDropletRetrieveResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.retrieve(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert_matches_type(GPUDropletRetrieveResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list()
        assert_matches_type(GPUDropletListResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list(
            name="name",
            page=1,
            per_page=1,
            tag_name="tag_name",
            type="droplets",
        )
        assert_matches_type(GPUDropletListResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert_matches_type(GPUDropletListResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert_matches_type(GPUDropletListResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.delete(
            3164444,
        )
        assert gpu_droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.delete(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert gpu_droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.delete(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert gpu_droplet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_by_tag(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.delete_by_tag(
            tag_name="tag_name",
        )
        assert gpu_droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_tag(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.delete_by_tag(
            tag_name="tag_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert gpu_droplet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_tag(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.delete_by_tag(
            tag_name="tag_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert gpu_droplet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_firewalls(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list_firewalls(
            droplet_id=3164444,
        )
        assert_matches_type(GPUDropletListFirewallsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_firewalls_with_all_params(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list_firewalls(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(GPUDropletListFirewallsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_firewalls(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.list_firewalls(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert_matches_type(GPUDropletListFirewallsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_firewalls(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.list_firewalls(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert_matches_type(GPUDropletListFirewallsResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_kernels(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list_kernels(
            droplet_id=3164444,
        )
        assert_matches_type(GPUDropletListKernelsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_kernels_with_all_params(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list_kernels(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(GPUDropletListKernelsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_kernels(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.list_kernels(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert_matches_type(GPUDropletListKernelsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_kernels(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.list_kernels(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert_matches_type(GPUDropletListKernelsResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_neighbors(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list_neighbors(
            3164444,
        )
        assert_matches_type(GPUDropletListNeighborsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_neighbors(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.list_neighbors(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert_matches_type(GPUDropletListNeighborsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_neighbors(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.list_neighbors(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert_matches_type(GPUDropletListNeighborsResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_snapshots(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list_snapshots(
            droplet_id=3164444,
        )
        assert_matches_type(GPUDropletListSnapshotsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_snapshots_with_all_params(self, async_client: AsyncGradient) -> None:
        gpu_droplet = await async_client.gpu_droplets.list_snapshots(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(GPUDropletListSnapshotsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_snapshots(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.with_raw_response.list_snapshots(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_droplet = await response.parse()
        assert_matches_type(GPUDropletListSnapshotsResponse, gpu_droplet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_snapshots(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.with_streaming_response.list_snapshots(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_droplet = await response.parse()
            assert_matches_type(GPUDropletListSnapshotsResponse, gpu_droplet, path=["response"])

        assert cast(Any, response.is_closed) is True
