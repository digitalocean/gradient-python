# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.genai.agents import (
    ChildAgentAddResponse,
    ChildAgentViewResponse,
    ChildAgentDeleteResponse,
    ChildAgentUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChildAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: DigitaloceanGenaiSDK) -> None:
        child_agent = client.genai.agents.child_agents.update(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        )
        assert_matches_type(ChildAgentUpdateResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        child_agent = client.genai.agents.child_agents.update(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
            body_child_agent_uuid="child_agent_uuid",
            if_case="if_case",
            body_parent_agent_uuid="parent_agent_uuid",
            route_name="route_name",
            uuid="uuid",
        )
        assert_matches_type(ChildAgentUpdateResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.agents.child_agents.with_raw_response.update(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child_agent = response.parse()
        assert_matches_type(ChildAgentUpdateResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.agents.child_agents.with_streaming_response.update(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child_agent = response.parse()
            assert_matches_type(ChildAgentUpdateResponse, child_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_parent_agent_uuid` but received ''"
        ):
            client.genai.agents.child_agents.with_raw_response.update(
                path_child_agent_uuid="child_agent_uuid",
                path_parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_child_agent_uuid` but received ''"):
            client.genai.agents.child_agents.with_raw_response.update(
                path_child_agent_uuid="",
                path_parent_agent_uuid="parent_agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DigitaloceanGenaiSDK) -> None:
        child_agent = client.genai.agents.child_agents.delete(
            child_agent_uuid="child_agent_uuid",
            parent_agent_uuid="parent_agent_uuid",
        )
        assert_matches_type(ChildAgentDeleteResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.agents.child_agents.with_raw_response.delete(
            child_agent_uuid="child_agent_uuid",
            parent_agent_uuid="parent_agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child_agent = response.parse()
        assert_matches_type(ChildAgentDeleteResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.agents.child_agents.with_streaming_response.delete(
            child_agent_uuid="child_agent_uuid",
            parent_agent_uuid="parent_agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child_agent = response.parse()
            assert_matches_type(ChildAgentDeleteResponse, child_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `parent_agent_uuid` but received ''"):
            client.genai.agents.child_agents.with_raw_response.delete(
                child_agent_uuid="child_agent_uuid",
                parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `child_agent_uuid` but received ''"):
            client.genai.agents.child_agents.with_raw_response.delete(
                child_agent_uuid="",
                parent_agent_uuid="parent_agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: DigitaloceanGenaiSDK) -> None:
        child_agent = client.genai.agents.child_agents.add(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        )
        assert_matches_type(ChildAgentAddResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        child_agent = client.genai.agents.child_agents.add(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
            body_child_agent_uuid="child_agent_uuid",
            if_case="if_case",
            body_parent_agent_uuid="parent_agent_uuid",
            route_name="route_name",
        )
        assert_matches_type(ChildAgentAddResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.agents.child_agents.with_raw_response.add(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child_agent = response.parse()
        assert_matches_type(ChildAgentAddResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.agents.child_agents.with_streaming_response.add(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child_agent = response.parse()
            assert_matches_type(ChildAgentAddResponse, child_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_add(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_parent_agent_uuid` but received ''"
        ):
            client.genai.agents.child_agents.with_raw_response.add(
                path_child_agent_uuid="child_agent_uuid",
                path_parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_child_agent_uuid` but received ''"):
            client.genai.agents.child_agents.with_raw_response.add(
                path_child_agent_uuid="",
                path_parent_agent_uuid="parent_agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_view(self, client: DigitaloceanGenaiSDK) -> None:
        child_agent = client.genai.agents.child_agents.view(
            "uuid",
        )
        assert_matches_type(ChildAgentViewResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_view(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.genai.agents.child_agents.with_raw_response.view(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child_agent = response.parse()
        assert_matches_type(ChildAgentViewResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_view(self, client: DigitaloceanGenaiSDK) -> None:
        with client.genai.agents.child_agents.with_streaming_response.view(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child_agent = response.parse()
            assert_matches_type(ChildAgentViewResponse, child_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_view(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.genai.agents.child_agents.with_raw_response.view(
                "",
            )


class TestAsyncChildAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        child_agent = await async_client.genai.agents.child_agents.update(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        )
        assert_matches_type(ChildAgentUpdateResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        child_agent = await async_client.genai.agents.child_agents.update(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
            body_child_agent_uuid="child_agent_uuid",
            if_case="if_case",
            body_parent_agent_uuid="parent_agent_uuid",
            route_name="route_name",
            uuid="uuid",
        )
        assert_matches_type(ChildAgentUpdateResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.agents.child_agents.with_raw_response.update(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child_agent = await response.parse()
        assert_matches_type(ChildAgentUpdateResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.agents.child_agents.with_streaming_response.update(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child_agent = await response.parse()
            assert_matches_type(ChildAgentUpdateResponse, child_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_parent_agent_uuid` but received ''"
        ):
            await async_client.genai.agents.child_agents.with_raw_response.update(
                path_child_agent_uuid="child_agent_uuid",
                path_parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_child_agent_uuid` but received ''"):
            await async_client.genai.agents.child_agents.with_raw_response.update(
                path_child_agent_uuid="",
                path_parent_agent_uuid="parent_agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        child_agent = await async_client.genai.agents.child_agents.delete(
            child_agent_uuid="child_agent_uuid",
            parent_agent_uuid="parent_agent_uuid",
        )
        assert_matches_type(ChildAgentDeleteResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.agents.child_agents.with_raw_response.delete(
            child_agent_uuid="child_agent_uuid",
            parent_agent_uuid="parent_agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child_agent = await response.parse()
        assert_matches_type(ChildAgentDeleteResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.agents.child_agents.with_streaming_response.delete(
            child_agent_uuid="child_agent_uuid",
            parent_agent_uuid="parent_agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child_agent = await response.parse()
            assert_matches_type(ChildAgentDeleteResponse, child_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `parent_agent_uuid` but received ''"):
            await async_client.genai.agents.child_agents.with_raw_response.delete(
                child_agent_uuid="child_agent_uuid",
                parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `child_agent_uuid` but received ''"):
            await async_client.genai.agents.child_agents.with_raw_response.delete(
                child_agent_uuid="",
                parent_agent_uuid="parent_agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        child_agent = await async_client.genai.agents.child_agents.add(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        )
        assert_matches_type(ChildAgentAddResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        child_agent = await async_client.genai.agents.child_agents.add(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
            body_child_agent_uuid="child_agent_uuid",
            if_case="if_case",
            body_parent_agent_uuid="parent_agent_uuid",
            route_name="route_name",
        )
        assert_matches_type(ChildAgentAddResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.agents.child_agents.with_raw_response.add(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child_agent = await response.parse()
        assert_matches_type(ChildAgentAddResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.agents.child_agents.with_streaming_response.add(
            path_child_agent_uuid="child_agent_uuid",
            path_parent_agent_uuid="parent_agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child_agent = await response.parse()
            assert_matches_type(ChildAgentAddResponse, child_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_add(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_parent_agent_uuid` but received ''"
        ):
            await async_client.genai.agents.child_agents.with_raw_response.add(
                path_child_agent_uuid="child_agent_uuid",
                path_parent_agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_child_agent_uuid` but received ''"):
            await async_client.genai.agents.child_agents.with_raw_response.add(
                path_child_agent_uuid="",
                path_parent_agent_uuid="parent_agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_view(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        child_agent = await async_client.genai.agents.child_agents.view(
            "uuid",
        )
        assert_matches_type(ChildAgentViewResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_view(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.genai.agents.child_agents.with_raw_response.view(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child_agent = await response.parse()
        assert_matches_type(ChildAgentViewResponse, child_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_view(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.genai.agents.child_agents.with_streaming_response.view(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child_agent = await response.parse()
            assert_matches_type(ChildAgentViewResponse, child_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_view(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.genai.agents.child_agents.with_raw_response.view(
                "",
            )
