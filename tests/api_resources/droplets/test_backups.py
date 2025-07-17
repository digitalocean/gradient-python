# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from do_gradientai import GradientAI, AsyncGradientAI
from do_gradientai.types.droplets import (
    BackupListResponse,
    BackupListPoliciesResponse,
    BackupRetrievePolicyResponse,
    BackupListSupportedPoliciesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBackups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: GradientAI) -> None:
        backup = client.droplets.backups.list(
            droplet_id=3164444,
        )
        assert_matches_type(BackupListResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: GradientAI) -> None:
        backup = client.droplets.backups.list(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(BackupListResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: GradientAI) -> None:
        response = client.droplets.backups.with_raw_response.list(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(BackupListResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: GradientAI) -> None:
        with client.droplets.backups.with_streaming_response.list(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(BackupListResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_policies(self, client: GradientAI) -> None:
        backup = client.droplets.backups.list_policies()
        assert_matches_type(BackupListPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_policies_with_all_params(self, client: GradientAI) -> None:
        backup = client.droplets.backups.list_policies(
            page=1,
            per_page=1,
        )
        assert_matches_type(BackupListPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_policies(self, client: GradientAI) -> None:
        response = client.droplets.backups.with_raw_response.list_policies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(BackupListPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_policies(self, client: GradientAI) -> None:
        with client.droplets.backups.with_streaming_response.list_policies() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(BackupListPoliciesResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_supported_policies(self, client: GradientAI) -> None:
        backup = client.droplets.backups.list_supported_policies()
        assert_matches_type(BackupListSupportedPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_supported_policies(self, client: GradientAI) -> None:
        response = client.droplets.backups.with_raw_response.list_supported_policies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(BackupListSupportedPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_supported_policies(self, client: GradientAI) -> None:
        with client.droplets.backups.with_streaming_response.list_supported_policies() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(BackupListSupportedPoliciesResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_policy(self, client: GradientAI) -> None:
        backup = client.droplets.backups.retrieve_policy(
            1,
        )
        assert_matches_type(BackupRetrievePolicyResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_policy(self, client: GradientAI) -> None:
        response = client.droplets.backups.with_raw_response.retrieve_policy(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(BackupRetrievePolicyResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_policy(self, client: GradientAI) -> None:
        with client.droplets.backups.with_streaming_response.retrieve_policy(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(BackupRetrievePolicyResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBackups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGradientAI) -> None:
        backup = await async_client.droplets.backups.list(
            droplet_id=3164444,
        )
        assert_matches_type(BackupListResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradientAI) -> None:
        backup = await async_client.droplets.backups.list(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(BackupListResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.droplets.backups.with_raw_response.list(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(BackupListResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradientAI) -> None:
        async with async_client.droplets.backups.with_streaming_response.list(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(BackupListResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_policies(self, async_client: AsyncGradientAI) -> None:
        backup = await async_client.droplets.backups.list_policies()
        assert_matches_type(BackupListPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_policies_with_all_params(self, async_client: AsyncGradientAI) -> None:
        backup = await async_client.droplets.backups.list_policies(
            page=1,
            per_page=1,
        )
        assert_matches_type(BackupListPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_policies(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.droplets.backups.with_raw_response.list_policies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(BackupListPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_policies(self, async_client: AsyncGradientAI) -> None:
        async with async_client.droplets.backups.with_streaming_response.list_policies() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(BackupListPoliciesResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_supported_policies(self, async_client: AsyncGradientAI) -> None:
        backup = await async_client.droplets.backups.list_supported_policies()
        assert_matches_type(BackupListSupportedPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_supported_policies(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.droplets.backups.with_raw_response.list_supported_policies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(BackupListSupportedPoliciesResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_supported_policies(self, async_client: AsyncGradientAI) -> None:
        async with async_client.droplets.backups.with_streaming_response.list_supported_policies() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(BackupListSupportedPoliciesResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_policy(self, async_client: AsyncGradientAI) -> None:
        backup = await async_client.droplets.backups.retrieve_policy(
            1,
        )
        assert_matches_type(BackupRetrievePolicyResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_policy(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.droplets.backups.with_raw_response.retrieve_policy(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(BackupRetrievePolicyResponse, backup, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_policy(self, async_client: AsyncGradientAI) -> None:
        async with async_client.droplets.backups.with_streaming_response.retrieve_policy(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(BackupRetrievePolicyResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True
