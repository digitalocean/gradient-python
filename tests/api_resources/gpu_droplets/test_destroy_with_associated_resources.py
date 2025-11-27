# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets import (
    DestroyWithAssociatedResourceListResponse,
    DestroyWithAssociatedResourceCheckStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDestroyWithAssociatedResources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        destroy_with_associated_resource = client.gpu_droplets.destroy_with_associated_resources.list(
            3164444,
        )
        assert_matches_type(
            DestroyWithAssociatedResourceListResponse, destroy_with_associated_resource, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.destroy_with_associated_resources.with_raw_response.list(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = response.parse()
        assert_matches_type(
            DestroyWithAssociatedResourceListResponse, destroy_with_associated_resource, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.list(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = response.parse()
            assert_matches_type(
                DestroyWithAssociatedResourceListResponse, destroy_with_associated_resource, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_status(self, client: Gradient) -> None:
        destroy_with_associated_resource = client.gpu_droplets.destroy_with_associated_resources.check_status(
            3164444,
        )
        assert_matches_type(
            DestroyWithAssociatedResourceCheckStatusResponse, destroy_with_associated_resource, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_status(self, client: Gradient) -> None:
        response = client.gpu_droplets.destroy_with_associated_resources.with_raw_response.check_status(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = response.parse()
        assert_matches_type(
            DestroyWithAssociatedResourceCheckStatusResponse, destroy_with_associated_resource, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_status(self, client: Gradient) -> None:
        with client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.check_status(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = response.parse()
            assert_matches_type(
                DestroyWithAssociatedResourceCheckStatusResponse, destroy_with_associated_resource, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_dangerous(self, client: Gradient) -> None:
        destroy_with_associated_resource = client.gpu_droplets.destroy_with_associated_resources.delete_dangerous(
            droplet_id=3164444,
            x_dangerous=True,
        )
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_dangerous(self, client: Gradient) -> None:
        response = client.gpu_droplets.destroy_with_associated_resources.with_raw_response.delete_dangerous(
            droplet_id=3164444,
            x_dangerous=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = response.parse()
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_dangerous(self, client: Gradient) -> None:
        with client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.delete_dangerous(
            droplet_id=3164444,
            x_dangerous=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = response.parse()
            assert destroy_with_associated_resource is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_selective(self, client: Gradient) -> None:
        destroy_with_associated_resource = client.gpu_droplets.destroy_with_associated_resources.delete_selective(
            droplet_id=3164444,
        )
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_selective_with_all_params(self, client: Gradient) -> None:
        destroy_with_associated_resource = client.gpu_droplets.destroy_with_associated_resources.delete_selective(
            droplet_id=3164444,
            floating_ips=["6186916"],
            reserved_ips=["6186916"],
            snapshots=["61486916"],
            volume_snapshots=["edb0478d-7436-11ea-86e6-0a58ac144b91"],
            volumes=["ba49449a-7435-11ea-b89e-0a58ac14480f"],
        )
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_selective(self, client: Gradient) -> None:
        response = client.gpu_droplets.destroy_with_associated_resources.with_raw_response.delete_selective(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = response.parse()
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_selective(self, client: Gradient) -> None:
        with client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.delete_selective(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = response.parse()
            assert destroy_with_associated_resource is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retry(self, client: Gradient) -> None:
        destroy_with_associated_resource = client.gpu_droplets.destroy_with_associated_resources.retry(
            3164444,
        )
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: Gradient) -> None:
        response = client.gpu_droplets.destroy_with_associated_resources.with_raw_response.retry(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = response.parse()
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: Gradient) -> None:
        with client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.retry(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = response.parse()
            assert destroy_with_associated_resource is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDestroyWithAssociatedResources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        destroy_with_associated_resource = await async_client.gpu_droplets.destroy_with_associated_resources.list(
            3164444,
        )
        assert_matches_type(
            DestroyWithAssociatedResourceListResponse, destroy_with_associated_resource, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.destroy_with_associated_resources.with_raw_response.list(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = await response.parse()
        assert_matches_type(
            DestroyWithAssociatedResourceListResponse, destroy_with_associated_resource, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.list(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = await response.parse()
            assert_matches_type(
                DestroyWithAssociatedResourceListResponse, destroy_with_associated_resource, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_status(self, async_client: AsyncGradient) -> None:
        destroy_with_associated_resource = (
            await async_client.gpu_droplets.destroy_with_associated_resources.check_status(
                3164444,
            )
        )
        assert_matches_type(
            DestroyWithAssociatedResourceCheckStatusResponse, destroy_with_associated_resource, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_status(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.destroy_with_associated_resources.with_raw_response.check_status(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = await response.parse()
        assert_matches_type(
            DestroyWithAssociatedResourceCheckStatusResponse, destroy_with_associated_resource, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_status(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.check_status(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = await response.parse()
            assert_matches_type(
                DestroyWithAssociatedResourceCheckStatusResponse, destroy_with_associated_resource, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_dangerous(self, async_client: AsyncGradient) -> None:
        destroy_with_associated_resource = (
            await async_client.gpu_droplets.destroy_with_associated_resources.delete_dangerous(
                droplet_id=3164444,
                x_dangerous=True,
            )
        )
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_dangerous(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.destroy_with_associated_resources.with_raw_response.delete_dangerous(
            droplet_id=3164444,
            x_dangerous=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = await response.parse()
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_dangerous(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.delete_dangerous(
            droplet_id=3164444,
            x_dangerous=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = await response.parse()
            assert destroy_with_associated_resource is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_selective(self, async_client: AsyncGradient) -> None:
        destroy_with_associated_resource = (
            await async_client.gpu_droplets.destroy_with_associated_resources.delete_selective(
                droplet_id=3164444,
            )
        )
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_selective_with_all_params(self, async_client: AsyncGradient) -> None:
        destroy_with_associated_resource = (
            await async_client.gpu_droplets.destroy_with_associated_resources.delete_selective(
                droplet_id=3164444,
                floating_ips=["6186916"],
                reserved_ips=["6186916"],
                snapshots=["61486916"],
                volume_snapshots=["edb0478d-7436-11ea-86e6-0a58ac144b91"],
                volumes=["ba49449a-7435-11ea-b89e-0a58ac14480f"],
            )
        )
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_selective(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.destroy_with_associated_resources.with_raw_response.delete_selective(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = await response.parse()
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_selective(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.delete_selective(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = await response.parse()
            assert destroy_with_associated_resource is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncGradient) -> None:
        destroy_with_associated_resource = await async_client.gpu_droplets.destroy_with_associated_resources.retry(
            3164444,
        )
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.destroy_with_associated_resources.with_raw_response.retry(
            3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destroy_with_associated_resource = await response.parse()
        assert destroy_with_associated_resource is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.destroy_with_associated_resources.with_streaming_response.retry(
            3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destroy_with_associated_resource = await response.parse()
            assert destroy_with_associated_resource is None

        assert cast(Any, response.is_closed) is True
