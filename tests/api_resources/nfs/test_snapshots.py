# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.nfs import (
    SnapshotListResponse,
    SnapshotRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        snapshot = client.nfs.snapshots.retrieve(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )
        assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.nfs.snapshots.with_raw_response.retrieve(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.nfs.snapshots.with_streaming_response.retrieve(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_snapshot_id` but received ''"):
            client.nfs.snapshots.with_raw_response.retrieve(
                nfs_snapshot_id="",
                region="region",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        snapshot = client.nfs.snapshots.list(
            region="region",
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        snapshot = client.nfs.snapshots.list(
            region="region",
            share_id="share_id",
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.nfs.snapshots.with_raw_response.list(
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.nfs.snapshots.with_streaming_response.list(
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        snapshot = client.nfs.snapshots.delete(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )
        assert snapshot is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.nfs.snapshots.with_raw_response.delete(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert snapshot is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.nfs.snapshots.with_streaming_response.delete(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert snapshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_snapshot_id` but received ''"):
            client.nfs.snapshots.with_raw_response.delete(
                nfs_snapshot_id="",
                region="region",
            )


class TestAsyncSnapshots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        snapshot = await async_client.nfs.snapshots.retrieve(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )
        assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.snapshots.with_raw_response.retrieve(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.snapshots.with_streaming_response.retrieve(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotRetrieveResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_snapshot_id` but received ''"):
            await async_client.nfs.snapshots.with_raw_response.retrieve(
                nfs_snapshot_id="",
                region="region",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        snapshot = await async_client.nfs.snapshots.list(
            region="region",
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        snapshot = await async_client.nfs.snapshots.list(
            region="region",
            share_id="share_id",
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.snapshots.with_raw_response.list(
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.snapshots.with_streaming_response.list(
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        snapshot = await async_client.nfs.snapshots.delete(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )
        assert snapshot is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.snapshots.with_raw_response.delete(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert snapshot is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.snapshots.with_streaming_response.delete(
            nfs_snapshot_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert snapshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_snapshot_id` but received ''"):
            await async_client.nfs.snapshots.with_raw_response.delete(
                nfs_snapshot_id="",
                region="region",
            )
