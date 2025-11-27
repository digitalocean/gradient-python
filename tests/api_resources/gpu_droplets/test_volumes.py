# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets import (
    VolumeListResponse,
    VolumeCreateResponse,
    VolumeRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolumes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
            description="Block store for examples",
            filesystem_label="example",
            filesystem_type="ext4",
            snapshot_id="b0798135-fb76-11eb-946a-0a58ac146f33",
            tags=["base-image", "prod"],
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.with_raw_response.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.with_streaming_response.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeCreateResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
            description="Block store for examples",
            filesystem_label="example",
            filesystem_type="ext4",
            snapshot_id="b0798135-fb76-11eb-946a-0a58ac146f33",
            tags=["base-image", "prod"],
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.with_raw_response.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.with_streaming_response.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeCreateResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.retrieve(
            "7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert_matches_type(VolumeRetrieveResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.with_raw_response.retrieve(
            "7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeRetrieveResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.with_streaming_response.retrieve(
            "7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeRetrieveResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.gpu_droplets.volumes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.list()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.list(
            name="name",
            page=1,
            per_page=1,
            region="nyc3",
        )
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(VolumeListResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.delete(
            "7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.with_raw_response.delete(
            "7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.with_streaming_response.delete(
            "7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.gpu_droplets.volumes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_by_name(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.delete_by_name()
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_by_name_with_all_params(self, client: Gradient) -> None:
        volume = client.gpu_droplets.volumes.delete_by_name(
            name="name",
            region="nyc3",
        )
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_by_name(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.with_raw_response.delete_by_name()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_name(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.with_streaming_response.delete_by_name() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True


class TestAsyncVolumes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
            description="Block store for examples",
            filesystem_label="example",
            filesystem_type="ext4",
            snapshot_id="b0798135-fb76-11eb-946a-0a58ac146f33",
            tags=["base-image", "prod"],
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.with_raw_response.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.with_streaming_response.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeCreateResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
            description="Block store for examples",
            filesystem_label="example",
            filesystem_type="ext4",
            snapshot_id="b0798135-fb76-11eb-946a-0a58ac146f33",
            tags=["base-image", "prod"],
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.with_raw_response.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.with_streaming_response.create(
            name="example",
            region="nyc3",
            size_gigabytes=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeCreateResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.retrieve(
            "7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert_matches_type(VolumeRetrieveResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.with_raw_response.retrieve(
            "7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeRetrieveResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.with_streaming_response.retrieve(
            "7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeRetrieveResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.gpu_droplets.volumes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.list()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.list(
            name="name",
            page=1,
            per_page=1,
            region="nyc3",
        )
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(VolumeListResponse, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.delete(
            "7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.with_raw_response.delete(
            "7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.with_streaming_response.delete(
            "7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.gpu_droplets.volumes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_by_name(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.delete_by_name()
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_by_name_with_all_params(self, async_client: AsyncGradient) -> None:
        volume = await async_client.gpu_droplets.volumes.delete_by_name(
            name="name",
            region="nyc3",
        )
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_name(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.with_raw_response.delete_by_name()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert volume is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_name(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.with_streaming_response.delete_by_name() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True
