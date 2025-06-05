# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.genai.agents import (
    FunctionCreateResponse,
    FunctionDeleteResponse,
    FunctionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DigitaloceanGenaiSDK) -> None:
        function = client.genai.agents.functions.create(
            path_agent_uuid="agent_uuid",
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        function = client.genai.agents.functions.create(
            path_agent_uuid="agent_uuid",
            body_agent_uuid="agent_uuid",
            description="description",
            faas_name="faas_name",
            faas_namespace="faas_namespace",
            function_name="function_name",
            input_schema={},
            output_schema={},
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.agents.functions.with_raw_response.create(
            path_agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.agents.functions.with_streaming_response.create(
            path_agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionCreateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            client.genai.agents.functions.with_raw_response.create(
                path_agent_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: DigitaloceanGenaiSDK) -> None:
        function = client.genai.agents.functions.update(
            path_function_uuid="function_uuid",
            path_agent_uuid="agent_uuid",
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        function = client.genai.agents.functions.update(
            path_function_uuid="function_uuid",
            path_agent_uuid="agent_uuid",
            body_agent_uuid="agent_uuid",
            description="description",
            faas_name="faas_name",
            faas_namespace="faas_namespace",
            function_name="function_name",
            body_function_uuid="function_uuid",
            input_schema={},
            output_schema={},
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.agents.functions.with_raw_response.update(
            path_function_uuid="function_uuid",
            path_agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.agents.functions.with_streaming_response.update(
            path_function_uuid="function_uuid",
            path_agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionUpdateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            client.genai.agents.functions.with_raw_response.update(
                path_function_uuid="function_uuid",
                path_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_uuid` but received ''"):
            client.genai.agents.functions.with_raw_response.update(
                path_function_uuid="",
                path_agent_uuid="agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DigitaloceanGenaiSDK) -> None:
        function = client.genai.agents.functions.delete(
            function_uuid="function_uuid",
            agent_uuid="agent_uuid",
        )
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.agents.functions.with_raw_response.delete(
            function_uuid="function_uuid",
            agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.agents.functions.with_streaming_response.delete(
            function_uuid="function_uuid",
            agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionDeleteResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            client.genai.agents.functions.with_raw_response.delete(
                function_uuid="function_uuid",
                agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.genai.agents.functions.with_raw_response.delete(
                function_uuid="",
                agent_uuid="agent_uuid",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        function = await async_client.genai.agents.functions.create(
            path_agent_uuid="agent_uuid",
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        function = await async_client.genai.agents.functions.create(
            path_agent_uuid="agent_uuid",
            body_agent_uuid="agent_uuid",
            description="description",
            faas_name="faas_name",
            faas_namespace="faas_namespace",
            function_name="function_name",
            input_schema={},
            output_schema={},
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.agents.functions.with_raw_response.create(
            path_agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.agents.functions.with_streaming_response.create(
            path_agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionCreateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            await async_client.genai.agents.functions.with_raw_response.create(
                path_agent_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        function = await async_client.genai.agents.functions.update(
            path_function_uuid="function_uuid",
            path_agent_uuid="agent_uuid",
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        function = await async_client.genai.agents.functions.update(
            path_function_uuid="function_uuid",
            path_agent_uuid="agent_uuid",
            body_agent_uuid="agent_uuid",
            description="description",
            faas_name="faas_name",
            faas_namespace="faas_namespace",
            function_name="function_name",
            body_function_uuid="function_uuid",
            input_schema={},
            output_schema={},
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.agents.functions.with_raw_response.update(
            path_function_uuid="function_uuid",
            path_agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.agents.functions.with_streaming_response.update(
            path_function_uuid="function_uuid",
            path_agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionUpdateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            await async_client.genai.agents.functions.with_raw_response.update(
                path_function_uuid="function_uuid",
                path_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_uuid` but received ''"):
            await async_client.genai.agents.functions.with_raw_response.update(
                path_function_uuid="",
                path_agent_uuid="agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        function = await async_client.genai.agents.functions.delete(
            function_uuid="function_uuid",
            agent_uuid="agent_uuid",
        )
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.agents.functions.with_raw_response.delete(
            function_uuid="function_uuid",
            agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.agents.functions.with_streaming_response.delete(
            function_uuid="function_uuid",
            agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionDeleteResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            await async_client.genai.agents.functions.with_raw_response.delete(
                function_uuid="function_uuid",
                agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.genai.agents.functions.with_raw_response.delete(
                function_uuid="",
                agent_uuid="agent_uuid",
            )
