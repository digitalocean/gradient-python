# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.fine_tuning.checkpoints import (
    PermissionDeleteResponse,
    ListFineTuningCheckpointPermission,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPermissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DigitaloceanGenaiSDK) -> None:
        permission = client.fine_tuning.checkpoints.permissions.create(
            permission_id="ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
            project_ids=["string"],
        )
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.fine_tuning.checkpoints.permissions.with_raw_response.create(
            permission_id="ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
            project_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        with client.fine_tuning.checkpoints.permissions.with_streaming_response.create(
            permission_id="ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
            project_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            client.fine_tuning.checkpoints.permissions.with_raw_response.create(
                permission_id="",
                project_ids=["string"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        permission = client.fine_tuning.checkpoints.permissions.retrieve(
            permission_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        permission = client.fine_tuning.checkpoints.permissions.retrieve(
            permission_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
            after="after",
            limit=0,
            order="ascending",
            project_id="project_id",
        )
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.fine_tuning.checkpoints.permissions.with_raw_response.retrieve(
            permission_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with client.fine_tuning.checkpoints.permissions.with_streaming_response.retrieve(
            permission_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            client.fine_tuning.checkpoints.permissions.with_raw_response.retrieve(
                permission_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DigitaloceanGenaiSDK) -> None:
        permission = client.fine_tuning.checkpoints.permissions.delete(
            "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
        )
        assert_matches_type(PermissionDeleteResponse, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.fine_tuning.checkpoints.permissions.with_raw_response.delete(
            "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionDeleteResponse, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with client.fine_tuning.checkpoints.permissions.with_streaming_response.delete(
            "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionDeleteResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            client.fine_tuning.checkpoints.permissions.with_raw_response.delete(
                "",
            )


class TestAsyncPermissions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        permission = await async_client.fine_tuning.checkpoints.permissions.create(
            permission_id="ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
            project_ids=["string"],
        )
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.fine_tuning.checkpoints.permissions.with_raw_response.create(
            permission_id="ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
            project_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.fine_tuning.checkpoints.permissions.with_streaming_response.create(
            permission_id="ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
            project_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            await async_client.fine_tuning.checkpoints.permissions.with_raw_response.create(
                permission_id="",
                project_ids=["string"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        permission = await async_client.fine_tuning.checkpoints.permissions.retrieve(
            permission_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        permission = await async_client.fine_tuning.checkpoints.permissions.retrieve(
            permission_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
            after="after",
            limit=0,
            order="ascending",
            project_id="project_id",
        )
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.fine_tuning.checkpoints.permissions.with_raw_response.retrieve(
            permission_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.fine_tuning.checkpoints.permissions.with_streaming_response.retrieve(
            permission_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(ListFineTuningCheckpointPermission, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            await async_client.fine_tuning.checkpoints.permissions.with_raw_response.retrieve(
                permission_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        permission = await async_client.fine_tuning.checkpoints.permissions.delete(
            "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
        )
        assert_matches_type(PermissionDeleteResponse, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.fine_tuning.checkpoints.permissions.with_raw_response.delete(
            "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionDeleteResponse, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.fine_tuning.checkpoints.permissions.with_streaming_response.delete(
            "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionDeleteResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            await async_client.fine_tuning.checkpoints.permissions.with_raw_response.delete(
                "",
            )
