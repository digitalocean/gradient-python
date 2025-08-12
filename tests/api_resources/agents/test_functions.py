# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents import (
    FunctionCreateResponse,
    FunctionDeleteResponse,
    FunctionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        function = client.agents.functions.create(
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        function = client.agents.functions.create(
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            description='"My Function Description"',
            faas_name='"my-function"',
            faas_namespace='"default"',
            function_name='"My Function"',
            input_schema={},
            output_schema={},
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.agents.functions.with_raw_response.create(
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.agents.functions.with_streaming_response.create(
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionCreateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            client.agents.functions.with_raw_response.create(
                path_agent_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        function = client.agents.functions.update(
            path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        function = client.agents.functions.update(
            path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            description='"My Function Description"',
            faas_name='"my-function"',
            faas_namespace='"default"',
            function_name='"My Function"',
            body_function_uuid='"12345678-1234-1234-1234-123456789012"',
            input_schema={},
            output_schema={},
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.agents.functions.with_raw_response.update(
            path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.agents.functions.with_streaming_response.update(
            path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionUpdateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            client.agents.functions.with_raw_response.update(
                path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                path_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_uuid` but received ''"):
            client.agents.functions.with_raw_response.update(
                path_function_uuid="",
                path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        function = client.agents.functions.delete(
            function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.agents.functions.with_raw_response.delete(
            function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.agents.functions.with_streaming_response.delete(
            function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionDeleteResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            client.agents.functions.with_raw_response.delete(
                function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            client.agents.functions.with_raw_response.delete(
                function_uuid="",
                agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        function = await async_client.agents.functions.create(
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        function = await async_client.agents.functions.create(
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            description='"My Function Description"',
            faas_name='"my-function"',
            faas_namespace='"default"',
            function_name='"My Function"',
            input_schema={},
            output_schema={},
        )
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.functions.with_raw_response.create(
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionCreateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.functions.with_streaming_response.create(
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionCreateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            await async_client.agents.functions.with_raw_response.create(
                path_agent_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        function = await async_client.agents.functions.update(
            path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        function = await async_client.agents.functions.update(
            path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            description='"My Function Description"',
            faas_name='"my-function"',
            faas_namespace='"default"',
            function_name='"My Function"',
            body_function_uuid='"12345678-1234-1234-1234-123456789012"',
            input_schema={},
            output_schema={},
        )
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.functions.with_raw_response.update(
            path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionUpdateResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.functions.with_streaming_response.update(
            path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionUpdateResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_agent_uuid` but received ''"):
            await async_client.agents.functions.with_raw_response.update(
                path_function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                path_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_uuid` but received ''"):
            await async_client.agents.functions.with_raw_response.update(
                path_function_uuid="",
                path_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        function = await async_client.agents.functions.delete(
            function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.functions.with_raw_response.delete(
            function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionDeleteResponse, function, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.functions.with_streaming_response.delete(
            function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionDeleteResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            await async_client.agents.functions.with_raw_response.delete(
                function_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_uuid` but received ''"):
            await async_client.agents.functions.with_raw_response.delete(
                function_uuid="",
                agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )
