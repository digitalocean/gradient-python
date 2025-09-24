# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.models.providers import (
    OpenAIListResponse,
    OpenAICreateResponse,
    OpenAIDeleteResponse,
    OpenAIUpdateResponse,
    OpenAIRetrieveResponse,
    OpenAIRetrieveAgentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpenAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        openai = client.models.providers.openai.create()
        assert_matches_type(OpenAICreateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        openai = client.models.providers.openai.create(
            api_key='"sk-proj--123456789098765432123456789"',
            name='"Production Key"',
        )
        assert_matches_type(OpenAICreateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.models.providers.openai.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAICreateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.models.providers.openai.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAICreateResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        openai = client.models.providers.openai.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(OpenAIRetrieveResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.models.providers.openai.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAIRetrieveResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.models.providers.openai.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAIRetrieveResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            client.models.providers.openai.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        openai = client.models.providers.openai.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(OpenAIUpdateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        openai = client.models.providers.openai.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            api_key='"sk-ant-12345678901234567890123456789012"',
            body_api_key_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"Production Key"',
        )
        assert_matches_type(OpenAIUpdateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.models.providers.openai.with_raw_response.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAIUpdateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.models.providers.openai.with_streaming_response.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAIUpdateResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_api_key_uuid` but received ''"):
            client.models.providers.openai.with_raw_response.update(
                path_api_key_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        openai = client.models.providers.openai.list()
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        openai = client.models.providers.openai.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.models.providers.openai.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.models.providers.openai.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAIListResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        openai = client.models.providers.openai.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(OpenAIDeleteResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.models.providers.openai.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAIDeleteResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.models.providers.openai.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAIDeleteResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            client.models.providers.openai.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_agents(self, client: Gradient) -> None:
        openai = client.models.providers.openai.retrieve_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(OpenAIRetrieveAgentsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_agents_with_all_params(self, client: Gradient) -> None:
        openai = client.models.providers.openai.retrieve_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
            page=0,
            per_page=0,
        )
        assert_matches_type(OpenAIRetrieveAgentsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_agents(self, client: Gradient) -> None:
        response = client.models.providers.openai.with_raw_response.retrieve_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAIRetrieveAgentsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_agents(self, client: Gradient) -> None:
        with client.models.providers.openai.with_streaming_response.retrieve_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAIRetrieveAgentsResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_agents(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.models.providers.openai.with_raw_response.retrieve_agents(
                uuid="",
            )


class TestAsyncOpenAI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.create()
        assert_matches_type(OpenAICreateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.create(
            api_key='"sk-proj--123456789098765432123456789"',
            name='"Production Key"',
        )
        assert_matches_type(OpenAICreateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.models.providers.openai.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAICreateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.models.providers.openai.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAICreateResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(OpenAIRetrieveResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.models.providers.openai.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAIRetrieveResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.models.providers.openai.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAIRetrieveResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            await async_client.models.providers.openai.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(OpenAIUpdateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            api_key='"sk-ant-12345678901234567890123456789012"',
            body_api_key_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"Production Key"',
        )
        assert_matches_type(OpenAIUpdateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.models.providers.openai.with_raw_response.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAIUpdateResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.models.providers.openai.with_streaming_response.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAIUpdateResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_api_key_uuid` but received ''"):
            await async_client.models.providers.openai.with_raw_response.update(
                path_api_key_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.list()
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.models.providers.openai.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAIListResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.models.providers.openai.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAIListResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(OpenAIDeleteResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.models.providers.openai.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAIDeleteResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.models.providers.openai.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAIDeleteResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            await async_client.models.providers.openai.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_agents(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.retrieve_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(OpenAIRetrieveAgentsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_agents_with_all_params(self, async_client: AsyncGradient) -> None:
        openai = await async_client.models.providers.openai.retrieve_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
            page=0,
            per_page=0,
        )
        assert_matches_type(OpenAIRetrieveAgentsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_agents(self, async_client: AsyncGradient) -> None:
        response = await async_client.models.providers.openai.with_raw_response.retrieve_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAIRetrieveAgentsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_agents(self, async_client: AsyncGradient) -> None:
        async with async_client.models.providers.openai.with_streaming_response.retrieve_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAIRetrieveAgentsResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_agents(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.models.providers.openai.with_raw_response.retrieve_agents(
                uuid="",
            )
