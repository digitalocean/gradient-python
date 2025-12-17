# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types import (
    NfListResponse,
    NfCreateResponse,
    NfRetrieveResponse,
    NfInitiateActionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNfs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        nf = client.nfs.create(
            name="sammy-share-drive",
            region="atl1",
            size_gib=1024,
            vpc_ids=["796c6fe3-2a1d-4da2-9f3e-38239827dc91"],
        )
        assert_matches_type(NfCreateResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.nfs.with_raw_response.create(
            name="sammy-share-drive",
            region="atl1",
            size_gib=1024,
            vpc_ids=["796c6fe3-2a1d-4da2-9f3e-38239827dc91"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = response.parse()
        assert_matches_type(NfCreateResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.nfs.with_streaming_response.create(
            name="sammy-share-drive",
            region="atl1",
            size_gib=1024,
            vpc_ids=["796c6fe3-2a1d-4da2-9f3e-38239827dc91"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = response.parse()
            assert_matches_type(NfCreateResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        nf = client.nfs.retrieve(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )
        assert_matches_type(NfRetrieveResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.nfs.with_raw_response.retrieve(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = response.parse()
        assert_matches_type(NfRetrieveResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.nfs.with_streaming_response.retrieve(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = response.parse()
            assert_matches_type(NfRetrieveResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            client.nfs.with_raw_response.retrieve(
                nfs_id="",
                region="region",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        nf = client.nfs.list(
            region="region",
        )
        assert_matches_type(NfListResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.nfs.with_raw_response.list(
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = response.parse()
        assert_matches_type(NfListResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.nfs.with_streaming_response.list(
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = response.parse()
            assert_matches_type(NfListResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        nf = client.nfs.delete(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )
        assert nf is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.nfs.with_raw_response.delete(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = response.parse()
        assert nf is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.nfs.with_streaming_response.delete(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = response.parse()
            assert nf is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            client.nfs.with_raw_response.delete(
                nfs_id="",
                region="region",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_action_overload_1(self, client: Gradient) -> None:
        nf = client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_action_with_all_params_overload_1(self, client: Gradient) -> None:
        nf = client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
            params={"size_gib": 2048},
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_action_overload_1(self, client: Gradient) -> None:
        response = client.nfs.with_raw_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = response.parse()
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_action_overload_1(self, client: Gradient) -> None:
        with client.nfs.with_streaming_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = response.parse()
            assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_action_overload_1(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            client.nfs.with_raw_response.initiate_action(
                nfs_id="",
                region="atl1",
                type="resize",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_action_overload_2(self, client: Gradient) -> None:
        nf = client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_action_with_all_params_overload_2(self, client: Gradient) -> None:
        nf = client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
            params={"name": "daily-backup"},
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_action_overload_2(self, client: Gradient) -> None:
        response = client.nfs.with_raw_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = response.parse()
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_action_overload_2(self, client: Gradient) -> None:
        with client.nfs.with_streaming_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = response.parse()
            assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_action_overload_2(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            client.nfs.with_raw_response.initiate_action(
                nfs_id="",
                region="atl1",
                type="resize",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_action_overload_3(self, client: Gradient) -> None:
        nf = client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_action_with_all_params_overload_3(self, client: Gradient) -> None:
        nf = client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
            params={"vpc_id": "vpc-id-123"},
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_action_overload_3(self, client: Gradient) -> None:
        response = client.nfs.with_raw_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = response.parse()
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_action_overload_3(self, client: Gradient) -> None:
        with client.nfs.with_streaming_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = response.parse()
            assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_action_overload_3(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            client.nfs.with_raw_response.initiate_action(
                nfs_id="",
                region="atl1",
                type="resize",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_action_overload_4(self, client: Gradient) -> None:
        nf = client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_action_with_all_params_overload_4(self, client: Gradient) -> None:
        nf = client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
            params={"vpc_id": "vpc-id-123"},
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_action_overload_4(self, client: Gradient) -> None:
        response = client.nfs.with_raw_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = response.parse()
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_action_overload_4(self, client: Gradient) -> None:
        with client.nfs.with_streaming_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = response.parse()
            assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_action_overload_4(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            client.nfs.with_raw_response.initiate_action(
                nfs_id="",
                region="atl1",
                type="resize",
            )


class TestAsyncNfs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.create(
            name="sammy-share-drive",
            region="atl1",
            size_gib=1024,
            vpc_ids=["796c6fe3-2a1d-4da2-9f3e-38239827dc91"],
        )
        assert_matches_type(NfCreateResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.with_raw_response.create(
            name="sammy-share-drive",
            region="atl1",
            size_gib=1024,
            vpc_ids=["796c6fe3-2a1d-4da2-9f3e-38239827dc91"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = await response.parse()
        assert_matches_type(NfCreateResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.with_streaming_response.create(
            name="sammy-share-drive",
            region="atl1",
            size_gib=1024,
            vpc_ids=["796c6fe3-2a1d-4da2-9f3e-38239827dc91"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = await response.parse()
            assert_matches_type(NfCreateResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.retrieve(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )
        assert_matches_type(NfRetrieveResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.with_raw_response.retrieve(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = await response.parse()
        assert_matches_type(NfRetrieveResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.with_streaming_response.retrieve(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = await response.parse()
            assert_matches_type(NfRetrieveResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            await async_client.nfs.with_raw_response.retrieve(
                nfs_id="",
                region="region",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.list(
            region="region",
        )
        assert_matches_type(NfListResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.with_raw_response.list(
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = await response.parse()
        assert_matches_type(NfListResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.with_streaming_response.list(
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = await response.parse()
            assert_matches_type(NfListResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.delete(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )
        assert nf is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.with_raw_response.delete(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = await response.parse()
        assert nf is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.with_streaming_response.delete(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = await response.parse()
            assert nf is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            await async_client.nfs.with_raw_response.delete(
                nfs_id="",
                region="region",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_action_overload_1(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_action_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
            params={"size_gib": 2048},
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_action_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.with_raw_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = await response.parse()
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_action_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.with_streaming_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = await response.parse()
            assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_action_overload_1(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            await async_client.nfs.with_raw_response.initiate_action(
                nfs_id="",
                region="atl1",
                type="resize",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_action_overload_2(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_action_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
            params={"name": "daily-backup"},
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_action_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.with_raw_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = await response.parse()
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_action_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.with_streaming_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = await response.parse()
            assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_action_overload_2(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            await async_client.nfs.with_raw_response.initiate_action(
                nfs_id="",
                region="atl1",
                type="resize",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_action_overload_3(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_action_with_all_params_overload_3(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
            params={"vpc_id": "vpc-id-123"},
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_action_overload_3(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.with_raw_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = await response.parse()
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_action_overload_3(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.with_streaming_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = await response.parse()
            assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_action_overload_3(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            await async_client.nfs.with_raw_response.initiate_action(
                nfs_id="",
                region="atl1",
                type="resize",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_action_overload_4(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_action_with_all_params_overload_4(self, async_client: AsyncGradient) -> None:
        nf = await async_client.nfs.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
            params={"vpc_id": "vpc-id-123"},
        )
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_action_overload_4(self, async_client: AsyncGradient) -> None:
        response = await async_client.nfs.with_raw_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nf = await response.parse()
        assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_action_overload_4(self, async_client: AsyncGradient) -> None:
        async with async_client.nfs.with_streaming_response.initiate_action(
            nfs_id="0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
            region="atl1",
            type="resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nf = await response.parse()
            assert_matches_type(NfInitiateActionResponse, nf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_action_overload_4(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nfs_id` but received ''"):
            await async_client.nfs.with_raw_response.initiate_action(
                nfs_id="",
                region="atl1",
                type="resize",
            )
