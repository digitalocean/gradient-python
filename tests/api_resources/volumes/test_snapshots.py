# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradientai import GradientAI, AsyncGradientAI
from tests.utils import assert_matches_type
from gradientai.types.volumes import (
    SnapshotListResponse,
    SnapshotCreateResponse,
    SnapshotRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: GradientAI) -> None:
        snapshot = client.volumes.snapshots.create(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            name="big-data-snapshot1475261774",
        )
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: GradientAI) -> None:
        snapshot = client.volumes.snapshots.create(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            name="big-data-snapshot1475261774",
            tags=["base-image", "prod"],
        )
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: GradientAI) -> None:
        response = client.volumes.snapshots.with_raw_response.create(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            name="big-data-snapshot1475261774",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: GradientAI) -> None:
        with client.volumes.snapshots.with_streaming_response.create(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            name="big-data-snapshot1475261774",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.volumes.snapshots.with_raw_response.create(
                volume_id="",
                name="big-data-snapshot1475261774",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: GradientAI) -> None:
        snapshot = client.volumes.snapshots.retrieve(
            "snapshot_id",
        )
        assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: GradientAI) -> None:
        response = client.volumes.snapshots.with_raw_response.retrieve(
            "snapshot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: GradientAI) -> None:
        with client.volumes.snapshots.with_streaming_response.retrieve(
            "snapshot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            client.volumes.snapshots.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: GradientAI) -> None:
        snapshot = client.volumes.snapshots.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: GradientAI) -> None:
        snapshot = client.volumes.snapshots.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            page=1,
            per_page=1,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: GradientAI) -> None:
        response = client.volumes.snapshots.with_raw_response.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: GradientAI) -> None:
        with client.volumes.snapshots.with_streaming_response.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.volumes.snapshots.with_raw_response.list(
                volume_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: GradientAI) -> None:
        snapshot = client.volumes.snapshots.delete(
            "snapshot_id",
        )
        assert snapshot is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: GradientAI) -> None:
        response = client.volumes.snapshots.with_raw_response.delete(
            "snapshot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert snapshot is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: GradientAI) -> None:
        with client.volumes.snapshots.with_streaming_response.delete(
            "snapshot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert snapshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            client.volumes.snapshots.with_raw_response.delete(
                "",
            )


class TestAsyncSnapshots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGradientAI) -> None:
        snapshot = await async_client.volumes.snapshots.create(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            name="big-data-snapshot1475261774",
        )
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradientAI) -> None:
        snapshot = await async_client.volumes.snapshots.create(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            name="big-data-snapshot1475261774",
            tags=["base-image", "prod"],
        )
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.volumes.snapshots.with_raw_response.create(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            name="big-data-snapshot1475261774",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradientAI) -> None:
        async with async_client.volumes.snapshots.with_streaming_response.create(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            name="big-data-snapshot1475261774",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.volumes.snapshots.with_raw_response.create(
                volume_id="",
                name="big-data-snapshot1475261774",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradientAI) -> None:
        snapshot = await async_client.volumes.snapshots.retrieve(
            "snapshot_id",
        )
        assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.volumes.snapshots.with_raw_response.retrieve(
            "snapshot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradientAI) -> None:
        async with async_client.volumes.snapshots.with_streaming_response.retrieve(
            "snapshot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            await async_client.volumes.snapshots.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGradientAI) -> None:
        snapshot = await async_client.volumes.snapshots.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradientAI) -> None:
        snapshot = await async_client.volumes.snapshots.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            page=1,
            per_page=1,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.volumes.snapshots.with_raw_response.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradientAI) -> None:
        async with async_client.volumes.snapshots.with_streaming_response.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.volumes.snapshots.with_raw_response.list(
                volume_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradientAI) -> None:
        snapshot = await async_client.volumes.snapshots.delete(
            "snapshot_id",
        )
        assert snapshot is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.volumes.snapshots.with_raw_response.delete(
            "snapshot_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert snapshot is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradientAI) -> None:
        async with async_client.volumes.snapshots.with_streaming_response.delete(
            "snapshot_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert snapshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            await async_client.volumes.snapshots.with_raw_response.delete(
                "",
            )
