# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.organization import (
    AdminAPIKey,
    AdminAPIKeyListResponse,
    AdminAPIKeyDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdminAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DigitaloceanGenaiSDK) -> None:
        admin_api_key = client.organization.admin_api_keys.create(
            name="New Admin Key",
        )
        assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.admin_api_keys.with_raw_response.create(
            name="New Admin Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_api_key = response.parse()
        assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.admin_api_keys.with_streaming_response.create(
            name="New Admin Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_api_key = response.parse()
            assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        admin_api_key = client.organization.admin_api_keys.retrieve(
            "key_id",
        )
        assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.admin_api_keys.with_raw_response.retrieve(
            "key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_api_key = response.parse()
        assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.admin_api_keys.with_streaming_response.retrieve(
            "key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_api_key = response.parse()
            assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.organization.admin_api_keys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DigitaloceanGenaiSDK) -> None:
        admin_api_key = client.organization.admin_api_keys.list()
        assert_matches_type(AdminAPIKeyListResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        admin_api_key = client.organization.admin_api_keys.list(
            after="after",
            limit=0,
            order="asc",
        )
        assert_matches_type(AdminAPIKeyListResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.admin_api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_api_key = response.parse()
        assert_matches_type(AdminAPIKeyListResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.admin_api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_api_key = response.parse()
            assert_matches_type(AdminAPIKeyListResponse, admin_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DigitaloceanGenaiSDK) -> None:
        admin_api_key = client.organization.admin_api_keys.delete(
            "key_id",
        )
        assert_matches_type(AdminAPIKeyDeleteResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.admin_api_keys.with_raw_response.delete(
            "key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_api_key = response.parse()
        assert_matches_type(AdminAPIKeyDeleteResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.admin_api_keys.with_streaming_response.delete(
            "key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_api_key = response.parse()
            assert_matches_type(AdminAPIKeyDeleteResponse, admin_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.organization.admin_api_keys.with_raw_response.delete(
                "",
            )


class TestAsyncAdminAPIKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        admin_api_key = await async_client.organization.admin_api_keys.create(
            name="New Admin Key",
        )
        assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.admin_api_keys.with_raw_response.create(
            name="New Admin Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_api_key = await response.parse()
        assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.admin_api_keys.with_streaming_response.create(
            name="New Admin Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_api_key = await response.parse()
            assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        admin_api_key = await async_client.organization.admin_api_keys.retrieve(
            "key_id",
        )
        assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.admin_api_keys.with_raw_response.retrieve(
            "key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_api_key = await response.parse()
        assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.admin_api_keys.with_streaming_response.retrieve(
            "key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_api_key = await response.parse()
            assert_matches_type(AdminAPIKey, admin_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.organization.admin_api_keys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        admin_api_key = await async_client.organization.admin_api_keys.list()
        assert_matches_type(AdminAPIKeyListResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        admin_api_key = await async_client.organization.admin_api_keys.list(
            after="after",
            limit=0,
            order="asc",
        )
        assert_matches_type(AdminAPIKeyListResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.admin_api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_api_key = await response.parse()
        assert_matches_type(AdminAPIKeyListResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.admin_api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_api_key = await response.parse()
            assert_matches_type(AdminAPIKeyListResponse, admin_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        admin_api_key = await async_client.organization.admin_api_keys.delete(
            "key_id",
        )
        assert_matches_type(AdminAPIKeyDeleteResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.admin_api_keys.with_raw_response.delete(
            "key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_api_key = await response.parse()
        assert_matches_type(AdminAPIKeyDeleteResponse, admin_api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.admin_api_keys.with_streaming_response.delete(
            "key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_api_key = await response.parse()
            assert_matches_type(AdminAPIKeyDeleteResponse, admin_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.organization.admin_api_keys.with_raw_response.delete(
                "",
            )
