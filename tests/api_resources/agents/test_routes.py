# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents import (
    RouteAddResponse,
    RouteViewResponse,
    RouteDeleteResponse,
    RouteUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        route = client.agents.routes.update(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        route = client.agents.routes.update(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_child_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            if_case='"use this to get weather information"',
            body_parent_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            route_name='"weather_route"',
            uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.agents.routes.with_raw_response.update(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.agents.routes.with_streaming_response.update(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteUpdateResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_parent_agent_uuid` but received ''"
        ):
            client.agents.routes.with_raw_response.update(
                path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                path_parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_child_agent_uuid` but received ''"):
            client.agents.routes.with_raw_response.update(
                path_child_agent_uuid="",
                path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        route = client.agents.routes.delete(
            child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.agents.routes.with_raw_response.delete(
            child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.agents.routes.with_streaming_response.delete(
            child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteDeleteResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `parent_agent_uuid` but received ''"):
            client.agents.routes.with_raw_response.delete(
                child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `child_agent_uuid` but received ''"):
            client.agents.routes.with_raw_response.delete(
                child_agent_uuid="",
                parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Gradient) -> None:
        route = client.agents.routes.add(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(RouteAddResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Gradient) -> None:
        route = client.agents.routes.add(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_child_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            if_case='"use this to get weather information"',
            body_parent_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            route_name='"weather_route"',
        )
        assert_matches_type(RouteAddResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Gradient) -> None:
        response = client.agents.routes.with_raw_response.add(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteAddResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Gradient) -> None:
        with client.agents.routes.with_streaming_response.add(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteAddResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Gradient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_parent_agent_uuid` but received ''"
        ):
            client.agents.routes.with_raw_response.add(
                path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                path_parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_child_agent_uuid` but received ''"):
            client.agents.routes.with_raw_response.add(
                path_child_agent_uuid="",
                path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_view(self, client: Gradient) -> None:
        route = client.agents.routes.view(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(RouteViewResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_view(self, client: Gradient) -> None:
        response = client.agents.routes.with_raw_response.view(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteViewResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_view(self, client: Gradient) -> None:
        with client.agents.routes.with_streaming_response.view(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteViewResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_view(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.agents.routes.with_raw_response.view(
                "",
            )


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        route = await async_client.agents.routes.update(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        route = await async_client.agents.routes.update(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_child_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            if_case='"use this to get weather information"',
            body_parent_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            route_name='"weather_route"',
            uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.routes.with_raw_response.update(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.routes.with_streaming_response.update(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteUpdateResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_parent_agent_uuid` but received ''"
        ):
            await async_client.agents.routes.with_raw_response.update(
                path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                path_parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_child_agent_uuid` but received ''"):
            await async_client.agents.routes.with_raw_response.update(
                path_child_agent_uuid="",
                path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        route = await async_client.agents.routes.delete(
            child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.routes.with_raw_response.delete(
            child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.routes.with_streaming_response.delete(
            child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteDeleteResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `parent_agent_uuid` but received ''"):
            await async_client.agents.routes.with_raw_response.delete(
                child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `child_agent_uuid` but received ''"):
            await async_client.agents.routes.with_raw_response.delete(
                child_agent_uuid="",
                parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncGradient) -> None:
        route = await async_client.agents.routes.add(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(RouteAddResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncGradient) -> None:
        route = await async_client.agents.routes.add(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_child_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            if_case='"use this to get weather information"',
            body_parent_agent_uuid='"12345678-1234-1234-1234-123456789012"',
            route_name='"weather_route"',
        )
        assert_matches_type(RouteAddResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.routes.with_raw_response.add(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteAddResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.routes.with_streaming_response.add(
            path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteAddResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncGradient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_parent_agent_uuid` but received ''"
        ):
            await async_client.agents.routes.with_raw_response.add(
                path_child_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
                path_parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_child_agent_uuid` but received ''"):
            await async_client.agents.routes.with_raw_response.add(
                path_child_agent_uuid="",
                path_parent_agent_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_view(self, async_client: AsyncGradient) -> None:
        route = await async_client.agents.routes.view(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(RouteViewResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_view(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.routes.with_raw_response.view(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteViewResponse, route, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_view(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.routes.with_streaming_response.view(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteViewResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_view(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.agents.routes.with_raw_response.view(
                "",
            )
