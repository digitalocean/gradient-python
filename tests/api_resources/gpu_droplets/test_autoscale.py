# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets import (
    AutoscaleListResponse,
    AutoscaleCreateResponse,
    AutoscaleUpdateResponse,
    AutoscaleRetrieveResponse,
    AutoscaleListHistoryResponse,
    AutoscaleListMembersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutoscale:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.create(
            config={
                "max_instances": 5,
                "min_instances": 1,
            },
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        )
        assert_matches_type(AutoscaleCreateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.create(
            config={
                "max_instances": 5,
                "min_instances": 1,
                "cooldown_minutes": 10,
                "target_cpu_utilization": 0.5,
                "target_memory_utilization": 0.6,
            },
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
                "ipv6": True,
                "name": "example.com",
                "project_id": "746c6152-2fa2-11ed-92d3-27aaa54e4988",
                "tags": ["env:prod", "web"],
                "user_data": "#cloud-config\nruncmd:\n  - touch /test.txt\n",
                "vpc_uuid": "760e09ef-dc84-11e8-981e-3cfdfeaae000",
                "with_droplet_agent": True,
            },
            name="my-autoscale-pool",
        )
        assert_matches_type(AutoscaleCreateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.gpu_droplets.autoscale.with_raw_response.create(
            config={
                "max_instances": 5,
                "min_instances": 1,
            },
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = response.parse()
        assert_matches_type(AutoscaleCreateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.gpu_droplets.autoscale.with_streaming_response.create(
            config={
                "max_instances": 5,
                "min_instances": 1,
            },
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = response.parse()
            assert_matches_type(AutoscaleCreateResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.retrieve(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        )
        assert_matches_type(AutoscaleRetrieveResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.autoscale.with_raw_response.retrieve(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = response.parse()
        assert_matches_type(AutoscaleRetrieveResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.autoscale.with_streaming_response.retrieve(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = response.parse()
            assert_matches_type(AutoscaleRetrieveResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            client.gpu_droplets.autoscale.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.update(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            config={"target_number_instances": 2},
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        )
        assert_matches_type(AutoscaleUpdateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.update(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            config={"target_number_instances": 2},
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
                "ipv6": True,
                "name": "example.com",
                "project_id": "746c6152-2fa2-11ed-92d3-27aaa54e4988",
                "tags": ["env:prod", "web"],
                "user_data": "#cloud-config\nruncmd:\n  - touch /test.txt\n",
                "vpc_uuid": "760e09ef-dc84-11e8-981e-3cfdfeaae000",
                "with_droplet_agent": True,
            },
            name="my-autoscale-pool",
        )
        assert_matches_type(AutoscaleUpdateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.gpu_droplets.autoscale.with_raw_response.update(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            config={"target_number_instances": 2},
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = response.parse()
        assert_matches_type(AutoscaleUpdateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.gpu_droplets.autoscale.with_streaming_response.update(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            config={"target_number_instances": 2},
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = response.parse()
            assert_matches_type(AutoscaleUpdateResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            client.gpu_droplets.autoscale.with_raw_response.update(
                autoscale_pool_id="",
                config={"target_number_instances": 2},
                droplet_template={
                    "image": "ubuntu-20-04-x64",
                    "region": "nyc3",
                    "size": "c-2",
                    "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
                },
                name="my-autoscale-pool",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.list()
        assert_matches_type(AutoscaleListResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.list(
            name="name",
            page=1,
            per_page=1,
        )
        assert_matches_type(AutoscaleListResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.autoscale.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = response.parse()
        assert_matches_type(AutoscaleListResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.autoscale.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = response.parse()
            assert_matches_type(AutoscaleListResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.delete(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        )
        assert autoscale is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.gpu_droplets.autoscale.with_raw_response.delete(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = response.parse()
        assert autoscale is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.gpu_droplets.autoscale.with_streaming_response.delete(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = response.parse()
            assert autoscale is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            client.gpu_droplets.autoscale.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_dangerous(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.delete_dangerous(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            x_dangerous=True,
        )
        assert autoscale is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_dangerous(self, client: Gradient) -> None:
        response = client.gpu_droplets.autoscale.with_raw_response.delete_dangerous(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            x_dangerous=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = response.parse()
        assert autoscale is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_dangerous(self, client: Gradient) -> None:
        with client.gpu_droplets.autoscale.with_streaming_response.delete_dangerous(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            x_dangerous=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = response.parse()
            assert autoscale is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_dangerous(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            client.gpu_droplets.autoscale.with_raw_response.delete_dangerous(
                autoscale_pool_id="",
                x_dangerous=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_history(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.list_history(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        )
        assert_matches_type(AutoscaleListHistoryResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_history_with_all_params(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.list_history(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            page=1,
            per_page=1,
        )
        assert_matches_type(AutoscaleListHistoryResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_history(self, client: Gradient) -> None:
        response = client.gpu_droplets.autoscale.with_raw_response.list_history(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = response.parse()
        assert_matches_type(AutoscaleListHistoryResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_history(self, client: Gradient) -> None:
        with client.gpu_droplets.autoscale.with_streaming_response.list_history(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = response.parse()
            assert_matches_type(AutoscaleListHistoryResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_history(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            client.gpu_droplets.autoscale.with_raw_response.list_history(
                autoscale_pool_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_members(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.list_members(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        )
        assert_matches_type(AutoscaleListMembersResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_members_with_all_params(self, client: Gradient) -> None:
        autoscale = client.gpu_droplets.autoscale.list_members(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            page=1,
            per_page=1,
        )
        assert_matches_type(AutoscaleListMembersResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_members(self, client: Gradient) -> None:
        response = client.gpu_droplets.autoscale.with_raw_response.list_members(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = response.parse()
        assert_matches_type(AutoscaleListMembersResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_members(self, client: Gradient) -> None:
        with client.gpu_droplets.autoscale.with_streaming_response.list_members(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = response.parse()
            assert_matches_type(AutoscaleListMembersResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_members(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            client.gpu_droplets.autoscale.with_raw_response.list_members(
                autoscale_pool_id="",
            )


class TestAsyncAutoscale:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.create(
            config={
                "max_instances": 5,
                "min_instances": 1,
            },
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        )
        assert_matches_type(AutoscaleCreateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.create(
            config={
                "max_instances": 5,
                "min_instances": 1,
                "cooldown_minutes": 10,
                "target_cpu_utilization": 0.5,
                "target_memory_utilization": 0.6,
            },
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
                "ipv6": True,
                "name": "example.com",
                "project_id": "746c6152-2fa2-11ed-92d3-27aaa54e4988",
                "tags": ["env:prod", "web"],
                "user_data": "#cloud-config\nruncmd:\n  - touch /test.txt\n",
                "vpc_uuid": "760e09ef-dc84-11e8-981e-3cfdfeaae000",
                "with_droplet_agent": True,
            },
            name="my-autoscale-pool",
        )
        assert_matches_type(AutoscaleCreateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.autoscale.with_raw_response.create(
            config={
                "max_instances": 5,
                "min_instances": 1,
            },
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = await response.parse()
        assert_matches_type(AutoscaleCreateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.autoscale.with_streaming_response.create(
            config={
                "max_instances": 5,
                "min_instances": 1,
            },
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = await response.parse()
            assert_matches_type(AutoscaleCreateResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.retrieve(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        )
        assert_matches_type(AutoscaleRetrieveResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.autoscale.with_raw_response.retrieve(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = await response.parse()
        assert_matches_type(AutoscaleRetrieveResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.autoscale.with_streaming_response.retrieve(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = await response.parse()
            assert_matches_type(AutoscaleRetrieveResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            await async_client.gpu_droplets.autoscale.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.update(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            config={"target_number_instances": 2},
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        )
        assert_matches_type(AutoscaleUpdateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.update(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            config={"target_number_instances": 2},
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
                "ipv6": True,
                "name": "example.com",
                "project_id": "746c6152-2fa2-11ed-92d3-27aaa54e4988",
                "tags": ["env:prod", "web"],
                "user_data": "#cloud-config\nruncmd:\n  - touch /test.txt\n",
                "vpc_uuid": "760e09ef-dc84-11e8-981e-3cfdfeaae000",
                "with_droplet_agent": True,
            },
            name="my-autoscale-pool",
        )
        assert_matches_type(AutoscaleUpdateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.autoscale.with_raw_response.update(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            config={"target_number_instances": 2},
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = await response.parse()
        assert_matches_type(AutoscaleUpdateResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.autoscale.with_streaming_response.update(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            config={"target_number_instances": 2},
            droplet_template={
                "image": "ubuntu-20-04-x64",
                "region": "nyc3",
                "size": "c-2",
                "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
            },
            name="my-autoscale-pool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = await response.parse()
            assert_matches_type(AutoscaleUpdateResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            await async_client.gpu_droplets.autoscale.with_raw_response.update(
                autoscale_pool_id="",
                config={"target_number_instances": 2},
                droplet_template={
                    "image": "ubuntu-20-04-x64",
                    "region": "nyc3",
                    "size": "c-2",
                    "ssh_keys": ["3b:16:e4:bf:8b:00:8b:b8:59:8c:a9:d3:f0:19:fa:45"],
                },
                name="my-autoscale-pool",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.list()
        assert_matches_type(AutoscaleListResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.list(
            name="name",
            page=1,
            per_page=1,
        )
        assert_matches_type(AutoscaleListResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.autoscale.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = await response.parse()
        assert_matches_type(AutoscaleListResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.autoscale.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = await response.parse()
            assert_matches_type(AutoscaleListResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.delete(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        )
        assert autoscale is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.autoscale.with_raw_response.delete(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = await response.parse()
        assert autoscale is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.autoscale.with_streaming_response.delete(
            "0d3db13e-a604-4944-9827-7ec2642d32ac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = await response.parse()
            assert autoscale is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            await async_client.gpu_droplets.autoscale.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_dangerous(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.delete_dangerous(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            x_dangerous=True,
        )
        assert autoscale is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_dangerous(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.autoscale.with_raw_response.delete_dangerous(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            x_dangerous=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = await response.parse()
        assert autoscale is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_dangerous(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.autoscale.with_streaming_response.delete_dangerous(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            x_dangerous=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = await response.parse()
            assert autoscale is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_dangerous(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            await async_client.gpu_droplets.autoscale.with_raw_response.delete_dangerous(
                autoscale_pool_id="",
                x_dangerous=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_history(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.list_history(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        )
        assert_matches_type(AutoscaleListHistoryResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_history_with_all_params(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.list_history(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            page=1,
            per_page=1,
        )
        assert_matches_type(AutoscaleListHistoryResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_history(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.autoscale.with_raw_response.list_history(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = await response.parse()
        assert_matches_type(AutoscaleListHistoryResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_history(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.autoscale.with_streaming_response.list_history(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = await response.parse()
            assert_matches_type(AutoscaleListHistoryResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_history(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            await async_client.gpu_droplets.autoscale.with_raw_response.list_history(
                autoscale_pool_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_members(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.list_members(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        )
        assert_matches_type(AutoscaleListMembersResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncGradient) -> None:
        autoscale = await async_client.gpu_droplets.autoscale.list_members(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
            page=1,
            per_page=1,
        )
        assert_matches_type(AutoscaleListMembersResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.autoscale.with_raw_response.list_members(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoscale = await response.parse()
        assert_matches_type(AutoscaleListMembersResponse, autoscale, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.autoscale.with_streaming_response.list_members(
            autoscale_pool_id="0d3db13e-a604-4944-9827-7ec2642d32ac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoscale = await response.parse()
            assert_matches_type(AutoscaleListMembersResponse, autoscale, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_members(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoscale_pool_id` but received ''"):
            await async_client.gpu_droplets.autoscale.with_raw_response.list_members(
                autoscale_pool_id="",
            )
