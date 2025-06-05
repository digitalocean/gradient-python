# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.genai.models import (
    APIKeyListResponse,
    APIKeyCreateResponse,
    APIKeyDeleteResponse,
    APIKeyUpdateResponse,
    APIKeyUpdateRegenerateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.genai.models.api_keys.create()
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.genai.models.api_keys.create(
            name="name",
        )
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.models.api_keys.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.models.api_keys.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.genai.models.api_keys.update(
            path_api_key_uuid="api_key_uuid",
        )
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.genai.models.api_keys.update(
            path_api_key_uuid="api_key_uuid",
            body_api_key_uuid="api_key_uuid",
            name="name",
        )
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.models.api_keys.with_raw_response.update(
            path_api_key_uuid="api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.models.api_keys.with_streaming_response.update(
            path_api_key_uuid="api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_api_key_uuid` but received ''"):
            client.genai.models.api_keys.with_raw_response.update(
                path_api_key_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.genai.models.api_keys.list()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.genai.models.api_keys.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.models.api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.models.api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.genai.models.api_keys.delete(
            "api_key_uuid",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.models.api_keys.with_raw_response.delete(
            "api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.models.api_keys.with_streaming_response.delete(
            "api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            client.genai.models.api_keys.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_regenerate(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.genai.models.api_keys.update_regenerate(
            "api_key_uuid",
        )
        assert_matches_type(APIKeyUpdateRegenerateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_regenerate(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.models.api_keys.with_raw_response.update_regenerate(
            "api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyUpdateRegenerateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_regenerate(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.models.api_keys.with_streaming_response.update_regenerate(
            "api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyUpdateRegenerateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_regenerate(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            client.genai.models.api_keys.with_raw_response.update_regenerate(
                "",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.genai.models.api_keys.create()
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.genai.models.api_keys.create(
            name="name",
        )
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.models.api_keys.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.models.api_keys.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyCreateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.genai.models.api_keys.update(
            path_api_key_uuid="api_key_uuid",
        )
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.genai.models.api_keys.update(
            path_api_key_uuid="api_key_uuid",
            body_api_key_uuid="api_key_uuid",
            name="name",
        )
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.models.api_keys.with_raw_response.update(
            path_api_key_uuid="api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.models.api_keys.with_streaming_response.update(
            path_api_key_uuid="api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_api_key_uuid` but received ''"):
            await async_client.genai.models.api_keys.with_raw_response.update(
                path_api_key_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.genai.models.api_keys.list()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.genai.models.api_keys.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.models.api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.models.api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.genai.models.api_keys.delete(
            "api_key_uuid",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.models.api_keys.with_raw_response.delete(
            "api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.models.api_keys.with_streaming_response.delete(
            "api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            await async_client.genai.models.api_keys.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_regenerate(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.genai.models.api_keys.update_regenerate(
            "api_key_uuid",
        )
        assert_matches_type(APIKeyUpdateRegenerateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_regenerate(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.models.api_keys.with_raw_response.update_regenerate(
            "api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyUpdateRegenerateResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_regenerate(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.models.api_keys.with_streaming_response.update_regenerate(
            "api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyUpdateRegenerateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_regenerate(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            await async_client.genai.models.api_keys.with_raw_response.update_regenerate(
                "",
            )
