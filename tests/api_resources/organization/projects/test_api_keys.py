# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.organization.projects import (
    APIKey,
    APIKeyListResponse,
    APIKeyDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.organization.projects.api_keys.retrieve(
            key_id="key_id",
            project_id="project_id",
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.projects.api_keys.with_raw_response.retrieve(
            key_id="key_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.projects.api_keys.with_streaming_response.retrieve(
            key_id="key_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.api_keys.with_raw_response.retrieve(
                key_id="key_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.organization.projects.api_keys.with_raw_response.retrieve(
                key_id="",
                project_id="project_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.organization.projects.api_keys.list(
            project_id="project_id",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.organization.projects.api_keys.list(
            project_id="project_id",
            after="after",
            limit=0,
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.projects.api_keys.with_raw_response.list(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.projects.api_keys.with_streaming_response.list(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.api_keys.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DigitaloceanGenaiSDK) -> None:
        api_key = client.organization.projects.api_keys.delete(
            key_id="key_id",
            project_id="project_id",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.projects.api_keys.with_raw_response.delete(
            key_id="key_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.projects.api_keys.with_streaming_response.delete(
            key_id="key_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.api_keys.with_raw_response.delete(
                key_id="key_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.organization.projects.api_keys.with_raw_response.delete(
                key_id="",
                project_id="project_id",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.organization.projects.api_keys.retrieve(
            key_id="key_id",
            project_id="project_id",
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.projects.api_keys.with_raw_response.retrieve(
            key_id="key_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.projects.api_keys.with_streaming_response.retrieve(
            key_id="key_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.api_keys.with_raw_response.retrieve(
                key_id="key_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.organization.projects.api_keys.with_raw_response.retrieve(
                key_id="",
                project_id="project_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.organization.projects.api_keys.list(
            project_id="project_id",
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.organization.projects.api_keys.list(
            project_id="project_id",
            after="after",
            limit=0,
        )
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.projects.api_keys.with_raw_response.list(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.projects.api_keys.with_streaming_response.list(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.api_keys.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        api_key = await async_client.organization.projects.api_keys.delete(
            key_id="key_id",
            project_id="project_id",
        )
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.projects.api_keys.with_raw_response.delete(
            key_id="key_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.projects.api_keys.with_streaming_response.delete(
            key_id="key_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.api_keys.with_raw_response.delete(
                key_id="key_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.organization.projects.api_keys.with_raw_response.delete(
                key_id="",
                project_id="project_id",
            )
